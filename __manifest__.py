{
    'name': "School Management",
    'version': '1.0',
    'sequence': -100,
    'depends': ['base', 'mail', 'sale', 'website'],
    'author': "Krushal Kalkani",
    'website': "https://krushaalkalkani.github.io/Krushal-Kalkani-Online-Resume/",
    'description': """
    Student managemnet module which help to maintain the student data.
    """,
    'summary': 'This module help to Manage student data.',
    'assets': {
        'web.assets_backend': [
            'school_management/static/src/components/**/*',
        ],
        'web.assets_frontend': [
            'school_management/static/src/scss/styles.scss',
            'school_management/static/src/js/info-school.js',
            'school_management/static/src/js/explore-school.js',
        ],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/school_management.xml',
        'views/teacher_management.xml',
        'views/school_info.xml',
        'views/menu.xml',
        'views/res_config_setting.xml',
        'views/sales_res_config_setting.xml',
        'views/snippets/info_school.xml',
        'views/snippets/info_snippet1.xml',
        'report/student_report_template.xml',
        'report/student_email_template.xml',
        'data/cron_job.xml'


    ],

    'demo': [
        'demo/demo_data.xml'
    ],

    'license': "LGPL-3",
    'category': "sales",
    'application': True,
    'demo': True,
    'auto_install': True,
    'installable': True
}
