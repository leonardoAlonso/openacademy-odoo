# -*- coding: utf-8 -*-

from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    # add new field to partner

    instructor = fields.Boolean("Instructor", default=False)
    session_ids = fields.Many2many('openacademy.session', string="Attended Session", readonly=True)