from openerp.osv import osv, fields

class AccountInvoice(osv.osv):
    _inherit = 'account.invoice'
    _columns = {
        'purchase_order': fields.many2one('purchase.order', 'Purchase Order'),
    }
