import time,datetime,dateutil,pytz
from datetime import datetime, timedelta
from dateutil import tz
import odoo.exceptions
from odoo import models, fields, api,_


class Participant(models.Model):
    _inherit = 'res.partner'
    _description = 'Participant'

    partner_type = fields.Selection([
        ('customer', 'Customer'),
        ('lead', 'Lead'),
        ('draft', ''),
    ], string='Contact Type',default='draft')
    communication_button=fields.Boolean(default=False)

    @api.model
    def default_get(self, fields):
        if self.sudo().env.context.get('communication_button'):
            self.communication_button = self.sudo().env.context.get('communication_button')
        if self.sudo().env.context.get('partner_type'):
            self.partner_type = self.sudo().env.context.get('partner_type')

        return super().default_get(fields)


    def open_start_sales_communication_wizard(self):
        context = {'active': True, 'partner_id': self.id}
        action = self.sudo().env.ref('sale_dashboard_ghazal.action_trigger_sale_communication_wizard').read()[0]
        action['context'] = context
        return action
