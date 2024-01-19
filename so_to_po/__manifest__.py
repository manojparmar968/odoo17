{
    "name": "SO Name In PO",
    "version": '1.0.0',
    "category": "Interview/others",
    "license": "AGPL-3",
    "description": """
            O2B 
        ==========================
        In sale order when click on confirm button, PO will create with the name of sale order
        in PO inside Tag there is a field name origin pass that create SO name in that field.
        ==========================
    """,
    "author": "Manoj Parmar",
    "maintainers": ["Manoj Parmar"],
    "website": "www.xyz.com",
    "depends": ['base_setup','mail','sale'],
    "data": [
        # "security/ir.model.access.csv",
        # "views/.xml",
        # "report/.xml",
        # "data/multiple_cron.xml",
    ],
    "installable": True,
    'auto_install': False,
    "application": True,
}
