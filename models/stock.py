from openerp.osv import osv, fields

class StockPicking(osv.osv):
    _inherit = 'stock.picking'
    _columns = {
	'purchase': fields.many2one('purchase.order', 'Purchase Order'),
    }

    def action_invoice_create(self, cr, uid, ids, journal_id, group=False, \
        type='out_invoice', context=None
        ):

        invoices = super(StockPicking, self).action_invoice_create(cr, uid, ids, journal_id, \
                group=False, type='out_invoice', context=None
        )

        print 'INVOICES', invoices

        return invoices

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
