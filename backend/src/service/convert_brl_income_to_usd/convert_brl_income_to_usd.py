from logging import Logger, getLogger

log: Logger = getLogger(__name__)


class BrlIncomeToUsdConverter:
    """
    A class to convert Brazilian monthly income (BRL) to an equivalent American monthly income (USD).
    """

    PURCHASE_POWER_RATE = 2.0
    COST_OF_LIVING_INDEX_BRAZIL = 40
    COST_OF_LIVING_INDEX_USA = 70
    AVERAGE_MONTHLY_INCOME_BRAZIL_IN_BRL = 2500
    AVERAGE_MONTHLY_INCOME_USA_IN_USD = 5000

    def calculate_equivalent_usd_income(self, brl_monthly_income: int) -> int:
        """
        Calculates the equivalent monthly income in USD for a given monthly income in BRL.

        Args:
            brl_monthly_income (int): The monthly income in BRL.

        Returns:
            int: The equivalent monthly income in USD.

        The function calculates the equivalent monthly income in USD for a given monthly income in BRL. It does this by
        converting the BRL income to USD using the PPP (Purchasing Power Parity) and adjusting it based on the cost of
        living index. The income ratio is calculated using the average monthly income in USD and BRL.

        The function first calculates the income ratio by dividing the average monthly income in USD by the average
        monthly income in BRL. It then converts the BRL income to USD using the PPP by dividing it by the purchase power
        rate. The adjusted USD income is calculated by multiplying the USD income obtained from the PPP conversion with
        the ratio obtained from the cost of living index. Finally, the equivalent monthly income in USD is calculated by
        multiplying the adjusted USD income with the income ratio.

        """
        try:
            if brl_monthly_income < 0:
                raise ValueError("Monthly BRL income is negative.")

            income_ratio = (
                self.AVERAGE_MONTHLY_INCOME_USA_IN_USD
                / self.AVERAGE_MONTHLY_INCOME_BRAZIL_IN_BRL
            )

            usd_income_ppp = brl_monthly_income / self.PURCHASE_POWER_RATE

            adjusted_usd_income = usd_income_ppp * (
                self.COST_OF_LIVING_INDEX_BRAZIL / self.COST_OF_LIVING_INDEX_USA
            )

            equivalent_usd_monthly_income = adjusted_usd_income * income_ratio

            return int(round(equivalent_usd_monthly_income))
        except Exception as e:
            log.error("Failed to calculate equivalent USD income: %s", e)
            raise e
