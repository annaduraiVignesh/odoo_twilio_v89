{
    'name': "Twilio SMS v8,9",
    'summary': """ This App has the ability to send SMS using twilio. This is for version 8 and 9. there is a seprate module for version 10 too(https://www.odoo.com/apps/modules/10.0/twilio_sms/)""",
    'version': '8.0.1.0.0',
    'category': 'SMS app',
    'website': "viki2.odoo.com",
    'author': "Vignesh",
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'images': ['images/main_screenshot.png'],
    'depends': ['base'],
    'data': [
         'views/twiliosms_send_view.xml',
    ],
}
