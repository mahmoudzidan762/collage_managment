from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import json


class Student(models.Model):
    _inherit = 'op.student'

    student_to_subject = fields.Many2many('op.subject', 'student_subject_rel', 'student_id', 'subject_id',
                                          string='Student subjects')
    doctor_name = fields.Many2one('op.faculty', string='Doctor')
    doctor_subject = fields.One2many('doctor.subject', 'student_id', string='Student subjects')
    mid_term_exam = fields.Float(string="ميد تيرم")
    practical_exam = fields.Float(string="الاعمال الفصلية")
    final_exam = fields.Float(string="النظري النهائي")
    total_practical_marks = fields.Float(string="المجموع الكلي للاعمال الفصلية")
    total_theoretical_marks = fields.Float(string="النظري الكلي")
    total_marks = fields.Float(string="المجموع الكلي")
    percentage = fields.Float(string="النسبة المؤية")
    grade = fields.Char(string='الرمز')
