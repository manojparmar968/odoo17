{
    "name": "Owl Inheritance",
    "version": '1.0',
    "category": "Interview/others",
    "license": "AGPL-3",
    "summary": "Owl inheritance ",
    'sequence': -1,
    'description':"""
        ==========================
            owl
        ==========================
    """,
    "author": "Manoj Parmar",
    "maintainers": ["Manoj Parmar"],
    "website": "www.xyz.com",
    "depends": ['base_setup','base', 'web'],
    "data": [
        # "security/ir.model.access.csv",

        "views/res_partner_views.xml",
        
        # "report/.xml",
        # "data/.xml",
    ],
    "installable": True,
    'auto_install': False,
    "application": True,
    'assets': {
        'web.assets_backend': [
            'owl_inheritance/static/src/components/*/*.js',
            'owl_inheritance/static/src/components/*/*.xml',
            'owl_inheritance/static/src/components/*/*.scss',
        ],
        # 'web.assets_web_dark': [],
        # 'web.assets_frontend': [],
    },
}
