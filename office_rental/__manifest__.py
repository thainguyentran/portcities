# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Office Rental",
    "version": "15.0.0.0.1",
    "sequence": 1,
    "author": "Nguyen Tran",
    "website": "https://github.com/thainguyentran",
    "depends": ["base"
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/contract_sequence.xml",
        "views/building.xml",
        "views/office.xml",
        "views/contract.xml",
        "views/tenant.xml",
        "views/menu.xml"
    ],
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
