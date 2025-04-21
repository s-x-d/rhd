#!/bin/bash

# EC2 Deployment Script for Django Application
# This script should be run on the EC2 instance to set up the application

# Exit on error
set -e

echo "Starting deployment process..."

# Update system packages
echo "Updating system packages..."
sudo apt-get update
sudo apt-get upgrade -y

# Install required system dependencies
echo "Installing system dependencies..."
sudo apt-get install -y python3-pip python3-dev libpq-dev nginx git

# Create application directory if it doesn't exist
APP_DIR=/home/ubuntu/aws-app
if [ ! -d "$APP_DIR" ]; then
    echo "Creating application directory..."
    mkdir -p $APP_DIR
fi

# Clone or update the repository
if [ ! -d "$APP_DIR/.git" ]; then
    echo "Cloning repository..."
    git clone https://github.com/yourusername/your-repo.git $APP_DIR
else
    echo "Updating repository..."
    cd $APP_DIR
    git pull
fi

# Set up Python virtual environment
echo "Setting up virtual environment..."
cd $APP_DIR
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create .env file for environment variables
echo "Setting up environment variables..."
cat > $APP_DIR/.env << EOL
DJANGO_SECRET_KEY=$(python -c "import secrets; print(secrets.token_urlsafe(50))")
ALLOWED_HOSTS=localhost,127.0.0.1,your-domain.com
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your-db-host.amazonaws.com
DB_PORT=5432
EOL

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --settings=aws.settings.prod

# Set up Gunicorn service
echo "Setting up Gunicorn service..."
sudo cat > /etc/systemd/system/gunicorn.service << EOL
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=$APP_DIR
ExecStart=$APP_DIR/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:$APP_DIR/aws.sock aws.wsgi:application
Environment="DJANGO_SETTINGS_MODULE=aws.settings.prod"
EnvironmentFile=$APP_DIR/.env

[Install]
WantedBy=multi-user.target
EOL

# Set up Nginx
echo "Setting up Nginx..."
sudo cat > /etc/nginx/sites-available/aws << EOL
server {
    listen 80;
    server_name your-domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root $APP_DIR;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:$APP_DIR/aws.sock;
    }
}
EOL

# Enable the Nginx site
sudo ln -sf /etc/nginx/sites-available/aws /etc/nginx/sites-enabled

# Test Nginx configuration
sudo nginx -t

# Restart services
echo "Restarting services..."
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl restart nginx

echo "Deployment completed successfully!"
echo "Please update the .env file with your actual database credentials and domain name."
echo "Then restart Gunicorn with: sudo systemctl restart gunicorn"