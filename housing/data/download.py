import requests
import os

FILES = [
    "http://files.zillowstatic.com/research/public/Neighborhood/Neighborhood_Zhvi_SingleFamilyResidence.csv",
    "http://wsgw.mass.gov/data/gispub/shape/state/zipcodes_nt.zip"
]

RAW_DIR = os.path.join("data", "raw")
def download(urls, target_dir=RAW_DIR):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for url in urls:
        filename = os.path.join(target_dir, os.path.basename(url))
        r = requests.get(FILES[0])
        with open(filename, 'w') as fp:
            print(r.content, file=fp)


download(FILES)
