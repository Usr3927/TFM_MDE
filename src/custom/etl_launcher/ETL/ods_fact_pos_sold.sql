select
  spo.id                    order_id,
  spo.name                  order_name,
  spo.date_order            order_date_order,
  spo.amount_tax            order_amount_tax,
  spo.amount_total          order_amount_total,
  spo.amount_paid           order_amount_paid,
  spo.amount_return         order_amount_return,
  spo.pos_reference         order_pos_reference,
  spol.id                   line_id,
  spol.name                 line_name,
  spol.price_unit           line_price_unit,
  spol.qty                  line_qty,
  spol.price_subtotal       line_price_subtotal,
  spol.price_subtotal_incl  line_price_subtotal_incl,
  spol.discount             line_discount,
  sps.id                    session_id,
  sps.name                  session_name,
  sps.start_at              session_start_at,
  sps.stop_at               session_stop_at,
  spt.id                    template_id,
  spt.name                  template_name,
  spt.description           template_description,
  spt.categ_id              template_categ_id,
  spt.list_price            template_list_price,
  spt.sale_ok               template_sale_ok,
  spt.purchase_ok           template_purchase_ok,
  spt.active                template_active,
  spt.pos_categ_id          template_pos_categ_id
from stg.stg_pos_order spo
left join stg.stg_pos_order_line spol on spo.id=spol.order_id
left join stg.stg_pos_session sps on sps.id=spo.session_id
left join stg.stg_product_product spp on spp.id=spol.product_id
left join stg.stg_product_template spt on spt.id=spp.product_tmpl_id;
