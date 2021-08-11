#!/bin/bash
python3 ~/odoo/odoo-bin --addons-path=~/odoo/addons,~/TFM_MDE/src/custom -d $USER -u recipes --without-demo=WITHOUT_DEMO
