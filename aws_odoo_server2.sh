#!/bin/bash
python3 ./odoo-14.0/odoo-bin -i base -r ubuntu -w tfmmde --addons-path=./odoo-14.0/addons,./src/custom -d ubuntu --db_host tfm-mde-bbdd.cnfvu3hjlwx5.eu-west-3.rds.amazonaws.com --db_port 5432
