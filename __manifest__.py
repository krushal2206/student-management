{
    'name': "School Management",
    'version': '1.0',
    'sequence': -100,
    'depends': ['base', 'mail'],
    'author': "Krushal Kalkani",
    'website': "https://krushaalkalkani.github.io/Krushal-Kalkani-Online-Resume/",
    'description': """
    Student managemnet module which help to maintain the student data.
    """,
    'summary': 'This module help to Manage student data.',
    'data': [
        'security/ir.model.access.csv',
        'views/school_management.xml',
        'views/teacher_management.xml',
        'views/menu.xml',
        'report/student_report_template.xml',
        'report/student_email_template.xml',
        'data/cron_job.xml',
    ],

    'demo': [
        'demo/demo_data.xml'
    ],
    'license': "LGPL-3",
    'category': "Student Management",
    'application': True,
    'demo': True,
    'auto_install': True,
    'installable': True
}
