from openerp.osv import osv, fields

class AccountInvoice(osv.osv):
    _inherit = 'account.invoice'
    _columns = {
        'purchase_order': fields.many2one('purchase.order', 'Purchase Order'),
    }



    def invoice_pay_customer(self, cr, uid, ids, context=None):
	invoice = self.browse(cr, uid, ids[0])
        vals = super(AccountInvoice, self).invoice_pay_customer(cr, uid, ids, context=context)
        if not vals['context'].get('default_invoice'):
	    vals['context']['default_invoice'] = invoice.id

	return vals
