import json
import re
import math

coordsFile = open("coordinates_creation\\coords.json", mode = "r")
coords_json = json.load(coordsFile)

namesFile = open("coordinates_creation\\names.json", mode = "r")
names_json = json.load(namesFile)
"""
parameters
    coord: a latitude or longitude
returns
    a negative or positive coordinate
"""
def str_coord_to_int_coord(coord : str) -> float:

    if coord[-1] == "S" or coord[-1] == "W":
        return -float(coord[:-2])

    return float(coord[:-2])

"""
parameters
    coords: a coordinate pair
returns
    latitude and longitude as a string
"""
def int_coord_to_str_coord(coords : tuple[float, float]) -> str:
    newLong= ""
    newLat = ""

    lat = coords[0]
    long = coords[1]


    if long < 0:
       long = abs(long)
       newLong = str(long) + "W"
    else:
        newLong = str(long) + "E"

    if lat < 0:
        lat = abs(lat)
        newLat = str(lat) + "S"
    else:
        newLat = str(lat) + "N"

    return newLat + " " + newLong
    

"""
parameters: 
    origin: coordinates of closest guess
    distance: distance from answer (in kilometers)
returns: 
    a list of all possible coordinates; ex ["34.56N 69.32E", "56.45S, 92.56W]
"""
def haversine(origin: tuple[str, str], distance:float) -> list[tuple]:
    print('running haversine')

    #print(f"""original coordinates: {origin[0]}, {origin[1]}""")
    
    # Convert string coordinates to float
    lat1 = math.radians(float(origin[0]))
    lon1 = math.radians(float(origin[1]))
    
    #print(f"""lat: {lat1}, long: {lon1}""")

    allPossibleCoords : list[tuple] = []

    angulardistance = distance / 111.1 

    for degree in range(0, 360, 1):
        bearing = math.radians(degree)

        lat2int = math.asin( math.sin(lat1) * math.cos(angulardistance) + math.cos(lat1) * math.sin(angulardistance) * math.cos(bearing))
        lon2int = lon1 + math.atan2( math.sin(bearing) * math.sin(angulardistance) * math.cos(lat1), math.cos(angulardistance) - math.sin(lat1) * math.sin(lat2int) )
    
        allPossibleCoords.append((round((math.degrees(lat2int)),2), round(math.degrees(lon2int),2)))

    # Print first few coordinates to verify
    print("First few coordinates:", allPossibleCoords[:5])
    return allPossibleCoords



def get_second_digit(num:str) -> int:
    s = str(num)
    
    if s[1] == ".":
        return int(s[2])
    
    return int(s[1])

def find_possible_countries(coords : list[tuple[str,str]]):# -> list[str]:
    print("running find_possible_countries()")
    allNames = []
    
    for pair in coords:
        lat = str(pair[0])
        long = str(pair[1])
        
        # Get the second digit and create appropriate range
        lat_second = get_second_digit(lat)
        long_second = get_second_digit(long)
        
        # Create ranges that are valid for regex
        lat_range = f"{max(0, lat_second-1)}-{min(9, lat_second+1)}"
        long_range = f"{max(0, long_second-1)}-{min(9, long_second+1)}"
        
        latPattern = rf"{lat[0]}[{lat_range}]\.\d+"
        longPattern = rf"{long[0]}[{long_range}]\.\d+"
        pattern = latPattern + " " + longPattern

        coordsJsonKeysString = " ".join(coords_json.keys())
        countriesForOneCoord = re.findall(pattern, coordsJsonKeysString)

        #print(countriesForOneCoord)

        for coord in countriesForOneCoord:
            country = coords_json.get(coord, {}).get("country", None)
            if country is None:
                continue
            allNames.append(country)

       
    return sorted(set(allNames))



print(
    find_possible_countries(
        haversine(
            origin = (
                float(names_json["italy".capitalize()].get("latitude")),
                float(names_json["italy".capitalize()].get("longitude"))
            ),
            distance = 11157
        )
    )
)

coordsFile.close()