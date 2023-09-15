from odoo import models, fields, api


class ConfSetting(models.TransientModel):
    _inherit = "res.config.settings"
    discount_limit = fields.Boolean(
        string="Discount Limit", store=True, config_parameter="school_management.discount_limit")
