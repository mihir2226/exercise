from odoo import fields, models, api, Command


class EstateAccount(models.Model):
    _inherit = "estate.property"

    def sold_button(self):
        # res = super(EstateAccount, self).sold_button()
        self.env['account.move'].create({
            'partner_id': self.buyer.id,
            'move_type': 'out_invoice',
            "invoice_line_ids": [
                Command.create({
                    'name': self.name,
                    'quantity': 1,
                    'price_unit': (self.selling_price*0.06+100) + self.selling_price,
                })
            ],
        })
        return super(EstateAccount, self).sold_button()

    # def sold_button(self):
    #     res = super(EstateAccount, self).sold_button()
    #     print('>>>>>>>>>>>>>>>>> overrided', self.buyer.id)
    #     Command = self.env['account.move.line'].with_context(
    #         default_move_type='out_invoice',
    #         default_quantity=1,
    #         default_price_unit=((self.selling_price*6)/100)+100.00,
    #     )
    #     self.env['account.move'].create({
    #         'name': self.name,
    #         'line_ids': [(0, 0, Command.create({
    #             'partner_id': self.buyer.id,
    #         }).values[0])],
    #     })
    #     return res

    # def sold_button(self):
    # 	res = super(EstateAccount, self).sold_button()
    # 	print('>>>>>>>>>>>>>>>>> overrided', self.buyer.id)
    # 	self.env['account.move'].create({
    # 		'name':self.name,
    # 		'partner_id':self.buyer.id,
    # 		'move_type':'out_invoice',
    # 		# 'quantity':1,
    # 		# 'price_unit':self.selling_price,
    # 		})
    # 	return res

        # copy
