#-*- coding:utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 OpenERP SA (<http://openerp.com>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api


class RegionWiseDetail(models.Model):
    _name = "sale.invoice.summary"

    form = fields.Date("From")
    to = fields.Date("To")
    invoice_to = fields.Char(string="Invoice To")
    invoice_from = fields.Char(string="Invoice From")
    slect_cust = fields.Many2many('res.partner',string="Select Customer")
    customer = fields.Selection([('all_cust','All Customer'),('spec_cust','Specfic Customer')],string="Customer")

class regionWiseDetail(models.Model):
    _inherit = "account.invoice"    

    @api.multi
    def create_report(self):
        return {
        'type': 'ir.actions.act_window',
        'name': 'Sale Invoice Summary',
        'res_model': 'sale.invoice.summary',
        'view_type': 'form',
        'view_mode': 'form',
        'target' : 'new',
        }
    
    
