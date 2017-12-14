from odoo import api, fields, models
from datetime import date, datetime


class Transaction(models.Model):
    _name = 'transaction'
    _description = 'Transaction Module'

    transaction_id  = fields.Char('Transaction ID', copy=False, readonly=True, default=lambda x: str('New Transaction'))
    time_now        = fields.Datetime('Time Transfer', required=True, readonly=True , default=lambda self: fields.datetime.now())
    name_sender     = fields.Many2one('res.partner')
    name_recever    = fields.Many2one('res.partner')
    amount          = fields.Float(string='amount')
    supp_test_field = fields.Char(string="test field")
    file_name       = fields.Char('File Name')
    attachment_docs = fields.Binary('Docs')
    fees            = fields.Integer(string='fees')
    Totalammo       = fields.Float(string='Total transfer after commission', store=True, compute="_calcolatetotaltrans", readonly=True)
    currency_id     = fields.Many2one('res.currency', string='Currency',default=lambda self: self.env.user.company_id.currency_id)

    @api.model
    def create(self, vals):
        if not vals.get('transaction_id'):
            vals['transaction_id'] = self.env['ir.sequence'].next_by_code('transaction') or str('New')
        transref = super(Transaction, self).create(vals)
        return transref

    @api.one
    @api.depends('fees', 'amount')
    def _calcolatetotaltrans(self):
        total = self.amount - self.fees
        self.Totalammo = total
