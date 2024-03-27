# Generate-Tiles

Script que gera as tiles de um mapa a partir de um servidor OSM.

Os parâmetros que devem ser informados para utilizar o script:

```cmd
    '-z', '--zoom_min', type=int, help='Minimum zoom level'

    '-Z', '--zoom_max', type=int, help='Maximum zoom level'

    '-x', '--lat_min', type=float, help='Minimum latitude'

    '-X', '--lat_max', type=float, help='Maximum latitude'

    '-y', '--lon_min', type=float, help='Minimum longitude'

    '-Y', '--lon_max', type=float, help='Maximum longitude'

    '-o', '--output_dir', help='Output directory'
```

O Comando abaixo por exemplo, gera as tiles da cidade de são lepoldo, rio grande do sul, brasil. Do zoom 15 ao 19.

```cmd
time python3 generate_tiles.py -z 15 -Z 19 -x -29.812257 -X -29.671966 -y -51.210029 -Y -51.068000 -o /home/duh/tiles-15-19^Cl/
```

As coordenadas devem ser informadas no padrão [BBOX](https://wiki.openstreetmap.org/wiki/Bounding_box)

## Dependências

`python -m pip install requests`

`python -m pip install python-dotenv`

## Variáveis de ambiente

Deve ser criado um arquivo `.env`, com as mesmas variáveis do `.env.example`.

## Servidor utilizado

O servidor utilizado para gerar as tiles foi o do exemplo do [Switch2OSM](https://switch2osm.org/serving-tiles/).

## Instruções para localizar as coordenadas

Buscar o ID da cidade:
https://www.openstreetmap.org/

Gerar os polígonos da cidade:
https://polygons.openstreetmap.fr

Inserir os polígonos gerados e visualizar no mapa:
https://geojson.io/
http://bboxfinder.com/
