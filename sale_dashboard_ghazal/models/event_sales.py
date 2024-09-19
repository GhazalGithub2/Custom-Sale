from odoo import _, api, fields, models
from datetime import datetime, date, time,timedelta
import pytz
from odoo import exceptions

class EventSales(models.Model):
    _inherit='sale.order'
    _description = 'Event Sales'

    participant_ids = fields.Many2many('res.partner', string='Participants',store=True)


    def action_trigger_event_sales_particips(self):
        context = {'active': True, 'sale_order_id': self.id}
        action = self.sudo().env.ref('sale_dashboard_ghazal.action_trigger_direct_sales_wizard').read()[0]
        action['context'] = context
        return action