import overpass

api = overpass.API()

border = [48.710928, 2.186049, 48.719715, 2.221645]
bbox = f"{','.join(map(str, border))}"

query = f"""
[bbox:{bbox}];
node[amenity=bench];
out geom;
"""

data = api.get(query, verbosity="geom")

print(len(data.features))
