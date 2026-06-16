#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera relatorio_completo.html com tabelas, metodologia e análise detalhada dos 14 cenários."""

import csv, base64, math
from pathlib import Path

BASE = Path('/var/home/rafael/Documentos/Projetos/elon')
DATA = BASE / 'notebooks' / 'data'

def read_csv(f):
    with open(DATA / f, newline='', encoding='utf-8') as fh:
        return list(csv.DictReader(fh))

def b64(f):
    p = DATA / f
    return base64.b64encode(p.read_bytes()).decode() if p.exists() else ''

def img(key, alt=''):
    d = IMGS.get(key, '')
    return f'<img src="data:image/png;base64,{d}" alt="{alt}" class="chart-img">' if d else ''

def fmt_num(n, decimals=0):
    if n >= 1e12: return f'US$ {n/1e12:.2f} tri'
    if n >= 1e9:  return f'{n/1e9:.1f} bilhões'
    if n >= 1e6:  return f'{n/1e6:.1f} milhões'
    if n >= 1e3:  return f'{n:,.{decimals}f}'
    return f'{n:.{decimals}f}'

def tbl(headers, rows, highlight=None, notes=''):
    ths = ''.join(f'<th>{h}</th>' for h in headers)
    trs = ''
    for row in rows:
        cls = ' class="hl"' if highlight and highlight(row) else ''
        tds = ''.join(f'<td>{c}</td>' for c in row)
        trs += f'<tr{cls}>{tds}</tr>'
    note = f'<p class="tbl-note">{notes}</p>' if notes else ''
    return f'<div class="tbl-wrap"><table><thead><tr>{ths}</tr></thead><tbody>{trs}</tbody></table>{note}</div>'

def fontes_html(lst):
    return ''.join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in lst)

def card(num, icon, tag, title, big, sub, metodo, analise, tabela, fontes_lst, extra_chart=''):
    f = fontes_html(fontes_lst)
    ch = img(num, title)
    return f'''
<section class="cenario" id="c{num:02d}">
  <header class="c-head">
    <div class="c-num">{num:02d}</div>
    <div class="c-icon">{icon}</div>
    <div class="c-meta"><span class="c-tag">{tag}</span><h2>{title}</h2></div>
  </header>
  <div class="c-destaque"><div class="c-big">{big}</div><div class="c-sub">{sub}</div></div>
  <div class="c-body">
    <div class="c-left">
      <div class="box box-met"><h3>📐 Metodologia</h3>{metodo}</div>
      <div class="box box-ana"><h3>🔍 Análise Detalhada</h3>{analise}</div>
    </div>
    <div class="c-right">
      <div class="box box-chart">{ch}{extra_chart}</div>
    </div>
  </div>
  <div class="c-data"><h3>🗃️ Dados Completos</h3>{tabela}</div>
  <div class="c-fontes"><span class="fl">📚 Fontes:</span>{f}</div>
</section>'''

# ── CONSTANTES ──────────────────────────────────────────────────────────────
MUSK       = 1_000_000_000_000
USD_BRL    = 5.71
MUSK_BRL   = MUSK * USD_BRL
AGE_UNI    = 13_800_000_000
RIQ_MUND   = 471_000_000_000_000
PIB_MUND   = 105_000_000_000_000
PIB_BR     = 2_132_000_000_000
POP_MUNDO  = 8_200_000_000
POP_BR     = 214_000_000

# ── DADOS ──────────────────────────────────────────────────────────────────
salarios   = read_csv('salarios_minimos_paises.csv')
pib_data   = read_csv('pib_paises_2024.csv')
musk_hist  = read_csv('historico_fortuna_musk.csv')
rua_br     = read_csv('historico_pop_rua_brasil.csv')
rua_eua    = read_csv('historico_pop_rua_eua.csv')
profs      = read_csv('profissoes_brasil.csv')

IMGS = {
    1:'output_01_tempo_salario.png', 2:'output_02_paises_pib.png',
    3:'output_03_riqueza_mundial.png', 4:'output_04_bolsa_familia.png',
    5:'output_05_deficit_habitacional.png', 6:'output_06_correlacao_rua.png',
    7:'output_07_gasto_milhao.png', 8:'output_08_orcamento.png',
    9:'output_09_cestas_basicas.png', 10:'output_10_escolas_hospitais.png',
    11:'output_11_pib_comparacao.png', 12:'output_12_profissoes.png',
    13:'output_13_distribuicao.png', 14:'output_14_correlacao_rua_eua.png',
    '14b':'output_14b_brasil_eua_comparacao.png',
}
IMGS = {k: b64(v) for k, v in IMGS.items()}

# ─────────────────────────────────────────────────────────────────────────────
# CENÁRIO 1
# ─────────────────────────────────────────────────────────────────────────────
rows1 = []
for s in sorted(salarios, key=lambda x: float(x['salario_mensal_usd'])):
    sal = float(s['salario_mensal_usd'])
    anos = MUSK / (sal * 12)
    uni  = anos / AGE_UNI
    rows1.append([
        s['pais'],
        s['moeda'],
        f"{float(s['salario_local']):,.0f}",
        f"US$ {sal:,.0f}",
        f"{anos/1e6:,.1f} milhões",
        f"{uni:.2f}×",
        s['fonte'],
    ])

br_anos = MUSK / (284 * 12)

c1 = card(1,'⏱️','Trabalho & Renda',
  'Tempo para Acumular US$ 1 Trilhão com Salário Mínimo',
  f'{br_anos/1e6:,.0f} milhões de anos',
  'é o tempo que um trabalhador brasileiro levaria poupando 100% do salário mínimo',
  '''<p><strong>Fórmula:</strong></p>
  <div class="formula">Anos = Fortuna ÷ (Salário mensal × 12 meses)</div>
  <p><strong>Premissa:</strong> O trabalhador poupa 100% do salário, sem gastar nada,
  sem inflação, sem juros e sem impostos. É um limite teórico absoluto — impossível
  na prática — que serve para dimensionar a escala da desigualdade.</p>
  <p><strong>Taxa de câmbio:</strong> US$ 1 = R$ 5,71 (jun/2026).</p>
  <p><strong>Dado de Musk:</strong> Forbes Real-Time Billionaires, junho/2026.</p>''',
  f'''<p>O exercício revela que a concentração de riqueza de Musk é de tal ordem que
  <em>nenhum trabalhador de salário mínimo, em qualquer país do mundo,</em> conseguiria
  acumulá-la em um prazo compreensível para a mente humana.</p>
  <p>O trabalhador <strong>brasileiro</strong> precisaria de <strong>{br_anos/1e6:,.0f} milhões de anos</strong>
  — equivalente a <strong>{br_anos/AGE_UNI:.1f}× a idade do universo</strong> (13,8 bilhões de anos).
  Mesmo o trabalhador <strong>australiano</strong>, com o maior salário mínimo do grupo analisado
  (US$ 2.503/mês), levaria <strong>{MUSK/(2503*12)/1e6:,.0f} milhões de anos</strong> —
  ainda mais de <strong>{MUSK/(2503*12)/AGE_UNI:.0f}× a idade do universo</strong>.</p>
  <p>A diferença entre países é relevante: o trabalhador australiano leva
  <strong>{br_anos/(MUSK/(2503*12)):.1f}× menos tempo</strong> que o brasileiro —
  mas ambos estão igualmente impossibilitados de chegar perto do trilhão.</p>
  <p>Outro modo de ver: Musk acumulou mais riqueza em 2025 sozinho (US$ 215 bilhões de ganhos)
  do que um trabalhador brasileiro ganharia em
  <strong>{215e9/(284*12):,.0f} anos</strong> de trabalho contínuo.</p>''',
  tbl(['País','Moeda','Salário Local','Salário (USD/mês)','Anos necessários','× Idade do universo','Fonte'],
      rows1, highlight=lambda r: r[0]=='Brasil',
      notes='* Presume poupança de 100% do salário, sem gastos, inflação ou juros.'),
  [('Decreto Federal – Salário Mínimo jan/2026','https://www.gov.br/planalto'),
   ('U.S. Dept of Labor – Minimum Wage','https://www.dol.gov/agencies/whd/minimum-wage'),
   ('Fair Work Commission Australia','https://www.fairwork.gov.au'),
   ('Bundesministerium für Arbeit (Alemanha)','https://www.bmas.de'),
   ('Forbes Billionaires – Elon Musk','https://www.forbes.com/real-time-billionaires/')])

# ─────────────────────────────────────────────────────────────────────────────
# CENÁRIO 2
# ─────────────────────────────────────────────────────────────────────────────
MUSK_BI = 1000
pib_sorted = sorted(pib_data, key=lambda x: float(x['pib_bilhoes_usd']), reverse=True)
acima = sum(1 for p in pib_data if float(p['pib_bilhoes_usd']) >= MUSK_BI)
abaixo = len(pib_data) - acima

rows2 = []
for p in pib_sorted:
    pib = float(p['pib_bilhoes_usd'])
    pct = pib / MUSK_BI * 100
    vezes = MUSK_BI / pib if pib < MUSK_BI else None
    status = '✅ Acima de Musk' if pib >= MUSK_BI else f'❌ {vezes:.1f}× menor'
    rows2.append([p['pais'], p['continente'], f'US$ {pib:,.0f}bi',
                  f'{pct:.1f}%', status])

menor_pib = min(pib_data, key=lambda x: float(x['pib_bilhoes_usd']))
menor_val  = float(menor_pib['pib_bilhoes_usd'])

