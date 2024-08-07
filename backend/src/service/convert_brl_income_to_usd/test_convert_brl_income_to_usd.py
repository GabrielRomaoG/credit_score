import unittest
from src.service.convert_brl_income_to_usd.convert_brl_income_to_usd import (
    BrlIncomeToUsdConverter,
)


class TestIncomeConverter(unittest.TestCase):

    def setUp(self):
        self.service = BrlIncomeToUsdConverter()

    def test_calculate_equivalent_usd_income(self):
        # Test typical income
        brl_income = 5000
        expected_usd_income = (
            (brl_income / BrlIncomeToUsdConverter.PURCHASE_POWER_RATE)
            * (
                BrlIncomeToUsdConverter.COST_OF_LIVING_INDEX_BRAZIL
                / BrlIncomeToUsdConverter.COST_OF_LIVING_INDEX_USA
            )
            * (
                BrlIncomeToUsdConverter.AVERAGE_MONTHLY_INCOME_USA_IN_USD
                / BrlIncomeToUsdConverter.AVERAGE_MONTHLY_INCOME_BRAZIL_IN_BRL
            )
        )

        result = self.service.calculate_equivalent_usd_income(brl_income)
        self.assertIsInstance(result, int)
        self.assertEqual(
            result,
            int(round(expected_usd_income)),
        )

    def test_zero_income(self):
        # Test zero income
        brl_income = 0
        expected_usd_income = 0
        self.assertEqual(
            self.service.calculate_equivalent_usd_income(brl_income),
            expected_usd_income,
        )

    def test_high_income(self):
        # Test very high income
        brl_income = 100000
        expected_usd_income = (
            (brl_income / BrlIncomeToUsdConverter.PURCHASE_POWER_RATE)
            * (
                BrlIncomeToUsdConverter.COST_OF_LIVING_INDEX_BRAZIL
                / BrlIncomeToUsdConverter.COST_OF_LIVING_INDEX_USA
            )
            * (
                BrlIncomeToUsdConverter.AVERAGE_MONTHLY_INCOME_USA_IN_USD
                / BrlIncomeToUsdConverter.AVERAGE_MONTHLY_INCOME_BRAZIL_IN_BRL
            )
        )
        self.assertEqual(
            self.service.calculate_equivalent_usd_income(brl_income),
            int(round(expected_usd_income)),
        )

    def test_negative_income(self):
        # Test negative income
        brl_income = -1000
        with self.assertRaises(ValueError) as context:
            self.service.calculate_equivalent_usd_income(brl_income)

        self.assertEqual(str(context.exception), "Monthly BRL income is negative.")
