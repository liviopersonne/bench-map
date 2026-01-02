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

        for placemark in folder.Placemark:
            yield parse_bench(placemark)

def tagsearch(data, name):
    KML_NS = "{http://www.opengis.net/kml/2.2}"
    content = data.find(f"{KML_NS}Data[@name='{name}']")
    if content is not None:
        value = str(content.value).strip()
        if name == "image":
            content = replace_img_link(value)
        return value

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
        seats = tagsearch(data, "seats")
        amenity = tagsearch(data, "amenity")
        leisure = tagsearch(data, "leisure")
        covered = parse_bool(tagsearch(data, "covered"))
        image = tagsearch(data, "image")

        if amenity and amenity.lower() == "bench":
            return Bench(id,latitude,longitude,backrest,material,seats,"bench",covered,image)
        if amenity and amenity.lower() == "sports bench":
            return Bench(id,latitude,longitude,backrest,material,seats,"sports_bench",covered,image)
        if leisure and leisure.lower() == "picnic_table":
            return Bench(id,latitude,longitude,backrest,material,seats,"picnic_table",covered,image)
        if amenity and amenity.lower() == "transat":
            return Bench(id,latitude,longitude,backrest,material,seats,"transat",covered,image)
        else:
            return Bench(id,latitude,longitude,backrest,material,seats,None,covered,image)
    except ValueError as e:
        print("Invalid data:", id, e)

def download_image(img, counter):
    shortImg = img[57:75]
    # print("Downloading", img)
    os.rename(f"docs/images/download({counter}).png", f"docs/images/{shortImg}.png")

def replace_img_link(image):
    base_url = "https://liviopersonne.github.io/bench-map/images/"
    if image is not None:
        github_img = base_url + image[57:75] + ".png"
        # print(image)
        return f'<img src="{github_img}" width="400"/>'

if __name__ == '__main__':
    basedir = "dumps"
    kml_filepath = os.path.join(basedir, "full_map.kml")

    imgCounter = 0

    for b in parse_kml(kml_filepath):
        if b is not None:
            # print(b)
            if b.image is not None:
                print(b.image[54:64], imgCounter)
                # download_image(b.image, imgCounter)
                imgCounter += 1
    