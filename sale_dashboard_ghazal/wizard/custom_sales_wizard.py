from odoo import _, api, fields, models
from datetime import datetime, date, time,timedelta
import pytz
from odoo import exceptions


class CustomSalesWizard(models.TransientModel):
    _name = 'custom.sales.wizard'
    _description = "Custom Sales"
    _inherit = ['mail.thread.main.attachment', 'mail.activity.mixin']



    def action_direct_sale(self):
        print('action_direct_sale')
        action = self.sudo().env.ref('sale_dashboard_ghazal.action_trigger_direct_sales_wizard').read()[0]
        return action

    def action_event_sale(self):
        print('action_event_sale')
        return {
            'type': 'ir.actions.act_window',
            'name': _('Event Sales'),
            'res_model': 'sale.order',
            'view_mode': 'list',
            'domain': [],
            'context': {},
        }

