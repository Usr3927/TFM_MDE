#!/bin/bash
python3 ~/odoo/odoo-bin -i base -r ubuntu --addons-path=~/odoo/addons,~/TFM_MDE/src/custom -d ubuntu --db_host localhost --db_port 5432 --without-demo=WITHOUT_DEMO
