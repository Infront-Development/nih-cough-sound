#!/bin/sh
source env/bin/activate
python manage.py collectstatic --no-input
echo "Running systemctl Daemon Reload ... " 
systemctl daemon-reload
echo "Restarting Gunicorn Socket " 
systemctl restart gunicorn
echo "Restarting Nginx server" 
systemctl restart nginx
