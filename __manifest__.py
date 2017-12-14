# -*- coding: utf-8 -*-
{
    'name': "Transaction",
    'summary': "Transaction bMs",
    'category': 'transactions',
    'version': '1.0',
    'depends': ['base', 'web'],
    'data': [
             'security/user_groups.xml',
             'security/ir.model.access.csv',
             'views/view.xml',
             'report/report.xml',
             ],
    'application': True,
    'installable': True,
    'images': ['static\description\icon.png'],
}