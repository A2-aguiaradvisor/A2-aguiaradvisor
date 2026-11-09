import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from compare_insurers import load_data, build_snapshot, ratio_percent, earnings_yield_percent, change_percent


class ComparisonTests(unittest.TestCase):
    def test_dividend_yield_bbse(self):
        self.assertAlmostEqual(ratio_percent(4.59, 38.24), 12.003138, places=4)

    def test_dividend_yield_cxse(self):
        self.assertAlmostEqual(ratio_percent(1.38, 20.50), 6.731707, places=4)

    def test_earnings_yield(self):
        self.assertAlmostEqual(earnings_yield_percent(8.1), 12.345679, places=4)

    def test_missing_cxse_q3_not_imputed(self):
        rows = {row["ticker"]: row for row in build_snapshot(load_data())}
        self.assertIsNone(rows["CXSE3"]["reported_2026q3_managerial_profit_brl_million"])
        self.assertGreater(rows["BBSE3"]["reported_2026q3_managerial_profit_brl_million"], 0)

    def test_bb_seguridade_yoy_decline(self):
        company = load_data()["securities"]["BBSE3"]
        q = company["quarterly"]
        self.assertAlmostEqual(change_percent(q["2026Q3"]["managerial_recurring_net_income_brl_million"], q["2025Q3"]["managerial_recurring_net_income_brl_million"]), -5.0677, places=1)

    def test_zero_denominator_rejected(self):
        with self.assertRaises(ValueError):
            ratio_percent(100, 0)


if __name__ == "__main__":
    unittest.main()
