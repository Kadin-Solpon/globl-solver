import json
readFile = open(f"""coordinates_creation\\coordinates_from_google.txt""", mode = "r")

writeFile = open("coordinates_creation\\coords.json", mode = "w")

"""
reads coordinates_from_google.txt
returns a list of lists; each list is a line, and each element is a specifier (eg capital, coordinate country name)
also removes \n escape character
"""

def parse_lines():
    print("parse lines running")
    unCutLines = readFile.readlines()
    cutLines = []
    for line in unCutLines:
        newLine = line.split("\t")
        if newLine[-1][-1] == "\n":
            newLine[-1] = newLine[-1][:-1:]
        cutLines.append(newLine)
        
    print(cutLines)
    return cutLines

parse_lines()


"""
indices:
capital, country, longitude, latitude
"""
def make_key_value_pair(text:list[str]):
    new_dict = {
        capital : list[0],
        country : list[1],
        latitude : list[2],
        latitude : list[3],
        name : list[2] + list[3]
    }

    return new_dict


