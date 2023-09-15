from odoo import http


class SchoolInfo(http.Controller):

    @http.route('/schools/', auth="public", type="json", methods=['POST'])
    def all_schools(self):
        schools = http.request.env['school.info'].search_read(
            [], ['school_name', 'country_id', 'state_id', 'image'])
        return schools
