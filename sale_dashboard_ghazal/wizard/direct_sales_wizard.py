from odoo import _, api, fields, models
from datetime import datetime, date, time,timedelta
import pytz
from odoo import exceptions


class DirectSalesWizard(models.TransientModel):
    _name = 'direct.sales.wizard'
    _description = "Direct Sales"
    _inherit = ['mail.thread.main.attachment', 'mail.activity.mixin']

    direct_sales_type=fields.Selection(selection=[('lead','Lead'),('customer','Customer'),('draft','')],
                                       string='Direct Sales Type',
                                       store=True,default='draft')
    is_existing_lead=fields.Boolean('Is Existing Lead?',default=False,store=True)
    is_new_customer=fields.Boolean('Is New Customer?',default=True,store=True)
    participant_type = fields.Selection(selection=[('individual', 'Individual'), ('company', 'Company')],
                                         string='Participant Type',store=True)

    @api.model
    def default_get(self, fields):
        # if self.sudo().env.context.get('communication_button'):
        #     self.communication_button = self.sudo().env.context.get('communication_button')
        # if self.sudo().env.context.get('partner_type'):
        #     self.partner_type = self.sudo().env.context.get('partner_type')

        return super().default_get(fields)
    def action_submit(self):
        print('action_submit')
        if self.is_existing_lead:
            return {
                'type': 'ir.actions.act_window',
                'name': _('Participant List(Leads)'),
                'res_model': 'res.partner',
                'view_mode': 'kanban,form',
                'domain': [('partner_type', 'in', ['lead'])],
                'context': {'communication_button': True},
            }
        elif not self.is_existing_lead:
            return {
                'type': 'ir.actions.act_window',
                'name': _('New Leader'),
                'res_model': 'res.partner',
                'view_mode': 'form',
                'context': {'partner_type': 'lead', 'communication_button': False},

            }
        elif not self.is_new_customer:
            return {
                'type': 'ir.actions.act_window',
                'name': _('Participant List(Customers)'),
                'res_model': 'res.partner',
                'view_mode': 'kanban,form',
                'domain': [('partner_type', 'in', ['customer'])],
                'context': {'communication_button': True},
            }
        elif self.is_new_customer:
            return {
                'type': 'ir.actions.act_window',
                'name': _('New Customer'),
                'res_model': 'res.partner',
                'view_mode': 'form',
                'context': {'partner_type': 'customer', 'communication_button': False},
            }
