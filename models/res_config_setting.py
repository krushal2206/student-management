from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    global_field = fields.Char("Global Field", config_parameter="school_management.global_field")