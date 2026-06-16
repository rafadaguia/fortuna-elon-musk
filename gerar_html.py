#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o arquivo resultado.html com todos os cenários, charts e fontes."""

import base64
from pathlib import Path

BASE = Path('/var/home/rafael/Documentos/Projetos/elon')
DATA = BASE / 'notebooks' / 'data'


def img_b64(fname):
    path = DATA / fname
    if path.exists():
        with open(path, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    return ''


IMGS = {i: img_b64(f'output_{i:02d}_{name}.png') for i, name in [
    (1, 'tempo_salario'), (2, 'paises_pib'), (3, 'riqueza_mundial'),
    (4, 'bolsa_familia'), (5, 'deficit_habitacional'), (6, 'correlacao_rua'),
    (7, 'gasto_milhao'), (8, 'orcamento'), (9, 'cestas_basicas'),
    (10, 'escolas_hospitais'), (11, 'pib_comparacao'), (12, 'profissoes'),
    (13, 'distribuicao'),
]}
# Cenário 14 tem dois gráficos — usamos o principal (série + scatter)
IMGS[14]  = img_b64('output_14_correlacao_rua_eua.png')
IMGS['14b'] = img_b64('output_14b_brasil_eua_comparacao.png')


def img_tag(n, alt):
    b64 = IMGS.get(n, '')
    if b64:
        return f'<img src="data:image/png;base64,{b64}" alt="{alt}" class="chart-img" loading="lazy">'
    return f'<div class="no-chart">Gráfico não disponível</div>'


CENARIOS = [
    {
        'num': 1, 'icon': '⏱️',
        'titulo': 'Tempo para Acumular US$ 1 Trilhão com Salário Mínimo',
        'tag': 'Trabalho & Renda',
        'destaque': '293 milhões de anos',
        'destaque_sub': 'é o tempo que um trabalhador brasileiro precisaria para acumular a fortuna de Musk',
        'texto': '''
            <p>Calculamos quanto tempo levaria para um trabalhador com salário mínimo acumular
            <strong>US$ 1 trilhão</strong>, poupando 100% do salário (sem nenhum gasto).</p>
            <ul>
                <li>🇧🇷 <strong>Brasil</strong> (R$ 1.621/mês = US$ 284): <b>293 milhões de anos</b> — 65x a idade do universo</li>
                <li>🇮🇳 <strong>Índia</strong> (US$ 214/mês): <b>389 milhões de anos</b></li>
                <li>🇺🇸 <strong>Estados Unidos</strong> (US$ 1.255/mês): <b>66 milhões de anos</b></li>
                <li>🇦🇺 <strong>Austrália</strong> (US$ 2.503/mês): <b>33 milhões de anos</b></li>
            </ul>
            <p>O universo tem aproximadamente <strong>13,8 bilhões de anos</strong>. Um trabalhador
            brasileiro precisaria de mais de <strong>21x a idade do universo</strong> para acumular
            o que Musk acumulou em sua vida.</p>
        ''',
        'fontes': [
            ('Decreto Federal – Salário Mínimo 2026', 'https://www.gov.br/planalto'),
            ('U.S. Department of Labor – Minimum Wage', 'https://www.dol.gov/agencies/whd/minimum-wage'),
            ('Fair Work Commission Australia', 'https://www.fairwork.gov.au'),
            ('Forbes Billionaires – Elon Musk', 'https://www.forbes.com/real-time-billionaires/'),
        ]
    },
    {
        'num': 2, 'icon': '🌍',
        'titulo': 'Países com PIB Menor que a Fortuna de Musk',
        'tag': 'PIB & Nações',
        'destaque': '~176 países',
        'destaque_sub': 'têm PIB anual menor do que a fortuna individual de Elon Musk',
        'texto': '''
            <p>O PIB (Produto Interno Bruto) representa <em>toda a riqueza produzida por um país em um ano</em>.
            Segundo o FMI, apenas <strong>19 países</strong> têm PIB nominal acima de US$ 1 trilhão.</p>
            <ul>
                <li>De ~195 países, <strong>176 têm PIB anual menor</strong> que a fortuna de Musk</li>
                <li>Isso inclui países como <strong>Argentina</strong> (US$ 621bi), <strong>Noruega</strong> (US$ 547bi),
                    <strong>Nigeria</strong> (US$ 362bi), <strong>Portugal</strong> (US$ 286bi)</li>
                <li>O menor PIB da base de dados é <strong>Libéria</strong> com US$ 4 bilhões —
                    Musk é <b>250x mais rico</b> que o PIB inteiro da Libéria</li>
            </ul>
            <p>A fortuna de uma única pessoa supera a produção econômica anual de nações inteiras com
            decenas de milhões de habitantes.</p>
        ''',
        'fontes': [
            ('FMI – World Economic Outlook Database 2024', 'https://www.imf.org/en/Publications/WEO'),
            ('Banco Mundial – GDP Data', 'https://data.worldbank.org/indicator/NY.GDP.MKTP.CD'),
            ('Forbes Billionaires – Elon Musk', 'https://www.forbes.com/real-time-billionaires/'),
        ]
    },
    {
        'num': 3, 'icon': '💰',
        'titulo': 'Percentual da Riqueza Total da Humanidade',
        'tag': 'Concentração de Riqueza',
        'destaque': '0,21%',
        'destaque_sub': 'da riqueza total da humanidade está nas mãos de uma única pessoa',
        'texto': '''
            <p>O UBS Global Wealth Report 2025 estima que a riqueza total da humanidade ao final de 2024
            era de <strong>US$ 471 trilhões</strong>.</p>
            <ul>
                <li>Musk representa <strong>0,2124%</strong> de toda a riqueza global</li>
                <li>Os <strong>50% mais pobres da humanidade</strong> (3,8 bilhões de pessoas)
                    possuem juntos apenas US$ 2,35 trilhões — Musk tem <b>42,5% dessa quantia sozinho</b></li>
                <li>O <strong>1% mais rico</strong> controla US$ 209 trilhões (44,5% da riqueza mundial)</li>
                <li>Se Musk dividisse sua fortuna entre os 3,8 bilhões de pessoas mais pobres,
                    cada uma receberia <strong>US$ 263</strong></li>
            </ul>
        ''',
        'fontes': [
            ('UBS Global Wealth Report 2025', 'https://www.ubs.com/global/en/wealthmanagement/insights/global-wealth-report.html'),
            ('Forbes Billionaires – Elon Musk', 'https://www.forbes.com/real-time-billionaires/'),
        ]
    },
    {
        'num': 4, 'icon': '🤝',
        'titulo': 'Bolsa Família: Quantos Anos Poderia Financiar?',
        'tag': 'Assistência Social',
        'destaque': '35,7 anos',
        'destaque_sub': 'de Bolsa Família para 19,8 milhões de famílias brasileiras',
        'texto': '''
            <p>O Bolsa Família 2025 tem orçamento de <strong>R$ 160 bilhões/ano</strong> (aprox. US$ 28 bilhões),
            atendendo <strong>19,8 milhões de famílias</strong> com benefício médio de R$ 680/mês.</p>
            <ul>
                <li>Com US$ 1 trilhão, o programa poderia ser financiado por <strong>35,7 anos consecutivos</strong></li>
                <li>Isso representa <b>mais de uma geração inteira</b> (35 anos) sem precisar de recurso público</li>
                <li>Alternativamente, poderia atender <strong>69,6 milhões de famílias</strong> por 1 ano
                    (3,5x mais famílias do que hoje)</li>
                <li>O orçamento anual de Bolsa Família representa apenas <strong>2,8%</strong> da fortuna de Musk</li>
            </ul>
        ''',
        'fontes': [
            ('MDS – Bolsa Família 2025', 'https://www.gov.br/mds'),
            ('CNN Brasil – Orçamento Bolsa Família 2025', 'https://www.cnnbrasil.com.br/economia/macroeconomia/bolsa-familia-tera-orcamento-de-r-158-bilhoes-em-2026/'),
            ('Forbes Billionaires – Elon Musk', 'https://www.forbes.com/real-time-billionaires/'),
        ]
    },
    {
        'num': 5, 'icon': '🏠',
        'titulo': 'Resolver o Déficit Habitacional Brasileiro',
        'tag': 'Moradia',
        'destaque': '28,5 milhões',
        'destaque_sub': 'de casas populares poderiam ser construídas — 4,9x o déficit atual',
        'texto': '''
            <p>O Brasil tem um déficit habitacional de <strong>5,77 milhões de moradias</strong>
            (Fundação João Pinheiro 2024). O custo médio de uma habitação pelo programa
            Minha Casa, Minha Vida é de <strong>R$ 200.000</strong> (US$ 35.026).</p>
            <ul>
                <li>Com a fortuna de Musk, seria possível construir <strong>28,5 milhões de casas</strong></li>
                <li>Isso resolve o déficit habitacional <b>4,9 vezes</b></li>
                <li>Depois de zerar o déficit, <strong>sobraria dinheiro para 22,7 milhões de casas adicionais</strong></li>
                <li>Toda família sem-teto no Brasil poderia ter moradia digna —
                    e o Brasil ainda receberia 4 casas extras para cada 1 que precisava</li>
            </ul>
        ''',
        'fontes': [
            ('Fundação João Pinheiro – Déficit Habitacional 2024', 'https://fjp.mg.gov.br/deficit-habitacional-recua-34-no-brasil-e-soma-5-773-983-domicilios/'),
            ('Ministério das Cidades – Minha Casa Minha Vida', 'https://www.gov.br/cidades'),
            ('Forbes Billionaires – Elon Musk', 'https://www.forbes.com/real-time-billionaires/'),
        ]
    },
    {
        'num': 6, 'icon': '📈',
        'titulo': 'Correlação: Fortuna de Musk × População de Rua no Brasil',
        'tag': 'Correlação & Desigualdade',
        'destaque': 'r ≈ 0,97',
        'destaque_sub': 'correlação positiva muito forte entre crescimento da fortuna de Musk e aumento da população de rua',
        'texto': '''
            <p>Enquanto a fortuna de Musk cresceu de <strong>US$ 2 bilhões (2012)</strong> para
            <strong>US$ 1 trilhão (2026)</strong>, a população em situação de rua no Brasil cresceu de
            <strong>94.163 (2012)</strong> para <strong>365.822 (2025)</strong>.</p>
            <ul>
                <li>Crescimento da fortuna de Musk (2012–2026): <b>+49.900%</b></li>
                <li>Crescimento da população de rua no Brasil (2012–2025): <b>+288%</b></li>
                <li>O coeficiente de Pearson indica correlação positiva muito forte (r ≈ 0,97)</li>
            </ul>
            <p>⚠️ <strong>Nota metodológica:</strong> Correlação não implica causalidade. Ambos os fenômenos
            refletem tendências macroeconômicas globais: concentração de capital financeiro, pandemia de COVID-19,
            desindustrialização e ausência de políticas redistributivas efetivas.</p>
        ''',
        'fontes': [
            ('IPEA – População em Situação de Rua no Brasil', 'https://www.ipea.gov.br/portal/ipea-g20/noticias-g20/13457-populacao-em-situacao-de-rua-supera-281-4-mil-pessoas-no-brasil'),
            ('OBPopRua/UFMG – 365 mil em situação de rua (2025)', 'https://agenciabrasil.ebc.com.br/direitos-humanos/noticia/2026-01/estudo-aponta-mais-365-mil-pessoas-em-situacao-de-rua-no-brasil'),
            ('Bloomberg Billionaires Index', 'https://www.bloomberg.com/billionaires/'),
        ]
    },
    {
        'num': 7, 'icon': '📅',
        'titulo': 'Gastando US$ 1 Milhão por Dia — Quanto Tempo Duraria?',
        'tag': 'Escala do Tempo',
        'destaque': '2.738 anos',
        'destaque_sub': 'gastando US$ 1 milhão por dia, todos os dias, sem parar',
        'texto': '''
            <p>US$ 1.000.000 por dia é um gasto absurdamente alto — mas mesmo assim,
            <strong>US$ 1 trilhão duraria 2.738 anos</strong>.</p>
            <ul>
                <li>Para gastar toda a fortuna a esse ritmo, Musk teria de ter começado no <b>ano 712 d.C.</b>
                    (na época da Dinastia Tang na China e do Califado Omíada)</li>
                <li>São <strong>1.000.000 dias</strong> de gastos contínuos</li>
                <li>Se gastasse o salário mínimo brasileiro inteiro por dia (US$ 9,47),
                    levaria <b>289 milhões de anos</b></li>
                <li>Em 2026, Musk ainda teria <strong>99,97% da fortuna intacta</strong>
                    se tivesse começado a gastar US$ 1M/dia em 1990</li>
            </ul>
        ''',
        'fontes': [
            ('Forbes Billionaires – Elon Musk', 'https://www.forbes.com/real-time-billionaires/'),
            ('Decreto Federal – Salário Mínimo 2026', 'https://www.gov.br/planalto'),
        ]
    },
    {
        'num': 8, 'icon': '🏛️',
        'titulo': 'Comparação com o Orçamento Federal do Brasil',
        'tag': 'Finanças Públicas',
        'destaque': '16,7 meses',
        'destaque_sub': 'de orçamento federal completo do Brasil (sem refinanciamento da dívida)',
        'texto': '''
            <p>O Orçamento Federal do Brasil para 2025 é de <strong>R$ 4,1 trilhões</strong>
            (sem refinanciamento da dívida pública) = US$ 719 bilhões.</p>
            <ul>
                <li>Fortuna de Musk = <b>US$ 1 trilhão = R$ 5,71 trilhões</b></li>
                <li>Equivale a <strong>1,39 orçamentos federais anuais</strong></li>
                <li>Poderia financiar a <strong>Saúde (R$ 245bi)</strong> por 28 anos</li>
                <li>Poderia financiar a <strong>Educação (R$ 226bi)</strong> por 30 anos</li>
                <li>Poderia financiar o <strong>Bolsa Família (R$ 160bi)</strong> por 35,6 anos</li>
                <li>Poderia financiar <strong>Ciência e Tecnologia (R$ 12bi)</strong> por 475 anos</li>
            </ul>
        ''',
        'fontes': [
            ('Senado Federal – LOA 2025', 'https://www12.senado.leg.br/noticias/materias/2025/03/20/congresso-aprova-orcamento-de-2025-para-destinacao-de-5-7-trilhoes'),
            ('Câmara dos Deputados – Orçamento 2025', 'https://www.camara.leg.br/noticias/1142456-congresso-nacional-aprova-proposta-de-orcamento-de-2025/'),
            ('Forbes Billionaires – Elon Musk', 'https://www.forbes.com/real-time-billionaires/'),
        ]
    },
    {
        'num': 9, 'icon': '🛒',
        'titulo': 'Quantas Cestas Básicas?',
        'tag': 'Alimentação',
        'destaque': '7,6 bilhões',
        'destaque_sub': 'de cestas básicas mensais poderiam ser compradas com a fortuna de Musk',
        'texto': '''
            <p>A cesta básica em São Paulo custou <strong>R$ 845,95</strong> em dezembro de 2025
            (DIEESE). A média nacional é estimada em <strong>R$ 750/mês</strong>.</p>
            <ul>
                <li>Total de cestas possíveis: <b>7,61 bilhões</b> de cestas mensais</li>
                <li>Poderia alimentar as <strong>19,8 milhões de famílias do Bolsa Família</strong>
                    por <b>32 anos</b> ininterruptos</li>
                <li>Poderia alimentar <strong>toda a população do Brasil</strong> (214M pessoas) por <b>3 anos</b></li>
                <li>Poderia comprar uma cesta básica para <strong>cada um dos 8,2 bilhões de seres humanos</strong>
                    — e sobrariam recursos para mais 7 meses</li>
            </ul>
        ''',
        'fontes': [
            ('DIEESE – Análise Cesta Básica dez/2025', 'https://www.dieese.org.br/analisecestabasica/2025/202511cestabasica.html'),
            ('Agência Brasil – Cesta básica 2025', 'https://agenciabrasil.ebc.com.br/economia/noticia/2026-01/cesta-basica-fica-mais-cara-em-17-capitais-em-dezembro'),
            ('Forbes Billionaires – Elon Musk', 'https://www.forbes.com/real-time-billionaires/'),
        ]
    },
    {
        'num': 10, 'icon': '🏥',
        'titulo': 'Escolas e Hospitais: Infraestrutura Social',
        'tag': 'Infraestrutura',
        'destaque': '1,9 milhão de escolas',
        'destaque_sub': 'ou 11.415 hospitais de grande porte poderiam ser construídos',
        'texto': '''
            <p>Com base em dados do FNDE/MEC e do Ministério da Saúde sobre custos de construção:</p>
            <ul>
                <li><strong>Escolas municipais</strong> (R$ 3M cada): poderia construir
                    <b>1,9 milhão</b> — <b>10,5x mais</b> que as 181.939 escolas públicas existentes</li>
                <li><strong>Hospitais grandes</strong> (R$ 500M cada): poderia construir
                    <b>11.415</b> — <b>1,9x mais</b> que os 5.988 hospitais do SUS</li>
                <li><strong>UPAs 24h</strong> (R$ 8M cada): poderia construir
                    <b>713.750</b> — <b>1.189x</b> as ~600 UPAs existentes</li>
                <li><strong>Creches municipais</strong> (R$ 1,5M cada): poderia construir
                    <b>3,8 milhões</b> — <b>47x</b> as ~80 mil creches públicas</li>
            </ul>
        ''',
        'fontes': [
            ('FNDE/MEC – Custos de Construção Escolar', 'https://www.fnde.gov.br'),
            ('Ministério da Saúde – Investimentos 2024-25', 'https://www.gov.br/saude/pt-br/assuntos/noticias/2025/novembro/ministerio-da-saude-vai-investir-r-4-5-bilhoes-em-rede-de-hospitais'),
            ('INEP – Censo Escolar 2023', 'https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar'),
            ('Forbes Billionaires – Elon Musk', 'https://www.forbes.com/real-time-billionaires/'),
        ]
    },
    {
        'num': 11, 'icon': '📊',
        'titulo': 'Comparação com o PIB Brasileiro e Mundial',
        'tag': 'PIB & Macroeconômico',
        'destaque': '46,9% do PIB brasileiro',
        'destaque_sub': 'a fortuna de Musk equivale a quase metade de toda a riqueza produzida pelo Brasil em 1 ano',
        'texto': '''
            <p>O Brasil produziu <strong>US$ 2,132 trilhões</strong> em 2024 — um dos maiores PIBs do mundo.
            A fortuna pessoal de Musk representa:</p>
            <ul>
                <li><b>46,9%</b> do PIB anual do Brasil (2024)</li>
                <li><b>0,95%</b> do PIB mundial (US$ 105 trilhões)</li>
                <li>Para o Brasil gerar essa riqueza: <b>5,6 meses de PIB inteiro</b></li>
                <li>Equivale ao PIB somado de países como: Argentina + Chile + Colômbia + Peru
                    + Equador + Bolívia + Paraguai + Uruguai (toda a América do Sul exceto Brasil)</li>
                <li>Multiplica o orçamento de <strong>Ciência e Tecnologia</strong> brasileiro em <b>264x</b></li>
            </ul>
        ''',
        'fontes': [
            ('FMI – World Economic Outlook 2024', 'https://www.imf.org/en/Publications/WEO'),
            ('Banco Mundial – GDP 2024', 'https://data.worldbank.org'),
            ('Senado Federal – LOA 2025', 'https://www12.senado.leg.br'),
            ('Forbes Billionaires – Elon Musk', 'https://www.forbes.com/real-time-billionaires/'),
        ]
    },
    {
        'num': 12, 'icon': '👩‍⚕️',
        'titulo': 'Renda Vitalícia de Profissões Essenciais',
        'tag': 'Trabalho & Desigualdade',
        'destaque': '3,9 milhões de vidas',
        'destaque_sub': 'de trabalho de uma enfermeira seriam necessárias para igualar a fortuna de Musk',
        'texto': '''
            <p>Calculamos a renda vitalícia (35 anos de trabalho) de profissões essenciais no Brasil
            e quantas vidas de trabalho equivalem à fortuna de Musk:</p>
            <ul>
                <li>🌾 <strong>Trabalhador rural</strong> (R$ 1.621/mês): <b>8,4 milhões de vidas</b> de trabalho</li>
                <li>🧹 <strong>Auxiliar de limpeza</strong> (R$ 1.800/mês): <b>7,6 milhões de vidas</b></li>
                <li>📚 <strong>Professor (Ensino Fundamental)</strong> (R$ 3.200/mês): <b>4,3 milhões de vidas</b></li>
                <li>💉 <strong>Enfermeiro(a)</strong> (R$ 4.750/mês): <b>2,9 milhões de vidas</b></li>
                <li>🩺 <strong>Médico SUS</strong> (R$ 12.000/mês): <b>1,14 milhão de vidas</b></li>
            </ul>
            <p>Nem <em>um milhão de médicos trabalhando 35 anos cada um</em> chegariam a acumular o
            que Musk tem hoje.</p>
        ''',
        'fontes': [
            ('CFE – Piso de Enfermagem (Lei 14.434/2022)', 'https://www.gov.br'),
            ('MEC – Piso Nacional do Magistério 2025', 'https://www.gov.br/mec'),
            ('CFM – Pesquisa Médica 2024', 'https://www.cfm.org.br'),
            ('Forbes Billionaires – Elon Musk', 'https://www.forbes.com/real-time-billionaires/'),
        ]
    },
    {
        'num': 13, 'icon': '🌐',
        'titulo': 'E Se Fosse Distribuída Igualmente?',
        'tag': 'Distribuição de Renda',
        'destaque': 'US$ 121,95',
        'destaque_sub': 'é o que cada ser humano receberia se a fortuna de Musk fosse dividida igualmente',
        'texto': '''
            <p>Um exercício hipotético: se a fortuna de US$ 1 trilhão fosse distribuída de forma igualitária:</p>
            <ul>
                <li>🌍 <strong>Para toda a humanidade</strong> (8,2 bilhões): <b>US$ 121,95/pessoa</b></li>
                <li>🇧🇷 <strong>Para todos os brasileiros</strong> (214 milhões): <b>US$ 4.673/pessoa</b></li>
                <li>😟 <strong>Para pessoas em pobreza</strong> (3,5 bilhões, < US$5,50/dia): <b>US$ 286/pessoa</b> = 52 dias de subsistência</li>
                <li>🚨 <strong>Para os em pobreza extrema</strong> (700 milhões, < US$2,15/dia): <b>US$ 1.428/pessoa</b> = 665 dias de sustento mínimo</li>
            </ul>
            <p>Cada pessoa em pobreza extrema poderia receber o equivalente a quase 2 anos de
            alimentação básica com uma única redistribuição desta fortuna.</p>
        ''',
        'fontes': [
            ('Banco Mundial – Pobreza Global 2024', 'https://www.worldbank.org/en/topic/poverty'),
            ('IBGE – Projeção Populacional Brasil 2024', 'https://www.ibge.gov.br'),
            ('ONU – World Population 2024', 'https://www.un.org/development/desa/pd/'),
            ('Forbes Billionaires – Elon Musk', 'https://www.forbes.com/real-time-billionaires/'),
        ]
    },
    {
        'num': 14, 'icon': '🏘️',
        'titulo': 'Correlação: Fortuna de Musk × População de Rua nos EUA',
        'tag': 'Correlação & EUA',
        'destaque': '771.480 sem-teto',
        'destaque_sub': 'recorde histórico nos EUA em 2024 — +36% desde 2019, enquanto a fortuna de Musk cresceu +2.050% no mesmo período',
        'texto': '''
            <p>O HUD (Department of Housing and Urban Development) realiza anualmente o
            <em>Point-in-Time Count</em>, um censo noturno da população em situação de rua nos EUA.
            Os dados revelam uma trajetória em duas fases distintas:</p>
            <ul>
                <li>🟢 <strong>2010–2016 (queda):</strong> políticas de <em>Housing First</em> reduziram
                    o sem-teto de <b>647.258 para 549.928 pessoas</b> (–15%) mesmo com crescimento da riqueza de Musk</li>
                <li>🔴 <strong>2019–2024 (aceleração):</strong> recorde de <b>771.480 pessoas</b> em 2024
                    (+18% em um único ano — o maior salto já registrado pelo HUD)</li>
                <li>📐 <strong>Correlação de Pearson</strong> (Musk × sem-teto EUA): <b>moderada positiva</b> —
                    mais baixa que o Brasil (r ≈ 0,97) porque os EUA reduziram o sem-teto entre 2010 e 2016</li>
                <li>📐 <strong>Correlação de Spearman (ρ)</strong>: mais elevada — os movimentos por <em>ranking</em>
                    são mais consistentes do que a magnitude linear</li>
            </ul>
            <p>⚠️ O <strong>contraste Brasil × EUA</strong> é a principal lição analítica deste cenário:
            políticas de habitação efetivas (<em>Housing First</em>) conseguiram reduzir o sem-teto mesmo
            num contexto de crescente concentração de riqueza. Quando essas políticas foram enfraquecidas,
            os números voltaram a crescer — e o recorde de 2024 coincide com cortes em programas habitacionais.</p>
            <p>O segundo gráfico gerado pelo notebook compara diretamente a correlação Brasil vs. EUA
            e mostra a evolução relativa (índice base 100) das duas séries em cada país.</p>
        ''',
        'fontes': [
            ('HUD – 2024 Annual Homelessness Assessment Report (AHAR)', 'https://www.huduser.gov/portal/publications/2024-ahar-part-1-pit-estimates-of-homelessness.html'),
            ('National Alliance to End Homelessness – HUD 2024', 'https://endhomelessness.org/media/news-releases/hud-releases-2024-annual-homelessness-assessment-report/'),
            ('Bipartisan Policy Center – Homelessness at a Record High (2024)', 'https://bipartisanpolicy.org/article/homelessness-at-a-record-high-key-takeaways-from-the-2024-pit-count/'),
            ('Bloomberg Billionaires Index – Histórico de Riqueza', 'https://www.bloomberg.com/billionaires/'),
            ('Forbes Billionaires – Elon Musk', 'https://www.forbes.com/real-time-billionaires/'),
        ]
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# GERAR HTML
# ─────────────────────────────────────────────────────────────────────────────

def cenario_html(c):
    fontes_html = ''.join(
        f'<a href="{url}" target="_blank" rel="noopener">{nome}</a>'
        for nome, url in c['fontes']
    )
    # Cenário 14 tem dois gráficos
    if c['num'] == 14:
        b64_a = IMGS.get(14, '')
        b64_b = IMGS.get('14b', '')
        img_a = (f'<img src="data:image/png;base64,{b64_a}" alt="{c["titulo"]}" class="chart-img" loading="lazy">'
                 if b64_a else '')
        img_b = (f'<img src="data:image/png;base64,{b64_b}" alt="Comparação Brasil vs EUA" class="chart-img" loading="lazy">'
                 if b64_b else '')
        img = f'{img_a}{img_b}'
    else:
        img = img_tag(c['num'], c['titulo'])
    return f'''
    <section class="cenario" id="cenario-{c["num"]}">
        <div class="cenario-header">
            <div class="cenario-num">{c["num"]:02d}</div>
            <div class="cenario-icon">{c["icon"]}</div>
            <div class="cenario-meta">
                <span class="cenario-tag">{c["tag"]}</span>
                <h2 class="cenario-titulo">{c["titulo"]}</h2>
            </div>
        </div>
        <div class="cenario-destaque">
            <div class="destaque-numero">{c["destaque"]}</div>
            <div class="destaque-sub">{c["destaque_sub"]}</div>
        </div>
        <div class="cenario-body{'  cenario-body-full' if c['num'] == 14 else ''}">
            <div class="cenario-texto">{c["texto"]}</div>
            <div class="cenario-chart{'  cenario-chart-dual' if c['num'] == 14 else ''}">{img}</div>
        </div>
        <div class="cenario-fontes">
            <span class="fontes-label">📚 Fontes:</span>
            {fontes_html}
        </div>
    </section>
    '''


HTML = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>US$ 1 Trilhão: A Fortuna de Elon Musk e a Desigualdade Social</title>
<style>
:root {{
  --vermelho:    #c0392b;
  --vermelho-esc:#922b21;
  --vermelho-cl: #e74c3c;
  --cinza-esc:   #1a1a2e;
  --cinza-med:   #16213e;
  --cinza-cl:    #0f3460;
  --branco:      #f8f9fa;
  --texto:       #2c3e50;
  --destaque-bg: #fff5f5;
  --borda:       #ffd5d5;
  --tag-bg:      #c0392b22;
  --sombra:      0 4px 20px rgba(0,0,0,.08);
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
  background: #f0f2f5;
  color: var(--texto);
  line-height: 1.6;
}}

/* ── HERO ── */
.hero {{
  background: linear-gradient(135deg, var(--cinza-esc) 0%, var(--vermelho-esc) 100%);
  color: #fff;
  text-align: center;
  padding: 80px 20px 60px;
  position: relative;
  overflow: hidden;
}}
.hero::before {{
  content: '';
  position: absolute; inset: 0;
  background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.03'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E") repeat;
}}
.hero-badge {{
  display: inline-block;
  background: rgba(255,255,255,.15);
  border: 1px solid rgba(255,255,255,.3);
  border-radius: 20px;
  padding: 6px 18px;
  font-size: .85rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  margin-bottom: 20px;
}}
.hero h1 {{
  font-size: clamp(2rem, 5vw, 3.5rem);
  font-weight: 800;
  line-height: 1.2;
  margin-bottom: 16px;
}}
.hero-valor {{
  font-size: clamp(3rem, 8vw, 6rem);
  font-weight: 900;
  color: #ff6b6b;
  text-shadow: 0 0 40px rgba(255,107,107,.5);
  display: block;
  margin: 20px 0;
  letter-spacing: -.02em;
}}
.hero p {{
  font-size: 1.15rem;
  opacity: .85;
  max-width: 700px;
  margin: 0 auto 30px;
}}
.hero-stats {{
  display: flex;
  justify-content: center;
  gap: 40px;
  flex-wrap: wrap;
  margin-top: 30px;
}}
.hero-stat {{ text-align: center; }}
.hero-stat-num {{
  font-size: 2rem;
  font-weight: 800;
  color: #ff6b6b;
}}
.hero-stat-label {{
  font-size: .8rem;
  opacity: .7;
  text-transform: uppercase;
  letter-spacing: .05em;
}}

/* ── NAV ── */
nav {{
  background: var(--cinza-med);
  padding: 14px 20px;
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  justify-content: center;
  position: sticky; top: 0; z-index: 100;
  box-shadow: 0 2px 10px rgba(0,0,0,.3);
}}
nav a {{
  color: rgba(255,255,255,.7);
  text-decoration: none;
  font-size: .78rem;
  padding: 4px 10px;
  border-radius: 12px;
  transition: all .2s;
  font-weight: 500;
}}
nav a:hover {{
  background: var(--vermelho);
  color: #fff;
}}

/* ── MAIN ── */
main {{ max-width: 1200px; margin: 40px auto; padding: 0 20px; }}

/* ── CENÁRIO ── */
.cenario {{
  background: #fff;
  border-radius: 16px;
  box-shadow: var(--sombra);
  margin-bottom: 40px;
  overflow: hidden;
  border-left: 5px solid var(--vermelho);
  transition: transform .2s, box-shadow .2s;
}}
.cenario:hover {{
  transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(0,0,0,.12);
}}
.cenario-header {{
  display: flex;
  align-items: center;
  gap: 16px;
  background: linear-gradient(135deg, #fff 60%, var(--destaque-bg));
  padding: 24px 28px;
  border-bottom: 1px solid var(--borda);
}}
.cenario-num {{
  background: var(--vermelho);
  color: #fff;
  font-size: 1.4rem;
  font-weight: 900;
  width: 52px;
  height: 52px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}}
.cenario-icon {{ font-size: 2rem; flex-shrink: 0; }}
.cenario-tag {{
  background: var(--tag-bg);
  color: var(--vermelho-esc);
  font-size: .72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .08em;
  padding: 3px 10px;
  border-radius: 8px;
  display: inline-block;
  margin-bottom: 6px;
}}
.cenario-titulo {{
  font-size: clamp(1.1rem, 2.5vw, 1.4rem);
  font-weight: 700;
  color: var(--cinza-esc);
  line-height: 1.3;
}}

/* ── DESTAQUE ── */
.cenario-destaque {{
  background: linear-gradient(135deg, var(--vermelho) 0%, var(--vermelho-esc) 100%);
  color: #fff;
  padding: 24px 28px;
  text-align: center;
}}
.destaque-numero {{
  font-size: clamp(2rem, 5vw, 3.5rem);
  font-weight: 900;
  letter-spacing: -.02em;
  line-height: 1.1;
  text-shadow: 0 2px 10px rgba(0,0,0,.3);
}}
.destaque-sub {{
  font-size: .95rem;
  opacity: .9;
  margin-top: 8px;
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
}}

/* ── BODY ── */
.cenario-body {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
}}
@media (max-width: 768px) {{
  .cenario-body {{ grid-template-columns: 1fr; }}
}}
.cenario-texto {{
  padding: 28px;
  border-right: 1px solid #f0f0f0;
}}
.cenario-texto p {{ margin-bottom: 14px; color: #444; }}
.cenario-texto ul {{ padding-left: 20px; }}
.cenario-texto li {{ margin-bottom: 8px; color: #444; }}
.cenario-texto strong, .cenario-texto b {{ color: var(--vermelho-esc); }}
.cenario-texto em {{ color: #666; font-style: italic; }}
.cenario-chart {{
  padding: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #fafafa;
}}
.chart-img {{
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  border: 1px solid #e8e8e8;
}}
.no-chart {{
  color: #aaa;
  font-size: .9rem;
  text-align: center;
  padding: 40px;
}}
.cenario-body-full {{
  grid-template-columns: 1fr 2fr;
}}
.cenario-chart-dual {{
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 16px;
}}

/* ── FONTES ── */
.cenario-fontes {{
  padding: 14px 28px;
  background: #fafafa;
  border-top: 1px solid #f0f0f0;
  font-size: .78rem;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  color: #888;
}}
.fontes-label {{ font-weight: 700; color: #666; white-space: nowrap; }}
.cenario-fontes a {{
  color: var(--vermelho);
  text-decoration: none;
  border: 1px solid #ffd5d5;
  border-radius: 6px;
  padding: 2px 8px;
  transition: all .2s;
  white-space: nowrap;
}}
.cenario-fontes a:hover {{
  background: var(--vermelho);
  color: #fff;
  border-color: var(--vermelho);
}}

/* ── FOOTER ── */
footer {{
  background: var(--cinza-esc);
  color: rgba(255,255,255,.6);
  text-align: center;
  padding: 40px 20px;
  margin-top: 60px;
}}
footer h3 {{
  color: #fff;
  font-size: 1.2rem;
  margin-bottom: 20px;
}}
.footer-fontes {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 12px;
  max-width: 1000px;
  margin: 0 auto 30px;
  text-align: left;
}}
.footer-fontes a {{
  color: rgba(255,255,255,.7);
  text-decoration: none;
  font-size: .82rem;
  padding: 8px 12px;
  background: rgba(255,255,255,.05);
  border-radius: 8px;
  display: block;
  transition: background .2s;
}}
.footer-fontes a:hover {{ background: rgba(255,255,255,.12); color: #fff; }}
.footer-note {{
  font-size: .8rem;
  opacity: .5;
  margin-top: 20px;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}}
.metodologia {{
  background: #fff;
  border-radius: 16px;
  box-shadow: var(--sombra);
  padding: 32px;
  margin-bottom: 40px;
  border-left: 5px solid #3498db;
}}
.metodologia h2 {{
  color: var(--cinza-esc);
  margin-bottom: 16px;
  font-size: 1.3rem;
}}
.metodologia p {{ color: #555; margin-bottom: 10px; }}
.metodologia ul {{ padding-left: 20px; color: #555; }}
.metodologia li {{ margin-bottom: 6px; }}
.metodologia code {{
  background: #f0f2f5;
  padding: 2px 6px;
  border-radius: 4px;
  font-family: monospace;
  font-size: .85em;
}}
</style>
</head>
<body>

<div class="hero">
  <div class="hero-badge">Análise de Dados · Desigualdade Social · 2026</div>
  <h1>A Fortuna de US$ 1 Trilhão de Elon Musk</h1>
  <span class="hero-valor">US$ 1.000.000.000.000</span>
  <p>
    Em junho de 2026, Elon Musk se tornou o primeiro trilionário da história segundo a Forbes.
    Este estudo analisa o que esse valor representa em termos de desigualdade social,
    poder de compra e comparações com realidades do Brasil e do mundo.
  </p>
  <div class="hero-stats">
    <div class="hero-stat">
      <div class="hero-stat-num">14</div>
      <div class="hero-stat-label">Cenários analisados</div>
    </div>
    <div class="hero-stat">
      <div class="hero-stat-num">6</div>
      <div class="hero-stat-label">Fontes de dados</div>
    </div>
    <div class="hero-stat">
      <div class="hero-stat-num">R$ 5,71tri</div>
      <div class="hero-stat-label">Em reais (câmbio jun/2026)</div>
    </div>
    <div class="hero-stat">
      <div class="hero-stat-num">~176</div>
      <div class="hero-stat-label">Países com PIB menor</div>
    </div>
  </div>
</div>

<nav>
  <a href="#metodologia">Metodologia</a>
  {"".join(f'<a href="#cenario-{c["num"]}">{c["num"]:02d}. {c["tag"]}</a>' for c in CENARIOS)}
</nav>

<main>

<section class="metodologia" id="metodologia">
  <h2>📋 Metodologia e Dados</h2>
  <p>Este estudo utiliza dados públicos de fontes primárias (organismos governamentais,
  organismos internacionais e institutos de pesquisa reconhecidos). Todas as análises foram
  realizadas em <strong>Jupyter Notebooks Python</strong> disponíveis na pasta <code>notebooks/</code>.</p>
  <ul>
    <li><strong>Fortuna de Musk:</strong> US$ 1 trilhão (Forbes Real-Time Billionaires, junho/2026)</li>
    <li><strong>Câmbio USD/BRL:</strong> R$ 5,71 (taxa de câmbio aproximada em junho/2026)</li>
    <li><strong>Dados socioeconômicos do Brasil:</strong> IBGE, IPEA, DIEESE, Fundação João Pinheiro</li>
    <li><strong>Dados internacionais:</strong> FMI, Banco Mundial, UBS Global Wealth Report 2025</li>
    <li><strong>Dados históricos de riqueza:</strong> Forbes Billionaires, Bloomberg Billionaires Index</li>
    <li><strong>Population de rua:</strong> IPEA, OBPopRua/UFMG</li>
  </ul>
  <p style="margin-top:12px; color:#888; font-size:.9rem;">
    Os notebooks Jupyter com o código-fonte completo estão disponíveis em
    <code>notebooks/</code> e os dados em <code>notebooks/data/</code>.
  </p>
</section>

{''.join(cenario_html(c) for c in CENARIOS)}

</main>

<footer>
  <h3>📚 Todas as Fontes Utilizadas</h3>
  <div class="footer-fontes">
    <a href="https://www.forbes.com/real-time-billionaires/" target="_blank">Forbes Real-Time Billionaires – Fortuna de Musk (jun/2026)</a>
    <a href="https://www.bloomberg.com/billionaires/" target="_blank">Bloomberg Billionaires Index – Histórico de Riqueza</a>
    <a href="https://www.imf.org/en/Publications/WEO" target="_blank">FMI – World Economic Outlook 2024 (PIB dos países)</a>
    <a href="https://data.worldbank.org/indicator/NY.GDP.MKTP.CD" target="_blank">Banco Mundial – GDP Data 2024</a>
    <a href="https://www.ubs.com/global/en/wealthmanagement/insights/global-wealth-report.html" target="_blank">UBS Global Wealth Report 2025 – Riqueza Global</a>
    <a href="https://www.ipea.gov.br/portal/ipea-g20/noticias-g20/13457-populacao-em-situacao-de-rua-supera-281-4-mil-pessoas-no-brasil" target="_blank">IPEA – Pop. em Situação de Rua (2022)</a>
    <a href="https://agenciabrasil.ebc.com.br/direitos-humanos/noticia/2026-01/estudo-aponta-mais-365-mil-pessoas-em-situacao-de-rua-no-brasil" target="_blank">Agência Brasil – 365 mil em situação de rua (2025)</a>
    <a href="https://fjp.mg.gov.br/deficit-habitacional-recua-34-no-brasil-e-soma-5-773-983-domicilios/" target="_blank">Fundação João Pinheiro – Déficit Habitacional 2024</a>
    <a href="https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias/2025/12/publicado-decreto-que-reajusta-salario-minimo-para-r-1-621-a-partir-de-1o-de-janeiro" target="_blank">Planalto – Salário Mínimo R$ 1.621 (jan/2026)</a>
    <a href="https://www12.senado.leg.br/noticias/materias/2025/03/20/congresso-aprova-orcamento-de-2025-para-destinacao-de-5-7-trilhoes" target="_blank">Senado Federal – LOA 2025</a>
    <a href="https://www.gov.br/mds" target="_blank">MDS – Bolsa Família 2025 (19,8M famílias, R$ 160bi)</a>
    <a href="https://www.dieese.org.br/analisecestabasica/2025/202511cestabasica.html" target="_blank">DIEESE – Cesta Básica nov/dez 2025</a>
    <a href="https://www.worldbank.org/en/topic/poverty" target="_blank">Banco Mundial – Linhas de Pobreza Global 2024</a>
    <a href="https://www.gov.br/saude/pt-br/assuntos/noticias/2025/novembro/ministerio-da-saude-vai-investir-r-4-5-bilhoes-em-rede-de-hospitais" target="_blank">Ministério da Saúde – Investimentos Hospitalares 2025</a>
    <a href="https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar" target="_blank">INEP – Censo Escolar 2023</a>
    <a href="https://www.dol.gov/agencies/whd/minimum-wage" target="_blank">U.S. Dept of Labor – Salário Mínimo Federal (EUA)</a>
    <a href="https://www.fairwork.gov.au" target="_blank">Fair Work Commission – Salário Mínimo Austrália 2025</a>
    <a href="https://www.un.org/development/desa/pd/" target="_blank">ONU – Projeção Populacional Mundial 2024</a>
    <a href="https://www.huduser.gov/portal/publications/2024-ahar-part-1-pit-estimates-of-homelessness.html" target="_blank">HUD – 2024 Annual Homelessness Assessment Report (EUA)</a>
    <a href="https://endhomelessness.org/media/news-releases/hud-releases-2024-annual-homelessness-assessment-report/" target="_blank">National Alliance to End Homelessness – HUD 2024</a>
    <a href="https://bipartisanpolicy.org/article/homelessness-at-a-record-high-key-takeaways-from-the-2024-pit-count/" target="_blank">Bipartisan Policy Center – Homelessness at a Record High (2024)</a>
  </div>
  <div class="footer-note">
    Este estudo tem finalidade exclusivamente educativa e informativa. Os dados utilizados provêm
    de fontes públicas e reconhecidas. Correlações identificadas não implicam relações causais diretas.
    Análises geradas em Jupyter Notebooks Python com bibliotecas Pandas, Matplotlib e Seaborn.
    <br><br>
    © 2026 · Análise de Dados · Desigualdade Social · US$ 1 Trilhão em Perspectiva
  </div>
</footer>

</body>
</html>'''

out = BASE / 'resultado.html'
out.write_text(HTML, encoding='utf-8')
size = out.stat().st_size / 1024 / 1024
print(f"\n✅ HTML gerado com sucesso!")
print(f"   Arquivo: {out}")
print(f"   Tamanho: {size:.2f} MB")
print(f"   Cenários: {len(CENARIOS)}")
print(f"   Imagens embeddadas: {sum(1 for v in IMGS.values() if v)}/{len(IMGS)}")
