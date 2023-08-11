from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date


class SchoolManagement(models.Model):
    _name = "school.management"
    _description = "School Management"
    _rec_name = "student_name"
    _inherit = ['mail.thread']

    global_field = fields.Char(string="Global Field")
    student_name = fields.Char(string="Name", required=True)
    standard = fields.Integer(string="Standard")
    student_division = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
    ], string='Division')
    roll_number = fields.Char(string="Roll Number")

    # ENR Number Generate
    enr_number = fields.Char(string="Enrollment Number", copy=False, readonly=True,
                             index=True, default=lambda self: _(''))
    image = fields.Image(string="Image")

    @api.model
    def create(self, vals):
        record = super(SchoolManagement, self).create(vals)
        record.enr_number = "ENR" + str(record.id).zfill(3)
        print(type(record), "It's Return a Object")
        return record

# this is for updated li 
        

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
        'teacher.management', string="Class Teacher")

    stream = fields.Selection([
        ('Science', 'Science'),
        ('Commerce', 'Commerce'),
        ('Arts', 'Arts')
    ], string="Stream")
    birth_month = fields.Char(compute='_compute_birth_month', store=True)
    result = fields.Char()
    family_history = fields.Char(readonly='1')
    student_email=fields.Char(string="Student Email")
    

    # Behaviour of Compute field with store true and false, and with depends and without depends.
    fees = fields.Float(string='Fees', digits=(10, 2))
    discount = fields.Float(string='Discount (%)', digits=(5, 2))
    discounted_fees = fields.Float(string='Discounted Price', digits=(
        10, 2), compute='_compute_discounted_fees', store=False)

    @api.depends('fees', 'discount')
    def _compute_discounted_fees(self):
        for product in self:
            product.discounted_fees = product.fees * \
                (1 - (product.discount / 100))

    # Allocate a class teacher
    @api.onchange('standard', 'student_division')
    def _onchange_standard_student_division(self):
        print("Onchange triggered!")
        if self.standard and self.student_division:
            print(f"Standard: {self.standard}, Division: {self.student_division}")
            teacher = self.env['teacher.management'].search([
                ('standard', '=', self.standard),
                ('division', '=', self.student_division)
            ], limit=1)
            print(f"Found Teacher: {teacher.teacher_name if teacher else None}")
            self.class_teacher = teacher or False


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
# Email template 
    def email_temp(self):
        mail_template = self.env.ref('school_management.school_email_template')
        mail_template.send_mail(self.id, force_send=True)

    @api.model
    def send_confirmation_email(self):
        print("HHHHHHHHHHHHHHH")
        confirmed_students = self.search([('admission_date', '!=', False), ('leaving_date', '!=', False)])
        print(confirmed_students)

        for student in confirmed_students:
            student.email_temp()

    @api.model
    def send_confirmation_email_cron(self):
        self.send_confirmation_email()

# PSQL Queries along with Table JOINS 
    def action_psql_queries(self):
        # query = """SELECT student_name, standard FROM school_management"""
        # query = """SELECT student_name, standard FROM school_management WHERE standard = '11'"""
        # query = """SELECT student_name, standard FROM school_management WHERE standard = '11'"""
        query = """UPDATE school_management SET student_name='Kevin' WHERE id=1"""
        
        self.env.cr.execute(query)
        # res = self.env.cr.fetchall()
        # print(res)