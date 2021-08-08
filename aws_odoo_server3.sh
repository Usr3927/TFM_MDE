#!/bin/bash
python3 ./odoo/odoo-bin -r firm01 -w firm01 --addons-path=./odoo/addons -d firm01 --db_host odoo-db.cnfvu3hjlwx5.eu-west-3.rds.amazonaws.com --db_port 5432
