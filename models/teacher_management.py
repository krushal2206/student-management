from odoo import fields, models


class TeacherManagement(models.Model):
    _name = "teacher.management"
    _description = "Teacher Management"
    _rec_name = "teacher_name"

    teacher_name = fields.Char(string="Teacher Name")
    division = fields.Char(string='Division')
    standard = fields.Char(string="Standard")
