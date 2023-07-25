from odoo import fields,models,api

class SheduleConfirmDraft(models.Model):
	_inherit='sale.order'

	def confirm_order(self):
		orders = self.env['sale.order'].search([('state','=','draft')]).action_confirm()

# bija module ma shedular set karva inherit karvu pade
