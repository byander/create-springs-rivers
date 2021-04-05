## Description / Descrição

Create points from springs from rivers. Tested only UTM coordinates.

Criar pontos de nascentes a partir dos rios. Teste apenas com coordenadas UTM.

### Observations / Observações

The rivers must be polylines features and segmented.

Os rios devem ser feições de polilinhas e segmentadas.

### Installation .gitignore/ Instalação

To execute this Python script, it's necessary the Geopandas package.  
See the documentation from Geopandas how install the lib.

Para executar este script Python, é necessário o pacote Geopandas.  
Veja a documentação do Geopandas como instalar a biblioteca.

### How use / Como usar

* Show help / Mostrar ajuda: `python main.py -h`

### Parameters / Parâmetros

* -i: Input - Name (with extension) and path of the rivers shapefile.  
  Entrada - Nome (com extensão) e caminho do shapefile dos rios.


* -o: Output - Name (with extension) and shapefile path of springs points  
  Saída - Nome (com extensão) e caminho do shapefile dos pontos das nascentes


Example / Exemplo  
`python main.py -i 'F:\Trabalho\Lactec\Projetos\P231_VantIA\Camadas\Vetores\rivers.shp' -o 'points_spring'`

### Requirements / Requerimentos
* Geopandas: https://geopandas.org/getting_started/install.html