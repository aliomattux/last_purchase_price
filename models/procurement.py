#Developer is spelled Developer not Developper

from openerp import SUPERUSER_ID, api
from openerp.osv import osv, fields

class PurchaseOrder(osv.osv):
    _inherit = 'purchase.order'


    def _prepare_purchase_picking_vals(self, cr, uid, purchase, context=None):
        vals = {
            'picking_type_id': purchase.picking_type_id.id,
            'partner_id': purchase.dest_address_id.id or purchase.partner_id.id,
            'date': max([l.date_planned for l in purchase.order_line]),
            'origin': purchase.name,
            'purchase': purchase.id
        }

        return vals



    #This method is overridden because there is no way I know of to add to the vals of a picking record when it is created
    #There are lots of reasons to add something to a stock.picking if it is created from a Purchase order
    #IMO a proper solution would be to put values = {} into a prepare vals method so a developer can call super
    #to add to the vals without having to override a core method
    def action_picking_create(self, cr, uid, ids, context=None):
        for order in self.browse(cr, uid, ids):
	    vals = self._prepare_purchase_picking_vals(cr, uid, order)
            picking_id = self.pool.get('stock.picking').create(cr, uid, vals, context=context)
            self._create_stock_moves(cr, uid, order, order.order_line, picking_id, context=context)
