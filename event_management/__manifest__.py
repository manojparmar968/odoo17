{
    "name": "event management",
    "version": '1.0',
    "category": "Interview/others",
    "license": "AGPL-3",
    "summary": "event management",
    "author": "Manoj Parmar",
    "maintainers": ["Manoj Parmar"],
    "website": "www.xyz.com",
    "depends": ['base_setup','base'],
    "data": [
        'security/event_management_security.xml',
        "security/ir.model.access.csv",

        "views/event_management_views.xml",
        "views/menuitem.xml",
        
        # "report/.xml",
        # "data/multiple_cron.xml",
    ],
    "installable": True,
    'auto_install': False,
    "application": True,
}
