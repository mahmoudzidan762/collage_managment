from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import json


class Subject(models.Model):
    _inherit = 'op.subject'

    subject_to_student = fields.Many2many('op.student', 'student_subject_rel', 'subject_id', 'student_id',
                                          string='Subject students')
    doctor_name = fields.Many2one('op.faculty', string='Doctor')
    doctor_name_domain = fields.Char(compute='get_doctor_name_domain')
    subject_faculty_ids = fields.Many2many('op.faculty', string='Faculty(s)')

    @api.onchange('opposite.doc_subjects')
    def get_doctor_name_domain(self):
        for rec in self:
            ids = []
            for doc in rec.subject_faculty_ids:
                ids.append(doc.id)
            rec.doctor_name_domain = json.dumps([('id', 'in', ids)])
