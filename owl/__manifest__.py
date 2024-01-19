{
    "name": "Owl Tutorial",
    "version": '1.0',
    "category": "Interview/others",
    "license": "AGPL-3",
    "summary": "Owl Tutorial",
    'description':"""
    owl
    """,
    "author": "Manoj Parmar",
    "maintainers": ["Manoj Parmar"],
    "website": "www.xyz.com",
    "depends": ['base_setup','base', 'web', 'sale', 'board'],
    "data": [
        # 'security/event_management_security.xml',
        # "security/ir.model.access.csv",

        "views/sales_dashboard.xml",
        "views/menuitem.xml",
        
        # "report/.xml",
        # "data/multiple_cron.xml",
    ],
    "installable": True,
    'auto_install': False,
    "application": True,
    'assets': {
        'web.assets_backend': [
            'owl/static/src/components/**/*.js',
            'owl/static/src/components/**/*.xml',
            'owl/static/src/components/**/*.scss',
            # 'owl/static/momentjs/moment.min.js',

        ],
        # 'web.assets_web_dark': [],
        # 'web.assets_frontend': [],
    },
}
