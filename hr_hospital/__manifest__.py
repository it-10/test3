{
    'name': 'Hospital',
    'summary': '',

    'author': 'it-10',
    'website': '',

    'category': 'Customizations',
    'license': '',
    'version': '15.0.1.0.0',

    'depends': [
    ],

    'external_dependencies': {'python': [], },

    'data': [
        'security/ir.model.access.csv',

        'views/hr_hospital_menus.xml',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/diagnoz_views.xml',
        'views/patient_card_views.xml',

    ],
    'demo': [
    ],

    'installable': True,
    'auto_install': True,

    'images': [
        'static/description/cover.png',
        'static/description/icon.png',

    ],

    'price': 0,
    'currency': 'EUR',

}
