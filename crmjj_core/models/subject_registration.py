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


class OpSubjectRegistration(models.Model):
    _name = 'op.subject.registration'
    _inherit = ['mail.thread']

    name = fields.Char('Nombre', readonly=True, default='New')
    category_id = fields.Many2one('op.category', 'Categoría')
    student_id = fields.Many2one('op.student', 'Estudiante', required=True,
                                 track_visibility='onchange')
    course_id = fields.Many2one('op.course', 'Curso', required=True,
                                track_visibility='onchange')
    batch_id = fields.Many2one('op.batch', 'Lote', required=True,
                               track_visibility='onchange')
    compulsory_subject_ids = fields.Many2many(
        'op.subject', 'subject_compulsory_rel',
        'register_id', 'subject_id', string="Sujetos compulsivos",
        readonly=True)
    elective_subject_ids = fields.Many2many(
        'op.subject', string="Materias electivas")
    state = fields.Selection([
        ('draft', 'Borrador'), ('submitted', 'Presentado'),
        ('approved', 'Aprobado'), ('rejected', 'Rechazado')],
        default='draft', string='estado', copy=False,
        track_visibility='onchange')
    max_unit_load = fields.Float('Unidad máxima de carga',
                                 track_visibility='onchange')
    min_unit_load = fields.Float('Unidad mínima de carga',
                                 track_visibility='onchange')

    @api.multi
    def action_reset_draft(self):
        self.state = 'draft'

    @api.multi
    def action_reject(self):
        self.state = 'rejected'

    @api.multi
    def action_approve(self):
        for record in self:
            subject_ids = []
            for sub in record.compulsory_subject_ids:
                subject_ids.append(sub.id)
            for sub in record.elective_subject_ids:
                subject_ids.append(sub.id)
            course_id = self.env['op.student.course'].search([
                ('student_id', '=', record.student_id.id),
                ('course_id', '=', record.course_id.id)
            ], limit=1)
            if course_id:
                course_id.write({
                    'subject_ids': [[6, 0, list(set(subject_ids))]]
                })
                record.state = 'approved'
            else:
                raise ValidationError(
                    _("Curso no encontrado en la admisión del estudiante!"))

    @api.multi
    def action_submitted(self):
        self.state = 'submitted'

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'op.subject.registration') or '/'
        return super(OpSubjectRegistration, self).create(vals)

    @api.multi
    def get_subjects(self):
        for record in self:
            subject_ids = []
            if record.course_id and record.course_id.subject_ids:
                for subject in record.course_id.subject_ids:
                    if subject.subject_type == 'compulsory':
                        subject_ids.append(subject.id)
            record.compulsory_subject_ids = [(6, 0, subject_ids)]
