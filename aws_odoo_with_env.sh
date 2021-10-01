#!/bin/bash
source /home/TFM_MDE/VirtualEnvrnmnt/odoo/bin/activate
python3 /home/TFM_MDE/odoo/odoo-bin -r odoo -w odoo --addons-path=~/odoo/addons,~/TFM_MDE/src/custom -d odoo --db_host localhost --db_port 5432 --without-demo=WITHOUT_DEMO
