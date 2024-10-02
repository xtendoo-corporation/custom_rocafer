{
    "name": "rocafer_custom_report",
    "summary": """Formatos de documentos Rocafer""",
    "version": "17.0.1.0.0",
    "description": """Formatos de documentos Rocafer""",
    "company": "Xtendoo",
    "website": "http://www.xtendoo.es",
    "category": "Warehouse Management",
    "depends": [
        'stock',
        'stock_picking_report_valued',
    ],
    "license": "AGPL-3",
    "data": [
        "reports/stock_picking_report_valued.xml",
        "views/stock_picking_view.xml",
    ],
    "installable": True,
}
