#!/bin/bash
python3 ./odoo-14.0/odoo-bin -r firm01 -w firm01 --addons-path=./odoo-14.0/addons,./src/custom -d firm01 --db_host odoo-db.cnfvu3hjlwx5.eu-west-3.rds.amazonaws.com --db_port 5432
