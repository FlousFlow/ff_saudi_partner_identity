{
    "name": "FlousFlow Saudi Partner Identity",
    "summary": "Store and validate Saudi national IDs on contacts.",
    "description": """
FlousFlow Saudi Partner Identity
================================

Adds an optional Saudi national ID field to contacts. When provided, the
value is validated as a ten-digit Saudi national ID or residency ID beginning
with 1 or 2.
""",
    "version": "20.0.1.0.1",
    "category": "Contacts",
    "author": "FlousFlow",
    "maintainer": "FlousFlow",
    "website": "https://flousflow.com",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "views/res_partner_views.xml",
    ],
    "installable": True,
    "application": False,
}
