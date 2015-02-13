from openerp.osv import osv, fields

class StockPicking(osv.osv):
    _inherit = 'stock.picking'
    _columns = {
	'purchase': fields.many2one('purchase.order', 'Purchase Order'),
    }


    def _get_invoice_vals(self, cr, uid, key, inv_type, journal_id, move, context=None):
	invoice_vals = super(StockPicking, self)._get_invoice_vals(cr, uid, key, inv_type, journal_id, \
		move, context=context
	)

	#add the purchase name into the origin so it can be searched for in invoices
	if move.picking_id.purchase:
            origin = move.picking_id.purchase.name + '/' + move.picking_id.name
	    invoice_vals.update({'purchase_order': move.picking_id.purchase.id,
				 'origin': origin
	    })

	return invoice_vals


