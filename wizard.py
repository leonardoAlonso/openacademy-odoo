# -*- coding: utf-8 -*-

from odoo import  models, fields, api

class Wizard(models.TransientModel):

    def _default_session(self):
        return self.env['openacademy.session'].browse(self._context.get('active_ids'))

    _name = "openacademy.wizard"
    session_ids = fields.Many2many('openacademy.session',
                                 string="Session",
                                 required=True,
                                 default=_default_session)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    @api.multi
    def subscribe(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
        return {}