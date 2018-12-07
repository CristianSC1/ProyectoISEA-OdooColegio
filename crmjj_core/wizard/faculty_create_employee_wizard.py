

from odoo import models, fields, api


class WizardOpFacultyEmployee(models.TransientModel):
    _name = 'wizard.op.faculty.employee'
    _description = "Crear empleado y usuario de la facultad"

    user_boolean = fields.Boolean("¿Quieres crear usuario también?", default=True)

    @api.multi
    def create_employee(self):
        for record in self:
            active_id = self.env.context.get('active_ids', []) or []
            faculty = self.env['op.faculty'].browse(active_id)
            faculty.create_employee()
            if record.user_boolean and not faculty.user_id:
                user_group = self.env.ref('crmjj_core.group_op_faculty')
                self.env['res.users'].create_user(faculty, user_group)
