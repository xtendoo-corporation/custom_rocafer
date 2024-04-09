{
    "name": "Rocafer Custom",
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
        'mrp',
    ],
    "data": [
        'views/product_template_view.xml',
        'views/print_orientation_view.xml',
        'security/ir.model.access.csv',
    ],
    "installable": True,
}
