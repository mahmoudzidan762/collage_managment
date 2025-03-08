from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import json


class DoctorSheetTable(models.Model):
    _name = 'doctor.sheet.table'

    opposite = fields.Many2one('doctor.sheet')
    students_name = fields.Many2one('op.student', string='اسم الطالب')
    mid_term_exam = fields.Float(string="ميد تيرم")
    practical_exam = fields.Float(string="الاعمال الفصلية")
    final_exam = fields.Float(string="النظري النهائي")
    total_practical_marks = fields.Float(string="المجموع الكلي للاعمال الفصلية")
    total_theoretical_marks = fields.Float(string="النظري الكلي")
    total_marks = fields.Float(string="المجموع الكلي")
    percentage = fields.Float(string="النسبة المؤية")
    grade = fields.Char(string='الرمز')







