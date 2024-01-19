{
    "name": "Contact Report Graph",
    "version": '1.0',
    "category": "Interview/others",
    "license": "AGPL-3",
    "summary": "Contact Report Graph",
    "author": "Manoj Parmar",
    "maintainers": ["Manoj Parmar"],
    "website": "www.xyz.com",
    "depends": ['base_setup','base', 'contacts', 'bus', 'web'],
    "data": [
        # 'security/event_management_security.xml',
        # "security/ir.model.access.csv",

        "data/contact_report_views.xml",
        "data/report_actions.xml",

        # "views/contact_report_views.xml",
        "views/menuitem.xml",
        
        # "report/.xml",
        # "data/multiple_cron.xml",
    ],
    "installable": True,
    'auto_install': False,
    "application": True,
    'assets': {
        'web.assets_backend': [
            # 'contact_report_graph/static/src/js/res_partner.js',
        ],
        # 'web.assets_web_dark': [],
        # 'web.assets_frontend': [],
    },
}
