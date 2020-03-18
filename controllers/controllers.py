# -*- coding: utf-8 -*-
from odoo import http

class CoursesController(http.Controller):
    @http.route('/openacademy/openacademy/', auth='public', website=True)
    def index(self, **kw):
        courses = http.request.env['openacademy.course']
        return http.request.render('openacademy-odoo.index', {
            'courses': courses.search([])
        })


    @http.route('/openacademy/<model("openacademy.course"):course>/', auth='public', website=True)
    def detail(self, course):
        return http.request.render('openacademy-odoo.detail', {
            'course': course
        })
