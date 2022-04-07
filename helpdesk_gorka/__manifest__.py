{
    'name': 'HelpDesk_Gorka',
    'summary': 'Gestión de Tickets',
    'version': '15.0.1.0.0',
    'author': 'Gorka',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv',
        'views/helpdesk_views.xml',
        'views/helpdesk_ticket_tag_views.xml',
    ],
}