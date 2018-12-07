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


class OpAttendanceSheet(models.Model):
    _name = 'op.attendance.sheet'
    _inherit = ['mail.thread']

    @api.multi
    @api.depends('attendance_line.present')
    def _compute_total_present(self):
        for record in self:
            record.total_present = self.env['op.attendance.line'].search_count(
                [('present', '=', True), ('attendance_id', '=', record.id)])

    @api.multi
    @api.depends('attendance_line.present')
    def _compute_total_absent(self):
        for record in self:
            record.total_absent = self.env['op.attendance.line'].search_count(
                [('present', '=', False), ('attendance_id', '=', record.id)])

    name = fields.Char('Nombre', required=True, size=32)
    register_id = fields.Many2one(
        'op.attendance.register', 'Registro', required=True,
        track_visibility="onchange")
    course_id = fields.Many2one(
        'op.course', related='register_id.course_id', store=True,
        readonly=True)
    
    session_id = fields.Many2one('op.session', 'Sesión')
    attendance_date = fields.Date(
        'Date', required=True, default=lambda self: fields.Date.today(),
        track_visibility="onchange")
    attendance_line = fields.One2many(
        'op.attendance.line', 'attendance_id', 'Linea de asistencia')
    total_present = fields.Integer(
        'Presente total', compute='_compute_total_present',
        track_visibility="onchange")
    total_absent = fields.Integer(
        'Total ausente', compute='_compute_total_absent',
        track_visibility="onchange")
    faculty_id = fields.Many2one('op.faculty', 'Facultad')

    _sql_constraints = [
        ('unique_register_sheet',
         'unique(register_id,session_id,attendance_date)',
         'Sheet must be unique per Register/Session.'),
    ]
