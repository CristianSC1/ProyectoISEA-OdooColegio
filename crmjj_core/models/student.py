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

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class OpStudentCourse(models.Model):
    _name = 'op.student.course'
    _description = 'Detalles del curso del estudiante'

    student_id = fields.Many2one('op.student', 'Estudiante', ondelete="cascade")
    course_id = fields.Many2one('op.course', 'Curso', required=True)
    batch_id = fields.Many2one('op.batch', 'Lote', required=True)
    roll_number = fields.Char('Número de rollo')
    category_id = fields.Many2one('op.category', 'Categoría')
    subject_ids = fields.Many2many('op.subject', string='Asignaturas')

    _sql_constraints = [
        ('unique_name_roll_number_id',
         'unique(roll_number,course_id,batch_id,student_id)',
         'Roll Number & Student must be unique per Batch!'),
        ('unique_name_roll_number_course_id',
         'unique(roll_number,course_id,batch_id)',
         'Roll Number must be unique per Batch!'),
        ('unique_name_roll_number_student_id',
         'unique(student_id,course_id,batch_id)',
         'Student must be unique per Batch!'),
    ]



    
class OpStudent(models.Model):
    _name = 'op.student'
    _inherits = {'res.partner':'partner_id'}
    
    middle_name = fields.Char('Primer apellido', size=128)
    last_name = fields.Char('Segundo apellido', size=128)
    birth_date = fields.Date('Fecha de nacimiento')
    gender = fields.Selection(
        [('m', 'Masculino'), ('f', 'Mujer'),
         ('o', 'Otros')], 'Género')
    nationality = fields.Many2one('res.country', 'Nacionalidad')
    classroom_id = fields.Many2one('op.classroom', 'Salón de clases')
    mobile = fields.Char(
        'Mobil', size=16)
    already_partner = fields.Boolean('Ya socio')
    partner_id = fields.Many2one(
        'res.partner', 'Compañero', required=True, ondelete="cascade")
    gr_no = fields.Char("GR Number", size=20)
    category_id = fields.Many2one('op.category', 'Categoría')
    course_detail_ids = fields.One2many('op.student.course', 'student_id',
                                        'Detalles del curso')

    @api.multi
    @api.constrains('birth_date')
    def _check_birthdate(self):
        for record in self:
            if record.birth_date > fields.Date.today():
                raise ValidationError(_(
                    "La fecha de nacimiento no puede ser mayor que la fecha actual!"))
