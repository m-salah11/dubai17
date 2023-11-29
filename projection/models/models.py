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

