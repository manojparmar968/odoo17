{
    "name": "Owl Tutorial v17",
    "version": '1.0',
    "category": "Interview/others",
    "license": "AGPL-3",
    "summary": "Owl Tutorial ",
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
        "security/ir.model.access.csv",

        "views/todo_list_views.xml",
        
        # "report/.xml",
        # "data/.xml",
    ],
    "installable": True,
    'auto_install': False,
    "application": True,
    'assets': {
        'web.assets_backend': [
            'owl1/static/src/components/*/*.js',
            'owl1/static/src/components/*/*.xml',
            'owl1/static/src/components/*/*.scss',
        ],
        # 'web.assets_web_dark': [],
        # 'web.assets_frontend': [],
    },
}
