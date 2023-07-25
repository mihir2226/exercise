from odoo import api,fields,models

class SaleOrder(models.Model):
	_inherit = "sale.order"

	service_total = fields.Integer(compute="_compute_stotal")
	in_company_id = fields.Boolean(related="partner_id.is_company") #related use karvu
	# @api.onchange('order_line')
	@api.depends('order_line')
	def _compute_stotal(self):
		for rec in self:
			rec.service_total = sum(rec.order_line.filtered(lambda x:x.product_id.detailed_type == 'service').mapped('price_subtotal'))

	# @api.onchange('partner_id')
	# def rr(self):
	# 	for rec in self:
	# 		rec.in_company_id = rec.partner_id.is_company
	# 		print('>>>>>>>>> partner ',rec.partner_id.name)
	# 		print('>>>>>>>>> partner_id.is_company ',rec.partner_id.is_company)
	# 		print('>>>>>>>>> Its working',rec.partner_id.is_company == True)
	# 		print('>>>>>>>>> company_id ',rec.company_id)
	# 		print('>>>>>>>>>',rec.in_company_id)
	# 			