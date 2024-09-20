import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Função principal que realiza todas as operações
def draw_cat_plot():
    # Importar os dados
    df = pd.read_csv('medical_examination.csv')

    # 1. Criar a coluna 'overweight' calculando o IMC
    df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2).apply(lambda x: 1 if x > 25 else 0)

    # 2. Normalizar os dados de colesterol e gluc
    df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
    df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

    # 3. Criar gráfico categórico
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 4. Agrupar os dados e contar os valores
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 5. Desenhar o gráfico categórico
    cat_plot = sns.catplot(x='variable', y='total', hue='value', col='cardio', kind='bar', data=df_cat)
    fig = cat_plot.fig

    return fig


def draw_heat_map():
    # Importar os dados
    df = pd.read_csv('medical_examination.csv')

    # 6. Limpar os dados
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # 7. Calcular a matriz de correlação
    corr = df_heat.corr()

    # 8. Gerar uma máscara para o triângulo superior
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 9. Configurar o gráfico de calor (heatmap)
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', ax=ax, cmap='coolwarm', vmax=0.3, center=0)

    return fig
