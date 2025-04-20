# AWS Deployment Guide

## Environment Variables

The following environment variables need to be set in your AWS environment for proper deployment:

### Security Settings
- `DJANGO_SECRET_KEY`: A secure random string used for cryptographic signing. Generate a new one for production!
  Example: `python -c "import secrets; print(secrets.token_urlsafe(50))"`

### Host Settings
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts for your application.
  Example: `myapp.example.com,www.myapp.example.com`

### Database Settings
- `DB_NAME`: The name of your PostgreSQL database.
- `DB_USER`: The username for your PostgreSQL database.
- `DB_PASSWORD`: The password for your PostgreSQL database.
- `DB_HOST`: The hostname for your PostgreSQL database (e.g., RDS endpoint).
- `DB_PORT`: The port for your PostgreSQL database (default: 5432).

## Setting Environment Variables in AWS

### For Elastic Beanstalk
1. Go to your Elastic Beanstalk environment.
2. Navigate to Configuration > Software.
3. Under "Environment properties", add each of the environment variables listed above.
4. Apply the changes.

### For EC2 Instances
Add the environment variables to `/etc/environment` or the appropriate systemd service file.

Example for systemd:
```
[Service]
Environment="DJANGO_SECRET_KEY=your_secret_key_here"
Environment="ALLOWED_HOSTS=myapp.example.com,www.myapp.example.com"
Environment="DB_NAME=your_db_name"
Environment="DB_USER=your_db_user"
Environment="DB_PASSWORD=your_db_password"
Environment="DB_HOST=your.db.host.amazonaws.com"
Environment="DB_PORT=5432"
```

## Static Files

Static files are configured to be collected to the `staticfiles` directory. Make sure to run:

```
python manage.py collectstatic --settings=aws.settings.prod
```

For AWS deployment, you should configure your web server (e.g., Nginx) to serve files from this directory, or use AWS S3 for static file hosting.

## Running the Application

To run the application with production settings:

```
python manage.py runserver --settings=aws.settings.prod
```

### WSGI and ASGI Configuration

The WSGI and ASGI configuration files (wsgi.py and asgi.py) have been updated to use the production settings by default. This means that when you deploy your application to AWS, it will automatically use the production settings without any additional configuration.

For deployment, use a WSGI server like Gunicorn:

```
gunicorn aws.wsgi:application
```

Or for ASGI servers like Uvicorn:

```
uvicorn aws.asgi:application
```

If you need to use different settings for some reason, you can set the DJANGO_SETTINGS_MODULE environment variable:

```
export DJANGO_SETTINGS_MODULE=aws.settings.local
gunicorn aws.wsgi:application
```
