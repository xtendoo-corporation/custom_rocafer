{
    "name": "Rocafer Work_order Custom",
    "summary": "Customization for work-order",
    "version": "17.0.1.0.0",
    "category": "Products",
    "author": "Manuel Calero, Salvador Gonzalez, Abraham Carrasco, Xtendoo",
    "license": "LGPL-3",
    "application": True,
    "depends": [
        'product',
        'contacts',
        'stock',
    ],
    "data": [
        'views/product_template_view.xml',
        'views/varnish_type_view.xml',
        'views/stamping_option_view.xml',
        'security/ir.model.access.csv',
    ],
    "installable": True,
}
