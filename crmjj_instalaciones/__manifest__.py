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
    'name': 'CRMJJ Instalaciones',
    'version': '11.0.1.0.0',
    'license': 'LGPL-3',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Gestionar Facilidad',
    'complexity': "easy",
    'author': 'CRMJJ',
    'website': 'http://www.openeducat.org',
    'depends': ['crmjj_core'],
    'data': [
        'views/facility_view.xml',
        'views/facility_line_view.xml',
        'security/ir.model.access.csv',
        'facility_menu.xml',
    ],
    'demo': [
        'demo/facility_demo.xml'
    ],
    'images': [
        'static/description/openeducat_facility_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
