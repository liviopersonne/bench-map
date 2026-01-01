import os
from pykml import parser

class Bench:
    def __init__(self, id: str, latitude: float, longitude: float, backrest: bool, material: str, seats: int, amenity: str, covered: bool, image: str):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.backrest = backrest
        self.material = material
        self.seats = seats
        self.amenity = amenity
        self.covered = covered
        self.image = image

    def __repr__(self):
        if(self.amenity == "bench"):
            return f"Bench<{self.latitude} {self.longitude} {self.backrest} {self.material} {self.seats} {self.covered} {self.image[54:64]}>"

def show_kml_content(kml_filepath):
    kml_file = open(kml_filepath, "rb")
    root = parser.parse(kml_file).getroot()
    kml_file.close()
    for child in root.Document.getchildren():
        print(" -", child.tag)

def parse_kml(kml_filepath):
    kml_file = open(kml_filepath, "rb")
    root = parser.parse(kml_file).getroot()
    kml_file.close()
    doc = root.Document

    for folder in doc.Folder:
        folder_name = folder.name.text
        print("Folder", folder_name)

        for placemark in folder.Placemark[:4]:
            yield parse_bench(placemark)

def tagsearch(data, name):
    KML_NS = "{http://www.opengis.net/kml/2.2}"
    content = data.find(f"{KML_NS}Data[@name='{name}']")
    if content is not None:
        return str(content.value).strip().lower()

def parse_bool(b):
    if b == "yes":
        return True
    if b == "no":
        return False

def parse_bench(placemark):
    data = placemark.ExtendedData

    try:
        id = placemark.name.text
        latitude = float(tagsearch(data, "@lat"))
        longitude = float(tagsearch(data, "@lon"))
        backrest = parse_bool(tagsearch(data, "backrest"))
        material = tagsearch(data, "material")
        seats = int(float(tagsearch(data, "seats")))
        amenity = tagsearch(data, "amenity")
        covered = parse_bool(tagsearch(data, "covered"))
        image = tagsearch(data, "gx_media_links")

        if amenity == "bench":
            return Bench(id,latitude,longitude,backrest,material,seats,amenity,covered,image)
        else:
            print("Invalid data:", id, "amenity: ", amenity)
    except ValueError as e:
        print("Invalid data:", id, e)


if __name__ == '__main__':
    basedir = "dumps"
    kml_filepath = os.path.join(basedir, "full_map.kml")
    parse_kml(kml_filepath)
    