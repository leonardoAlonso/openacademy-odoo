# -*- coding: utf-8 -*-

from odoo import  models, fields, api

class Wizard(models.TransientModel):

    def _default_session(self):
        return self.env['openacademy.session'].browse(self._context.get('active_id'))

    _name = "openacademy.wizard"
    session_id = fields.Many2one('openacademy.session',
                                 string="Session",
                                 required=True,
                                 default=_default_session)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")