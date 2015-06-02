from openerp.osv import orm, fields,osv
from openerp.osv.osv import except_osv
from openerp.tools.translate import _
from openerp import netsvc

class Custom(osv.osv):
    '''Custom'''

    _inherit = 'res.partner'

    _columns = {
        'phone_sec': fields.char('Secondary Phone',size=64),
    }

Custom()