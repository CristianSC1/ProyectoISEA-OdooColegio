# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    'name': 'crmjj fees',
    'version': '11.0.1.0.0',
    'license': 'LGPL-3',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Administrar las tarifas',
    'complexity': "easy",
    'author': 'CRMJJ',
    'website': 'http://www.cristoluz.org',
    'depends': ['crmjj_core', 'account_invoicing'],
    'data': [
        'report/report_menu.xml',
        'report/fees_analysis_report_view.xml',
        'wizard/fees_detail_report_wizard_view.xml',
        'views/fees_terms_view.xml',
        'views/student_view.xml',
        'views/course_view.xml',
        'security/fees_security.xml',
        'fees_menu.xml',
        'security/ir.model.access.csv'
    ],
    'images': [
        'static/description/openeducat_fees_banner.jpg',
    ],
    'demo': [
        'demo/fees_terms_line_demo.xml',
        'demo/fees_terms_demo.xml',
        'demo/course_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
