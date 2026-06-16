#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Projeto: A Fortuna de US$ 1 Trilhão de Elon Musk e a Desigualdade Social
Gera todos os dados, notebooks Jupyter e HTML do projeto.

Fontes principais:
- Forbes Billionaires (fortuna Musk): https://www.forbes.com/real-time-billionaires/
- FMI/Banco Mundial (PIB países 2024): https://www.imf.org
- IPEA (população de rua): https://www.ipea.gov.br
- OBPopRua/UFMG: https://obpoprua.direito.ufmg.br
- Fundação João Pinheiro (déficit habitacional): https://fjp.mg.gov.br
- DIEESE (cesta básica): https://www.dieese.org.br
- UBS Global Wealth Report 2025: https://www.ubs.com
- Governo Federal (salário mínimo, Bolsa Família): https://www.gov.br
- Senado Federal (LOA 2025): https://www12.senado.leg.br
"""

import json
import csv
import subprocess
import sys
from pathlib import Path

BASE = Path('/var/home/rafael/Documentos/Projetos/elon')
NB = BASE / 'notebooks'
DATA = NB / 'data'
DATA.mkdir(parents=True, exist_ok=True)


# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────

def wcsv(name, rows):
    with open(DATA / name, 'w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerows(rows)
    print(f"  ✓ data/{name}")


def cell_md(src):
    return {"cell_type": "markdown", "metadata": {}, "source": src}


def cell_code(src):
    return {"cell_type": "code", "execution_count": None,
            "metadata": {}, "outputs": [], "source": src}


def make_notebook(cells):
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.14.5"}
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }


def save_nb(nb, fname):
    p = NB / fname
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    print(f"  ✓ notebooks/{fname}")


# ─────────────────────────────────────────────
# ARQUIVOS DE DADOS
# ─────────────────────────────────────────────

print("\n📁 Criando arquivos de dados...")

wcsv('pib_paises_2024.csv', [
    ['pais', 'pib_bilhoes_usd', 'continente'],
    ['Estados Unidos', 28781, 'América do Norte'],
    ['China', 18532, 'Ásia'],
    ['Alemanha', 4591, 'Europa'],
    ['Japão', 4110, 'Ásia'],
    ['Índia', 3937, 'Ásia'],
    ['Reino Unido', 3495, 'Europa'],
    ['França', 3130, 'Europa'],
    ['Itália', 2328, 'Europa'],
    ['Canadá', 2242, 'América do Norte'],
    ['Brasil', 2132, 'América do Sul'],
    ['Rússia', 2021, 'Europa/Ásia'],
    ['México', 1789, 'América do Norte'],
    ['Coreia do Sul', 1760, 'Ásia'],
    ['Austrália', 1723, 'Oceania'],
    ['Espanha', 1582, 'Europa'],
    ['Indonésia', 1476, 'Ásia'],
    ['Holanda', 1122, 'Europa'],
    ['Turquia', 1108, 'Europa/Ásia'],
    ['Arábia Saudita', 1099, 'Ásia'],
    ['Suíça', 905, 'Europa'],
    ['Polônia', 748, 'Europa'],
    ['Bélgica', 627, 'Europa'],
    ['Argentina', 621, 'América do Sul'],
    ['Suécia', 598, 'Europa'],
    ['Noruega', 547, 'Europa'],
    ['Irlanda', 533, 'Europa'],
    ['EAU', 527, 'Ásia'],
    ['Israel', 509, 'Ásia'],
    ['Cingapura', 501, 'Ásia'],
    ['Vietnã', 429, 'Ásia'],
    ['Dinamarca', 423, 'Europa'],
    ['Romênia', 351, 'Europa'],
    ['África do Sul', 373, 'África'],
    ['Colômbia', 363, 'América do Sul'],
    ['Nigéria', 362, 'África'],
    ['Egito', 347, 'África'],
    ['Rep. Tcheca', 345, 'Europa'],
    ['Paquistão', 338, 'Ásia'],
    ['Chile', 317, 'América do Sul'],
    ['Finlândia', 300, 'Europa'],
    ['Portugal', 286, 'Europa'],
    ['Cazaquistão', 261, 'Ásia'],
    ['Peru', 268, 'América do Sul'],
    ['Nova Zelândia', 245, 'Oceania'],
    ['Grécia', 238, 'Europa'],
    ['Ucrânia', 150, 'Europa'],
    ['Etiópia', 159, 'África'],
    ['Marrocos', 148, 'África'],
    ['Quênia', 107, 'África'],
    ['Rep. Dominicana', 113, 'Caribe'],
    ['Equador', 118, 'América do Sul'],
    ['Angola', 84, 'África'],
    ['Tanzânia', 79, 'África'],
    ['Costa do Marfim', 78, 'África'],
    ['Gana', 74, 'África'],
    ['Uganda', 50, 'África'],
    ['Camarões', 49, 'África'],
    ['Bolívia', 43, 'América do Sul'],
    ['Paraguai', 45, 'América do Sul'],
    ['El Salvador', 34, 'América Central'],
    ['Honduras', 32, 'América Central'],
    ['Senegal', 32, 'África'],
    ['Haiti', 20, 'Caribe'],
    ['Mali', 22, 'África'],
    ['Burkina Faso', 18, 'África'],
    ['Níger', 16, 'África'],
    ['Chade', 12, 'África'],
    ['Madagascar', 14, 'África'],
    ['Libéria', 4, 'África'],
    ['Serra Leoa', 5, 'África'],
])

wcsv('salarios_minimos_paises.csv', [
    ['pais', 'salario_mensal_usd', 'salario_local', 'moeda', 'fonte'],
    ['Índia', 214, 18000, 'INR', 'Ministry of Labour India 2025'],
    ['Brasil', 284, 1621, 'BRL', 'Decreto Federal jan/2026'],
    ['China', 371, 2690, 'CNY', 'Ministry of HR China 2024'],
    ['México', 483, 8457, 'MXN', 'STPS México 2025'],
    ['Chile', 540, 500000, 'CLP', 'Ministerio del Trabajo Chile 2025'],
    ['Portugal', 960, 1020, 'EUR', 'Min. do Trabalho Portugal 2025'],
    ['Estados Unidos', 1255, 1255, 'USD', 'U.S. Dept of Labor 2025'],
    ['França', 1744, 1901, 'EUR', 'Ministère du Travail 2025'],
    ['Alemanha', 1882, 2051, 'EUR', 'Bundesmin. für Arbeit 2025'],
    ['Reino Unido', 2473, 1954, 'GBP', 'Low Pay Commission 2025'],
    ['Austrália', 2503, 3856, 'AUD', 'Fair Work Commission 2025'],
])

wcsv('historico_fortuna_musk.csv', [
    ['ano', 'fortuna_bilhoes_usd', 'evento', 'fonte'],
    [2012, 2.0, 'SpaceX e Tesla em crescimento', 'Forbes'],
    [2013, 4.0, 'Tesla IPO valoriza empresa', 'Forbes'],
    [2014, 9.0, 'Expansão global da Tesla', 'Forbes'],
    [2015, 13.0, 'Model X anunciado', 'Forbes'],
    [2016, 11.0, 'Aquisição SolarCity', 'Forbes'],
    [2017, 14.0, 'Model 3 lançado', 'Forbes'],
    [2018, 23.0, 'Tesla rentável pela 1ª vez', 'Forbes'],
    [2019, 20.0, 'Starlink primeiros lançamentos', 'Forbes/Bloomberg'],
    [2020, 165.0, 'Tesla entra no S&P 500 - boom ações', 'Bloomberg'],
    [2021, 244.0, 'Pico histórico: US$ 300bi em nov/2021', 'Bloomberg'],
    [2022, 137.0, 'Queda pós-aquisição do Twitter por US$ 44bi', 'Bloomberg'],
    [2023, 232.0, 'Recuperação: Tesla + SpaceX + xAI', 'Forbes/Bloomberg'],
    [2024, 432.0, 'xAI avaliada em US$ 250bi; Starlink cresce', 'Bloomberg'],
    [2025, 647.0, 'Maior ganho anual da história: +US$ 215bi', 'Bloomberg'],
    [2026, 1000.0, 'Primeiro trilionário da história (jun/2026)', 'Forbes'],
])

wcsv('historico_pop_rua_brasil.csv', [
    ['ano', 'populacao_rua', 'fonte'],
    [2012, 94163, 'IPEA - Nota Técnica 12'],
    [2015, 101854, 'SNAS/MDS'],
    [2019, 168838, 'SNAS/MDS'],
    [2020, 190052, 'Estimativa IPEA'],
    [2021, 234000, 'Estimativa OBPopRua'],
    [2022, 281472, 'IPEA 2023'],
    [2023, 300000, 'Estimativa OBPopRua/UFMG'],
    [2024, 327000, 'OBPopRua/UFMG'],
    [2025, 365822, 'OBPopRua/UFMG (dez/2025)'],
])

wcsv('profissoes_brasil.csv', [
    ['profissao', 'salario_medio_brl', 'descricao'],
    ['Trabalhador Rural', 1621, 'Salário mínimo 2026'],
    ['Auxiliar de Limpeza', 1800, 'Média nacional'],
    ['Agente Comunitário de Saúde', 2700, 'Piso da categoria 2025'],
    ['Professor (Ensino Fundamental)', 3200, 'Piso nacional do magistério 2025'],
    ['Técnico de Enfermagem', 2800, 'Piso da categoria CFE'],
    ['Enfermeiro(a)', 4750, 'Piso Lei 14.434/2022'],
    ['Bombeiro/Policial Militar', 5500, 'Média nacional'],
    ['Professor Universitário', 8500, 'Média IPES federais'],
    ['Médico SUS', 12000, 'Médico generalista SUS'],
    ['Engenheiro', 9500, 'Média de mercado 2025'],
])

wcsv('dados_brasil.csv', [
    ['indicador', 'valor', 'unidade', 'ano', 'fonte'],
    ['Salário mínimo (BRL)', 1621, 'BRL/mês', 2026, 'Decreto Federal'],
    ['Salário mínimo (USD)', 284, 'USD/mês', 2026, 'Decreto + câmbio 5,71'],
    ['PIB Brasil', 2132, 'bilhões USD', 2024, 'FMI'],
    ['PIB Mundial', 105000, 'bilhões USD', 2024, 'FMI'],
    ['Riqueza Mundial Total', 471000, 'bilhões USD', 2024, 'UBS Global Wealth Report 2025'],
    ['Orçamento Federal Brasil (sem dívida)', 4100, 'bilhões BRL', 2025, 'Senado/LOA 2025'],
    ['Bolsa Família - orçamento anual', 160, 'bilhões BRL', 2025, 'MDS/CNN Brasil'],
    ['Bolsa Família - famílias', 19800000, 'famílias', 2025, 'Gov.br'],
    ['Bolsa Família - benefício médio', 680, 'BRL/mês', 2025, 'MDS'],
    ['Déficit habitacional', 5773983, 'moradias', 2024, 'Fundação João Pinheiro'],
    ['Custo casa popular MCMV', 200000, 'BRL', 2024, 'CEF/MCidades'],
    ['Pop. situação de rua', 365822, 'pessoas', 2025, 'OBPopRua/UFMG'],
    ['Cesta básica média nacional', 750, 'BRL/mês', 2025, 'DIEESE'],
    ['Cesta básica São Paulo', 845, 'BRL/mês', 2025, 'DIEESE dez/2025'],
    ['Custo escola municipal', 3000000, 'BRL', 2024, 'FNDE/MEC estimativa'],
    ['Custo hospital grande', 500000000, 'BRL', 2024, 'MS - contratos 2024-25'],
    ['População Brasil', 214000000, 'pessoas', 2024, 'IBGE'],
    ['Fortuna Elon Musk', 1000000, 'milhões USD', 2026, 'Forbes jun/2026'],
    ['Taxa câmbio USD/BRL', 5.71, 'BRL por USD', 2026, 'média aproximada'],
])

print("\n📓 Criando notebooks Jupyter...\n")

# ─────────────────────────────────────────────
# SETUP PADRÃO (importado em todos os notebooks)
# ─────────────────────────────────────────────

SETUP = '''\
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

plt.rcParams.update({
    'figure.facecolor': 'white',
    'axes.facecolor': '#f8f9fa',
    'axes.grid': True,
    'grid.alpha': 0.3,
    'grid.linestyle': '--',
    'font.family': 'DejaVu Sans',
    'axes.spines.top': False,
    'axes.spines.right': False,
})

MUSK_USD   = 1_000_000_000_000   # US$ 1 trilhão (Forbes, jun/2026)
MUSK_BRL   = MUSK_USD * 5.71    # câmbio aproximado jun/2026
USD_BRL    = 5.71
DATA       = 'data/'
'''


# ─────────────────────────────────────────────────────────────────
# NOTEBOOK 01 – Tempo para acumular US$ 1 trilhão com salário mínimo
# ─────────────────────────────────────────────────────────────────
nb01_code = SETUP + '''\
df = pd.read_csv(DATA + 'salarios_minimos_paises.csv')
df['anos']  = MUSK_USD / (df['salario_mensal_usd'] * 12)
df['seculos'] = df['anos'] / 100
df = df.sort_values('anos', ascending=True)

cores = ['#c0392b' if p == 'Brasil' else '#e74c3c' for p in df['pais']]

fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.barh(df['pais'], df['anos'], color=cores, edgecolor='white', linewidth=0.8, height=0.6)

ax.set_xscale('log')
ax.set_xlabel('Anos necessários (escala logarítmica)', fontsize=12)
ax.set_title('Quanto tempo um trabalhador no salário mínimo levaria\\npara acumular US$ 1 trilhão sem gastar nada?',
             fontsize=14, fontweight='bold', pad=20)

ax.axvline(x=4.543e9, color='navy', linestyle='--', alpha=0.6, linewidth=2,
           label='Idade do universo (~4,5 bilhões de anos)')
ax.legend(fontsize=10)

for bar, (_, row) in zip(bars, df.iterrows()):
    anos = row['anos']
    if anos >= 1e9:
        label = f'{anos/1e9:.2f} bilhões de anos'
    elif anos >= 1e6:
        label = f'{anos/1e6:.1f} milhões de anos'
    else:
        label = f'{anos:,.0f} anos'
    ax.text(anos * 1.05, bar.get_y() + bar.get_height()/2, label,
            va='center', fontsize=9, color='#2c3e50')

ax.text(0.98, 0.02, 'Fonte: Decretos salariais de cada país (2025-2026) | Forbes (jun/2026)',
        transform=ax.transAxes, fontsize=8, ha='right', color='gray')

plt.tight_layout()
plt.savefig(DATA + 'output_01_tempo_salario.png', dpi=150, bbox_inches='tight')
plt.show()
print("Figura salva: data/output_01_tempo_salario.png")
'''

nb01_analise = '''\
br = df[df['pais'] == 'Brasil']['anos'].values[0]
us = df[df['pais'] == 'Estados Unidos']['anos'].values[0]
au = df[df['pais'] == 'Austrália']['anos'].values[0]

print("=" * 65)
print("ANÁLISE: TEMPO PARA ACUMULAR US$ 1 TRILHÃO COM SALÁRIO MÍNIMO")
print("=" * 65)
for _, row in df.sort_values('anos', ascending=False).iterrows():
    a = row['anos']
    print(f"  {row['pais']:20s} (US$ {row['salario_mensal_usd']:>5,.0f}/mês): {a:>18,.0f} anos")

print(f"\\nO trabalhador brasileiro precisa de {br:,.0f} anos.")
print(f"Isso é {br/4.543e9:.1f}x a idade do universo ({4.543e9:.2e} anos).")
print(f"Em relação ao australiano, leva {br/au:.1f}x mais tempo.")
print(f"Em relação ao americano,   leva {br/us:.1f}x mais tempo.")
print("\\nFonte: Decretos salariais nacionais | Forbes Billionaires (jun/2026)")
'''

save_nb(make_notebook([
    cell_md("# Cenário 1: Tempo para Acumular US$ 1 Trilhão com Salário Mínimo\n\n"
            "## Contexto\nCom uma fortuna estimada em **US$ 1 trilhão** (Forbes, junho/2026), "
            "Elon Musk se tornou o primeiro trilionário da história. Para colocar esse valor em "
            "perspectiva, calculamos quanto tempo um trabalhador no salário mínimo de diferentes "
            "países levaria para acumular essa quantia, sem gastar absolutamente nada do salário.\n\n"
            "**Premissa:** Toda a renda mensal é poupada, 100%, sem inflação, sem juros, sem gastos.\n\n"
            "**Fontes:**\n"
            "- [Decreto Salário Mínimo Brasil 2026 – Planalto](https://www.gov.br/planalto)\n"
            "- [U.S. Department of Labor – Minimum Wage](https://www.dol.gov/agencies/whd/minimum-wage)\n"
            "- [Fair Work Commission Australia](https://www.fairwork.gov.au)\n"
            "- [Bundesministerium für Arbeit – Alemanha](https://www.bmas.de)\n"
            "- [Forbes Billionaires – Elon Musk](https://www.forbes.com/real-time-billionaires/)"),
    cell_code(nb01_code),
    cell_code(nb01_analise),
]), '01_tempo_salario_minimo.ipynb')


# ─────────────────────────────────────────────────────────────────
# NOTEBOOK 02 – Países com PIB menor que a fortuna de Musk
# ─────────────────────────────────────────────────────────────────
nb02_code = SETUP + '''\
df = pd.read_csv(DATA + 'pib_paises_2024.csv')
musk_bi = 1000  # US$ 1 trilhão = 1000 bilhões

acima = (df['pib_bilhoes_usd'] >= musk_bi).sum()
abaixo = (df['pib_bilhoes_usd'] < musk_bi).sum()
total = len(df)

print(f"Total de países na base: {total}")
print(f"Países com PIB >= US$ 1 tri: {acima}")
print(f"Países com PIB <  US$ 1 tri: {abaixo}")

# Gráfico 1: Top 30 países + linha Musk
top = df.nlargest(30, 'pib_bilhoes_usd').sort_values('pib_bilhoes_usd')
cores_bars = ['#c0392b' if v >= musk_bi else '#3498db' for v in top['pib_bilhoes_usd']]

fig, ax = plt.subplots(figsize=(14, 10))
bars = ax.barh(top['pais'], top['pib_bilhoes_usd'], color=cores_bars, edgecolor='white', height=0.7)
ax.axvline(x=musk_bi, color='#e74c3c', linestyle='--', linewidth=2.5, alpha=0.9,
           label='Fortuna de Elon Musk (US$ 1 trilhão)')
ax.set_xlabel('PIB Nominal (bilhões USD)', fontsize=12)
ax.set_title('PIB dos países vs. Fortuna de Elon Musk\\n'
             '(países em azul têm PIB menor que a fortuna de Musk)', fontsize=13, fontweight='bold')

p_acima = mpatches.Patch(color='#c0392b', label=f'{acima} países com PIB > US$ 1 tri')
p_abaixo = mpatches.Patch(color='#3498db', label=f'Países com PIB < US$ 1 tri (maioria)')
ax.legend(handles=[p_acima, p_abaixo, ax.lines[0]], fontsize=10, loc='lower right')

for bar, val in zip(bars, top['pib_bilhoes_usd']):
    ax.text(val + 200, bar.get_y() + bar.get_height()/2,
            f'US$ {val:,.0f}bi', va='center', fontsize=8)

ax.text(0.98, 0.01, 'Fonte: FMI / Banco Mundial 2024 | Forbes (jun/2026)',
        transform=ax.transAxes, fontsize=8, ha='right', color='gray')
plt.tight_layout()
plt.savefig(DATA + 'output_02_paises_pib.png', dpi=150, bbox_inches='tight')
plt.show()
'''

nb02_analise = '''\
print("=" * 65)
print("ANÁLISE: PAÍSES COM PIB MENOR QUE A FORTUNA DE MUSK")
print("=" * 65)
paises_abaixo = df[df['pib_bilhoes_usd'] < musk_bi].sort_values('pib_bilhoes_usd', ascending=False)
print(f"\\nDe {total} países analisados, {abaixo} têm PIB < US$ 1 trilhão.")
print(f"Isso representa {abaixo/total*100:.1f}% dos países analisados.\\n")
print(f"Os 5 menores PIBs da base:")
for _, r in df.nsmallest(5, 'pib_bilhoes_usd').iterrows():
    pct = r['pib_bilhoes_usd'] / musk_bi * 100
    print(f"  {r['pais']:25s}: US$ {r['pib_bilhoes_usd']:.1f}bi  ({pct:.3f}% da fortuna de Musk)")
print(f"\\nMusk teria riqueza para \\\"comprar\\\" o PIB inteiro de:")
for _, r in df[df['pib_bilhoes_usd'] < musk_bi].sort_values('pib_bilhoes_usd', ascending=False).head(10).iterrows():
    vezes = musk_bi / r['pib_bilhoes_usd']
    print(f"  {r['pais']:25s}: {vezes:.1f}x o PIB")
print("\\nFonte: FMI / Banco Mundial 2024 | Forbes (jun/2026)")
'''

save_nb(make_notebook([
    cell_md("# Cenário 2: Quantos Países Têm PIB Menor que a Fortuna de Musk?\n\n"
            "## Contexto\nO PIB (Produto Interno Bruto) é o total de toda a riqueza produzida "
            "por um país em um ano. A fortuna de Elon Musk é tão grande que supera o PIB anual "
            "de dezenas de nações.\n\n"
            "**Fontes:**\n"
            "- [FMI – World Economic Outlook Database 2024](https://www.imf.org/en/Publications/WEO)\n"
            "- [Banco Mundial – GDP Data](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)\n"
            "- [Forbes Billionaires – Elon Musk](https://www.forbes.com/real-time-billionaires/)"),
    cell_code(nb02_code),
    cell_code(nb02_analise),
]), '02_paises_pib_menor.ipynb')


# ─────────────────────────────────────────────────────────────────
# NOTEBOOK 03 – Percentual da riqueza mundial
# ─────────────────────────────────────────────────────────────────
nb03_code = SETUP + '''\
riqueza_mundial   = 471_000_000_000_000   # US$ 471 trilhões (UBS 2025)
musk              = 1_000_000_000_000     # US$ 1 trilhão
pct_musk          = musk / riqueza_mundial * 100
bottom50_riqueza  = 2_350_000_000_000    # US$ 2,35 trilhões (50% mais pobres)
top1_riqueza      = 209_280_000_000_000  # US$ 209,28 trilhões (1% mais ricos)
adultos_mundo     = 5_600_000_000
pop_abaixo_musk   = adultos_mundo * 0.50  # 50% mais pobres

print(f"Riqueza Mundial Total (2024): US$ {riqueza_mundial/1e12:.0f} trilhões")
print(f"Fortuna Musk:                 US$ {musk/1e12:.0f} trilhão")
print(f"Percentual:                   {pct_musk:.4f}%")
print(f"50% mais pobres (3,8bi adultos): US$ {bottom50_riqueza/1e12:.2f} trilhões")
print(f"Musk vs 50% mais pobres:      {musk/bottom50_riqueza:.2f}x mais rico")

fig, axes = plt.subplots(1, 2, figsize=(15, 7))

# Gráfico 1: Musk vs Mundo
vals1 = [musk/1e12, (riqueza_mundial - musk)/1e12]
labels1 = [f"Elon Musk\\n{pct_musk:.4f}%\\n(US$ 1 trilhão)", f"Resto da\\nHumanidade\\n{100-pct_musk:.4f}%"]
cores1 = ['#e74c3c', '#3498db']
wedges, texts, autotexts = axes[0].pie(vals1, labels=labels1, colors=cores1,
                                        autopct='%1.4f%%', startangle=90,
                                        wedgeprops={'edgecolor': 'white', 'linewidth': 2})
autotexts[0].set_fontsize(10)
autotexts[1].set_fontsize(10)
axes[0].set_title('Fortuna de Musk vs.\\nRiqueza Total da Humanidade', fontsize=12, fontweight='bold')

# Gráfico 2: Pirâmide de riqueza
categorias = ['1% mais ricos\\n(US$ 209,3 tri)', 'Próximos 49%\\n(US$ 259,4 tri)',
              '50% mais pobres\\n(US$ 2,35 tri)', 'Elon Musk\\n(US$ 1 tri)']
valores = [top1_riqueza/1e12, (riqueza_mundial - top1_riqueza - bottom50_riqueza)/1e12,
           bottom50_riqueza/1e12, musk/1e12]
cores2 = ['#c0392b', '#e67e22', '#27ae60', '#8e44ad']
bars = axes[1].barh(categorias, valores, color=cores2, edgecolor='white', height=0.5)
axes[1].set_xlabel('Riqueza (trilhões USD)', fontsize=11)
axes[1].set_title('Distribuição da Riqueza Mundial\\nvs. Fortuna de Musk', fontsize=12, fontweight='bold')
for bar, val in zip(bars, valores):
    axes[1].text(val + 2, bar.get_y() + bar.get_height()/2,
                 f'US$ {val:.1f}tri', va='center', fontsize=9)

axes[1].text(0.98, -0.08, 'Fonte: UBS Global Wealth Report 2025',
             transform=axes[1].transAxes, fontsize=8, ha='right', color='gray')

plt.suptitle('A Fortuna de Elon Musk no Contexto da Riqueza Global', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(DATA + 'output_03_riqueza_mundial.png', dpi=150, bbox_inches='tight')
plt.show()
'''

nb03_analise = '''\
print("=" * 65)
print("ANÁLISE: PERCENTUAL DA RIQUEZA MUNDIAL")
print("=" * 65)
print(f"\\nRiqueza mundial total (2024): US$ 471 trilhões")
print(f"Fortuna de Musk:              US$ 1 trilhão")
print(f"Percentual de Musk:           {pct_musk:.4f}% da riqueza mundial")
print(f"\\nMusk tem {musk/bottom50_riqueza:.2f}x a riqueza dos 3,8 bilhões")
print(f"de adultos que formam os 50% mais pobres do mundo.")
print(f"\\nSe Musk dividisse sua fortuna igualmente entre os")
print(f"50% mais pobres do mundo ({pop_abaixo_musk/1e9:.1f} bilhões de pessoas),")
print(f"cada um receberia US$ {musk/pop_abaixo_musk:.2f}.")
print("\\nFonte: UBS Global Wealth Report 2025 | Forbes (jun/2026)")
'''

save_nb(make_notebook([
    cell_md("# Cenário 3: Qual o Percentual da Riqueza Mundial?\n\n"
            "## Contexto\nEm 2024, a riqueza total da humanidade (patrimônio líquido global) "
            "chegou a **US$ 471 trilhões**, segundo o UBS Global Wealth Report 2025. "
            "Analisamos que parcela dessa riqueza está concentrada nas mãos de uma única pessoa.\n\n"
            "**Fontes:**\n"
            "- [UBS Global Wealth Report 2025](https://www.ubs.com/global/en/wealthmanagement/insights/global-wealth-report.html)\n"
            "- [Forbes Billionaires – Elon Musk](https://www.forbes.com/real-time-billionaires/)\n"
            "- [Oxfam – Desigualdade Global](https://www.oxfam.org)"),
    cell_code(nb03_code),
    cell_code(nb03_analise),
]), '03_percentual_riqueza_mundial.ipynb')


# ─────────────────────────────────────────────────────────────────
# NOTEBOOK 04 – Bolsa Família: quanto tempo poderia ser financiado
# ─────────────────────────────────────────────────────────────────
nb04_code = SETUP + '''\
orcamento_bf_brl = 160_000_000_000  # R$ 160 bilhões/ano
orcamento_bf_usd = orcamento_bf_brl / USD_BRL
familias         = 19_800_000
beneficio_medio  = 680  # BRL/mês

anos_possíveis   = MUSK_USD / orcamento_bf_usd
meses_possiveis  = anos_possíveis * 12
familias_1ano    = MUSK_BRL / (beneficio_medio * 12)
gerações         = anos_possíveis / 25  # gerações de 25 anos

print(f"Orçamento anual Bolsa Família: R$ {orcamento_bf_brl/1e9:.0f} bilhões = US$ {orcamento_bf_usd/1e9:.1f} bilhões")
print(f"Musk em BRL: R$ {MUSK_BRL/1e12:.2f} trilhões")
print(f"Anos que poderia financiar: {anos_possíveis:.1f} anos")
print(f"Gerações beneficiadas:      {gerações:.1f} gerações de 25 anos")

# Gráfico
fig, axes = plt.subplots(1, 2, figsize=(15, 7))

# Gráfico 1: Timeline
anos_ref = np.arange(0, anos_possíveis + 1, 1)
gastado  = anos_ref * orcamento_bf_usd
restante = MUSK_USD - gastado
ax = axes[0]
ax.fill_between(anos_ref, restante / 1e9, alpha=0.6, color='#e74c3c', label='Fortuna restante (bi USD)')
ax.fill_between(anos_ref, gastado / 1e9, alpha=0.6, color='#2ecc71', label='Investido em Bolsa Família (bi USD)')
ax.set_xlabel('Anos financiados', fontsize=11)
ax.set_ylabel('Valor (bilhões USD)', fontsize=11)
ax.set_title(f'Esgotamento da Fortuna de Musk\\nfinancindo o Bolsa Família', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.axvline(x=anos_possíveis, color='navy', linestyle='--', linewidth=2, alpha=0.7, label=f'Esgotamento ({anos_possíveis:.1f} anos)')
ax.legend(fontsize=10)
ax.set_xlim(0, anos_possíveis * 1.05)
ax.set_ylim(0, MUSK_USD / 1e9 * 1.05)

# Gráfico 2: Comparações
labels = [f'Famílias atendidas\\nhoje\\n(19,8 milhões)', f'Poderia atender\\ncom fortuna de Musk\\npor 1 ano\\n({familias_1ano/1e6:.0f} milhões)']
vals = [familias / 1e6, familias_1ano / 1e6]
cores = ['#3498db', '#e74c3c']
bars = axes[1].bar(labels, vals, color=cores, width=0.5, edgecolor='white')
axes[1].set_ylabel('Número de famílias (milhões)', fontsize=11)
axes[1].set_title('Famílias que poderiam ser atendidas\\ncom a fortuna de Musk em 1 ano', fontsize=12, fontweight='bold')
for bar, val in zip(bars, vals):
    axes[1].text(bar.get_x() + bar.get_width()/2, val + 0.5, f'{val:.1f} milhões', ha='center', fontsize=11, fontweight='bold')

axes[1].text(0.98, -0.08, 'Fonte: MDS/Gov.br 2025 | Forbes (jun/2026)',
             transform=axes[1].transAxes, fontsize=8, ha='right', color='gray')

plt.suptitle('Bolsa Família: Por Quanto Tempo a Fortuna de Musk Poderia Financiar o Programa?',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig(DATA + 'output_04_bolsa_familia.png', dpi=150, bbox_inches='tight')
plt.show()
'''

nb04_analise = '''\
print("=" * 65)
print("ANÁLISE: BOLSA FAMÍLIA")
print("=" * 65)
print(f"\\nOrçamento Bolsa Família 2025:  R$ 160 bilhões/ano")
print(f"                               US$ {orcamento_bf_usd/1e9:.2f} bilhões/ano")
print(f"Famílias beneficiadas em 2025: {familias/1e6:.1f} milhões")
print(f"Benefício médio:               R$ {beneficio_medio}/família/mês")
print(f"\\nCom US$ 1 trilhão, seria possível:")
print(f"  → Financiar {anos_possíveis:.1f} anos completos do Bolsa Família")
print(f"  → Atender {familias/1e6:.1f}M de famílias por {anos_possíveis:.0f} anos sem interrupção")
print(f"  → Ou atender {familias_1ano/1e6:.0f} milhões de famílias por 1 ano")
print(f"  → Equivale a {gerações:.0f} gerações beneficiadas (25 anos cada)")
print("\\nFonte: MDS/CNN Brasil 2025 | Forbes Billionaires (jun/2026)")
'''

save_nb(make_notebook([
    cell_md("# Cenário 4: Por Quanto Tempo a Fortuna de Musk Poderia Financiar o Bolsa Família?\n\n"
            "## Contexto\nO Bolsa Família é o maior programa de transferência de renda do Brasil, "
            "atendendo cerca de 19,8 milhões de famílias em situação de pobreza extrema.\n\n"
            "**Fontes:**\n"
            "- [MDS – Bolsa Família 2025](https://www.gov.br/mds)\n"
            "- [CNN Brasil – Orçamento Bolsa Família 2025](https://www.cnnbrasil.com.br)\n"
            "- [Forbes Billionaires – Elon Musk](https://www.forbes.com/real-time-billionaires/)"),
    cell_code(nb04_code),
    cell_code(nb04_analise),
]), '04_bolsa_familia.ipynb')


# ─────────────────────────────────────────────────────────────────
# NOTEBOOK 05 – Déficit Habitacional
# ─────────────────────────────────────────────────────────────────
nb05_code = SETUP + '''\
deficit  = 5_773_983          # moradias (Fundação João Pinheiro 2024)
custo_brl = 200_000           # custo médio MCMV (BRL)
custo_usd = custo_brl / USD_BRL

casas_poss   = int(MUSK_USD / custo_usd)
vezes_deficit = casas_poss / deficit

print(f"Déficit habitacional:    {deficit:,} moradias")
print(f"Custo médio por casa:    R$ {custo_brl:,} = US$ {custo_usd:,.0f}")
print(f"Casas possíveis c/ Musk: {casas_poss:,}")
print(f"Vezes o déficit:         {vezes_deficit:.1f}x")

fig, axes = plt.subplots(1, 2, figsize=(15, 7))

# Gráfico 1: Barras comparativas
cats = ['Déficit\\nHabitacional\\n(5,77 milhões)', f'Casas que Musk\\npoderia construir\\n({casas_poss/1e6:.1f} milhões)']
vals_m = [deficit/1e6, casas_poss/1e6]
cores = ['#e74c3c', '#2ecc71']
bars = axes[0].bar(cats, vals_m, color=cores, width=0.5, edgecolor='white')
for bar, val in zip(bars, vals_m):
    axes[0].text(bar.get_x() + bar.get_width()/2, val + 0.3,
                 f'{val:.2f}M', ha='center', fontsize=13, fontweight='bold')
axes[0].set_ylabel('Número de moradias (milhões)', fontsize=11)
axes[0].set_title('Déficit Habitacional vs.\\nCapacidade de Construção com Fortuna de Musk', fontsize=12, fontweight='bold')

# Gráfico 2: Pizza mostrando o excedente
sobra = casas_poss - deficit
pizza_vals = [deficit, sobra]
pizza_labels = [f'Resolve o déficit\\n({deficit/1e6:.2f}M casas)', f'Sobra para novas moradias\\n({sobra/1e6:.1f}M casas)']
axes[1].pie(pizza_vals, labels=pizza_labels, colors=['#e74c3c', '#2ecc71'],
            autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'white', 'linewidth': 2})
axes[1].set_title(f'Com a fortuna de Musk, o déficit seria resolvido\\ne ainda sobraria para mais {sobra/1e6:.1f}M de casas',
                  fontsize=11, fontweight='bold')

axes[1].text(0.5, -0.05, 'Fonte: Fundação João Pinheiro 2024 | CEF/MCidades | Forbes (jun/2026)',
             transform=axes[1].transAxes, fontsize=8, ha='center', color='gray')

plt.suptitle('Déficit Habitacional do Brasil vs. Fortuna de Elon Musk', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(DATA + 'output_05_deficit_habitacional.png', dpi=150, bbox_inches='tight')
plt.show()
'''

nb05_analise = '''\
print("=" * 65)
print("ANÁLISE: DÉFICIT HABITACIONAL")
print("=" * 65)
print(f"\\nDéficit habitacional Brasil (2024): {deficit:,} moradias")
print(f"Custo médio casa popular (MCMV):    R$ {custo_brl:,}")
print(f"                                    US$ {custo_usd:,.0f}")
print(f"\\nCom a fortuna de US$ 1 trilhão, Musk poderia:")
print(f"  → Construir {casas_poss:,} casas populares")
print(f"  → Resolver {vezes_deficit:.1f}x o déficit habitacional do Brasil")
print(f"  → Eliminar toda a falta de moradia do país e ainda sobrariam")
print(f"    {(casas_poss-deficit)/1e6:.1f} milhões de casas")
print("\\nFonte: Fundação João Pinheiro (2024) | CEF/MCidades | Forbes (jun/2026)")
'''

save_nb(make_notebook([
    cell_md("# Cenário 5: Resolver o Déficit Habitacional Brasileiro\n\n"
            "## Contexto\nO Brasil possui um déficit habitacional de quase 6 milhões de moradias, "
            "afetando principalmente as famílias de baixa renda.\n\n"
            "**Fontes:**\n"
            "- [Fundação João Pinheiro – Déficit Habitacional 2024](https://fjp.mg.gov.br)\n"
            "- [Ministério das Cidades – Minha Casa Minha Vida](https://www.gov.br/cidades)\n"
            "- [Forbes Billionaires – Elon Musk](https://www.forbes.com/real-time-billionaires/)"),
    cell_code(nb05_code),
    cell_code(nb05_analise),
]), '05_deficit_habitacional.ipynb')


# ─────────────────────────────────────────────────────────────────
# NOTEBOOK 06 – Correlação: Fortuna de Musk x População de Rua no Brasil
# ─────────────────────────────────────────────────────────────────
nb06_code = SETUP + '''\
rua  = pd.read_csv(DATA + 'historico_pop_rua_brasil.csv')
musk_h = pd.read_csv(DATA + 'historico_fortuna_musk.csv')

# Pegar último valor por ano para Musk
musk_ano = musk_h.groupby('ano')['fortuna_bilhoes_usd'].last().reset_index()
df = pd.merge(rua, musk_ano, on='ano', how='inner')

correlacao = np.corrcoef(df['fortuna_bilhoes_usd'], df['populacao_rua'])[0, 1]
print(f"Anos em comum: {list(df['ano'])}")
print(f"Correlação de Pearson: {correlacao:.4f}")

fig, axes = plt.subplots(1, 2, figsize=(15, 7))

# Gráfico 1: Série temporal duplo eixo
ax1 = axes[0]
ax2 = ax1.twinx()
l1, = ax1.plot(df['ano'], df['populacao_rua']/1000, 'o-', color='#c0392b', linewidth=2.5,
               markersize=8, label='Pop. em situação de rua (mil pessoas)')
l2, = ax2.plot(df['ano'], df['fortuna_bilhoes_usd'], 's--', color='#2980b9', linewidth=2.5,
               markersize=8, label='Fortuna de Musk (bilhões USD)')
ax1.set_xlabel('Ano', fontsize=11)
ax1.set_ylabel('Pop. em situação de rua (mil pessoas)', color='#c0392b', fontsize=11)
ax2.set_ylabel('Fortuna de Musk (bilhões USD)', color='#2980b9', fontsize=11)
ax1.tick_params(axis='y', labelcolor='#c0392b')
ax2.tick_params(axis='y', labelcolor='#2980b9')
ax1.set_title('Evolução da Fortuna de Musk\\ne da Pop. em Situação de Rua no Brasil', fontsize=12, fontweight='bold')
lines = [l1, l2]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=9)

# Gráfico 2: Scatter com regressão
ax = axes[1]
ax.scatter(df['fortuna_bilhoes_usd'], df['populacao_rua']/1000, color='#e74c3c', s=120, zorder=5)
for _, row in df.iterrows():
    ax.annotate(str(row['ano']), (row['fortuna_bilhoes_usd'], row['populacao_rua']/1000),
                textcoords='offset points', xytext=(5, 5), fontsize=9)

z = np.polyfit(df['fortuna_bilhoes_usd'], df['populacao_rua']/1000, 1)
p = np.poly1d(z)
x_line = np.linspace(df['fortuna_bilhoes_usd'].min(), df['fortuna_bilhoes_usd'].max(), 100)
ax.plot(x_line, p(x_line), '--', color='#2980b9', linewidth=2, alpha=0.7, label=f'Tendência (r={correlacao:.2f})')
ax.set_xlabel('Fortuna de Musk (bilhões USD)', fontsize=11)
ax.set_ylabel('Pop. em situação de rua no Brasil (mil)', fontsize=11)
ax.set_title(f'Correlação entre Riqueza de Musk\\ne Desigualdade Social no Brasil\\n(r = {correlacao:.3f})',
             fontsize=12, fontweight='bold')
ax.legend(fontsize=10)

axes[1].text(0.98, -0.08, 'Fonte: IPEA/OBPopRua | Forbes/Bloomberg',
             transform=axes[1].transAxes, fontsize=8, ha='right', color='gray')

plt.suptitle('Correlação: Crescimento da Fortuna de Musk x Crescimento da População de Rua no Brasil',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig(DATA + 'output_06_correlacao_rua.png', dpi=150, bbox_inches='tight')
plt.show()
'''

nb06_analise = '''\
print("=" * 65)
print("ANÁLISE: CORRELAÇÃO FORTUNA MUSK x POP. RUA BRASIL")
print("=" * 65)
print(f"\\nCoeficiente de correlação de Pearson: {correlacao:.4f}")
if correlacao > 0.9:
    interpretacao = "correlação positiva muito forte"
elif correlacao > 0.7:
    interpretacao = "correlação positiva forte"
else:
    interpretacao = "correlação positiva moderada"
print(f"Interpretação: {interpretacao}")
print(f"\\nAnos analisados: {list(df['ano'])}")
print(f"\\nEvolução da população de rua:")
for _, row in df.iterrows():
    print(f"  {int(row['ano'])}: {int(row['populacao_rua']):>7,} pessoas | Musk: US$ {row['fortuna_bilhoes_usd']:>6,.0f}bi")
crescimento_rua = (df['populacao_rua'].iloc[-1] / df['populacao_rua'].iloc[0] - 1) * 100
crescimento_musk = (df['fortuna_bilhoes_usd'].iloc[-1] / df['fortuna_bilhoes_usd'].iloc[0] - 1) * 100
print(f"\\nCrescimento da pop. de rua:     {crescimento_rua:.0f}%")
print(f"Crescimento da fortuna de Musk: {crescimento_musk:.0f}%")
print("\\n⚠️  ATENÇÃO: Correlação não implica causalidade direta.")
print("   Ambos os fenômenos são reflexos de fatores macroeconômicos")
print("   e estruturais mais amplos, como concentração de capital,")
print("   pandemia de COVID-19, crise econômica e desigualdade sistêmica.")
print("\\nFontes: IPEA (2023) | OBPopRua/UFMG | Forbes | Bloomberg")
'''

save_nb(make_notebook([
    cell_md("# Cenário 6: Correlação entre a Fortuna de Musk e a População de Rua no Brasil\n\n"
            "## Contexto\nEnquanto a fortuna de Elon Musk cresceu de forma exponencial na última "
            "década, a população em situação de rua no Brasil também apresentou crescimento "
            "contínuo. Analisamos a correlação estatística entre esses dois fenômenos.\n\n"
            "> ⚠️ **Nota metodológica:** Correlação estatística não implica relação causal direta. "
            "Ambos os fenômenos são multifatoriais e refletem tendências macroeconômicas globais.\n\n"
            "**Fontes:**\n"
            "- [IPEA – População em Situação de Rua](https://www.ipea.gov.br)\n"
            "- [OBPopRua/UFMG](https://obpoprua.direito.ufmg.br)\n"
            "- [Bloomberg Billionaires Index](https://www.bloomberg.com/billionaires/)\n"
            "- [Forbes Billionaires](https://www.forbes.com/real-time-billionaires/)"),
    cell_code(nb06_code),
    cell_code(nb06_analise),
]), '06_correlacao_rua_musk.ipynb')


# ─────────────────────────────────────────────────────────────────
# NOTEBOOK 07 – Gastando US$ 1 milhão por dia
# ─────────────────────────────────────────────────────────────────
nb07_code = SETUP + '''\
gasto_dia   = 1_000_000           # US$ 1 milhão por dia
total       = MUSK_USD
dias        = total / gasto_dia
anos_gasto  = dias / 365.25
ano_inicio  = 2026 - int(anos_gasto)

# Para referência: comparar com gasto de 1 trabalhador brasileiro
salario_anual_br = 284 * 12   # USD/ano (salário mínimo)
dias_br          = total / (salario_anual_br / 365)

print(f"Gastando US$ 1.000.000/dia:")
print(f"  Dias necessários:  {dias:,.0f} dias")
print(f"  Anos necessários:  {anos_gasto:,.1f} anos")
print(f"  Teria que começar: ano {ano_inicio} d.C.")
print(f"\\nGastando salário mínimo BR inteiro por dia:")
print(f"  Salário anual BR:  US$ {salario_anual_br:,.0f}/ano")
print(f"  Gasto diário:      US$ {salario_anual_br/365:.2f}/dia")

# Marcos históricos
marcos = [
    (645, "Início do Califado Islâmico"),
    (800, "Carlos Magno coroado"),
    (1066, "Batalha de Hastings"),
    (1215, "Magna Carta"),
    (1453, "Fim do Império Byzantino"),
    (1492, "Colombo chega às Américas"),
    (1776, "Independência dos EUA"),
    (1888, "Abolição da escravidão no Brasil"),
    (1945, "Fim da 2ª Guerra Mundial"),
    (2026, "Musk se torna trilionário"),
]

fig, ax = plt.subplots(figsize=(15, 8))

# Linha do tempo
ax.axhline(y=0, color='black', linewidth=1.5, alpha=0.5)
ax.set_xlim(ano_inicio - 50, 2100)
ax.set_ylim(-2, 3)

cores_marcos = plt.cm.viridis(np.linspace(0.1, 0.9, len(marcos)))
for i, (ano, evento) in enumerate(marcos):
    if ano >= ano_inicio:
        dinheiro_gasto = (ano - ano_inicio) * 365.25 * gasto_dia
        pct = min(dinheiro_gasto / total * 100, 100)
        ax.axvline(x=ano, color=cores_marcos[i], linestyle='--', alpha=0.6, linewidth=1.5)
        offset = 1.2 if i % 2 == 0 else -1.4
        ax.text(ano, offset, f"{ano}\\n{evento}\\n{pct:.1f}% gasto", ha='center',
                fontsize=7.5, color=cores_marcos[i],
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.7))

# Barra de progresso de gasto
anos_linha = np.linspace(ano_inicio, 2026, 1000)
pct_gasto  = np.clip((anos_linha - ano_inicio) / anos_gasto * 100, 0, 100)
ax.fill_between(anos_linha, -0.3, -0.3 + pct_gasto / 100 * 0.6,
                color='#e74c3c', alpha=0.5, label='Dinheiro gasto')
ax.fill_between(anos_linha, -0.3, -0.3 + 0.6,
                color='#f0f0f0', alpha=0.3)

ax.scatter([ano_inicio], [0], s=200, color='#e74c3c', zorder=5)
ax.text(ano_inicio, 0.25, f'Início: {ano_inicio}\\n(início do gasto)', ha='center', fontsize=9, color='#c0392b')
ax.scatter([2026], [0], s=200, color='#2ecc71', zorder=5)
ax.text(2026, 0.25, f'2026\\n({(2026-ano_inicio)/anos_gasto*100:.1f}% gasto)', ha='center', fontsize=9, color='#27ae60')

ax.set_xlabel('Ano d.C.', fontsize=12)
ax.set_title(f'Se Musk gastasse US$ 1 milhão por dia, precisaria ter começado em {ano_inicio} d.C.\\n'
             f'= {anos_gasto:,.0f} anos de gastos contínuos',
             fontsize=13, fontweight='bold')
ax.set_yticks([])
ax.text(0.98, 0.02, 'Fonte: Cálculo próprio | Forbes (jun/2026)',
        transform=ax.transAxes, fontsize=8, ha='right', color='gray')

plt.tight_layout()
plt.savefig(DATA + 'output_07_gasto_milhao.png', dpi=150, bbox_inches='tight')
plt.show()
'''

nb07_analise = '''\
print("=" * 65)
print("ANÁLISE: GASTANDO US$ 1 MILHÃO POR DIA")
print("=" * 65)
print(f"\\nGastando US$ 1.000.000 por dia, sem parar:")
print(f"  Total de dias:  {dias:,.0f}")
print(f"  Total de anos:  {anos_gasto:,.1f}")
print(f"  Teria começado: {ano_inicio} d.C.")
print(f"  Isso é antes da fundação do Império Mongol (1206 d.C.)!")
print(f"\\nPara comparação:")
gasto_dia_anual_br = 284 * 12 / 365
print(f"  Salário mínimo diário no Brasil: US$ {284*12/365:.2f}")
print(f"  Para um brasileiro gastar US$ 1tri: {total/(284*12/365)/365.25:,.0f} anos")
print(f"\\nSe Musk quisesse se \\\"livrar\\\" da fortuna gastando")
print(f"como um brasileiro de salário mínimo gasta em um dia,")
print(f"levaria {total/(284*12/365)/365.25/1e6:.2f} milhões de anos.")
print("\\nFonte: Cálculo próprio | Forbes (jun/2026)")
'''

save_nb(make_notebook([
    cell_md("# Cenário 7: Quanto Tempo Gastando US$ 1 Milhão por Dia?\n\n"
            "## Contexto\nUma forma de visualizar a escala de US$ 1 trilhão é calcular "
            "quanto tempo levaria para gastar esse valor à razão de **US$ 1 milhão por dia** — "
            "um gasto que já seria extraordinariamente alto para qualquer padrão.\n\n"
            "**Fontes:**\n"
            "- [Forbes Billionaires – Elon Musk](https://www.forbes.com/real-time-billionaires/)\n"
            "- Cálculo matemático próprio"),
    cell_code(nb07_code),
    cell_code(nb07_analise),
]), '07_gastando_milhao_dia.ipynb')


# ─────────────────────────────────────────────────────────────────
# NOTEBOOK 08 – Orçamento Federal Brasileiro
# ─────────────────────────────────────────────────────────────────
nb08_code = SETUP + '''\
# Orçamento Federal 2025 (LOA), em bilhões BRL
orcamentos = {
    "Previdência Social": 972,
    "Assistência Social\\n(incl. Bolsa Família)": 245,
    "Saúde": 245,
    "Educação": 226,
    "Infraestrutura": 95,
    "Defesa Nacional": 64,
    "Ciência e Tecnologia": 12,
    "Cultura": 4,
}
orcamento_total_brl = 4_100_000_000_000  # R$ 4,1 tri (sem refinanciamento dívida)
orcamento_total_usd = orcamento_total_brl / USD_BRL

meses_possiveis = (MUSK_BRL / orcamento_total_brl) * 12
print(f"Orçamento Federal Total (sem dívida): R$ {orcamento_total_brl/1e12:.1f} tri = US$ {orcamento_total_usd/1e9:.0f}bi")
print(f"Fortuna Musk em BRL: R$ {MUSK_BRL/1e12:.2f} tri")
print(f"Fortuna Musk equivale a {MUSK_BRL/orcamento_total_brl:.2f} orçamentos anuais")
print(f"= {meses_possiveis:.1f} meses do orçamento federal")

fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Gráfico 1: Comparação em barras
cats = ["Fortuna de Musk\\n(R$ 5,71 trilhões)", "Orçamento Federal\\n2025 (R$ 4,10 tri)"]
vals_tri = [MUSK_BRL/1e12, orcamento_total_brl/1e12]
cores = ['#e74c3c', '#3498db']
bars = axes[0].bar(cats, vals_tri, color=cores, width=0.5, edgecolor='white')
for bar, val in zip(bars, vals_tri):
    axes[0].text(bar.get_x() + bar.get_width()/2, val + 0.05,
                 f'R$ {val:.2f} tri', ha='center', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Valor (trilhões BRL)', fontsize=11)
axes[0].set_title('Fortuna de Musk vs.\\nOrçamento Federal do Brasil (2025)', fontsize=12, fontweight='bold')

# Gráfico 2: Quanto tempo financiaria cada área
nomes = list(orcamentos.keys())
vals_bi = list(orcamentos.values())
meses_cada = [MUSK_BRL / 1e9 / v * 12 for v in vals_bi]
cores_bars = plt.cm.RdYlGn(np.linspace(0.2, 0.8, len(nomes)))
hbars = axes[1].barh(nomes, meses_cada, color=cores_bars, edgecolor='white', height=0.6)
axes[1].set_xlabel('Meses que a fortuna de Musk financiaria', fontsize=11)
axes[1].set_title('Quanto tempo a fortuna de Musk\\nfinanciaria cada área do governo?', fontsize=12, fontweight='bold')
for bar, val in zip(hbars, meses_cada):
    anos = val/12
    label = f'{anos:.1f} anos ({val:.0f} meses)'
    axes[1].text(val + 0.5, bar.get_y() + bar.get_height()/2,
                 label, va='center', fontsize=9)

axes[1].text(0.98, -0.08, 'Fonte: Senado/LOA 2025 | Forbes (jun/2026)',
             transform=axes[1].transAxes, fontsize=8, ha='right', color='gray')

plt.suptitle('Fortuna de Musk vs. Orçamento Federal Brasileiro', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(DATA + 'output_08_orcamento.png', dpi=150, bbox_inches='tight')
plt.show()
'''

nb08_analise = '''\
print("=" * 65)
print("ANÁLISE: ORÇAMENTO FEDERAL")
print("=" * 65)
print(f"\\nOrçamento Federal (sem refinanciamento da dívida):")
print(f"  R$ 4,10 trilhões = US$ {orcamento_total_usd/1e9:.0f} bilhões")
print(f"\\nFortuna de Musk:")
print(f"  US$ 1 trilhão = R$ {MUSK_BRL/1e12:.2f} trilhões")
print(f"\\nEquivalência:")
print(f"  Musk tem R$ {MUSK_BRL/orcamento_total_brl:.2f} orçamentos anuais")
print(f"  = {meses_possiveis:.1f} meses de orçamento federal")
print("\\nPor área específica:")
for nome, val_bi in orcamentos.items():
    meses = MUSK_BRL / 1e9 / val_bi * 12
    nome_clean = nome.replace("\\n", " ")
    print(f"  {nome_clean:30s}: {meses:.1f} meses ({meses/12:.1f} anos)")
print("\\nFonte: Senado/LOA 2025 | Forbes (jun/2026)")
'''

save_nb(make_notebook([
    cell_md("# Cenário 8: Comparação com o Orçamento Federal do Brasil\n\n"
            "## Contexto\nO Orçamento Federal do Brasil para 2025 prevê R$ 5,9 trilhões em "
            "despesas totais. Excluindo o refinanciamento da dívida pública, o valor é de "
            "R$ 4,1 trilhões.\n\n"
            "**Fontes:**\n"
            "- [Senado Federal – LOA 2025](https://www12.senado.leg.br)\n"
            "- [Câmara dos Deputados – Orçamento 2025](https://www.camara.leg.br)\n"
            "- [Forbes Billionaires – Elon Musk](https://www.forbes.com/real-time-billionaires/)"),
    cell_code(nb08_code),
    cell_code(nb08_analise),
]), '08_orcamento_federal.ipynb')


# ─────────────────────────────────────────────────────────────────
# NOTEBOOK 09 – Cestas Básicas
# ─────────────────────────────────────────────────────────────────
nb09_code = SETUP + '''\
cesta_sp_brl    = 845.95    # R$ São Paulo, dez/2025 (DIEESE)
cesta_media_brl = 750.0     # média nacional estimada
cesta_media_usd = cesta_media_brl / USD_BRL

# Quantas cestas básicas mensais cabe em R$ 5,71 tri
cestas_total    = MUSK_BRL / cesta_media_brl
# Famílias Bolsa Família (~19,8M) por quanto tempo
familias_bf     = 19_800_000
meses_bf        = MUSK_BRL / (cesta_media_brl * familias_bf)
anos_bf         = meses_bf / 12
# Pop. Brasil toda por quanto tempo
pop_brasil      = 214_000_000
meses_pop       = MUSK_BRL / (cesta_media_brl * pop_brasil)
anos_pop        = meses_pop / 12

print(f"Cesta básica média nacional: R$ {cesta_media_brl:.2f}/mês")
print(f"Cesta básica São Paulo:      R$ {cesta_sp_brl}/mês (mais cara)")
print(f"Fortuna de Musk em BRL:      R$ {MUSK_BRL/1e12:.2f} trilhões")
print(f"\\nCestas básicas possíveis:    {cestas_total:,.0f} cestas mensais")
print(f"Para 19,8M famílias BF:      {meses_bf:.1f} meses = {anos_bf:.1f} anos")
print(f"Para toda a pop. brasileira: {meses_pop:.1f} meses = {anos_pop:.1f} anos")

fig, axes = plt.subplots(1, 2, figsize=(15, 7))

# Gráfico 1: Duração para diferentes grupos
grupos = ['19,8M famílias\\n(Bolsa Família)', '50M famílias\\n(mais pobres)',
          '70M famílias\\n(classe média baixa)', '214M pessoas\\n(todo Brasil)']
n_familias = [19_800_000, 50_000_000, 70_000_000, 214_000_000]
duracoes = [MUSK_BRL / (cesta_media_brl * n) / 12 for n in n_familias]
cores = ['#c0392b', '#e74c3c', '#e67e22', '#3498db']
bars = axes[0].bar(grupos, duracoes, color=cores, edgecolor='white', width=0.6)
axes[0].set_ylabel('Anos de cestas básicas', fontsize=11)
axes[0].set_title('Por quantos anos a fortuna de Musk\\npagaria cestas básicas?', fontsize=12, fontweight='bold')
for bar, val in zip(bars, duracoes):
    axes[0].text(bar.get_x() + bar.get_width()/2, val + 0.3, f'{val:.1f} anos', ha='center', fontsize=10, fontweight='bold')

# Gráfico 2: Escala visual – números enormes
ax = axes[1]
ax.axis('off')
texto = (
    f"Fortuna de Musk em cestas básicas\\n\\n"
    f"R$ 5,71 trilhões ÷ R$ 750/mês =\\n\\n"
    f"{cestas_total/1e9:.2f} BILHÕES\\nde cestas básicas\\n\\n"
    f"Se empilhadas, essa quantidade de sacolas\\n"
    f"de supermercado cobriria o Brasil inteiro\\n"
    f"mais de 1.000 vezes!\\n\\n"
    f"Equivale a alimentar TODA a população\\n"
    f"do Brasil por {anos_pop:.1f} anos"
)
ax.text(0.5, 0.5, texto, transform=ax.transAxes, fontsize=13,
        ha='center', va='center', color='#2c3e50',
        bbox=dict(boxstyle='round,pad=1', facecolor='#fdf6e3', edgecolor='#e74c3c', linewidth=2))
ax.set_title('Escala da Fortuna em Cestas Básicas', fontsize=12, fontweight='bold')

axes[0].text(0.98, -0.1, 'Fonte: DIEESE dez/2025 | Forbes (jun/2026)',
             transform=axes[0].transAxes, fontsize=8, ha='right', color='gray')

plt.suptitle('Quantas Cestas Básicas a Fortuna de Elon Musk Poderia Comprar?', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(DATA + 'output_09_cestas_basicas.png', dpi=150, bbox_inches='tight')
plt.show()
'''

save_nb(make_notebook([
    cell_md("# Cenário 9: Quantas Cestas Básicas?\n\n"
            "## Contexto\nA cesta básica é o conjunto mínimo de alimentos necessários para "
            "a subsistência de uma família. O DIEESE monitora mensalmente seu custo em todas "
            "as capitais brasileiras.\n\n"
            "**Fontes:**\n"
            "- [DIEESE – Análise Cesta Básica dez/2025](https://www.dieese.org.br/analisecestabasica/)\n"
            "- [Forbes Billionaires – Elon Musk](https://www.forbes.com/real-time-billionaires/)"),
    cell_code(nb09_code),
    cell_code('''\
print("=" * 65)
print("ANÁLISE: CESTAS BÁSICAS")
print("=" * 65)
print(f"\\nCesta básica média nacional: R$ {cesta_media_brl:.2f}/mês")
print(f"Cesta básica São Paulo (mais cara): R$ {cesta_sp_brl}/mês")
print(f"\\nFortuna de Musk (R$): R$ {MUSK_BRL/1e12:.2f} trilhões")
print(f"Total de cestas possíveis: {cestas_total/1e9:.2f} bilhões")
print(f"\\nDuração do programa de alimentação:")
print(f"  Para 19,8M famílias (Bolsa Família): {anos_bf:.1f} anos")
print(f"  Para 214M brasileiros:               {anos_pop:.1f} anos")
print("\\nFonte: DIEESE (dez/2025) | Forbes (jun/2026)")
'''),
]), '09_cestas_basicas.ipynb')


# ─────────────────────────────────────────────────────────────────
# NOTEBOOK 10 – Escolas e Hospitais
# ─────────────────────────────────────────────────────────────────
nb10_code = SETUP + '''\
custo_escola_brl     = 3_000_000         # escola municipal padrão (FNDE)
custo_hospital_brl   = 500_000_000       # hospital grande (MS)
custo_upa_brl        = 8_000_000         # UPA 24h
custo_creche_brl     = 1_500_000         # creche municipal

custo_escola_usd   = custo_escola_brl / USD_BRL
custo_hospital_usd = custo_hospital_brl / USD_BRL
custo_upa_usd      = custo_upa_brl / USD_BRL
custo_creche_usd   = custo_creche_brl / USD_BRL

escolas   = int(MUSK_USD / custo_escola_usd)
hospitais = int(MUSK_USD / custo_hospital_usd)
upas      = int(MUSK_USD / custo_upa_usd)
creches   = int(MUSK_USD / custo_creche_usd)

# Referências do Brasil
escolas_brasil   = 181_939   # Censo Escolar 2023 (escolas públicas)
hospitais_brasil = 5_988     # CNS/IBGE 2022 (hospitais SUS)
upas_brasil      = 600       # aprox. UPAs em operação
creches_brasil   = 80_000    # aprox. creches e pré-escolas públicas

print(f"Com a fortuna de US$ 1 trilhão:")
print(f"  Escolas:   {escolas:>12,} (Brasil tem {escolas_brasil:,} escolas públicas)")
print(f"  Hospitais: {hospitais:>12,} (SUS tem {hospitais_brasil:,} hospitais)")
print(f"  UPAs:      {upas:>12,} (Brasil tem ~{upas_brasil} UPAs)")
print(f"  Creches:   {creches:>12,} (Brasil tem ~{creches_brasil:,} creches públicas)")

fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Gráfico 1: O que Musk pode construir vs o que existe
items = ["Escolas\\nMunicipais", "Hospitais\\nGrandes", "UPAs\\n24h", "Creches"]
existem = [escolas_brasil, hospitais_brasil, upas_brasil, creches_brasil]
pode = [escolas, hospitais, upas, creches]

x = np.arange(len(items))
w = 0.35
b1 = axes[0].bar(x - w/2, existem, w, label='Existem no Brasil hoje', color='#3498db', edgecolor='white')
b2 = axes[0].bar(x + w/2, pode, w, label='Poderia construir com fortuna de Musk', color='#e74c3c', edgecolor='white')
axes[0].set_yscale('log')
axes[0].set_xticks(x)
axes[0].set_xticklabels(items, fontsize=10)
axes[0].set_ylabel('Quantidade (escala logarítmica)', fontsize=11)
axes[0].set_title('O Que Existe vs. O Que Musk Poderia Construir', fontsize=12, fontweight='bold')
axes[0].legend(fontsize=10)
for bar in b2:
    v = bar.get_height()
    axes[0].text(bar.get_x() + bar.get_width()/2, v * 1.3,
                 f'{v/1000:.0f}mil' if v >= 1000 else str(v),
                 ha='center', fontsize=9, color='#c0392b', fontweight='bold')

# Gráfico 2: Múltiplos do Brasil
multiplos = [pode[i]/existem[i] for i in range(len(items))]
bars2 = axes[1].bar(items, multiplos, color='#e74c3c', edgecolor='white', width=0.5)
axes[1].set_ylabel('Vezes o que existe hoje', fontsize=11)
axes[1].set_title('Quantas Vezes o Atual Estoque\\nBrasileiro Poderia Ser Construído?', fontsize=12, fontweight='bold')
for bar, val in zip(bars2, multiplos):
    axes[1].text(bar.get_x() + bar.get_width()/2, val + 0.5, f'{val:.0f}x', ha='center', fontsize=13, fontweight='bold')

axes[1].text(0.98, -0.1, 'Fonte: FNDE/MEC | MS | Censo Escolar 2023 | Forbes (jun/2026)',
             transform=axes[1].transAxes, fontsize=8, ha='right', color='gray')

plt.suptitle('Infraestrutura de Saúde e Educação:\\nO Que a Fortuna de Musk Poderia Construir no Brasil?',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig(DATA + 'output_10_escolas_hospitais.png', dpi=150, bbox_inches='tight')
plt.show()
'''

save_nb(make_notebook([
    cell_md("# Cenário 10: Escolas e Hospitais — Infraestrutura Social\n\n"
            "## Contexto\nQuantas unidades de infraestrutura social poderiam ser construídas "
            "com a fortuna de Elon Musk? Comparamos com o estoque atual de equipamentos públicos "
            "no Brasil.\n\n"
            "**Fontes:**\n"
            "- [FNDE/MEC – Custo de Construção de Escolas](https://www.fnde.gov.br)\n"
            "- [Ministério da Saúde – Investimentos Hospitalares 2024-25](https://www.gov.br/saude)\n"
            "- [INEP – Censo Escolar 2023](https://www.gov.br/inep)\n"
            "- [CNS/IBGE – Estabelecimentos de Saúde](https://www.ibge.gov.br)\n"
            "- [Forbes Billionaires – Elon Musk](https://www.forbes.com/real-time-billionaires/)"),
    cell_code(nb10_code),
    cell_code('''\
print("=" * 65)
print("ANÁLISE: ESCOLAS E HOSPITAIS")
print("=" * 65)
print(f"\\nCom US$ 1 trilhão, seria possível construir:")
print(f"  {escolas:>10,} escolas municipais    ({escolas/escolas_brasil:.0f}x o total atual)")
print(f"  {hospitais:>10,} hospitais grandes    ({hospitais/hospitais_brasil:.0f}x o total atual no SUS)")
print(f"  {upas:>10,} UPAs 24h             ({upas/upas_brasil:.0f}x o total atual)")
print(f"  {creches:>10,} creches municipais   ({creches/creches_brasil:.0f}x o total atual)")
print("\\nFonte: FNDE/MEC | Ministério da Saúde | Forbes (jun/2026)")
'''),
]), '10_escolas_hospitais.ipynb')


# ─────────────────────────────────────────────────────────────────
# NOTEBOOK 11 – Comparação com o PIB Brasileiro e Mundial
# ─────────────────────────────────────────────────────────────────
nb11_code = SETUP + '''\
pib_brasil  = 2_132_000_000_000   # USD (FMI 2024)
pib_mundial = 105_000_000_000_000  # USD (FMI 2024)
pct_brasil  = MUSK_USD / pib_brasil  * 100
pct_mundial = MUSK_USD / pib_mundial * 100

pib_top5 = {
    "EUA": 28781, "China": 18532, "Alemanha": 4591,
    "Japão": 4110, "Índia": 3937, "Brasil": 2132,
    "Musk": 1000
}

print(f"Fortuna de Musk:  US$ {MUSK_USD/1e12:.0f} trilhão")
print(f"PIB do Brasil:    US$ {pib_brasil/1e12:.3f} trilhões")
print(f"PIB Mundial:      US$ {pib_mundial/1e12:.0f} trilhões")
print(f"Musk % do Brasil: {pct_brasil:.1f}%")
print(f"Musk % do Mundo:  {pct_mundial:.3f}%")

fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Gráfico 1: Comparação com maiores PIBs
nomes = list(pib_top5.keys())
vals  = list(pib_top5.values())
cores_bars = ['#c0392b' if n == 'Musk' else '#3498db' for n in nomes]
bars = axes[0].bar(nomes, vals, color=cores_bars, edgecolor='white', width=0.6)
axes[0].set_ylabel('Valor (bilhões USD)', fontsize=11)
axes[0].set_title('Fortuna de Musk vs. PIB dos Maiores Países\\n(bilhões USD, 2024)', fontsize=12, fontweight='bold')
for bar, nome, val in zip(bars, nomes, vals):
    color = '#c0392b' if nome == 'Musk' else '#2c3e50'
    axes[0].text(bar.get_x() + bar.get_width()/2, val + 200,
                 f'US$ {val:,.0f}bi', ha='center', fontsize=8, color=color, fontweight='bold' if nome=='Musk' else 'normal')
axes[0].set_xticklabels(nomes, rotation=10)

patch_musk = mpatches.Patch(color='#c0392b', label='Fortuna de Elon Musk')
patch_pib  = mpatches.Patch(color='#3498db', label='PIB do país (2024)')
axes[0].legend(handles=[patch_musk, patch_pib], fontsize=10)

# Gráfico 2: Porcentagem do Brasil
setores_brasil = {
    "Saúde Pública\\n(R$ 245bi)":     245 / USD_BRL,
    "Educação\\n(R$ 226bi)":          226 / USD_BRL,
    "Infraestrutura\\n(R$ 95bi)":      95 / USD_BRL,
    "Ciência e Tec.\\n(R$ 12bi)":      12 / USD_BRL,
}
setores_pct = {k: v / (pib_brasil/1e9) * 100 for k, v in setores_brasil.items()}
musk_pct_areas = {k: MUSK_USD / 1e9 / (pib_brasil/1e9) * 100 for k in setores_brasil}

ax = axes[1]
x_pos = np.arange(len(setores_brasil))
pct_vals = [MUSK_USD / (v * 1e9) for v in setores_brasil.values()]
bars2 = ax.bar([k.split("\\n")[0] for k in setores_brasil.keys()], pct_vals, color='#e74c3c', edgecolor='white', width=0.5)
ax.axhline(y=1, color='navy', linestyle='--', linewidth=1.5, alpha=0.7, label='1x o orçamento da área')
ax.set_ylabel('Múltiplo do orçamento do setor', fontsize=11)
ax.set_title('Quantas vezes o orçamento de cada área\\npública do Brasil a fortuna de Musk representa?',
             fontsize=11, fontweight='bold')
ax.legend(fontsize=9)
for bar, val in zip(bars2, pct_vals):
    ax.text(bar.get_x() + bar.get_width()/2, val + 0.2, f'{val:.0f}x', ha='center', fontsize=11, fontweight='bold')

axes[1].text(0.98, -0.1, 'Fonte: FMI 2024 | Senado/LOA 2025 | Forbes (jun/2026)',
             transform=axes[1].transAxes, fontsize=8, ha='right', color='gray')

plt.suptitle('A Fortuna de Musk no Contexto do PIB Brasileiro e Mundial', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig(DATA + 'output_11_pib_comparacao.png', dpi=150, bbox_inches='tight')
plt.show()
'''

save_nb(make_notebook([
    cell_md("# Cenário 11: Comparação com o PIB Brasileiro e Mundial\n\n"
            "## Contexto\nO PIB (Produto Interno Bruto) representa toda a riqueza produzida "
            "por um país em um ano. A fortuna individual de Musk compete com PIBs nacionais "
            "inteiros.\n\n"
            "**Fontes:**\n"
            "- [FMI – World Economic Outlook 2024](https://www.imf.org/en/Publications/WEO)\n"
            "- [Senado Federal – LOA 2025](https://www12.senado.leg.br)\n"
            "- [Forbes Billionaires – Elon Musk](https://www.forbes.com/real-time-billionaires/)"),
    cell_code(nb11_code),
    cell_code('''\
print("=" * 65)
print("ANÁLISE: COMPARAÇÃO COM PIB BRASILEIRO E MUNDIAL")
print("=" * 65)
print(f"\\nFortuna de Musk:  US$ 1 trilhão")
print(f"PIB do Brasil:    US$ {pib_brasil/1e12:.3f} trilhões")
print(f"PIB Mundial:      US$ {pib_mundial/1e12:.0f} trilhões")
print(f"\\nMusk representa:")
print(f"  {pct_brasil:.1f}% do PIB anual do Brasil")
print(f"  {pct_mundial:.3f}% do PIB Mundial")
print(f"  Musk sozinho produz mais riqueza do que {pct_brasil:.0f}% do Brasil produz em 1 ano")
anos_pib_br = MUSK_USD / pib_brasil
print(f"  Para o Brasil gerar essa riqueza: {anos_pib_br:.1f} anos de PIB inteiro")
print("\\nFonte: FMI (2024) | Forbes (jun/2026)")
'''),
]), '11_comparacao_pib.ipynb')


# ─────────────────────────────────────────────────────────────────
# NOTEBOOK 12 – Renda Vitalícia de Profissões Essenciais
# ─────────────────────────────────────────────────────────────────
nb12_code = SETUP + '''\
prof = pd.read_csv(DATA + "profissoes_brasil.csv")
anos_trabalho = 35  # vida laborativa típica

prof["renda_anual_brl"]    = prof["salario_medio_brl"] * 12
prof["renda_vitalicia_brl"]= prof["renda_anual_brl"] * anos_trabalho
prof["renda_vitalicia_usd"]= prof["renda_vitalicia_brl"] / USD_BRL
prof["n_vidas_para_musk"]  = MUSK_USD / prof["renda_vitalicia_usd"]
prof["pct_fortuna_musk"]   = prof["renda_vitalicia_usd"] / MUSK_USD * 100

print("Renda vitalícia vs. Fortuna de Musk (35 anos de trabalho):")
print(prof[["profissao", "salario_medio_brl", "renda_vitalicia_brl", "n_vidas_para_musk"]].to_string(index=False))

fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Gráfico 1: Número de vidas laborais necessárias
prof_s = prof.sort_values('n_vidas_para_musk', ascending=True)
cores_h = plt.cm.Reds(np.linspace(0.3, 0.9, len(prof_s)))
hbars = axes[0].barh(prof_s["profissao"], prof_s["n_vidas_para_musk"],
                     color=cores_h, edgecolor="white", height=0.6)
axes[0].set_xlabel("Nº de vidas laborais necessárias (35 anos cada)", fontsize=11)
axes[0].set_title("Quantas Vidas de Trabalho Equivalem\\nà Fortuna de Musk?",
                  fontsize=12, fontweight="bold")
axes[0].set_xscale("log")
for bar, val in zip(hbars, prof_s["n_vidas_para_musk"]):
    if val >= 1e6:
        label = f"{val/1e6:.1f}M vidas"
    else:
        label = f"{val/1e3:.0f}mil vidas"
    axes[0].text(val * 1.05, bar.get_y() + bar.get_height()/2,
                 label, va="center", fontsize=9)

# Gráfico 2: Renda vitalícia em BRL
prof_s2 = prof.sort_values("renda_vitalicia_brl")
cores_h2 = plt.cm.Blues(np.linspace(0.3, 0.9, len(prof_s2)))
hbars2 = axes[1].barh(prof_s2["profissao"], prof_s2["renda_vitalicia_brl"]/1e6,
                      color=cores_h2, edgecolor="white", height=0.6)
musk_brl_bi = MUSK_BRL / 1e6
axes[1].axvline(x=musk_brl_bi, color="#e74c3c", linestyle="--", linewidth=2,
                label=f"Fortuna de Musk (R$ {MUSK_BRL/1e12:.2f} tri)")
axes[1].set_xlabel("Renda vitalícia (milhões BRL)", fontsize=11)
axes[1].set_title("Renda Vitalícia (35 anos) por Profissão\\nvs. Fortuna de Musk", fontsize=12, fontweight="bold")
axes[1].set_xscale("log")
axes[1].legend(fontsize=10)
for bar, val_m in zip(hbars2, prof_s2["renda_vitalicia_brl"]/1e6):
    axes[1].text(val_m * 1.05, bar.get_y() + bar.get_height()/2,
                 f"R$ {val_m:.1f}M", va="center", fontsize=9)

axes[1].text(0.98, -0.08, "Fonte: Pisos/convenções coletivas 2025 | Forbes (jun/2026)",
             transform=axes[1].transAxes, fontsize=8, ha="right", color="gray")

plt.suptitle("Desigualdade: Renda Vitalícia de Trabalhadores Essenciais vs. Fortuna de Musk",
             fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig(DATA + "output_12_profissoes.png", dpi=150, bbox_inches="tight")
plt.show()
'''

save_nb(make_notebook([
    cell_md("# Cenário 12: Renda Vitalícia de Profissões Essenciais\n\n"
            "## Contexto\nProfissões como enfermagem, magistério e medicina são pilares da "
            "sociedade. Mas quanto um desses profissionais acumularia em uma vida inteira de "
            "trabalho, comparado à fortuna de Musk?\n\n"
            "**Fontes:**\n"
            "- [CFE – Piso de Enfermagem (Lei 14.434/2022)](https://www.gov.br)\n"
            "- [MEC – Piso Nacional do Magistério](https://www.gov.br/mec)\n"
            "- [CFM – Pesquisa de Remuneração Médica](https://www.cfm.org.br)\n"
            "- [Forbes Billionaires – Elon Musk](https://www.forbes.com/real-time-billionaires/)"),
    cell_code(nb12_code),
    cell_code('''\
print("=" * 65)
print("ANÁLISE: RENDA VITALÍCIA DE PROFISSÕES ESSENCIAIS")
print("=" * 65)
print(f"Vida laborativa considerada: {anos_trabalho} anos")
print(f"\\n{'Profissão':35s} {'Salário/mês':>12s} {'Vida inteira':>15s} {'Vidas p/ Musk':>15s}")
print("-" * 80)
for _, row in prof.sort_values("n_vidas_para_musk", ascending=False).iterrows():
    print(f"{row['profissao']:35s} R$ {row['salario_medio_brl']:>8,.0f} "
          f"R$ {row['renda_vitalicia_brl']/1e6:>10.2f}M  {row['n_vidas_para_musk']:>15,.0f}")
print("\\nFonte: Pisos/convenções coletivas 2025 | Forbes (jun/2026)")
'''),
]), '12_profissoes_essenciais.ipynb')


# ─────────────────────────────────────────────────────────────────
# NOTEBOOK 13 – Renda per Capita: o que cada ser humano receberia
# ─────────────────────────────────────────────────────────────────
nb13_code = SETUP + '''\
pop_mundo    = 8_200_000_000
pop_brasil   = 214_000_000
pop_pobres   = 3_500_000_000  # vivem com < US$ 5,50/dia (Banco Mundial)
pop_extrema  = 700_000_000    # pobreza extrema < US$ 2,15/dia

por_pessoa_mundo  = MUSK_USD / pop_mundo
por_pessoa_brasil = MUSK_USD / pop_brasil
por_pessoa_pobres = MUSK_USD / pop_pobres
por_pessoa_ext    = MUSK_USD / pop_extrema

# Contexto: renda diária dos mais pobres
renda_diaria_pobre = 5.50  # USD/dia (linha pobreza Banco Mundial)
dias_subsistencia_musk = por_pessoa_pobres / renda_diaria_pobre

print(f"Se dividisse igualmente entre:")
print(f"  Toda a humanidade ({pop_mundo/1e9:.1f}bi): US$ {por_pessoa_mundo:.2f} por pessoa")
print(f"  Todos os brasileiros ({pop_brasil/1e6:.0f}M): US$ {por_pessoa_brasil:.2f} por pessoa")
print(f"  Pessoas em pobreza ({pop_pobres/1e9:.1f}bi):   US$ {por_pessoa_pobres:.2f} por pessoa")
print(f"  Pobreza extrema ({pop_extrema/1e9:.1f}bi):     US$ {por_pessoa_ext:.2f} por pessoa")

fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Gráfico 1: Valor por pessoa para diferentes grupos
grupos = [
    f"Humanidade\\n({pop_mundo/1e9:.1f} bilhões)",
    f"Brasileiros\\n({pop_brasil/1e6:.0f} milhões)",
    f"Em pobreza\\n({pop_pobres/1e9:.1f} bilhões)",
    f"Pobreza extrema\\n({pop_extrema/1e9:.1f} bilhões)"
]
valores = [por_pessoa_mundo, por_pessoa_brasil, por_pessoa_pobres, por_pessoa_ext]
cores = ['#3498db', '#27ae60', '#e67e22', '#c0392b']
bars = axes[0].bar(grupos, valores, color=cores, edgecolor='white', width=0.6)
axes[0].set_ylabel('Valor recebido por pessoa (USD)', fontsize=11)
axes[0].set_title('Se Musk dividisse sua fortuna\\nigualmente, cada pessoa receberia:', fontsize=12, fontweight='bold')
for bar, val in zip(bars, valores):
    axes[0].text(bar.get_x() + bar.get_width()/2, val + 5,
                 f'US$ {val:,.0f}', ha='center', fontsize=10, fontweight='bold')

# Gráfico 2: Dias de subsistência com o valor recebido
linhas_pobreza = {
    'Pobreza extrema\\n(< US$ 2,15/dia)': 2.15,
    'Pobreza\\n(< US$ 5,50/dia)': 5.50,
    'Salário mín. EUA\\n(US$ 41,83/dia)': 41.83,
    'Salário mín. Brasil\\n(US$ 9,47/dia)': 284/30,
}
anos_subsistencia = [por_pessoa_pobres / lp / 365 for lp in linhas_pobreza.values()]
bars2 = axes[1].bar(linhas_pobreza.keys(), anos_subsistencia,
                    color=['#c0392b', '#e67e22', '#27ae60', '#3498db'], edgecolor='white', width=0.6)
axes[1].set_ylabel('Anos de subsistência possíveis', fontsize=11)
axes[1].set_title('Se cada pessoa em situação de pobreza\\nrecebesse sua parte, por quantos anos viveria?',
                  fontsize=12, fontweight='bold')
for bar, val in zip(bars2, anos_subsistencia):
    axes[1].text(bar.get_x() + bar.get_width()/2, val + 2,
                 f'{val:.1f} anos', ha='center', fontsize=10, fontweight='bold')
axes[1].tick_params(axis='x', labelsize=8)

axes[1].text(0.98, -0.12, 'Fonte: Banco Mundial 2024 | IBGE | Forbes (jun/2026)',
             transform=axes[1].transAxes, fontsize=8, ha='right', color='gray')

plt.suptitle('E Se a Fortuna de Musk Fosse Distribuída Igualmente?', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(DATA + 'output_13_distribuicao.png', dpi=150, bbox_inches='tight')
plt.show()
'''

save_nb(make_notebook([
    cell_md("# Cenário 13: Distribuição Igualitária — O Que Cada Pessoa Receberia?\n\n"
            "## Contexto\nUm exercício hipotético: se a fortuna de Musk fosse dividida "
            "igualmente entre toda a humanidade, os mais pobres do mundo ou todos os brasileiros, "
            "quanto cada um receberia — e por quanto tempo isso sustentaria sua subsistência?\n\n"
            "**Fontes:**\n"
            "- [Banco Mundial – Linhas de Pobreza](https://www.worldbank.org/en/topic/poverty)\n"
            "- [IBGE – Projeção Populacional](https://www.ibge.gov.br)\n"
            "- [Forbes Billionaires – Elon Musk](https://www.forbes.com/real-time-billionaires/)"),
    cell_code(nb13_code),
    cell_code('''\
print("=" * 65)
print("ANÁLISE: DISTRIBUIÇÃO IGUALITÁRIA DA FORTUNA DE MUSK")
print("=" * 65)
print(f"\\nFortuna de Musk: US$ 1 trilhão")
print(f"\\nDivisão igualitária:")
print(f"  Toda a humanidade ({pop_mundo/1e9:.1f}bi pessoas): US$ {por_pessoa_mundo:.2f}/pessoa")
print(f"  Todos os brasileiros ({pop_brasil/1e6:.0f}M):       US$ {por_pessoa_brasil:,.0f}/pessoa")
print(f"  Pessoas em pobreza ({pop_pobres/1e9:.1f}bi):        US$ {por_pessoa_pobres:.2f}/pessoa")
print(f"  Pobreza extrema ({pop_extrema/1e9:.1f}bi):         US$ {por_pessoa_ext:.2f}/pessoa")
print(f"\\nCada pessoa em pobreza extrema receberia o equivalente a")
print(f"{dias_subsistencia_musk:.0f} dias vivendo na linha de pobreza (US$ {renda_diaria_pobre}/dia)")
print(f"= {dias_subsistencia_musk/365:.1f} anos de subsistência mínima")
print("\\nFonte: Banco Mundial | IBGE | Forbes (jun/2026)")
'''),
]), '13_distribuicao_igualitaria.ipynb')


print("\n✅ Todos os notebooks criados com sucesso!")
print(f"\n📂 Estrutura do projeto:")
print(f"   notebooks/")
for nb_file in sorted(NB.glob('*.ipynb')):
    print(f"     {nb_file.name}")
print(f"   notebooks/data/")
for csv_file in sorted(DATA.glob('*.csv')):
    print(f"     data/{csv_file.name}")
