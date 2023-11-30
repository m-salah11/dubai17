# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Project(models.Model):
    _inherit = 'project.project'

    AED = fields.Many2one('res.currency')
    USD = fields.Many2one('res.currency')
    USD_rate = fields.Float()

    jan = fields.Monetary(currency_field='AED')
    feb = fields.Monetary(currency_field='AED')
    mar = fields.Monetary(currency_field='AED')
    apr = fields.Monetary(currency_field='AED')
    may = fields.Monetary(currency_field='AED')
    jun = fields.Monetary(currency_field='AED')
    jul = fields.Monetary(currency_field='AED')
    aug = fields.Monetary(currency_field='AED')
    sep = fields.Monetary(currency_field='AED')
    oct = fields.Monetary(currency_field='AED')
    nov = fields.Monetary(currency_field='AED')
    dec = fields.Monetary(currency_field='AED')

    total_AED = fields.Monetary(compute='_compute_usd', currency_field='AED')

    jan_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')
    feb_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')
    mar_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')
    apr_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')
    may_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')
    jun_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')
    jul_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')
    aug_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')
    sep_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')
    oct_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')
    nov_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')
    dec_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')

    total_USD = fields.Monetary(compute='_compute_usd', currency_field='USD')

    def _compute_usd(self):
        for record in self:
            record.jan_usd = record.jan / record.USD_rate if record.USD_rate else 0
            record.feb_usd = record.feb / record.USD_rate if record.USD_rate else 0
            record.mar_usd = record.mar / record.USD_rate if record.USD_rate else 0
            record.apr_usd = record.apr / record.USD_rate if record.USD_rate else 0
            record.may_usd = record.may / record.USD_rate if record.USD_rate else 0
            record.jun_usd = record.jun / record.USD_rate if record.USD_rate else 0
            record.jul_usd = record.jul / record.USD_rate if record.USD_rate else 0
            record.aug_usd = record.aug / record.USD_rate if record.USD_rate else 0
            record.sep_usd = record.sep / record.USD_rate if record.USD_rate else 0
            record.oct_usd = record.oct / record.USD_rate if record.USD_rate else 0
            record.nov_usd = record.nov / record.USD_rate if record.USD_rate else 0
            record.dec_usd = record.dec / record.USD_rate if record.USD_rate else 0
            record.total_AED = (
                    record.jan +
                    record.feb +
                    record.mar +
                    record.apr +
                    record.may +
                    record.jun +
                    record.jul +
                    record.aug +
                    record.sep +
                    record.oct +
                    record.nov +
                    record.dec
            )
            record.total_USD = record.total_AED / record.USD_rate if record.USD_rate else 0


class Projection(models.Model):
    _name = 'project.projection'
    _description = 'project.projection'
    _inherit = ['portal.mixin', 'mail.alias.mixin', 'rating.parent.mixin', 'mail.thread', 'mail.activity.mixin']

    def create_project(self):
        if not self.project_id:
            project = self.env['project.project'].create({
                'name': self.name,
                'user_id': self.user_id.id,
                'partner_id': self.partner_id.id,
                'date_start': self.date_start,
                'AED': self.AED.id,
                'USD': self.USD.id,
                'USD_rate': self.USD_rate,
                'jan': self.jan,
                'feb': self.feb,
                'mar': self.mar,
                'apr': self.apr,
                'may': self.may,
                'jun': self.jun,
                'jul': self.jul,
                'aug': self.aug,
                'sep': self.sep,
                'oct': self.oct,
                'nov': self.nov,
                'dec': self.dec,
            })

            self.project_id = project

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'project.project',
            'view_mode': 'form',
            'res_id': self.project_id.id,
            'target': 'current',
        }

    project_id = fields.Many2one(
        comodel_name='project.project',
        required=False)

    name = fields.Char(required=1)
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Project Manager',
        required=False)

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Customer',
        required=False)

    date_start = fields.Date(
        string='Planned Date',
        required=False)

    AED = fields.Many2one('res.currency')
    USD = fields.Many2one('res.currency')
    USD_rate = fields.Float()

    jan = fields.Monetary(currency_field='AED')
    feb = fields.Monetary(currency_field='AED')
    mar = fields.Monetary(currency_field='AED')
    apr = fields.Monetary(currency_field='AED')
    may = fields.Monetary(currency_field='AED')
    jun = fields.Monetary(currency_field='AED')
    jul = fields.Monetary(currency_field='AED')
    aug = fields.Monetary(currency_field='AED')
    sep = fields.Monetary(currency_field='AED')
    oct = fields.Monetary(currency_field='AED')
    nov = fields.Monetary(currency_field='AED')
    dec = fields.Monetary(currency_field='AED')

    total_AED = fields.Monetary(compute='_compute_usd', currency_field='AED')

    jan_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')
    feb_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')
    mar_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')
    apr_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')
    may_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')
    jun_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')
    jul_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')
    aug_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')
    sep_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')
    oct_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')
    nov_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')
    dec_usd = fields.Monetary(compute='_compute_usd', currency_field='USD')

    total_USD = fields.Monetary(compute='_compute_usd', currency_field='USD')

    def _compute_usd(self):
        for record in self:
            record.jan_usd = record.jan / record.USD_rate if record.USD_rate else 0
            record.feb_usd = record.feb / record.USD_rate if record.USD_rate else 0
            record.mar_usd = record.mar / record.USD_rate if record.USD_rate else 0
            record.apr_usd = record.apr / record.USD_rate if record.USD_rate else 0
            record.may_usd = record.may / record.USD_rate if record.USD_rate else 0
            record.jun_usd = record.jun / record.USD_rate if record.USD_rate else 0
            record.jul_usd = record.jul / record.USD_rate if record.USD_rate else 0
            record.aug_usd = record.aug / record.USD_rate if record.USD_rate else 0
            record.sep_usd = record.sep / record.USD_rate if record.USD_rate else 0
            record.oct_usd = record.oct / record.USD_rate if record.USD_rate else 0
            record.nov_usd = record.nov / record.USD_rate if record.USD_rate else 0
            record.dec_usd = record.dec / record.USD_rate if record.USD_rate else 0
            record.total_AED = (
                    record.jan +
                    record.feb +
                    record.mar +
                    record.apr +
                    record.may +
                    record.jun +
                    record.jul +
                    record.aug +
                    record.sep +
                    record.oct +
                    record.nov +
                    record.dec
            )
            record.total_USD = record.total_AED / record.USD_rate if record.USD_rate else 0