c2 = card(2,'🌍','PIB & Nações',
  'Países com PIB Menor que a Fortuna de Musk',
  f'{abaixo} de {len(pib_data)} países',
  'na base de dados têm PIB anual inferior à fortuna individual de Elon Musk',
  '''<p><strong>Conceito:</strong> O PIB (Produto Interno Bruto) nominal mede o valor total de
  todos os bens e serviços produzidos por um país em um ano, em dólares correntes.</p>
  <p><strong>Comparação:</strong> Fortuna de Musk (US$ 1 trilhão = US$ 1.000 bilhões) vs.
  PIB de cada país (FMI, estimativas 2024).</p>
  <p><strong>Limitação:</strong> A fortuna de Musk é um estoque de riqueza; o PIB é um
  fluxo anual de produção. Não são exatamente comparáveis, mas a comparação ilustra
  a magnitude da concentração.</p>''',
  f'''<p>De {len(pib_data)} países analisados, apenas <strong>{acima}</strong> possuem PIB maior
  que a fortuna individual de Musk. Os demais <strong>{abaixo}</strong> ({abaixo/len(pib_data)*100:.0f}%)
  produzem menos em um ano inteiro do que Musk possui.</p>
  <p>O menor PIB da base é <strong>{menor_pib["pais"]}</strong> com
  US$ {menor_val:.1f} bilhões — Musk é <strong>{MUSK_BI/menor_val:.0f}×</strong> mais rico
  que o PIB anual desse país.</p>
  <p>Países como <strong>Portugal</strong> (US$ 286bi), <strong>Chile</strong> (US$ 317bi) e
  <strong>Noruega</strong> (US$ 547bi) — nações de padrão de vida elevado e economias desenvolvidas
  — têm PIB inferior à fortuna de um único empresário.</p>
  <p>A fortuna de Musk equivale a <strong>{MUSK_BI/float(next(p for p in pib_data if p["pais"]=="Brasil")["pib_bilhoes_usd"]):.2f}×</strong>
  o PIB do Brasil e <strong>{MUSK_BI/float(next(p for p in pib_data if p["pais"]=="Argentina")["pib_bilhoes_usd"]):.1f}×</strong>
  o da Argentina.</p>''',
  tbl(['País','Continente','PIB 2024 (USD)','% da fortuna de Musk','Status'],
      rows2, highlight=lambda r: 'Brasil' in r[0] or 'Estados' in r[0]),
  [('FMI – World Economic Outlook Database 2024','https://www.imf.org/en/Publications/WEO'),
   ('Banco Mundial – GDP Data','https://data.worldbank.org/indicator/NY.GDP.MKTP.CD'),
   ('Forbes Billionaires – Elon Musk','https://www.forbes.com/real-time-billionaires/')])

# ─────────────────────────────────────────────────────────────────────────────
# CENÁRIO 3
# ─────────────────────────────────────────────────────────────────────────────
pct_musk   = MUSK / RIQ_MUND * 100
bot50_val  = 2_350_000_000_000
top1_val   = 209_280_000_000_000
mid49_val  = RIQ_MUND - top1_val - bot50_val
bot50_pop  = int(POP_MUNDO * 0.50)
top1_pop   = int(POP_MUNDO * 0.01)

rows3 = [
    ['1% mais ricos','82 milhões de adultos',f'US$ {top1_val/1e12:.1f} trilhões',
     f'{top1_val/RIQ_MUND*100:.1f}%', f'{top1_val/MUSK:.0f}× Musk'],
    ['49% (classe média global)','~4 bilhões de adultos',f'US$ {mid49_val/1e12:.1f} trilhões',
     f'{mid49_val/RIQ_MUND*100:.1f}%', f'{mid49_val/MUSK:.0f}× Musk'],
    ['50% mais pobres','~4,1 bilhões de adultos',f'US$ {bot50_val/1e12:.2f} trilhões',
     f'{bot50_val/RIQ_MUND*100:.2f}%', f'{bot50_val/MUSK:.2f}× Musk'],
    ['Elon Musk','1 pessoa',f'US$ {MUSK/1e12:.0f} trilhão',
     f'{pct_musk:.4f}%', '1× (referência)'],
]

c3 = card(3,'💰','Concentração de Riqueza',
  'Percentual da Riqueza Total da Humanidade',
  f'{pct_musk:.4f}%',
  f'da riqueza total da humanidade (US$ {RIQ_MUND/1e12:.0f} trilhões) está nas mãos de uma única pessoa',
  f'''<p><strong>Fonte base:</strong> UBS Global Wealth Report 2025 — riqueza total global ao
  final de 2024: <strong>US$ {RIQ_MUND/1e12:.0f} trilhões</strong>.</p>
  <p><strong>Cálculo:</strong> US$ 1 trilhão ÷ US$ {RIQ_MUND/1e12:.0f} trilhões × 100 = {pct_musk:.4f}%.</p>
  <p><strong>Distribuição por decil:</strong> baseada em dados do UBS/Oxfam sobre concentração
  de riqueza global em 2024.</p>''',
  f'''<p>Musk detém <strong>{pct_musk:.4f}%</strong> da riqueza total da humanidade —
  individualmente, mais do que o PIB de <strong>{abaixo}</strong> países.</p>
  <p>Os <strong>50% mais pobres do mundo</strong> (~{bot50_pop/1e9:.1f} bilhões de pessoas)
  possuem juntos US$ {bot50_val/1e12:.2f} trilhões.
  Musk tem sozinho <strong>{MUSK/bot50_val:.1f}×</strong> esse valor.</p>
  <p>Se Musk dividisse sua fortuna igualmente entre os {bot50_pop/1e9:.1f} bilhões de pessoas
  mais pobres, cada uma receberia <strong>US$ {MUSK/bot50_pop:.2f}</strong>.</p>
  <p>O <strong>1% mais rico</strong> (82 milhões de pessoas) detém US$ {top1_val/1e12:.1f} trilhões —
  <strong>{top1_val/MUSK:.0f}×</strong> a fortuna de Musk — reforçando que a concentração
  extrema não é exclusividade de Musk, mas ele é seu símbolo mais extremo.</p>
  <p>Para perspectiva: se a riqueza mundial fosse distribuída igualmente,
  cada adulto teria US$ {RIQ_MUND/POP_MUNDO:.0f}. Musk tem
  <strong>{MUSK/(RIQ_MUND/POP_MUNDO):.0f}×</strong> essa cota igualitária.</p>''',
  tbl(['Grupo','População','Riqueza total','% da riqueza mundial','Relação com Musk'], rows3,
      highlight=lambda r: 'Musk' in r[0]),
  [('UBS Global Wealth Report 2025','https://www.ubs.com/global/en/wealthmanagement/insights/global-wealth-report.html'),
   ('Oxfam – Inequality Report 2024','https://www.oxfam.org'),
   ('Forbes Billionaires – Elon Musk','https://www.forbes.com/real-time-billionaires/')])

# ─────────────────────────────────────────────────────────────────────────────
# CENÁRIO 4
# ─────────────────────────────────────────────────────────────────────────────
BF_BRL_ANO   = 160_000_000_000
BF_USD_ANO   = BF_BRL_ANO / USD_BRL
BF_FAMILIAS  = 19_800_000
BF_BENEFICIO = 680
anos_bf      = MUSK / BF_USD_ANO
familias_1y  = MUSK_BRL / (BF_BENEFICIO * 12)
beneficio_dobro = MUSK_BRL / (BF_BENEFICIO * 2 * 12 * BF_FAMILIAS)  # anos dobrando benefício

rows4 = [
    ['Orçamento anual 2025','R$ 160 bilhões','US$ 28 bilhões','—'],
    ['Famílias atendidas','19,8 milhões','—','—'],
    ['Benefício médio / família','R$ 680/mês','US$ 119/mês','—'],
    ['Anos que Musk financiaria',f'{anos_bf:.1f} anos',f'{anos_bf:.1f} anos','Mantendo as 19,8M famílias'],
    ['Famílias em 1 ano (fortuna toda)',f'{familias_1y/1e6:.1f} milhões','—','3,5× mais que hoje'],
    ['Dobrar benefício para 19,8M fam.',f'{beneficio_dobro:.1f} anos','—','R$ 1.360/família/mês'],
    ['Custo diário do programa','R$ 438 milhões','US$ 76,7 milhões','—'],
    ['% do orçamento anual que Musk =',f'{MUSK_BRL/BF_BRL_ANO:.1f}×','—','Orçamentos completos'],
]

c4 = card(4,'🤝','Assistência Social',
  'Bolsa Família: Por Quanto Tempo a Fortuna Poderia Financiar?',
  f'{anos_bf:.1f} anos',
  'de Bolsa Família para 19,8 milhões de famílias, sem precisar de nenhum recurso público',
  f'''<p><strong>Dados do programa (2025):</strong></p>
  <ul>
    <li>Orçamento: R$ 160 bilhões/ano = US$ {BF_USD_ANO/1e9:.1f} bilhões/ano</li>
    <li>Famílias: {BF_FAMILIAS/1e6:.1f} milhões</li>
    <li>Benefício médio: R$ {BF_BENEFICIO}/família/mês</li>
  </ul>
  <p><strong>Cálculo:</strong> US$ 1 trilhão ÷ US$ {BF_USD_ANO/1e9:.1f}bi/ano = {anos_bf:.1f} anos.</p>
  <p>Em BRL: R$ {MUSK_BRL/1e12:.2f} trilhões ÷ R$ {BF_BRL_ANO/1e9:.0f}bi/ano = {MUSK_BRL/BF_BRL_ANO:.1f} anos.</p>''',
  f'''<p>Com US$ 1 trilhão seria possível financiar o Bolsa Família por
  <strong>{anos_bf:.1f} anos</strong> — mais do que uma geração inteira (25 anos).</p>
  <p>Alternativamente, a fortuna poderia atender
  <strong>{familias_1y/1e6:.1f} milhões de famílias</strong> por 1 ano —
  <strong>{familias_1y/BF_FAMILIAS:.1f}×</strong> mais famílias do que o programa atual cobre.</p>
  <p>Outra opção: manter as atuais {BF_FAMILIAS/1e6:.1f}M famílias por {anos_bf:.0f} anos
  <em>e ainda dobrar o benefício para R$ {BF_BENEFICIO*2:,.0f}/família/mês</em>
  durante <strong>{beneficio_dobro:.1f} anos</strong>.</p>
  <p>O orçamento anual do Bolsa Família representa apenas
  <strong>{BF_USD_ANO/MUSK*100:.1f}%</strong> da fortuna de Musk —
  ou seja, Musk poderia financiá-lo com os juros sobre sua fortuna
  (rendendo ~5% ao ano), sem jamais tocar no principal.</p>''',
  tbl(['Métrica','Em BRL','Em USD','Observação'], rows4),
  [('MDS – Bolsa Família 2025','https://www.gov.br/mds'),
   ('CNN Brasil – Orçamento Bolsa Família 2025','https://www.cnnbrasil.com.br/economia/macroeconomia/bolsa-familia-tera-orcamento-de-r-158-bilhoes-em-2026/'),
   ('Gov.br – Bolsa Família nov/2025','https://www.gov.br/secom/pt-br/assuntos/noticias/2025/11/bolsa-familia-chega-a-18-65-milhoes-de-lares'),
   ('Forbes Billionaires – Elon Musk','https://www.forbes.com/real-time-billionaires/')])

# ─────────────────────────────────────────────────────────────────────────────
# CENÁRIO 5
# ─────────────────────────────────────────────────────────────────────────────
DEFICIT   = 5_773_983
CASA_BRL  = 200_000
CASA_USD  = CASA_BRL / USD_BRL
casas_pos = int(MUSK / CASA_USD)
vezes     = casas_pos / DEFICIT
custo_total_deficit_brl = DEFICIT * CASA_BRL

