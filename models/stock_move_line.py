# -*- coding: utf-8 -*- 

from odoo import models,fields,api,_
from odoo.exceptions import ValidationError


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"


    def _action_done(self):
        # The assumption here is the all move lines comes from the same object (picking,mrp_production)
        picking = self.mapped('picking_id')
        if picking and picking.picking_type_id.code == 'incoming' and picking.purchase_id:
            return super(StockMoveLine, self.with_context(purchase_order_id=picking.purchase_id))._action_done()
        else:
            return super(StockMoveLine, self)._action_done()



    

