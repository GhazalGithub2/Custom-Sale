from odoo import _, api, fields, models
from datetime import datetime, date, time,timedelta
import pytz
from odoo import exceptions


class SalesCommunicationWizard(models.TransientModel):
    _name = 'sales.communication.wizard'
    _description = "Sales Communication"
    _inherit = ['mail.thread.main.attachment', 'mail.activity.mixin']

    partner_id=fields.Many2one('res.partner','Partner',store=True,compute="_compute_partner")
    subject=fields.Char('Subject',store=True,required=True)
    message= fields.Text('Send Message',store=True,required=True)


    def _compute_partner(self):
      self.partner_id = self.sudo().env.context.get('partner_id')

    def action_done(self):
        for rec in self:
            # rec.state = 'confirm'
            rec._compute_partner()
            body = _('Hello %s %s , Thanks.', rec.partner_id.name,rec.message)
            print(body,rec.partner_id)
            rec.message_post(body=body,subject=rec.subject,partner_ids=[rec.partner_id.id])
