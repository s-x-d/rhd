const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const BundleTracker = require('webpack-bundle-tracker');
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin'); // New: Plugin for CSS minification

module.exports = {
  // Dynamically set mode based on the environment; defaults to 'production'
  mode: process.env.NODE_ENV === 'development' ? 'development' : 'production',

  entry: {
    app: './assets/js/app.js', // Entry point for your app
  },

  output: {
    path: path.resolve('./static/bundles/'), // Output directory
    filename: '[name].js', // Output JS filename(s)
    publicPath: '/static/bundles/', // Public URL of the output files
  },

  plugins: [
    new MiniCssExtractPlugin({
      filename: 'app.css', // Output CSS filename
    }),
    new BundleTracker({
      path: __dirname,
      filename: 'webpack-stats.json', // Webpack stats file
    }),
  ],

  module: {
    rules: [
      // Rule for transpiling JavaScript files
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env'], // Transpile modern JS to target browsers
          },
        },
      },
      // Rule for SCSS and compiling it into CSS
      {
        test: /\.s[ac]ss$/i, // Match SCSS and Sass files
        use: [
          MiniCssExtractPlugin.loader, // Extract CSS during production
          'css-loader', // Resolves imports and URLs in CSS
          {
            loader: 'sass-loader', // Compiles SCSS into CSS
            options: {
              implementation: require('sass'), // Explicitly use Dart Sass
              sassOptions: {
                quietDeps: true, // Suppress warnings from dependencies
                includePaths: [
                  path.resolve(__dirname, 'node_modules/bootstrap/scss'), // Bootstrap SCSS path
                ],
              },
            },
          },
        ],
      },
      // Rule for processing plain CSS files (e.g., bootstrap-icons.css)
      {
        test: /\.css$/i, // Match CSS files
        use: [
          MiniCssExtractPlugin.loader, // Extract CSS during production
          'css-loader', // Resolves CSS imports and URLs
        ],
      },
      // Rule for handling font assets (used in bootstrap-icons.css or @font-face)
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/i, // Match font files
        type: 'asset/resource', // Emit fonts in the output directory
        generator: {
          filename: 'fonts/[name][ext]', // Output directory for fonts
        },
      },
    ],
  },

  optimization: {
    minimize: process.env.NODE_ENV !== 'development', // Only minimize in production mode
    minimizer: [
      `...`, // Retain Webpack's default TerserPlugin for JS minification
      new CssMinimizerPlugin(), // Minify CSS using CssMinimizerPlugin
    ],
  },

  resolve: {
    extensions: ['.js', '.jsx'], // Resolve these file extensions
  },

  devServer: {
    static: {
      directory: path.resolve(__dirname, 'static'), // Serve files from the 'static' directory
    },
    headers: { 'Access-Control-Allow-Origin': '*' }, // Enable CORS for dev server
    compress: true, // Enable gzip compression for the output files
    port: 8080, // Run the dev server on port 8080
    hot: true, // Enable hot module replacement (HMR)
    liveReload: true, // Reload assets (e.g., CSS/JS) that don't support HMR
    open: true, // Automatically open the browser when the dev server starts

    // Proxy requests to the Django server backend
    proxy: [
      {
        context: ['/'],
        target: 'http://127.0.0.1:8000/', // Forward requests to Django
        changeOrigin: true, // Fix potential CORS issues
      },
    ],

    // Watch for changes in these files or directories
    watchFiles: ['assets/**/*.{scss,css,js}', 'core/templates/**/*.html'],
  },
};