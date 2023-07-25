{
    'name': 'exercise',
    'version': '1.0',
    'summary': 'it is exercise module',
    'discription': '',
    'website': 'https://strataprop.com/',
    'author': 'Mihir nayak',
    'category': 'Sales',
    'depends': ['sale_management'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        'views/sale_order_view.xml',
        'views/invoice_view.xml',
        'views/shedule_confirm_draft_view.xml',
        # 'report/sale_order_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
