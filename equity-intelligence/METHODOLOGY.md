# Metodologia e trilha de auditoria

## Definições

- **Preço de referência:** último fechamento disponível na mesma data de negociação (06/11/2026). Preço ajustado para proventos/desdobramentos exige outra série e anotação da política.
- **Market cap:** preço por classe e ações disponíveis, fornecido por fonte de mercado. Não é capital próprio contábil.
- **P/L:** valor de mercado / lucro contábil últimos 12 meses. A fonte de referência pode usar normalizações; reconciliar P/L à CVM antes de investir.
- **Earnings yield:** 100 / P/L; indicador retrospectivo, não retorno realizado e não custo de capital.
- **DY 12m:** soma de proventos por ação da janela e dividida pelo preço da sessão de referência. Janela pode ser por data-com ou pagamento, devendo ficar explícita no feed operacional. Histórico não projeta dividendos futuros.
- **Variação de preço 12m:** (P_fim/P_início - 1)*100, sem dividendos reinvestidos. Retorno total depende de calendário ex, valor líquido/bruto e política de reinvestimento.
- **Lucro gerencial recorrente:** divulgado pela emissora. Não comparar automaticamente com IFRS17/CPC50, sem ponte contábil e análise de ajustes. 3T26 CXSE pendente em 09/11 na coleta.
- **ROE:** lucro TTM / PL médio ou ajustado conforme a emissora. Não misturar ROE gerencial, contábil, TTM ou anualizado.
- **Índice combinado e sinistralidade:** só comparar na mesma linha operacional e perímetro de consolidação. Holding com equivalência patrimonial não equivale a seguradora operacional.
- **Grau de alavancagem:** analisar dívida financeira efetiva, compromissos e exigências regulatórias; EV/EBITDA ou dívida/EBITDA não descrevem apropriadamente holdings de participações em seguros.
- **Capital de giro:** ativo circulante menos passivo circulante, mas relevância deve ser contextualizada; não converter mecanicamente em score.
- **Valuation avançado:** preferir dividend discount model ou fluxo de caixa ao acionista com hipóteses de payout, ROE, reinvestimento, crescimento e custo de capital; sempre cenários e sensibilidade.

## Validação dos dados e escopo

- Recomendação: auditoria de qualidade por período, granularidade, empresa, unidade, moeda e método de contabilização.
- Fonte primária: RI e arquivos CVM. Plataforma Status Invest / Cota B3 apenas referência de interface ou snapshot secundário, sem raspagem automatizada não autorizada.
- O código atual demonstra o pipeline **snapshot → validação → cálculo → interpretação**, não ingere automaticamente DFP/ITR nem gera valuation prospectivo. Essa é etapa posterior.
- Não armazenar tokens/API keys em repositórios públicos.
- Dados operacionais e de preços são sensíveis a data; não anunciar como cotação atual quando se tratar de fotografia histórica.

## Atualização 3T26 pendente

1. Localizar release RI CXSE3 publicado em 09/11/2026.
2. Conferir números em DRE e balanço CPC50.
3. Registrar lucro gerencial e reconciliação com IFRS17.
4. Atualizar JSON com `source`, período e data de captura.
5. Reexecutar testes, comparar mesmo período 3T26 BBSE3 × CXSE3 e versionar um novo relatório.
