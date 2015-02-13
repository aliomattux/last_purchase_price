from openerp.osv import osv, fields

class AccountVoucher(osv.osv):
    _inherit = 'account.voucher'
    _columns = {
	'invoice': fields.many2one('account.invoice', 'Invoice'),
    }


    def update_item_cost(self, cr, uid, invoice):
	for line in invoice.invoice_line:
	    cost = line.price_unit
	    if line.product_id.standard_price != cost:
		line.product_id.standard_price = cost
	return True


    def action_move_line_create(self, cr, uid, ids, context=None):
        #Process the voucher first. If there is an error here we can easily rollback
        #If we process the external payment and encounter a voucher problem
        #we cannot rollback the payment
        res = super(AccountVoucher, self).action_move_line_create(cr, uid, ids, context)
	voucher = self.browse(cr, uid, ids[0])
	if voucher.invoice.purchase_order:
	    self.update_item_cost(cr, uid, voucher.invoice)
	return res
