# -*- coding: utf-8 -*-
###################################################################################
{
    'name': 'Sale Dashboard',
    'version': '1.0',
    'category': 'Sales/',
    'sequence': 10,
    'author': 'Ghazal Sabha',
    'company': '',
    'website': "",
    'depends': ['base_setup', 'website', 'sale'],
    'data': [
        # 'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/custom_sales_wizard.xml',
        'wizard/direct_sales_wizard.xml',
        'wizard/sales_communication_wizard.xml',
        'views/custom_sale_views.xml',
        'views/res_partner_view_inherit.xml',
        'views/sale_order_view_inherit.xml'

    ],
'assets': {
        'web.assets_backend': [
            # 'sale_dashboard_ghazal/static/src/js/custom_sale.js',
            # 'sale_dashboard_ghazal/static/src/js/custom_sale.xml',

        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
