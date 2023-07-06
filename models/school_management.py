from odoo import fields, models, api
from odoo.exceptions import UserError
from datetime import date


class SchoolManagement(models.Model):
    _name = "school.management"
    _description = "School Management"
    _rec_name = "student_name"
    _inherit = 'mail.thread'

    student_name = fields.Char(string="Name", required=True)
    standard = fields.Integer(string="Standard")
    student_division = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
    ], string='Division')
    roll_number = fields.Integer(string="Roll Number")
    enr_number = fields.Char(string="Enrollment Number",
                             compute='_compute_enr_number', store=True,)
    address_line1 = fields.Char(string="Address Line 1")
    address_line2 = fields.Char(string="Address Line 2")
    city = fields.Char(string="City")
    state = fields.Char(string="State/Province/Region")
    zip = fields.Char(string="Zip/Postal Code")
    country = fields.Char(string="Country")
    phone_no = fields.Char(string="Phone Number", tracking=True,required=True)
    dob = fields.Date(string="Date of Birth", required=True)
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    parent_name = fields.Char(string="Parent Name")
    relation = fields.Selection([
        ('mother', 'Mother'),
        ('father', 'Father'),
        ('sister', 'Sister'),
        ('brother', 'Brother'),
        ('husband', 'Husband'),
        ('wife', 'Wife'),
        ('other', 'Other')
    ], string="Relation")
    parent_phone_number = fields.Char(string="Phone Number")
    parent_email = fields.Char(string="Email")
    previous_school_name = fields.Char(string="Previous School Name")
    previous_school_enr_no = fields.Char(string="Enrollment Number")
    admission_date = fields.Date(string="Admission Date")
    leaving_date = fields.Date(string="Leaving Date")
    class_teacher = fields.Many2one(
        'teacher.management', string="Class Teacher", readonly=True)
    stream = fields.Selection([
        ('Science', 'Science'),
        ('Commerce', 'Commerce'),
        ('Arts', 'Arts')
    ], string="Stream")
    birth_month = fields.Char(compute='_compute_birth_month', store=True)

    # Allocate a class teacher
    @api.onchange('standard', 'student_division')
    def _onchange_standard_student_division(self):
        if self.standard and self.student_division:
            teacher = self.env['teacher.management'].search([
                ('standard', '=', self.standard),
                ('division', '=', self.student_division)
            ], limit=1)
            if teacher:
                self.class_teacher = teacher.id
            else:
                self.class_teacher = False
        else:
            self.class_teacher = False

    # calculate the age
    @api.depends('dob')
    def _compute_age(self):
        today = fields.Date.today()
        for record in self:
            if record.dob:
                birth_date = fields.Date.from_string(record.dob)
                age = today.year - birth_date.year
                if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
                    age -= 1
                record.age = age
                if age < 4:
                    raise UserError(
                        "Kids are not allowed you are only 4 years old!!!.")

    @api.onchange('dob')
    def _onchange_dob(self):
        if self.dob:
            self._compute_age()

    
    # enr number auto generate based on phone number
    # @api.depends('phone_no')
    # def _compute_enr_number(self):
    #     for record in self:
            
    #         if record.phone_no:
                
    #             if (len(record.phone_no) == 10):
    #                 record.enr_number = 'ENR' + record.phone_no if record.phone_no else ''
    
    @api.depends('phone_no')
    def _compute_enr_number(self):
        for record in self:
            if record.phone_no and len(record.phone_no) != 10:
                record.enr_number = 'ENR' + record.phone_no
            else:
                record.enr_number = ''

    # Phone number restriction
    @api.constrains('phone_no')
    def _check_phone_number(self):
        for record in self:
            if record.phone_no and (len(record.phone_no) != 10):
                raise UserError(
                    "Check your number it not more than 10 digit!!!")
            if record.phone_no:
                existing_records = self.search(
                    [('phone_no', '=', record.phone_no), ('id', '!=', record.id)])
                if existing_records:
                    raise UserError(
                        "This phone number is already existing, Please correct it or contact admin asap!!!.")

    # Group by similar people of same birthdate 
    @api.depends('dob')
    def _compute_birth_month(self):
        for record in self:
            if record.dob:
                birth_date = fields.Date.from_string(record.dob)
                birth_month = birth_date.strftime('%B')
                record.birth_month = birth_month
            else:
                record.birth_month = False