#!/bin/bash
python3 ./odoo/odoo-bin -r ubuntu -w tfmmde --addons-path=./odoo/addons -d ubuntu --db_host tfm-mde-bbdd.cnfvu3hjlwx5.eu-west-3.rds.amazonaws.com --db_port 5432