regioes = [
    ('Sudeste',     2_350_000, CASA_BRL),
    ('Nordeste',    1_460_000, CASA_BRL),
    ('Sul',           743_170, CASA_BRL),
    ('Norte',         673_554, CASA_BRL),
    ('Centro-Oeste',  547_259, CASA_BRL),
]
rows5_reg = []
for reg, def_reg, custo in regioes:
    custo_brl = def_reg * custo
    custo_usd = custo_brl / USD_BRL
    pct_musk  = custo_usd / MUSK * 100
    rows5_reg.append([reg, f'{def_reg:,}', f'R$ {custo_brl/1e9:.1f}bi',
                       f'US$ {custo_usd/1e9:.1f}bi', f'{pct_musk:.2f}% da fortuna'])

rows5_comp = [
    ['Déficit habitacional total', f'{DEFICIT:,} moradias', '100% do problema'],
    ['Custo total do déficit', f'R$ {custo_total_deficit_brl/1e9:.1f}bi = US$ {custo_total_deficit_brl/USD_BRL/1e9:.1f}bi',
     f'{custo_total_deficit_brl/USD_BRL/MUSK*100:.1f}% da fortuna de Musk'],
    ['Casas possíveis com fortuna Musk', f'{casas_pos:,} casas', f'{vezes:.1f}× o déficit'],
    ['Casas extras após resolver o déficit', f'{casas_pos - DEFICIT:,}', f'{(casas_pos-DEFICIT)/DEFICIT:.1f}× o déficit novamente'],
    ['Custo por casa (MCMV)', 'R$ 200.000 = US$ 35.026', 'Minha Casa Minha Vida'],
]

c5 = card(5,'🏠','Moradia',
  'Resolver o Déficit Habitacional do Brasil',
  f'{casas_pos/1e6:.1f} milhões de casas',
  f'poderiam ser construídas — {vezes:.1f}× o déficit habitacional de {DEFICIT/1e6:.2f} milhões de moradias',
  f'''<p><strong>Dados base:</strong></p>
  <ul>
    <li>Déficit habitacional: {DEFICIT:,} moradias (Fundação João Pinheiro, 2024)</li>
    <li>Custo médio MCMV: R$ {CASA_BRL:,}/unidade = US$ {CASA_USD:,.0f}</li>
    <li>Fortuna Musk em BRL: R$ {MUSK_BRL/1e12:.2f} trilhões</li>
  </ul>
  <p><strong>Cálculo:</strong> US$ 1 trilhão ÷ US$ {CASA_USD:,.0f}/casa = {casas_pos:,} casas.</p>
  <p><strong>Custo real do déficit:</strong> {DEFICIT:,} × R$ {CASA_BRL:,} = R$ {custo_total_deficit_brl/1e9:.1f}bi
  = apenas <strong>{custo_total_deficit_brl/USD_BRL/MUSK*100:.1f}%</strong> da fortuna de Musk.</p>''',
  f'''<p>O déficit habitacional brasileiro de <strong>{DEFICIT:,} moradias</strong> poderia ser
  inteiramente resolvido com apenas <strong>{custo_total_deficit_brl/USD_BRL/MUSK*100:.1f}%</strong>
  da fortuna de Musk — sobraria <strong>{(1 - custo_total_deficit_brl/USD_BRL/MUSK)*100:.1f}%</strong>
  intacto.</p>
  <p>Com a fortuna completa, seria possível construir <strong>{casas_pos/1e6:.1f} milhões de casas</strong>
  — resolver o déficit <strong>{vezes:.0f} vezes</strong> consecutivas.</p>
  <p>A região com maior déficit é o <strong>Sudeste</strong> (2,35M moradias = 40,7% do total),
  cujo custo (R$ {regioes[0][1]*CASA_BRL/1e9:.0f}bi) representa apenas
  <strong>{regioes[0][1]*CASA_BRL/USD_BRL/MUSK*100:.2f}%</strong> da fortuna de Musk.</p>
  <p>O programa <strong>Minha Casa Minha Vida</strong> entregou 923,9 mil moradias em 2023–2024,
  reduzindo o déficit 3,4%. Musk poderia financiar 6× esse ritmo por 10 anos.</p>''',
  '<h4>Por Região</h4>' + tbl(['Região','Déficit','Custo (BRL)','Custo (USD)','% da fortuna Musk'], rows5_reg)
  + '<h4>Resumo Geral</h4>' + tbl(['Métrica','Valor','Contexto'], rows5_comp),
  [('Fundação João Pinheiro – Déficit Habitacional 2024','https://fjp.mg.gov.br/deficit-habitacional-recua-34-no-brasil-e-soma-5-773-983-domicilios/'),
   ('Min. das Cidades – Minha Casa Minha Vida','https://www.gov.br/cidades'),
   ('Forbes Billionaires – Elon Musk','https://www.forbes.com/real-time-billionaires/')])

# ─────────────────────────────────────────────────────────────────────────────
# CENÁRIO 6
# ─────────────────────────────────────────────────────────────────────────────
musk_by_ano = {int(r['ano']): float(r['fortuna_bilhoes_usd'])
               for r in sorted(musk_hist, key=lambda x: (x['ano'], x.get('mes','0')))}
# latest per year
from collections import defaultdict
latest = defaultdict(float)
for r in musk_hist:
    ano = int(r['ano'])
    val = float(r['fortuna_bilhoes_usd'])
    if val > latest[ano]: latest[ano] = val

rows6 = []
for r in rua_br:
    ano = int(r['ano'])
    pop = int(r['populacao_rua'])
    musk_val = latest.get(ano)
    musk_str = f'US$ {musk_val:.0f}bi' if musk_val else '—'
    rows6.append([str(ano), f'{pop:,}', musk_str, r['fonte']])

# Pearson
anos_cm = [int(r['ano']) for r in rua_br if latest.get(int(r['ano']))]
pop_cm  = [int(r['populacao_rua']) for r in rua_br if latest.get(int(r['ano']))]
musk_cm = [latest[a] for a in anos_cm]
n = len(anos_cm)
if n > 1:
    mx = sum(musk_cm)/n; my = sum(pop_cm)/n
    num = sum((musk_cm[i]-mx)*(pop_cm[i]-my) for i in range(n))
    den = (sum((m-mx)**2 for m in musk_cm) * sum((p-my)**2 for p in pop_cm))**0.5
    r_br = num/den if den else 0
else:
    r_br = 0

cresc_rua = (int(rua_br[-1]['populacao_rua'])/int(rua_br[0]['populacao_rua'])-1)*100
cresc_musk_br = (latest[int(rua_br[-1]['ano'])]/latest[int(rua_br[0]['ano'])]-1)*100 if latest.get(int(rua_br[0]['ano'])) else 0

c6 = card(6,'📈','Correlação & Desigualdade',
  'Correlação: Fortuna de Musk × População de Rua no Brasil',
  f'r = {r_br:.3f}',
  'correlação de Pearson positiva muito forte entre crescimento da fortuna de Musk e aumento da população de rua no Brasil',
  f'''<p><strong>Método:</strong> Coeficiente de Correlação de Pearson (r) entre a fortuna
  anual de Musk (Bloomberg/Forbes, valores de fim de ano) e a população em situação de rua
  no Brasil (IPEA/OBPopRua) nos anos com dados disponíveis em ambas as séries.</p>
  <p><strong>r = {r_br:.4f}</strong> → correlação positiva muito forte.</p>
  <p><strong>Importante:</strong> correlação ≠ causalidade. Ambas as séries são influenciadas
  por fatores estruturais comuns (desigualdade sistêmica, políticas macroeconômicas,
  pandemia de COVID-19). O aumento da riqueza de Musk não causa diretamente o aumento
  do sem-teto — mas ambos são sintomas do mesmo sistema econômico.</p>''',
  f'''<p>Entre {rua_br[0]["ano"]} e {rua_br[-1]["ano"]}, a população em situação de rua
  no Brasil cresceu <strong>{cresc_rua:.0f}%</strong>
  (de {int(rua_br[0]["populacao_rua"]):,} para {int(rua_br[-1]["populacao_rua"]):,} pessoas).
  No mesmo período, a fortuna de Musk cresceu <strong>{cresc_musk_br:.0f}%</strong>.</p>
  <p>O coeficiente de Pearson de <strong>{r_br:.3f}</strong> indica que quando a fortuna
  de Musk sobe, o número de sem-teto no Brasil tende a subir proporcionalmente —
  embora a relação seja indireta e mediada por fatores estruturais.</p>
  <p>O crescimento mais acelerado ocorreu pós-2019: a pandemia de COVID-19, a crise
  econômica e o desmonte de políticas sociais coincidiram com o boom da riqueza de Musk,
  impulsionado pelo mercado financeiro.</p>
  <p>Comparando com os EUA (Cenário 14), onde a correlação é mais fraca por causa
  das políticas de <em>Housing First</em> (2010–2016), o Brasil mostra uma correlação
  mais forte pois nunca implementou política habitacional equivalente para a população de rua.</p>''',
  tbl(['Ano','Pop. em situação de rua','Fortuna de Musk','Fonte'], rows6,
      highlight=lambda r: r[0] in ['2022','2025'],
      notes='Fortuna de Musk: valor de fim de ano (Bloomberg/Forbes). Dados de 2026 não incluídos por ausência de censo atualizado.'),
  [('IPEA – Pop. em Situação de Rua no Brasil','https://www.ipea.gov.br/portal/ipea-g20/noticias-g20/13457-populacao-em-situacao-de-rua-supera-281-4-mil-pessoas-no-brasil'),
   ('OBPopRua/UFMG – 365 mil pessoas (2025)','https://agenciabrasil.ebc.com.br/direitos-humanos/noticia/2026-01/estudo-aponta-mais-365-mil-pessoas-em-situacao-de-rua-no-brasil'),
   ('Agência Brasil – crescimento 25% em 2025','https://agenciabrasil.ebc.com.br/direitos-humanos/noticia/2025-01/aumenta-em-25-o-numero-de-pessoas-em-situacao-de-rua-no-pais'),
   ('Bloomberg Billionaires Index','https://www.bloomberg.com/billionaires/')])

# ─────────────────────────────────────────────────────────────────────────────
# CENÁRIO 7
# ─────────────────────────────────────────────────────────────────────────────
GASTO_DIA = 1_000_000
dias      = MUSK / GASTO_DIA
anos_g    = dias / 365.25
ano_ini   = int(2026 - anos_g)

