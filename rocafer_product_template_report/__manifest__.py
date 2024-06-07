{
    "name": "Rocafer Custom Order Report",
    "summary": "Customization for work-order report",
    "version": "17.0.1.0.0",
    "category": "Products",
    "author": "Manuel Calero, Salvador Gonzalez, Abraham Carrasco, Xtendoo",
    "license": "LGPL-3",
    "application": True,
    "depends": [
        'product',
        'rocafer_product_template',
    ],
    "data": [
        "views/report_order_product_rocafer.xml",
        "views/report_product_rocafer.xml",
        "reports/rocafer_report.xml",
    ],
    "installable": True,
}
