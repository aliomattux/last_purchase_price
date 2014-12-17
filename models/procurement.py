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
