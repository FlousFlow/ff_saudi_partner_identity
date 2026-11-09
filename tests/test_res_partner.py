from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase


class TestSaudiPartnerIdentity(TransactionCase):
    def test_valid_national_id(self):
        partner = self.env["res.partner"].create(
            {"name": "Saudi Contact", "sa_national_id": " 1012345678 "}
        )
        self.assertEqual(partner.sa_national_id, "1012345678")

    def test_invalid_national_id(self):
        with self.assertRaises(ValidationError):
            self.env["res.partner"].create(
                {"name": "Invalid Contact", "sa_national_id": "12345"}
            )
