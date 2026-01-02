import os

if __name__ == '__main__':
    basedir = "dumps"
    base_url = "https://liviopersonne.github.io/bench-map/images/"
    kml_filepath = os.path.join(basedir, "full_map.kml")
    out_filepath = os.path.join(basedir, "full_map_good.kml")


    infile = open(kml_filepath, "r")
    outfile = open(out_filepath, "w")

    prefix = "            <value><![CDATA["
    suffix = "]]></value>"

    for line in infile.readlines():
        if line.startswith("            <value><![CDATA[https://mymaps"):

            url = line.split("[")[-1].split("]")[0]
            github_url = base_url + url[57:75] + ".png"
            github_img = f'<img src="{github_url}" width="400"/>'
            newline = prefix + github_img + suffix + "\n"

            # print(line)
            # print(newline)
            outfile.write(newline)
        else:
            outfile.write(line)

    infile.close()
    outfile.close()