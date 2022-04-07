from odoo import fields, models

class HelpdeskTicketAction(models.Model):
    _name = "helpdesk.ticket.action"
    _description = "Heldesk Ticket Action"
    _order = "sequence"

    sequence = fields.Integer()
    name = fields.Char(required=True)
    description = fields.Text()
    duration = fields.Float()
    ticket_id = fields.Many2one(comodel_name='helpdesk.gorka')

    def review(self):
        for record in self:
            record.description = '%s\n%s' % (record.description, '- OK') 