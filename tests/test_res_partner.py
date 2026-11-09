from odoo.tests.common import TransactionCase


class TestSaudiPartnerIdentity(TransactionCase):
    def test_identity_reference_is_trimmed(self):
        partner = self.env["res.partner"].create(
            {"name": "Saudi Contact", "sa_national_id": "  CR-123/ABC  "}
        )
        self.assertEqual(partner.sa_national_id, "CR-123/ABC")

    def test_identity_reference_accepts_short_values(self):
        partner = self.env["res.partner"].create(
            {"name": "Other Contact", "sa_national_id": "12345"}
        )
        self.assertEqual(partner.sa_national_id, "12345")
