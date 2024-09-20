from medical_data_visualizer import draw_cat_plot, draw_heat_map

# Executar as funções e gerar os gráficos
if __name__ == "__main__":
    # Gerar e salvar o gráfico categórico
    cat_plot_figure = draw_cat_plot()
    cat_plot_figure.savefig('catplot.png')

    # Gerar e salvar o gráfico de calor (heatmap)
    heat_map_figure = draw_heat_map()
    heat_map_figure.savefig('heatmap.png')
