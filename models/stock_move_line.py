# -*- coding: utf-8 -*- 

from odoo import models,fields,api,_
from odoo.exceptions import ValidationError


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    def _action_done(self):
        try:
            picking = self.mapped('picking_id')[0]
        except IndexError as ie:
            return super(StockMoveLine, self)._action_done()
        if picking.picking_type_id.code == 'incoming' and picking.purchase_id:
            return super(StockMoveLine, self.with_context(purchase_order_id=picking.purchase_id))._action_done()
        else:
            return super(StockMoveLine, self)._action_done()


    

