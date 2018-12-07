# -*- coding: utf-8 -*-
##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
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
##############################################################################
from odoo import models, api, fields, exceptions, _


class OpFeesTermsLine(models.Model):
    _name = 'op.fees.terms.line'
    _rec_name = 'due_days'

    due_days = fields.Integer('Días de vencimiento')
    value = fields.Float('Valor (%)')
    fees_id = fields.Many2one('op.fees.terms', 'Fees')


class OpFeesTerms(models.Model):
    _name = 'op.fees.terms'

    name = fields.Char('Términos de tarifas', required=True)
    active = fields.Boolean('Activo', default=True)
    note = fields.Text('Descripción')
    company_id = fields.Many2one('res.company', 'Compañia', required=True,
                                 default=lambda self: self.env.user.company_id)
    no_days = fields.Integer('No de dias')
    day_type = fields.Selection([('before', 'antes de'), ('after', 'Despues')],
                                'Type')
    line_ids = fields.One2many('op.fees.terms.line', 'fees_id', 'Condiciones')

    @api.model
    def create(self, vals):
        res = super(OpFeesTerms, self).create(vals)
        if not res.line_ids:
            raise exceptions.AccessError(_("Honorarios Términos deben ser requeridos!"))
        total = 0.0
        for line in res.line_ids:
            if line.value:
                total += line.value
        if total != 100.0:
            raise exceptions.AccessError(_("Los términos de las tarifas deben ser divididos \
            como tal resumen en 100%"))
        return res
