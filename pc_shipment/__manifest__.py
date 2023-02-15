# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "PC Shipment",
    "version": "15.0.0.0.1",
    "sequence": 1,
    "author": "Nguyen Tran",
    "website": "https://github.com/thainguyentran",
    "depends": ["base"
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/delivery_request_sequence.xml",
        "views/delivery_request.xml",
        "views/product_move.xml",
        "views/product.xml",
        "views/warehouse.xml",
        "views/location.xml",
        "views/menu.xml",

    ],
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