eventos = [
    (ano_ini, 'Início do gasto (US$ 1M/dia)'),
    (800,  'Renascimento Carolíngio — coroação de Carlos Magno'),
    (900,  'Ápice do Califado Abássida'),
    (1066, 'Batalha de Hastings — início da Inglaterra normanda'),
    (1215, 'Magna Carta assinada'),
    (1347, 'Início da Peste Negra na Europa'),
    (1440, 'Invenção da imprensa por Gutenberg'),
    (1492, 'Colombo chega às Américas'),
    (1500, 'Cabral chega ao Brasil'),
    (1776, 'Independência dos EUA'),
    (1789, 'Revolução Francesa'),
    (1822, 'Independência do Brasil'),
    (1888, 'Abolição da escravidão no Brasil'),
    (1945, 'Fim da 2ª Guerra Mundial'),
    (2026, 'Musk se torna trilionário (ainda gastando)'),
]
rows7 = []
for ano, evento in eventos:
    if ano >= ano_ini:
        gasto  = (ano - ano_ini) * 365.25 * GASTO_DIA
        restante = max(MUSK - gasto, 0)
        pct_gasto = min(gasto / MUSK * 100, 100)
        rows7.append([str(ano), evento,
                      f'US$ {gasto/1e9:.1f}bi gastos',
                      f'{pct_gasto:.4f}% gasto',
                      f'US$ {restante/1e12:.4f}tri restante'])

sal_br_dia = 284 * 12 / 365
anos_br_dia = MUSK / sal_br_dia / 365.25

c7 = card(7,'📅','Escala do Tempo',
  'Gastando US$ 1 Milhão por Dia — Quanto Tempo Duraria?',
  f'{anos_g:,.0f} anos',
  f'gastando US$ 1.000.000 por dia, todos os dias — seria necessário ter começado em {ano_ini} d.C.',
  f'''<p><strong>Cálculo:</strong></p>
  <div class="formula">Dias = US$ 1.000.000.000.000 ÷ US$ 1.000.000/dia = {dias:,.0f} dias</div>
  <div class="formula">Anos = {dias:,.0f} ÷ 365,25 = {anos_g:,.1f} anos</div>
  <div class="formula">Início = 2026 − {anos_g:.0f} = {ano_ini} d.C.</div>
  <p><strong>Para comparação — salário mínimo brasileiro (US$ {284}/mês = US$ {sal_br_dia:.2f}/dia):</strong></p>
  <div class="formula">Anos = US$ 1tri ÷ US$ {sal_br_dia:.2f}/dia ÷ 365,25 = {anos_br_dia/1e6:.0f} milhões de anos</div>''',
  f'''<p>US$ 1 milhão por dia é um gasto extraordinário — equivale a contratar
  <strong>3.521 trabalhadores brasileiros</strong> de salário mínimo por um dia inteiro.
  Ainda assim, a fortuna de Musk duraria <strong>{anos_g:,.0f} anos</strong>.</p>
  <p>Em {ano_ini} d.C., o Islã estava em sua expansão inicial, o Império Tang dominava
  a China e os Maias construíam suas cidades no México. Se Musk tivesse começado a gastar
  nessa época, em 2026 ainda restaria toda a fortuna — acabaria de chegar ao ponto atual.</p>
  <p>Comparação com o salário mínimo: um trabalhador de salário mínimo que "gastasse"
  toda a sua renda diária (US$ {sal_br_dia:.2f}) levaria <strong>{anos_br_dia/1e6:.0f} milhões de anos</strong>
  para gastar 1 trilhão — {anos_br_dia/anos_g/1e6:.0f} milhões de vezes mais.</p>
  <p>Se Musk quisesse <em>dar</em> US$ 1 milhão por dia para caridade desde que nasceu (1971),
  teria doado apenas <strong>US$ {(2026-1971)*365.25*1e6/1e9:.1f} bilhões</strong>
  — apenas <strong>{(2026-1971)*365.25*1e6/MUSK*100:.2f}%</strong> de sua fortuna.</p>''',
  tbl(['Ano','Evento histórico','Gasto acumulado','% gasto','Fortuna restante'], rows7,
      highlight=lambda r: r[0] == '2026'),
  [('Forbes Billionaires – Elon Musk','https://www.forbes.com/real-time-billionaires/'),
   ('Decreto Federal – Salário Mínimo 2026','https://www.gov.br/planalto')])

# ─────────────────────────────────────────────────────────────────────────────
# CENÁRIO 8
# ─────────────────────────────────────────────────────────────────────────────
ORCAMENTO_BRL = 4_100_000_000_000
ORCAMENTO_USD = ORCAMENTO_BRL / USD_BRL
areas = [
    ('Previdência Social',      972_000_000_000),
    ('Saúde',                   245_000_000_000),
    ('Assistência Social / BF', 245_000_000_000),
    ('Educação',                226_000_000_000),
    ('Infraestrutura/PAC',       95_000_000_000),
    ('Defesa Nacional',          64_000_000_000),
    ('Ciência e Tecnologia',     12_000_000_000),
    ('Cultura',                   4_000_000_000),
]
rows8 = []
for nome, val_brl in areas:
    val_usd  = val_brl / USD_BRL
    meses    = MUSK_BRL / val_brl * 12   # errado, recalcular
    meses    = MUSK / (val_usd / 12)     # meses = fortuna / (area_usd/12)
    anos_a   = meses / 12
    pct_fort = val_usd / MUSK * 100
    rows8.append([nome, f'R$ {val_brl/1e9:.0f}bi', f'US$ {val_usd/1e9:.1f}bi',
                  f'{meses:.0f} meses', f'{anos_a:.1f} anos', f'{pct_fort:.2f}% de Musk'])

meses_total = MUSK / (ORCAMENTO_USD / 12)
rows8.append(['TOTAL (sem refinanciamento)', f'R$ {ORCAMENTO_BRL/1e12:.1f}tri',
              f'US$ {ORCAMENTO_USD/1e9:.0f}bi', f'{meses_total:.1f} meses',
              f'{meses_total/12:.2f} anos', '100% de Musk'])

c8 = card(8,'🏛️','Finanças Públicas',
  'Comparação com o Orçamento Federal do Brasil',
  f'{meses_total:.1f} meses',
  'de orçamento federal completo do Brasil (excluindo refinanciamento da dívida pública)',
  f'''<p><strong>Orçamento Federal 2025 (LOA):</strong> R$ 5,9 trilhões totais.
  Excluindo o refinanciamento da dívida pública (R$ 1,8tri), o valor efetivo de
  despesas é <strong>R$ 4,1 trilhões = US$ {ORCAMENTO_USD/1e9:.0f} bilhões</strong>.</p>
  <p><strong>Fortuna Musk em BRL:</strong> R$ {MUSK_BRL/1e12:.2f} trilhões.</p>
  <p><strong>Relação:</strong> R$ {MUSK_BRL/1e12:.2f}tri ÷ R$ {ORCAMENTO_BRL/1e12:.1f}tri/ano
  = <strong>{MUSK_BRL/ORCAMENTO_BRL:.2f} orçamentos anuais</strong>
  = {meses_total:.1f} meses de governo.</p>''',
  f'''<p>A fortuna de Musk equivale a <strong>{MUSK_BRL/ORCAMENTO_BRL:.2f} orçamentos federais
  anuais do Brasil</strong> — ou seja, poderia financiar todo o governo federal
  (saúde, educação, previdência, infraestrutura, defesa) por
  <strong>{meses_total:.0f} meses e {(meses_total%12):.0f} dias</strong>.</p>
  <p>Detalhe revelador: a área de <strong>Ciência e Tecnologia</strong> (R$ 12bi) recebe
  apenas <strong>{12e9/ORCAMENTO_BRL*100:.2f}%</strong> do orçamento federal —
  Musk poderia financiá-la por <strong>{MUSK_BRL/(12e9)*12:.0f} meses</strong> (mais de
  {MUSK_BRL/(12e9):.0f} anos).</p>
  <p>A <strong>Previdência Social</strong> (R$ 972bi) é a maior despesa —
  mas mesmo ela poderia ser financiada por <strong>{MUSK_BRL/972e9:.1f} anos</strong>
  com a fortuna de Musk.</p>
  <p>Para contexto: o Brasil arrecada em impostos aproximadamente R$ 3 trilhões/ano.
  Musk tem quase <strong>2× a arrecadação federal anual do Brasil</strong>.</p>''',
  tbl(['Área de Governo','Orçamento (BRL)','Orçamento (USD)','Meses financiados','Anos financiados','% da fortuna'],
      rows8, highlight=lambda r: 'TOTAL' in r[0]),
  [('Senado Federal – LOA 2025','https://www12.senado.leg.br/noticias/materias/2025/03/20/congresso-aprova-orcamento-de-2025-para-destinacao-de-5-7-trilhoes'),
   ('Câmara dos Deputados – Orçamento 2025','https://www.camara.leg.br/noticias/1142456-congresso-nacional-aprova-proposta-de-orcamento-de-2025/'),
   ('Forbes Billionaires – Elon Musk','https://www.forbes.com/real-time-billionaires/')])

# ─────────────────────────────────────────────────────────────────────────────
# CENÁRIO 9
# ─────────────────────────────────────────────────────────────────────────────
CESTA_SP  = 845.95
CESTA_MED = 750.0
CESTA_USD = CESTA_MED / USD_BRL
cestas_total = MUSK_BRL / CESTA_MED

