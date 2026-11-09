# FlousFlow Saudi Partner Identity

Odoo 20 Community addon that adds an optional Saudi National ID field to
`res.partner` and displays it on the standard contact form.

The field accepts any non-empty text value, covering Saudi national IDs,
residency IDs, commercial registration numbers, and other identity references.
Leading and trailing spaces are removed. It does not enforce uniqueness because
the same person or reference may be represented in multiple companies or
databases.

## Installation

Install `ff_saudi_partner_identity` from the Odoo Apps menu or with the Odoo
command line on the target database.
