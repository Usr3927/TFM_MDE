#!/bin/bash
python3 ~/odoo/odoo-bin -r odoo -w odoo --addons-path=~/odoo/addons,~/TFM_MDE/src/custom -d odoo --db_host localhost --db_port 5432 --without-demo=WITHOUT_DEMO