grupos9 = [
    ('19,8M fam. Bolsa Família', 19_800_000, CESTA_MED),
    ('50M famílias mais pobres',  50_000_000, CESTA_MED),
    ('70M famílias baixa renda',  70_000_000, CESTA_MED),
    ('Toda a população BR (214M pessoas / família de 3)', 214_000_000//3, CESTA_MED),
    ('Toda a humanidade (8,2bi pessoas / família de 4)',  POP_MUNDO//4, CESTA_MED),
]
rows9 = []
for nome, n_fam, custo in grupos9:
    meses_dur = cestas_total / n_fam
    anos_dur  = meses_dur / 12
    custo_1y  = n_fam * custo * 12
    rows9.append([nome, f'{n_fam:,}', f'R$ {custo:,.2f}/mês',
                  f'{meses_dur:.1f} meses', f'{anos_dur:.2f} anos',
                  f'R$ {custo_1y/1e9:.1f}bi/ano'])

c9 = card(9,'🛒','Alimentação',
  'Quantas Cestas Básicas?',
  f'{cestas_total/1e9:.2f} bilhões',
  f'de cestas básicas mensais — com a fortuna convertida em R$ {MUSK_BRL/1e12:.2f} trilhões',
  f'''<p><strong>Cesta básica (DIEESE, dez/2025):</strong></p>
  <ul>
    <li>São Paulo (mais cara): R$ {CESTA_SP}/mês</li>
    <li>Média nacional estimada: R$ {CESTA_MED}/mês</li>
    <li>Em USD: US$ {CESTA_USD:.2f}/mês</li>
  </ul>
  <p><strong>Cálculo total:</strong> R$ {MUSK_BRL/1e12:.2f}tri ÷ R$ {CESTA_MED:.2f}
  = <strong>{cestas_total/1e9:.2f} bilhões</strong> de cestas mensais.</p>
  <p><strong>Premissa:</strong> preço constante (sem inflação). Na prática, o volume de compras
  causaria deflação no preço dos alimentos, aumentando ainda mais o poder de compra.</p>''',
  f'''<p>R$ {MUSK_BRL/1e12:.2f} trilhões comprariam <strong>{cestas_total/1e9:.2f} bilhões
  de cestas básicas</strong> — o suficiente para alimentar as
  <strong>19,8 milhões de famílias do Bolsa Família por {cestas_total/19.8e6/12:.0f} anos</strong>
  ininterruptos.</p>
  <p>Para <em>toda</em> a população brasileira (considerando famílias de 3 pessoas),
  a fortuna pagaria <strong>{cestas_total/(214e6/3)/12:.1f} anos</strong> de alimentação básica.</p>
  <p>Se dividida entre <em>toda a humanidade</em> (famílias de 4 pessoas — 2,05 bilhões de famílias),
  cada família receberia <strong>{cestas_total/2.05e9:.1f} cestas</strong> —
  quase <strong>{cestas_total/2.05e9/12:.1f} anos</strong> de alimentação.</p>
  <p>Contexto: o gasto anual do governo federal em assistência alimentar e nutricional
  é de aproximadamente R$ 12 bilhões — Musk poderia financiá-lo por
  <strong>{MUSK_BRL/12e9:.0f} anos</strong>.</p>''',
  tbl(['Grupo','Nº de famílias','Custo por mês','Duração','Duração (anos)','Custo anual'],
      rows9),
  [('DIEESE – Cesta Básica nov-dez/2025','https://www.dieese.org.br/analisecestabasica/2025/202511cestabasica.html'),
   ('Agência Brasil – Cesta Básica dez/2025','https://agenciabrasil.ebc.com.br/economia/noticia/2026-01/cesta-basica-fica-mais-cara-em-17-capitais-em-dezembro'),
   ('Forbes Billionaires – Elon Musk','https://www.forbes.com/real-time-billionaires/')])

# ─────────────────────────────────────────────────────────────────────────────
# CENÁRIO 10
# ─────────────────────────────────────────────────────────────────────────────
infra = [
    ('Escola municipal padrão',  3_000_000,  181_939, 'FNDE/MEC'),
    ('Hospital SUS de grande porte', 500_000_000, 5_988, 'Ministério da Saúde'),
    ('UPA 24h',                   8_000_000,     600, 'Ministério da Saúde'),
    ('Creche pública',            1_500_000,  80_000, 'FNDE/MEC'),
    ('Posto de saúde (UBS)',         800_000,  47_000, 'Ministério da Saúde'),
    ('Biblioteca pública',        1_200_000,   7_000, 'IBGE/MinC'),
]
rows10 = []
for nome, custo_brl, existe, fonte_i in infra:
    custo_usd = custo_brl / USD_BRL
    possivel  = int(MUSK / custo_usd)
    multiplo  = possivel / existe
    rows10.append([nome, f'R$ {custo_brl/1e6:.1f}M / US$ {custo_usd/1e6:.0f}M',
                   f'{existe:,}', f'{possivel:,}', f'{multiplo:.0f}×', fonte_i])

c10 = card(10,'🏥','Infraestrutura',
  'Escolas, Hospitais e Infraestrutura Social',
  '1,9 milhão de escolas',
  'ou 11.415 grandes hospitais — e ainda sobraria para construir muito mais',
  '''<p><strong>Metodologia:</strong> custos médios de construção obtidos de contratos
  e estimativas do FNDE/MEC e Ministério da Saúde (2024–2025). Convertidos para USD
  pelo câmbio de R$ 5,71/USD.</p>
  <p><strong>Referências de estoque atual:</strong> Censo Escolar 2023 (INEP), CNS/IBGE
  (hospitais SUS), dados governamentais.</p>
  <p><strong>Cálculo:</strong> US$ 1 trilhão ÷ custo unitário em USD = unidades possíveis.</p>''',
  f'''<p>Com US$ 1 trilhão, seria possível construir:</p>
  <ul>
    <li><strong>1,9 milhão de escolas</strong> — {int(MUSK/(3e6/USD_BRL))/181939:.0f}× o número atual de escolas públicas no Brasil</li>
    <li><strong>11.415 hospitais de grande porte</strong> — {int(MUSK/(500e6/USD_BRL))/5988:.1f}× todos os hospitais do SUS</li>
    <li><strong>713.750 UPAs 24h</strong> — {int(MUSK/(8e6/USD_BRL))/600:.0f}× as ~600 existentes</li>
    <li><strong>3,8 milhões de creches</strong> — {int(MUSK/(1.5e6/USD_BRL))/80000:.0f}× o estoque atual</li>
  </ul>
  <p>Para contexto: o Brasil leva décadas discutindo a construção de mais hospitais no SUS.
  A fortuna de Musk poderia construir <strong>todo o estoque hospitalar brasileiro</strong>
  e ainda teria dinheiro sobrando para mais {int(MUSK/(500e6/USD_BRL))-5988:,} hospitais.</p>
  <p>O Brasil tem uma média de <strong>{1/((181939)/(POP_BR/1000)):.0f} escolas por mil habitantes</strong>.
  Com Musk, essa média poderia ser multiplicada por {int(MUSK/(3e6/USD_BRL))/181939:.0f}×.</p>''',
  tbl(['Equipamento','Custo unitário','Existe hoje (BR)','Possível construir','Múltiplo','Fonte'],
      rows10, highlight=lambda r: 'Escola' in r[0] or 'Hospital' in r[0]),
  [('FNDE/MEC – Custo de Construção Escolar','https://www.fnde.gov.br'),
   ('Ministério da Saúde – Investimentos 2024-25','https://www.gov.br/saude/pt-br/assuntos/noticias/2025/novembro/ministerio-da-saude-vai-investir-r-4-5-bilhoes-em-rede-de-hospitais'),
   ('INEP – Censo Escolar 2023','https://www.gov.br/inep'),
   ('Forbes Billionaires – Elon Musk','https://www.forbes.com/real-time-billionaires/')])

# ─────────────────────────────────────────────────────────────────────────────
# CENÁRIO 11
# ─────────────────────────────────────────────────────────────────────────────
pib_top = sorted(pib_data, key=lambda x: float(x['pib_bilhoes_usd']), reverse=True)[:15]
rows11 = []
for p in pib_top:
    pib = float(p['pib_bilhoes_usd'])
    pct = MUSK/1e9 / pib * 100
    rows11.append([p['pais'], p['continente'], f'US$ {pib:,.0f}bi',
                   f'{pct:.1f}% de Musk', f'Musk = {MUSK/1e9/pib:.3f}× o PIB'])

rows11_extra = [
    ['PIB Mundial', '—', f'US$ {PIB_MUND/1e12:.0f}tri', f'{MUSK/PIB_MUND*100:.3f}% de Musk', '—'],
    ['Riqueza Mundial (UBS)', '—', f'US$ {RIQ_MUND/1e12:.0f}tri', f'{MUSK/RIQ_MUND*100:.4f}% de Musk', '—'],
]

c11 = card(11,'📊','PIB & Macroeconômico',
  'Comparação com o PIB Brasileiro e Mundial',
  f'{MUSK/PIB_BR*100:.1f}% do PIB do Brasil',
  f'a fortuna de Musk equivale a quase metade de toda a riqueza produzida pelo Brasil em um ano',
  f'''<p><strong>PIB nominal do Brasil (FMI 2024):</strong> US$ {PIB_BR/1e12:.3f} trilhões.</p>
  <p><strong>PIB Mundial (FMI 2024):</strong> US$ {PIB_MUND/1e12:.0f} trilhões.</p>
  <p><strong>Cálculo:</strong> US$ 1tri ÷ US$ {PIB_BR/1e12:.3f}tri = {MUSK/PIB_BR*100:.1f}% do PIB do Brasil.</p>
  <p><strong>Nota:</strong> PIB é fluxo anual de produção; fortuna é estoque de riqueza acumulada.
  A comparação serve para dimensionar escala, não para equivalência econômica direta.</p>''',
  f'''<p>A fortuna de Musk representa <strong>{MUSK/PIB_BR*100:.1f}%</strong> do PIB anual do Brasil
  — isto é, se o Brasil parasse de produzir qualquer coisa e destinasse <em>toda</em> a sua
  produção econômica para Musk, levaria <strong>{PIB_BR/MUSK*12:.1f} meses</strong> para
  "pagar" sua fortuna.</p>
  <p>Em relação ao <strong>PIB Mundial</strong> (US$ {PIB_MUND/1e12:.0f} trilhões),
  Musk representa <strong>{MUSK/PIB_MUND*100:.3f}%</strong> — ou seja, a produção econômica
  de {MUSK/PIB_MUND*100:.3f}% do planeta por um ano inteiro.</p>
  <p>Comparando com a América do Sul: a soma dos PIBs de
  Argentina (US$ 621bi), Chile (US$ 317bi), Colômbia (US$ 363bi), Peru (US$ 268bi),
  Venezuela, Equador, Bolívia e Paraguai totaliza aproximadamente US$ {(621+317+363+268+43+118+45+70):.0f}bi
  — ainda inferior à fortuna de Musk (US$ 1.000bi).</p>''',
  tbl(['País','Continente','PIB 2024','% da fortuna de Musk','Relação'], rows11 + rows11_extra,
      highlight=lambda r: 'Brasil' in r[0] or 'Musk' in r[0]),
  [('FMI – World Economic Outlook 2024','https://www.imf.org/en/Publications/WEO'),
   ('Banco Mundial – GDP Data 2024','https://data.worldbank.org'),
   ('Forbes Billionaires – Elon Musk','https://www.forbes.com/real-time-billionaires/')])

# ─────────────────────────────────────────────────────────────────────────────
# CENÁRIO 12
# ─────────────────────────────────────────────────────────────────────────────
ANOS_TRAB = 35
rows12 = []
for p in sorted(profs, key=lambda x: float(x['salario_medio_brl'])):
    sal  = float(p['salario_medio_brl'])
    anual_brl = sal * 12
    vita_brl  = anual_brl * ANOS_TRAB
    vita_usd  = vita_brl / USD_BRL
    vidas     = MUSK / vita_usd
    pct       = vita_usd / MUSK * 100
    sal_musk_dia = MUSK / 365.25 / (vita_usd / (ANOS_TRAB * 365.25))
    rows12.append([p['profissao'], f'R$ {sal:,.0f}/mês',
                   f'R$ {anual_brl:,.0f}/ano', f'R$ {vita_brl/1e6:.2f}M',
                   f'US$ {vita_usd/1e3:.1f}mil', f'{vidas:,.0f}',
                   f'{pct:.6f}%', p['descricao']])

enf_vidas = MUSK / (4750*12*35/USD_BRL)
med_vidas = MUSK / (12000*12*35/USD_BRL)
rural_vidas = MUSK / (1621*12*35/USD_BRL)

c12 = card(12,'👩‍⚕️','Trabalho & Desigualdade',
  'Renda Vitalícia de Profissões Essenciais',
  f'{rural_vidas:,.0f} vidas',
  'de trabalho de um trabalhador rural (salário mínimo, 35 anos) seriam necessárias para igualar a fortuna de Musk',
  f'''<p><strong>Metodologia:</strong></p>
  <div class="formula">Renda vitalícia = Salário mensal × 12 meses × {ANOS_TRAB} anos de trabalho</div>
  <div class="formula">Vidas necessárias = Fortuna de Musk ÷ Renda vitalícia (USD)</div>
  <p><strong>Premissas:</strong></p>
  <ul>
    <li>Vida laborativa: {ANOS_TRAB} anos (típico no Brasil)</li>
    <li>Salários: pisos das categorias e médias de mercado 2025</li>
    <li>Sem 13º salário, férias ou benefícios (simplificado)</li>
    <li>Sem crescimento salarial ou inflação (limite teórico)</li>
  </ul>''',
  f'''<p>Nem <strong>um milhão de médicos</strong> trabalhando {ANOS_TRAB} anos cada um
  chegariam a acumular o que Musk tem hoje — seriam necessários
  <strong>{med_vidas/1e6:.2f} milhões de vidas de médico</strong>.</p>
  <p>Para <strong>enfermeiros(as)</strong>, uma das categorias mais essenciais e historicamente
  mal remuneradas no Brasil, seriam necessárias <strong>{enf_vidas/1e6:.1f} milhões de vidas</strong>
  de trabalho — cada vida representando {ANOS_TRAB} anos de dedicação.</p>
  <p>Um <strong>trabalhador rural</strong> de salário mínimo (R$ 1.621/mês) acumula apenas
  <strong>R$ {1621*12*35/1e6:.2f}M</strong> em toda uma vida de trabalho —
  Musk acumulou essa quantia em menos de <strong>{1621*12*35/USD_BRL/(MUSK/365.25/24/3600):.0f} segundos</strong>
  em seu melhor ano (2025: ganho de US$ 215bi).</p>
  <p>Ou seja: enquanto um trabalhador rural trabalha um ano inteiro para ganhar
  R$ {1621*12:,.0f}, Musk ganhou em 2025 (em média)
  R$ {215e9*USD_BRL/365/1621/12*100:.0f} vezes esse valor por dia.</p>''',
  tbl(['Profissão','Salário/mês','Renda anual','Vida inteira (BRL)','Vida inteira (USD)',
       'Vidas p/ igualar Musk','% da fortuna','Referência'],
      rows12, highlight=lambda r: 'Enfermeiro' in r[0] or 'Trabalhador Rural' in r[0]),
  [('CFE – Piso de Enfermagem (Lei 14.434/2022)','https://www.gov.br'),
   ('MEC – Piso Nacional do Magistério 2025','https://www.gov.br/mec'),
   ('CFM – Remuneração Médica 2024','https://www.cfm.org.br'),
   ('Forbes Billionaires – Elon Musk','https://www.forbes.com/real-time-billionaires/')])

# ─────────────────────────────────────────────────────────────────────────────
# CENÁRIO 13
# ─────────────────────────────────────────────────────────────────────────────
grupos13 = [
    ('Toda a humanidade',          POP_MUNDO,     5.50, 'ONU 2024'),
    ('Toda a pop. brasileira',     POP_BR,        5.50, 'IBGE 2024'),
    ('50% mais pobres do mundo',   int(POP_MUNDO*0.5), 2.15, 'Banco Mundial'),
    ('Pobreza extrema mundial',    700_000_000,   2.15, 'Banco Mundial'),
    ('Sem-teto no Brasil (2025)',  365_822,        None, 'OBPopRua/UFMG'),
    ('Sem-teto nos EUA (2024)',    771_480,        None, 'HUD 2024'),
]
rows13 = []
for nome, pop, linha_pob, fonte_i in grupos13:
    por_pessoa = MUSK / pop
    if linha_pob:
        dias_sub = por_pessoa / linha_pob
        anos_sub = dias_sub / 365.25
        sub_str  = f'{anos_sub:.1f} anos'
    else:
        dias_sub = None
        sub_str  = 'N/A (sem linha definida)'
    rows13.append([nome, f'{pop:,}', f'US$ {por_pessoa:,.2f}',
                   f'US$ {por_pessoa*USD_BRL:,.2f} (BRL)' if por_pessoa < 1000 else f'R$ {por_pessoa*USD_BRL:,.0f}',
                   sub_str, fonte_i])

por_pessoa_br   = MUSK / POP_BR
por_pessoa_ext  = MUSK / 700_000_000
por_pessoa_rua_br = MUSK / 365_822

c13 = card(13,'🌐','Distribuição de Renda',
  'E Se Fosse Distribuída Igualmente?',
  f'US$ {MUSK/POP_BR:,.0f}',
  'seria o valor que cada brasileiro receberia se a fortuna de Musk fosse distribuída igualmente',
  f'''<p><strong>Premissa:</strong> distribuição igualitária da fortuna (US$ 1 trilhão)
  entre o grupo especificado.</p>
  <p><strong>Linha de pobreza (Banco Mundial 2024):</strong></p>
  <ul>
    <li>Pobreza extrema: US$ 2,15/dia</li>
    <li>Pobreza moderada: US$ 5,50/dia</li>
  </ul>
  <p><strong>Nota:</strong> é um exercício hipotético. Na prática, redistribuir
  US$ 1 trilhão em dinheiro causaria hiperinflação. A análise serve para
  dimensionar a magnitude da concentração.</p>''',
  f'''<p>Para <strong>toda a humanidade</strong> ({POP_MUNDO/1e9:.1f} bilhões de pessoas):
  cada um receberia <strong>US$ {MUSK/POP_MUNDO:.2f}</strong> —
  suficiente para sobreviver <strong>{MUSK/POP_MUNDO/5.50/365.25:.1f} anos</strong>
  na linha de pobreza moderada.</p>
  <p>Para <strong>todos os brasileiros</strong>: US$ {por_pessoa_br:,.0f} por pessoa
  = R$ {por_pessoa_br*USD_BRL:,.0f} — equivalente a
  <strong>{por_pessoa_br*USD_BRL/1621:.1f} salários mínimos de 2026</strong>.</p>
  <p>Para os <strong>700 milhões em pobreza extrema</strong>: US$ {por_pessoa_ext:,.2f} cada —
  o suficiente para <strong>{MUSK/700e6/2.15/365.25:.1f} anos</strong>
  acima da linha de pobreza extrema (US$ 2,15/dia).</p>
  <p>Para as <strong>{365_822:,} pessoas em situação de rua no Brasil</strong>:
  US$ {por_pessoa_rua_br:,.0f} = R$ {por_pessoa_rua_br*USD_BRL:,.0f} por pessoa —
  equivale a <strong>{por_pessoa_rua_br*USD_BRL/1621:.0f} meses</strong> de salário mínimo.</p>''',
  tbl(['Grupo','Nº de pessoas','Por pessoa (USD)','Por pessoa (BRL)','Anos na linha de pobreza','Fonte'],
      rows13, highlight=lambda r: 'brasileira' in r[0] or 'Brasil' in r[0]),
  [('Banco Mundial – Linhas de Pobreza 2024','https://www.worldbank.org/en/topic/poverty'),
   ('IBGE – Projeção Populacional 2024','https://www.ibge.gov.br'),
   ('ONU – World Population 2024','https://www.un.org/development/desa/pd/'),
   ('OBPopRua/UFMG – Sem-teto BR','https://agenciabrasil.ebc.com.br/direitos-humanos/noticia/2026-01/estudo-aponta-mais-365-mil-pessoas-em-situacao-de-rua-no-brasil'),
   ('HUD – 2024 AHAR','https://www.huduser.gov/portal/publications/2024-ahar-part-1-pit-estimates-of-homelessness.html'),
   ('Forbes Billionaires – Elon Musk','https://www.forbes.com/real-time-billionaires/')])

# ─────────────────────────────────────────────────────────────────────────────
# CENÁRIO 14
# ─────────────────────────────────────────────────────────────────────────────
eua_latest = {int(r['ano']): int(r['populacao_rua']) for r in rua_eua}
rows14 = []
for r in rua_eua:
    ano  = int(r['ano'])
    pop  = int(r['populacao_rua'])
    var  = r.get('variacao_pct', '—')
    musk_v = latest.get(ano)
    musk_s = f'US$ {musk_v:.0f}bi' if musk_v else '—'
    rows14.append([str(ano), f'{pop:,}', var + '%' if var and var != '—' and var != '' else '—',
                   musk_s, r['fonte']])

# Pearson EUA
anos_eua_cm = [int(r['ano']) for r in rua_eua if latest.get(int(r['ano']))]
pop_eua_cm  = [int(r['populacao_rua']) for r in rua_eua if latest.get(int(r['ano']))]
musk_eua_cm = [latest[a] for a in anos_eua_cm]
n2 = len(anos_eua_cm)
if n2 > 1:
    mx2 = sum(musk_eua_cm)/n2; my2 = sum(pop_eua_cm)/n2
    n2v = sum((musk_eua_cm[i]-mx2)*(pop_eua_cm[i]-my2) for i in range(n2))
    d2v = (sum((m-mx2)**2 for m in musk_eua_cm) * sum((p-my2)**2 for p in pop_eua_cm))**0.5
    r_eua = n2v/d2v if d2v else 0
else:
    r_eua = 0

pop_2012 = eua_latest.get(2012, eua_latest.get(2013, 0))
pop_2016 = eua_latest.get(2016, 0)
pop_2024 = eua_latest.get(2024, 0)
musk_2012 = latest.get(2012, 0)
musk_2024 = latest.get(2024, 0)

extra14 = img('14b', 'Comparação Brasil vs EUA')

c14 = card(14,'🏘️','Correlação & EUA',
  'Correlação: Fortuna de Musk × População de Rua nos EUA',
  f'r = {r_eua:.3f}',
  f'correlação de Pearson moderada — diferente do Brasil (r={r_br:.3f}) por causa de políticas de Housing First (2010–2016)',
  f'''<p><strong>Fonte base:</strong> HUD Annual Homeless Assessment Report (AHAR) —
  Point-in-Time Count anual (janeiro de cada ano).</p>
  <p><strong>Período:</strong> 2012–2024 (anos com dados em ambas as séries).
  2021 excluído por metodologia afetada pela pandemia.</p>
  <p><strong>Correlação de Pearson:</strong> r = {r_eua:.4f}</p>
  <p><strong>Comparação Brasil:</strong> r = {r_br:.4f}</p>
  <p><strong>Limitação:</strong> O PIT Count é uma contagem de uma única noite —
  subestima a população real. A verdadeira escala pode ser 3–5× maior ao longo do ano.</p>''',
  f'''<p>A análise dos EUA revela uma trajetória em <strong>duas fases opostas</strong>,
  tornando-a mais rica analyticamente que a brasileira:</p>
  <p><strong>Fase 1 – Redução (2012–2016):</strong> O sem-teto caiu de {pop_2012:,} para {pop_2016:,}
  pessoas (−{(pop_2016/pop_2012-1)*(-100):.1f}%), enquanto a fortuna de Musk crescia de
  US$ {musk_2012:.0f}bi para US$ {latest.get(2016, 0):.0f}bi.
  Isso foi possível graças ao programa <em>Housing First</em> — que prioriza moradia
  permanente antes de tratar outros problemas — amplamente financiado pelo governo Obama.</p>
  <p><strong>Fase 2 – Explosão (2019–2024):</strong> O sem-teto cresceu de
  {eua_latest.get(2019, 0):,} para {pop_2024:,} pessoas (+{(pop_2024/eua_latest.get(2019,1)-1)*100:.1f}%),
  enquanto a fortuna de Musk saltou de US$ 20bi para US$ {musk_2024:.0f}bi (+{(musk_2024/20-1)*100:.0f}%).</p>
  <p><strong>Lição crítica:</strong> O contraste Brasil × EUA demonstra que <em>política pública importa</em>.
  A queda americana de 2010–2016 prova que é possível reduzir o sem-teto mesmo em contexto de
  crescente concentração de riqueza — desde que haja investimento e vontade política.
  Quando essas políticas foram enfraquecidas, os números explodiriam: o 2024 foi o
  <strong>maior registro histórico</strong> (771.480 pessoas).</p>
  <p>O Brasil, que nunca implementou <em>Housing First</em> em escala nacional,
  apresenta correlação muito mais forte (r={r_br:.3f}) porque suas duas séries
  seguem trajetórias monotonicamente crescentes.</p>''',
  tbl(['Ano','Pop. sem-teto','Variação anual','Fortuna de Musk','Fonte HUD'], rows14,
      highlight=lambda r: r[0] in ['2016','2024'],
      notes='* 2021 excluído: metodologia de contagem alterada pela pandemia de COVID-19, dados incomparáveis.'),
  [('HUD – 2024 Annual Homelessness Assessment Report','https://www.huduser.gov/portal/publications/2024-ahar-part-1-pit-estimates-of-homelessness.html'),
   ('National Alliance to End Homelessness – HUD 2024','https://endhomelessness.org/media/news-releases/hud-releases-2024-annual-homelessness-assessment-report/'),
   ('Bipartisan Policy Center – Homelessness at a Record High','https://bipartisanpolicy.org/article/homelessness-at-a-record-high-key-takeaways-from-the-2024-pit-count/'),
   ('Bloomberg Billionaires Index','https://www.bloomberg.com/billionaires/'),
   ('Forbes Billionaires – Elon Musk','https://www.forbes.com/real-time-billionaires/')],
  extra_chart=f'<div class="box box-chart" style="margin-top:12px">{extra14}</div>')

# ─────────────────────────────────────────────────────────────────────────────
# MONTA O HTML
# ─────────────────────────────────────────────────────────────────────────────
nav_links = ''.join(
    f'<a href="#c{n:02d}">{n:02d}. {t}</a>'
    for n, t in [
        (1,'Salário Mínimo'),(2,'PIB Países'),(3,'Riqueza Mundial'),
        (4,'Bolsa Família'),(5,'Habitação'),(6,'Rua BR'),
        (7,'US$ 1M/dia'),(8,'Orçamento BR'),(9,'Cestas Básicas'),
        (10,'Infraestrutura'),(11,'PIB Comparação'),(12,'Profissões'),
        (13,'Distribuição'),(14,'Rua EUA'),
    ])

BODY = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14

HTML = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Relatório Completo — US$ 1 Trilhão de Elon Musk</title>
<style>
:root{{
  --r:#c0392b;--rd:#8e1a0e;--rl:#e74c3c;
  --bg:#f0f2f5;--white:#fff;--dark:#1a1a2e;
  --text:#2c3e50;--muted:#666;--border:#e0e0e0;
  --shadow:0 4px 20px rgba(0,0,0,.07);
  --met-bg:#eaf4fb;--ana-bg:#fdfefe;
}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Segoe UI',Arial,sans-serif;background:var(--bg);color:var(--text);line-height:1.65;font-size:15px}}

/* HERO */
.hero{{background:linear-gradient(135deg,#1a1a2e,#8e1a0e);color:#fff;padding:70px 20px 50px;text-align:center}}
.hero-badge{{display:inline-block;background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.3);border-radius:20px;padding:5px 16px;font-size:.8rem;letter-spacing:.1em;text-transform:uppercase;margin-bottom:18px}}
.hero h1{{font-size:clamp(1.8rem,4vw,3rem);font-weight:800;line-height:1.2;margin-bottom:12px}}
.hero-valor{{font-size:clamp(2.5rem,6vw,5rem);font-weight:900;color:#ff6b6b;display:block;margin:16px 0;letter-spacing:-.02em;text-shadow:0 0 30px rgba(255,107,107,.4)}}
.hero p{{opacity:.85;max-width:680px;margin:0 auto 24px;font-size:1.05rem}}
.hero-grid{{display:flex;justify-content:center;gap:36px;flex-wrap:wrap;margin-top:24px}}
.hero-stat .n{{font-size:1.9rem;font-weight:800;color:#ff6b6b}}
.hero-stat .l{{font-size:.75rem;opacity:.7;text-transform:uppercase;letter-spacing:.05em}}

/* NAV */
nav{{background:#16213e;padding:12px 16px;display:flex;flex-wrap:wrap;gap:6px;justify-content:center;position:sticky;top:0;z-index:100;box-shadow:0 2px 10px rgba(0,0,0,.3)}}
nav a{{color:rgba(255,255,255,.65);text-decoration:none;font-size:.72rem;padding:4px 9px;border-radius:10px;transition:.2s;font-weight:500}}
nav a:hover{{background:var(--r);color:#fff}}

/* LAYOUT */
main{{max-width:1300px;margin:36px auto;padding:0 18px}}

/* CENÁRIO */
.cenario{{background:var(--white);border-radius:14px;box-shadow:var(--shadow);margin-bottom:40px;border-left:5px solid var(--r);overflow:hidden}}
.c-head{{display:flex;align-items:center;gap:14px;padding:22px 26px;background:linear-gradient(135deg,#fff 60%,#fff5f5);border-bottom:1px solid #fde8e8}}
.c-num{{background:var(--r);color:#fff;font-size:1.3rem;font-weight:900;width:48px;height:48px;border-radius:10px;display:flex;align-items:center;justify-content:center;flex-shrink:0}}
.c-icon{{font-size:1.9rem;flex-shrink:0}}
.c-tag{{background:#fde8e8;color:var(--rd);font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;padding:2px 9px;border-radius:8px;display:inline-block;margin-bottom:5px}}
.c-meta h2{{font-size:clamp(1rem,2.2vw,1.3rem);font-weight:700;color:var(--dark)}}

/* DESTAQUE */
.c-destaque{{background:linear-gradient(135deg,var(--r),var(--rd));color:#fff;padding:22px 26px;text-align:center}}
.c-big{{font-size:clamp(1.8rem,4vw,3rem);font-weight:900;letter-spacing:-.02em;line-height:1.1;text-shadow:0 2px 8px rgba(0,0,0,.2)}}
.c-sub{{font-size:.92rem;opacity:.9;margin-top:7px;max-width:700px;margin-left:auto;margin-right:auto}}

/* BODY */
.c-body{{display:grid;grid-template-columns:1fr 1fr;gap:0}}
@media(max-width:800px){{.c-body{{grid-template-columns:1fr}}}}
.c-left{{padding:20px 22px;border-right:1px solid var(--border);display:flex;flex-direction:column;gap:16px}}
.c-right{{padding:20px 22px;display:flex;flex-direction:column;gap:14px;background:#fafafa}}

/* BOXES */
.box{{border-radius:10px;padding:16px 18px}}
.box h3{{font-size:.9rem;font-weight:700;margin-bottom:10px;color:var(--dark)}}
.box-met{{background:var(--met-bg);border-left:3px solid #2980b9}}
.box-ana{{background:var(--ana-bg);border-left:3px solid var(--r)}}
.box-chart{{background:#fff;border:1px solid var(--border);padding:10px}}

/* FORMULAS */
.formula{{background:#1a1a2e;color:#7fdbff;font-family:monospace;font-size:.85rem;padding:10px 14px;border-radius:6px;margin:8px 0;white-space:pre-wrap;word-break:break-all}}

/* TEXTO */
.box p{{margin-bottom:10px;font-size:.9rem;color:#444}}
.box ul{{padding-left:18px;margin-bottom:8px}}
.box li{{margin-bottom:6px;font-size:.9rem;color:#444}}
.box strong,.box b{{color:var(--rd)}}

/* CHART IMG */
.chart-img{{max-width:100%;height:auto;border-radius:6px;border:1px solid var(--border);display:block}}

/* DATA TABLE */
.c-data{{padding:20px 24px;border-top:1px solid var(--border)}}
.c-data h3{{font-size:.95rem;font-weight:700;color:var(--dark);margin-bottom:12px}}
.c-data h4{{font-size:.88rem;font-weight:700;color:var(--muted);margin:14px 0 8px}}
.tbl-wrap{{overflow-x:auto;border-radius:8px;border:1px solid var(--border)}}
table{{width:100%;border-collapse:collapse;font-size:.82rem}}
thead{{background:#1a1a2e;color:#fff}}
th{{padding:9px 12px;text-align:left;font-weight:600;white-space:nowrap}}
td{{padding:8px 12px;border-bottom:1px solid #f0f0f0;vertical-align:top}}
tr:last-child td{{border-bottom:none}}
tr:nth-child(even){{background:#fafafa}}
tr.hl{{background:#fff5f5!important;font-weight:600;color:var(--rd)}}
.tbl-note{{font-size:.75rem;color:var(--muted);margin-top:8px;font-style:italic;padding:0 4px}}

/* FONTES */
.c-fontes{{padding:12px 24px;background:#fafafa;border-top:1px solid var(--border);display:flex;flex-wrap:wrap;align-items:center;gap:7px;font-size:.75rem}}
.fl{{font-weight:700;color:#555;white-space:nowrap}}
.c-fontes a{{color:var(--r);text-decoration:none;border:1px solid #fde8e8;border-radius:6px;padding:2px 8px;transition:.2s;white-space:nowrap}}
.c-fontes a:hover{{background:var(--r);color:#fff;border-color:var(--r)}}

/* FOOTER */
footer{{background:#1a1a2e;color:rgba(255,255,255,.6);text-align:center;padding:40px 20px;margin-top:50px}}
footer h3{{color:#fff;margin-bottom:18px}}
.f-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:10px;max-width:1000px;margin:0 auto 24px;text-align:left}}
.f-grid a{{color:rgba(255,255,255,.65);text-decoration:none;font-size:.78rem;padding:7px 11px;background:rgba(255,255,255,.05);border-radius:6px;display:block;transition:.2s}}
.f-grid a:hover{{background:rgba(255,255,255,.12);color:#fff}}
.f-note{{font-size:.75rem;opacity:.45;margin-top:16px;max-width:560px;margin-left:auto;margin-right:auto}}

/* SUMÁRIO */
.sumario{{background:var(--white);border-radius:14px;box-shadow:var(--shadow);padding:28px;margin-bottom:36px;border-left:5px solid #2980b9}}
.sumario h2{{font-size:1.2rem;font-weight:700;color:var(--dark);margin-bottom:16px}}
.sum-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px}}
.sum-card{{background:#f0f7ff;border:1px solid #c5dff8;border-radius:8px;padding:12px;text-align:center}}
.sum-card .sn{{font-size:1.2rem;font-weight:900;color:var(--r);display:block}}
.sum-card .sl{{font-size:.72rem;color:var(--muted);margin-top:3px}}
</style>
</head>
<body>

<div class="hero">
  <div class="hero-badge">Relatório Completo · Análise de Dados · Desigualdade Social · 2026</div>
  <h1>A Fortuna de US$ 1 Trilhão de Elon Musk</h1>
  <span class="hero-valor">US$ 1.000.000.000.000</span>
  <p>Relatório completo com metodologia, dados brutos, tabelas e análise aprofundada
  dos 14 cenários que contextualizam a maior concentração de riqueza individual da história.</p>
  <div class="hero-grid">
    <div class="hero-stat"><div class="n">14</div><div class="l">Cenários</div></div>
    <div class="hero-stat"><div class="n">~176</div><div class="l">Países com PIB menor</div></div>
    <div class="hero-stat"><div class="n">R$ 5,71tri</div><div class="l">Em reais (jun/2026)</div></div>
    <div class="hero-stat"><div class="n">0,21%</div><div class="l">Da riqueza mundial</div></div>
    <div class="hero-stat"><div class="n">35,7 anos</div><div class="l">De Bolsa Família</div></div>
  </div>
</div>

<nav>{nav_links}</nav>

<main>

<div class="sumario">
  <h2>📌 Sumário Executivo — Números-Chave dos 14 Cenários</h2>
  <div class="sum-grid">
    <div class="sum-card"><span class="sn">{br_anos/1e6:,.0f}M anos</span><div class="sl">Trabalhador BR para acumular $1tri</div></div>
    <div class="sum-card"><span class="sn">{abaixo} países</span><div class="sl">Com PIB menor que a fortuna de Musk</div></div>
    <div class="sum-card"><span class="sn">{pct_musk:.4f}%</span><div class="sl">Da riqueza mundial ($471tri)</div></div>
    <div class="sum-card"><span class="sn">{anos_bf:.1f} anos</span><div class="sl">De Bolsa Família (19,8M famílias)</div></div>
    <div class="sum-card"><span class="sn">{vezes:.1f}×</span><div class="sl">O déficit habitacional do Brasil</div></div>
    <div class="sum-card"><span class="sn">r={r_br:.3f}</span><div class="sl">Correlação Musk × sem-teto BR</div></div>
    <div class="sum-card"><span class="sn">{anos_g:,.0f} anos</span><div class="sl">Gastando $1M/dia</div></div>
    <div class="sum-card"><span class="sn">{meses_total:.0f} meses</span><div class="sl">Do orçamento federal do Brasil</div></div>
    <div class="sum-card"><span class="sn">{cestas_total/1e9:.1f}bi</span><div class="sl">Cestas básicas mensais</div></div>
    <div class="sum-card"><span class="sn">{int(MUSK/(3e6/USD_BRL))/1e6:.1f}M</span><div class="sl">Escolas possíveis de construir</div></div>
    <div class="sum-card"><span class="sn">{MUSK/PIB_BR*100:.1f}%</span><div class="sl">Do PIB anual do Brasil</div></div>
    <div class="sum-card"><span class="sn">{rural_vidas/1e6:.1f}M vidas</span><div class="sl">De um trabalhador rural (35 anos)</div></div>
    <div class="sum-card"><span class="sn">US$ {MUSK/POP_BR:,.0f}</span><div class="sl">Por brasileiro se dividida igualmente</div></div>
    <div class="sum-card"><span class="sn">r={r_eua:.3f}</span><div class="sl">Correlação Musk × sem-teto EUA</div></div>
  </div>
</div>

{BODY}

</main>

<footer>
  <h3>📚 Todas as Fontes Utilizadas</h3>
  <div class="f-grid">
    <a href="https://www.forbes.com/real-time-billionaires/" target="_blank">Forbes Real-Time Billionaires — Fortuna de Musk (jun/2026)</a>
    <a href="https://www.bloomberg.com/billionaires/" target="_blank">Bloomberg Billionaires Index — Histórico de Riqueza</a>
    <a href="https://www.imf.org/en/Publications/WEO" target="_blank">FMI — World Economic Outlook 2024</a>
    <a href="https://data.worldbank.org/indicator/NY.GDP.MKTP.CD" target="_blank">Banco Mundial — GDP Data 2024</a>
    <a href="https://www.ubs.com/global/en/wealthmanagement/insights/global-wealth-report.html" target="_blank">UBS Global Wealth Report 2025</a>
    <a href="https://www.ipea.gov.br/portal/ipea-g20/noticias-g20/13457-populacao-em-situacao-de-rua-supera-281-4-mil-pessoas-no-brasil" target="_blank">IPEA — Pop. em Situação de Rua 2022</a>
    <a href="https://agenciabrasil.ebc.com.br/direitos-humanos/noticia/2026-01/estudo-aponta-mais-365-mil-pessoas-em-situacao-de-rua-no-brasil" target="_blank">OBPopRua/UFMG — 365 mil sem-teto (2025)</a>
    <a href="https://fjp.mg.gov.br/deficit-habitacional-recua-34-no-brasil-e-soma-5-773-983-domicilios/" target="_blank">Fundação João Pinheiro — Déficit Habitacional 2024</a>
    <a href="https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias/2025/12/publicado-decreto-que-reajusta-salario-minimo-para-r-1-621-a-partir-de-1o-de-janeiro" target="_blank">Planalto — Salário Mínimo R$ 1.621 (jan/2026)</a>
    <a href="https://www12.senado.leg.br/noticias/materias/2025/03/20/congresso-aprova-orcamento-de-2025-para-destinacao-de-5-7-trilhoes" target="_blank">Senado Federal — LOA 2025</a>
    <a href="https://www.gov.br/mds" target="_blank">MDS — Bolsa Família 2025</a>
    <a href="https://www.dieese.org.br/analisecestabasica/2025/202511cestabasica.html" target="_blank">DIEESE — Cesta Básica nov-dez/2025</a>
    <a href="https://www.worldbank.org/en/topic/poverty" target="_blank">Banco Mundial — Linhas de Pobreza 2024</a>
    <a href="https://www.huduser.gov/portal/publications/2024-ahar-part-1-pit-estimates-of-homelessness.html" target="_blank">HUD — 2024 Annual Homelessness Assessment Report (EUA)</a>
    <a href="https://bipartisanpolicy.org/article/homelessness-at-a-record-high-key-takeaways-from-the-2024-pit-count/" target="_blank">Bipartisan Policy Center — Homelessness at a Record High</a>
    <a href="https://www.gov.br/inep" target="_blank">INEP — Censo Escolar 2023</a>
    <a href="https://www.gov.br/saude/pt-br/assuntos/noticias/2025/novembro/ministerio-da-saude-vai-investir-r-4-5-bilhoes-em-rede-de-hospitais" target="_blank">Ministério da Saúde — Investimentos 2025</a>
    <a href="https://www.dol.gov/agencies/whd/minimum-wage" target="_blank">U.S. Dept of Labor — Minimum Wage 2025</a>
    <a href="https://www.fairwork.gov.au" target="_blank">Fair Work Commission — Salário Mínimo Austrália 2025</a>
    <a href="https://www.un.org/development/desa/pd/" target="_blank">ONU — Projeção Populacional Mundial 2024</a>
  </div>
  <div class="f-note">
    Dados de fontes públicas e reconhecidas. Correlações não implicam causalidade direta.
    Câmbio: US$ 1 = R$ 5,71 (aproximado jun/2026).
    Notebooks Jupyter disponíveis em notebooks/ · Dados em notebooks/data/
    <br><br>© 2026 · Análise de Dados · Desigualdade Social · US$ 1 Trilhão em Perspectiva
  </div>
</footer>
</body>
</html>'''

out = BASE / 'relatorio_completo.html'
out.write_text(HTML, encoding='utf-8')
mb = out.stat().st_size / 1024 / 1024
print(f"✅ relatorio_completo.html gerado — {mb:.1f} MB")
