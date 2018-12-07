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

from odoo import models, fields, api


class OpClassroom(models.Model):
    _name = 'op.classroom'

    name = fields.Char('Nombre', size=16, required=True)
    code = fields.Char('Codigo', size=16, required=True)
 
    capacity = fields.Integer(string='No de persona')
    facilities = fields.One2many(
        'op.facility.line', 'classroom_id', string='Lineas de Instalaciones')
    asset_line = fields.One2many('op.asset', 'asset_id', 'Activo')

    _sql_constraints = [
        ('unique_classroom_code',
         'unique(code)', 'Code should be unique per classroom!')]

   