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


    #Nothing done here yet.
#    def action_invoice_create(self, cr, uid, ids, journal_id, group=False, \
#        type='out_invoice', context=None
#        ):

#        invoices = super(StockPicking, self).action_invoice_create(cr, uid, ids, journal_id, \
 #               group=False, type='out_invoice', context=None
  #      )


   #     return invoices


####  Customer wants to update purchase price from supplier invoice not receipt.
####  If you want to update based on purchase line when receive, uncomment code below


#TODO: Possible to do multi write instead of one by one?
#Add a costing method last purchase price so its up to par with "standard" software
#How could an ERP not have a last purchase price costing method?

#class StockMove(osv.osv):
#    _inherit = 'stock.move'


#    def update_last_purchase_price(self, cr, uid, purchase_line):
#	product_obj = self.pool.get('product.product')
#	new_cost = purchase_line.price_unit
#	if new_cost != purchase_line.product_id.standard_price:
#	    purchase_line.product_id.standard_price = new_cost

#	return True


    #This seems like the easiest way to update last purchase price based on a basic review
    #An idea would be to use _check on procurement.order, but manual PO lines have no procurement
    #During and after receiving the PO line is never updated, the only way to detect the receipt is from action_done
    #Or by manipulating the memory wizard, or do_transfer(). The action_done interates over moves many times anyway...
#    def action_done(self, cr, uid, ids, context=None):
#        res = super(StockMove, self).action_done(cr, uid, ids, context=context)
#	for move in self.browse(cr, uid, ids):
#	    if move.state == 'done' and move.purchase_line_id:
#		self.update_last_purchase_price(cr, uid, move.purchase_line_id)

#	return res
