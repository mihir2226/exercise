from odoo import api,fields,models

class ResPartner(models.Model):
	_inherit = "res.partner"

	website = fields.Char(required=True)
