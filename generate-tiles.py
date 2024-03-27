import argparse
import math
import os
import requests
from dotenv import load_dotenv

load_dotenv()

SERVER_ADDRESS = os.getenv("SERVER_ADDRESS")
FILE_FORMAT = os.getenv("FILE_FORMAT")

def deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return xtile, ytile

def download_tiles(z_min,z_max, lat_min, lon_min, lat_max, lon_max, output_dir):
    for zoom in range(z_min, z_max + 1):
        xtile_min, ytile_max = deg2num(lat_min, lon_min, zoom)
        xtile_max, ytile_min = deg2num(lat_max, lon_max, zoom)
        for xtile in range(xtile_min, xtile_max + 1):
            for ytile in range(ytile_min, ytile_max + 1):
                url = f"http://{SERVER_ADDRESS}/{zoom}/{xtile}/{ytile}.{FILE_FORMAT}"
                subdir = os.path.join(output_dir, str(zoom), str(xtile))
                os.makedirs(subdir, exist_ok=True)
                filename = f"{subdir}/{ytile}.png"                                
                print(f"Downloading tile {url}")
                response = requests.get(url)
                with open(filename, 'wb') as f:
                    f.write(response.content)

                # os.system(f"wget -q -O {filename} {url}")

def main():
    parser = argparse.ArgumentParser(description='Download map tiles for a region.')
    parser.add_argument('-z', '--zoom_min', type=int, help='Minimum zoom level', required=True)
    parser.add_argument('-Z', '--zoom_max', type=int, help='Maximum zoom level', required=True)
    parser.add_argument('-x', '--lat_min', type=float, help='Minimum latitude', required=True)
    parser.add_argument('-X', '--lat_max', type=float, help='Maximum latitude', required=True)
    parser.add_argument('-y', '--lon_min', type=float, help='Minimum longitude', required=True)
    parser.add_argument('-Y', '--lon_max', type=float, help='Maximum longitude', required=True)
    parser.add_argument('-o', '--output_dir', help='Output directory', required=True)
    args = parser.parse_args()

    download_tiles(args.zoom_min, args.zoom_max, args.lat_min, args.lon_min, args.lat_max, args.lon_max, args.output_dir)

if __name__ == "__main__":
    main()
