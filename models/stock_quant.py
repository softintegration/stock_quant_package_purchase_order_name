# -*- coding: utf-8 -*- 

from odoo import models,fields,api,_
from odoo.exceptions import ValidationError


class QuantPackage(models.Model):
    _inherit = "stock.quant.package"

    purchase_order_id = fields.Many2one('purchase.order',string='Purchase order reference',readonly=True)
    
    
class StockQuant(models.Model):
    _inherit = "stock.quant"
    
    @api.model
    def create(self, vals):
        if vals.get('package_id') and self.env.context.get('purchase_order_id'):
            pack = self.env['stock.quant.package'].browse(vals.get('package_id'))
            if not pack.purchase_order_id:
                pack.purchase_order_id = self.env.context.get('purchase_order_id').id
        return super(StockQuant, self).create(vals)
    

