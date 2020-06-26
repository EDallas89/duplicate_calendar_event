# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CalendarEvent(models.Model):

#    tag_names = fields.Char(compute='_get_tag_names')
#
#    @api.one
#    @api.depends('categ_ids')
#    def _get_tag_names(self):
#        self.tag_names = ','.join(c.name for c in self.categ_ids)
