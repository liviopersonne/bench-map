import overpass
import json
import os
import csv

api = overpass.API()

border = [48.710928, 2.186049, 48.719715, 2.221645]
bbox = f"{','.join(map(str, border))}"
query = f"""node["amenity"="bench"]({bbox});"""

def get_json(outfile: str):
    assert(outfile.endswith("json"))
    data = api.get(query, verbosity="geom", responseformat="json")["elements"]
    file = open(outfile, "w")
    json.dump(data, file)
    file.close()

def get_csv(outfile:str):
    assert(outfile.endswith("csv"))
    format = 'csv(::id,::lat,::lon,"amenity","backrest","crossing","highway","tactile_paving","colour","material","seats")'
    data = api.get(query, verbosity="geom", responseformat=format)
    file = open(outfile, "w")
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
    file.close()


if __name__ == '__main__':
    basedir = "dumps"
    os.makedirs(basedir, exist_ok=True)

    jsonfile = os.path.join(basedir, "benches.json")
    get_json(jsonfile)

    csvfile = os.path.join(basedir, "benches.csv")
    get_csv(csvfile)
