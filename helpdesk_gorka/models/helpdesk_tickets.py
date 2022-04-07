import string
from odoo import fields, models, api

class Help(models.Model):
    _name = "helpdesk.gorka"
    _description = "Help Desk Gorka"
    _order= "sequence"

    name = fields.Char(string="Nombre del Ticket", required=True)
    description = fields.Text(string="Descripción", translate=True)
    date = fields.Date(help="Date when the ticket was created", string="Fecha del Ticket")
    datetime = fields.Datetime(help="Fecha y hora de la validez del ticket", string="Validez del Ticket")
    assigned = fields.Boolean(help="Ticket asignado a alguien", string="Asignado",readonly=True)
    actionsHtml = fields.Html(string="Notas varias")
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Assigned to'
    )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner'
    )
    action_ids = fields.One2many(
        comodel_name='helpdesk.ticket.action',
        inverse_name='ticket_id',
        string='Actions Done'
    )
    tag_ids = fields.Many2many(
        comodel_name='helpdesk.ticket.tag',
        #relation='table_name',
        #column1='col_name',
        #column2='other_column_name'
        string='Tags'
    )
    sequence = fields.Integer()
    state = fields.Selection(
        [('nuevo', 'Nuevo'),
         ('asignado', 'Asignado'),
         ('en_proceso', 'En proceso'),
         ('pendiente', 'Pendiente'),
         ('resuelto', 'Resuelto'),
         ('cancelado', 'Cancelado')],
        string='State',
        default='nuevo')

    def to_assigned(self):
        self.ensure_one()
        self.state = 'asignado'

    def to_proccess_in(self):
        self.write({'state': 'en_proceso'})

    def to_pendiente(self):
        for record in self:
            record.state = 'pendiente'

    def review_actions(self):
        self.ensure_one()
        self.action_ids.review()

    @api.model
    def get_amount_tickets(self):
        # Give amount of ticket for active user
        return self.search_count([('user_id', '=', self.env.user.id)])