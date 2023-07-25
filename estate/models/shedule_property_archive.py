from odoo import fields,models,api

class ShedulePropertyArchive(models.Model):
	_name="shedule.property.archive"
	
	def archive_property(self):
		allProperty = self.env['estate.property'].search([('active','=',True)])
		for prop in allProperty:
			if prop.state == 'cancel':
				prop.active = False


	# def archive_property(self):
	# 	allProperty = self.env['estate.property'].search([('state','=','cancel')])
	# 	for prop in allProperty:
	# 		prop.active = False