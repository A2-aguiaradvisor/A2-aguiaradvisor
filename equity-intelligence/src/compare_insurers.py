#!/usr/bin/env python3
"""Equity Intelligence: BBSE3 x CXSE3 (MVP reprodutível, apenas stdlib).

Execute: python equity-intelligence/src/compare_insurers.py
Tests:   python -m unittest discover -s equity-intelligence/tests -v
Nenhuma chave, raspagem de site ou conexão externa é exigida.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "pilot_2026-11-09.json"


def load_data(path: Path = DATA_FILE) -> dict[str, Any]:
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def ratio_percent(numerator: float, denominator: float) -> float:
    if denominator <= 0:
        raise ValueError("Denominador deve ser positivo")
    return numerator / denominator * 100.0


def earnings_yield_percent(pe: float) -> float:
    """Lucro/preço implícito no P/L; não equivale a retorno projetado."""
    return ratio_percent(1.0, pe)


def change_percent(current: float, base: float) -> float:
    return ratio_percent(current - base, base)


def build_snapshot(data: dict[str, Any]) -> list[dict[str, Any]]:
    records = []
    for ticker, company in data["securities"].items():
        close = float(company["close_brl"])
        payout = float(company["dividends_per_share_12m_brl"])
        pe = float(company["pe_ttm_reference"])
        row = {
            "ticker": ticker,
            "issuer": company["issuer"],
            "share_class": company["share_class"],
            "reference_session": data["metadata"]["market_reference_session"],
            "price_brl": close,
            "market_cap_brl": float(company["market_cap_brl"]),
            "pe_ttm_reference": pe,
            "earnings_yield_percent": round(earnings_yield_percent(pe), 2),
            "dividends_per_share_12m_brl": payout,
            "dividend_yield_percent": round(ratio_percent(payout, close), 2),
            "price_return_12m_percent": company["price_return_12m_percent"],
            "reported_2026q2_managerial_profit_brl_million": company["quarterly"]["2026Q2"]["managerial_recurring_net_income_brl_million"],
            "reported_2026q3_managerial_profit_brl_million": company["quarterly"].get("2026Q3", {}).get("managerial_recurring_net_income_brl_million"),
            "market_source": company["price_source"],
            "fundamental_sources": company["fundamental_sources"],
        }
        records.append(row)
    return records


def export_markdown(data: dict[str, Any]) -> str:
    rows = build_snapshot(data)
    heading = [
        "# Equity Intelligence — BBSE3 vs CXSE3",
        "",
        f"Referência de preço: {data['metadata']['market_reference_session']}. ",
        "Proventos brutos indicativos em 12 meses. Sem recomendação de compra/venda.",
        "",
        "| Métrica | BBSE3 | CXSE3 |",
        "|---|---:|---:|",
    ]
    by_ticker = {row["ticker"]: row for row in rows}
    a, b = by_ticker["BBSE3"], by_ticker["CXSE3"]
    pairs = [
        ("Preço (R$)", "price_brl", "R$ {:.2f}"),
        ("Valor de mercado (R$ bi)", "market_cap_brl", "R$ {:.2f}"),
        ("P/L referência (x)", "pe_ttm_reference", "{:.1f}"),
        ("Earnings yield implícito (%)", "earnings_yield_percent", "{:.2f}%"),
        ("Dividendos/ação últimos 12m (R$)", "dividends_per_share_12m_brl", "R$ {:.2f}"),
        ("Dividend yield calculado (%)", "dividend_yield_percent", "{:.2f}%"),
        ("Variação de preço 12m (%)", "price_return_12m_percent", "{:.1f}%"),
        ("Lucro gerencial 2T26 (R$ mi)", "reported_2026q2_managerial_profit_brl_million", "{:.1f}"),
        ("Lucro gerencial 3T26 (R$ mi)", "reported_2026q3_managerial_profit_brl_million", "{:.1f}"),
    ]
    for label, key, fmt in pairs:
        def present(row: dict[str, Any]) -> str:
            value = row.get(key)
            if value is None:
                return "Pendente de publicação/validação"
            if key == "market_cap_brl":
                value = value / 1e9
            return fmt.format(value)
        heading.append(f"| {label} | {present(a)} | {present(b)} |")
    heading.extend([
        "",
        "## Critérios de comparabilidade",
        "- P/L de mercado, histórico de dividendos e variação de preços têm definições dependentes do fornecedor.",
        "- Lucro gerencial recorrente da BBSE3 e lucro gerencial da CXSE3 não são equivalentes ao lucro IFRS17 sem reconciliação.",
        "- 2T26 foi publicado em ambas; 3T26 da CXSE3 permanecia não validado no instantâneo.",
        "- Capital de giro e dívida líquida/EBITDA genéricos não são score principal de holdings de seguridade.",
        "- Ausência de número não autoriza estimativa apresentada como fato.",
        "",
        "## Fontes documentadas",
    ])
    for source_id, source in data["sources"].items():
        heading.append(f"- {source_id}: {source['url']}")
    return "\n".join(heading) + "\n"


def main() -> None:
    data = load_data()
    report = export_markdown(data)
    print(report)


if __name__ == "__main__":
    main()
