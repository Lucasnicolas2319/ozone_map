import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.interpolate import griddata

# Lendo o arquivo, ignorando as linhas de metadados e corrigindo a intensidade
file_path1 = 'EspFontesCruz01_Sgg_Ri_LargurafonteX1_IV1_OK.csv'
file_path2 = 'EspFontesCruz01_Sga_Sgm_simulacao1_OK.csv' 
file_path3 = 'EspFontesCruz01_Sfv_Shv_simulacao15_OK.csv'
file_path4 = 'EspFontesCruz01_Sfp_Shp_simulacao14_OK.csv'
file_path5 = 'EspFontesCruz01_Seg_Sig_simulacao12_OK.csv'
file_path6 = 'EspFontesCruz01_Sbg_Slg_simulacao9_OK.csv'

def plot_ozone_map1 (file_path):
    """
    Função para ler um arquivo CSV, processar os dados e gerar um mapa de concentração de ozônio.
    
    Parâmetros:
    - file_path (str): Caminho para o arquivo CSV.
    
    Retorna:
    - Exibe o gráfico gerado.
    """
    # Lendo o arquivo e processando os dados
    df = pd.read_csv(file_path, comment='%', sep=',', skiprows=8, names=["surf3x", "surf3y", "Color"])
    df['Color'] = df['Color'] * (-1)
    df['Color'] = df['Color'].clip(lower=0)

    # Extraindo os dados
    horizontal = df['surf3x'].values
    vertical = df['surf3y'].values
    intensidade = df['Color'].values

    # Definindo os limites da grade
    x_min, x_max = -750, 750
    y_min, y_max = 0, 4000

    # Criando a grade uniforme
    grid_x, grid_y = np.meshgrid(
        np.linspace(x_min, x_max, 150),
        np.linspace(y_min, y_max, 400)
    )

    # Interpolação
    pontos = np.column_stack((horizontal, vertical))
    grid_z = griddata(pontos, intensidade, (grid_x, grid_y), method='linear')

    # Gerando o gráfico
    plt.figure(figsize=(8, 6))
    plt.imshow(
        grid_z, extent=(x_min, x_max, y_min, y_max), origin='lower',
        cmap='viridis', aspect='auto'
    )
    plt.colorbar(label='Concentração de Ozônio')
    plt.title(file_path)
    plt.xlabel('Medida Horizontal')
    plt.ylabel('Medida Vertical')
    plt.show()

def plot_ozone_map2 (file_path):
    """
    Função para ler um arquivo CSV, processar os dados e gerar um mapa de concentração de ozônio.
    
    Parâmetros:
    - file_path (str): Caminho para o arquivo CSV.
    
    Retorna:
    - Exibe o gráfico gerado.
    """
    # Lendo o arquivo e processando os dados
    df = pd.read_csv(file_path, comment='%', sep=',', skiprows=8, names=["surf3x", "surf3y", "Color"])
    df['Color'] = df['Color'].clip(lower=0)

    # Extraindo os dados
    horizontal = df['surf3x'].values
    vertical = df['surf3y'].values
    intensidade = df['Color'].values

    # Definindo os limites da grade
    x_min, x_max = -750, 750
    y_min, y_max = 0, 4000

    # Criando a grade uniforme
    grid_x, grid_y = np.meshgrid(
        np.linspace(x_min, x_max, 150),
        np.linspace(y_min, y_max, 400)
    )

    # Interpolação
    pontos = np.column_stack((horizontal, vertical))
    grid_z = griddata(pontos, intensidade, (grid_x, grid_y), method='linear')

    # Gerando o gráfico
    plt.figure(figsize=(8, 6))
    plt.imshow(
        grid_z, extent=(x_min, x_max, y_min, y_max), origin='lower',
        cmap='viridis', aspect='auto'
    )
    plt.colorbar(label='Concentração de Ozônio')
    plt.title(file_path)
    plt.xlabel('Medida Horizontal')
    plt.ylabel('Medida Vertical')
    plt.show()

plot_ozone_map1 (file_path1)
plot_ozone_map2 (file_path1)
plot_ozone_map1 (file_path2)
plot_ozone_map2 (file_path2)
plot_ozone_map1 (file_path3)
plot_ozone_map2 (file_path3)
plot_ozone_map1 (file_path4)
plot_ozone_map2 (file_path4)
plot_ozone_map1 (file_path5)
plot_ozone_map2 (file_path5)
plot_ozone_map1 (file_path6)
plot_ozone_map2 (file_path6)







