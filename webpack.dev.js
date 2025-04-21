const { merge } = require('webpack-merge');
const common = require('./webpack.config.js');
const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = merge(common, {
  mode: 'development',
  devtool: 'inline-source-map',
  output: {
    filename: '[name].js',
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: '[name].css',
    }),
  ],
  optimization: {
    minimize: false,
  },
  devServer: {
    static: {
      directory: path.resolve(__dirname, 'static'),
    },
    headers: { 'Access-Control-Allow-Origin': '*' },
    compress: true,
    port: 8080,
    hot: true,
    liveReload: true,
    open: true,
    proxy: [
      {
        context: ['/'],
        target: 'http://127.0.0.1:8000/',
        changeOrigin: true,
      },
    ],
    watchFiles: ['assets/**/*.{scss,css,js}', 'core/templates/**/*.html'],
  },
});