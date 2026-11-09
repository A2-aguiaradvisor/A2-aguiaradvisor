# Equity Intelligence — Piloto BBSE3 × CXSE3

Pesquisa com data-base **09/11/2026**. Escopo: comparação entre **ações ordinárias de duas holdings listadas de seguridade**, e não entre Banco do Brasil BBAS3 e Caixa Econômica Federal não listada. Proposta técnica independente; **não constitui recomendação de investimento nem relatório emitido por analista credenciado CNPI/CFA**.

## Estado da informação

- **BBSE3:** demonstrações/relatório gerencial 3T26 divulgados em **03/11/2026**.
- **CXSE3:** 3T26 previsto para **09/11/2026**; ainda não havia documento 3T26 validado na captura. Valores faltantes permanecem `null`.
- **Comparação homogênea de lucro:** 2T26 disponível para ambas, **mas o lucro gerencial utiliza critérios próprios de cada emissora**. Não confundir lucro gerencial/CPC11 e lucro contábil CPC50/IFRS17.
- **Preço e múltiplos:** fotografia de mercado secundária da sessão de 06/11/2026 (indicativa). Não são feed em tempo real nem série total-return.
- **Limitação MCP brapi:** API de cotação individual disponível; conta gratuita não inclui dividendos, balanços trimestrais nem histórico de 1 ano. Nunca usar scraping irregular para suprir restrição de planos.

## Como executar

```bash
python equity-intelligence/src/compare_insurers.py
python -m unittest discover -s equity-intelligence/tests -v
```

Implementação sem dependências de terceiros. Os dados utilizados são transparentes em `data/pilot_2026-11-09.json`. As funções calculam dividend yield com base no valor informado por ação e preço, earnings yield por P/L e alterações percentuais. Dados e fórmulas são separáveis para auditoria.

## Indicadores do produto-alvo

**Valuation:** P/L normalizado, P/VP, retorno sobre lucro implícito, histórico e sustentabilidade de distribuição de dividendos, preço/lucro prospectivo com cenários (sem vender projeção como fato).

**Operação:** prêmios emitidos/ganhos por modalidade, sinistralidade, combinado, taxa de gestão e saldo sob administração em previdência, receitas de distribuição, comportamento de consórcios e ganhos na equivalência patrimonial.

**Balanço e risco:** patrimônio líquido ajustado, ROE com método explícito, liquidez, obrigações regulatórias e alocação de capital. Indicadores IFRS17/CPC50 devem permanecer separados de relatórios gerenciais CPC11.

**Capital de giro:** não usar P/capital de giro como determinante de compra para holdings de seguridade sem analisar contratos, caixa livre, passivos de seguro e investimentos. **Dívida líquida/EBITDA** não é KPI central comparável a seguradoras.

**Estratégia:** BBSE3 dependência da originação do agronegócio, Brasilseg, BB Corretora e Brasilprev; CXSE3 dependência de hipotecas e da rede Caixa, e exposição a previdência, seguros e consórcios. Monitorar mercado, juros, política comercial e qualidade do resultado operacional.

## Interpretação executiva — instantâneo inicial

- **BBSE3:** P/L secundário ~8,1x, DY ~12% (passado), 3T26 lucro gerencial recorrente R$ 2,432 bi (-5,1% a/a); queda de emissão de prêmios na Brasilseg pressiona crescimento. Investigar normalização e sustentabilidade de distribuição antes de inferir subavaliação.
- **CXSE3:** P/L secundário ~14,3x, DY ~6,7% (passado), 2T26 lucro gerencial R$ 1,14 bi (+9,5% a/a); habitação e previdência impulsionaram operações. O prêmio de múltiplo pode precificar maior continuidade de crescimento, cuja hipótese exige teste de cenário.
- **Nunca** comparar 3T26 de BBSE3 ao 2T26 de CXSE3 como par diretamente equivalente.

## Modelo de qualidade

1. Registrar cada documento oficial com URL, tipo, período e data de publicação.
2. Diferenciar dados observados, normalizações analíticas e cenários estimados.
3. Não unir preços com datas-base divergentes.
4. Calcular retornos históricos **com** e **sem** proventos em séries explicitamente diferentes.
5. Incluir dados de capitalização e volume com data exata e política de licenciamento.
6. Adicionar atualização trimestral via documentos oficiais após publicação do 3T26 de CXSE3.
7. Validar cálculos com testes unitários e reconciliação ao relatório da companhia.

## Arquivos

- `data/pilot_2026-11-09.json`: observações datadas e fontes.
- `src/compare_insurers.py`: métrica, cálculo, relatório Markdown.
- `tests/test_compare_insurers.py`: testes de fórmulas e ausência explícita de dados.
- `METHODOLOGY.md`: dicionário e política contábil.

A pasta está isolada em uma **branch de revisão** para não alterar o site nem a apresentação do perfil do GitHub.
