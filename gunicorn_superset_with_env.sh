#!/bin/bash
source /home/ubuntu/VirtualEnvrnmnt/superset/bin/activate
gunicorn --workers=1 'superset:create_app()' -b 0.0.0.0:8088
