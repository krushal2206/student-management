{
    'name': "School Management",
    'version': '1.0',
    'author': "Krushal Kalkani",
    'depends': ['base', 'mail'],
    'description': """
    School Management Module.
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/school_management.xml',
        'views/teacher_management.xml',
        'views/menu.xml',
        'data/demo_data.xml',
    ],
    'application': True,
    'demo': True
}
