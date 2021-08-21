#!/bin/bash
gunicorn --workers=1 'superset:create_app()'
