from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError
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

    # ENR Number Generate
    enr_number = fields.Char(string="Enrollment Number", copy=False, readonly=True,
                             index=True, default=lambda self: _(''))

    @api.model
    def create(self, vals):
        record = super(SchoolManagement, self).create(vals)
        record.enr_number = "ENR" + str(record.id).zfill(3)
        return record

    # Address field
    address_line1 = fields.Char(string="Address Line 1")
    address_line2 = fields.Char(string="Address Line 2")
    city = fields.Char(string="City")
    state = fields.Many2one('res.country.state',
                            domain="[('country_id', '=', country)]")
    zip = fields.Char(string="Zip/Postal Code")
    country = fields.Many2one('res.country')

    phone_no = fields.Char(string="Phone Number", tracking=True, required=True)
    dob = fields.Date(string="Date of Birth", required=True)

    # age
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
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
                    raise UserError("Kids under 4 years old are not allowed.")

    @api.onchange('dob')
    def _onchange_dob(self):
        if self.dob:
            self._compute_age()

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
    result = fields.Char()
    family_history = fields.Char(readonly='1')

    # Allocate a class teacher
    @api.onchange('standard', 'student_division')
    def _onchange_standard_student_division(self):
        if self.standard and self.student_division:
            teacher = self.env['teacher.management'].search([
                ('standard', '=', self.standard),
                ('division', '=', self.student_division)
            ], limit=1)
            self.class_teacher = teacher.id if teacher else False

    # Phone number restriction

    @api.constrains('phone_no')
    def _check_phone_number(self):
        for record in self:
            if record.phone_no and len(record.phone_no) != 10:
                raise UserError(
                    "Check your number; it should not exceed 10 digits.")
            if record.phone_no:
                existing_record = self.search(
                    [('phone_no', '=', record.phone_no), ('id', '!=', record.id)], limit=1)
                if existing_record:
                    raise UserError(
                        "This phone number already exists. Please correct it or contact the admin.")

    # Group by similar people of the same birthdate
    @api.depends('dob')
    def _compute_birth_month(self):
        for record in self:
            if record.dob:
                birth_date = fields.Date.from_string(record.dob)
                record.birth_month = birth_date.strftime('%B')
            else:
                record.birth_month = False

    def school_management_heading(self):

        pass

# server action
    def result_passed(self):
        for record in self:
            if not record.result:
                record.result = "Passed"

# url action
    def done_button(self):
        return {
            'type': 'ir.actions.act_url',
            'url': 'https://www.odoo.com'
        }
