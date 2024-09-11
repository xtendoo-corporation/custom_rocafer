{
    "name": "Rocafer Custom",
    "summary": "Customization view for work-order",
    "version": "17.0.1.0.0",
    "category": "Manufacturing",
    "author": "Salvador Gonzalez Xtendoo",
    "license": "LGPL-3",
    "application": True,
    "depends": [
        'base',
        'product',
        'stock',
        'purchase',
        'contacts',
        'mrp',
        'sale',
        'mrp_sale_info',
    ],
    "data": [
        'views/mrp_workorder_view.xml',
        'views/mrp_routing_workcenter_view.xml',
    ],
    "installable": True,
}
