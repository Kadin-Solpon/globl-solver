# import json


# readFile = open(f"""coordinates_creation\\coordinates_from_google.txt""", mode = "r")

# namesFile = open("coordinates_creation\\names.json", mode = "w")
# coordsFile = open("coordinates_creation\\coords.json", mode = "w")
# """
# reads coordinates_from_google.txt
# returns a list of lists; each list is a line, and each element is a specifier (eg capital, coordinate country name)
# also removes \n escape character
# """
# def directions_to_positives(coord : str) -> str:
#     print(coord)
#     coord = coord.strip()
#     if coord[-1].upper() == "S" or coord[-1].upper() == "W":
#         return str(-float(coord[0:-1]))
#     return str(float(coord[0:-1]))


# def parse_lines() -> list[list[str]]:
#     print("parse lines running")
#     unCutLines = readFile.readlines()
#     cutLines = []
#     for line in unCutLines:
#         newLine = line.split("\t")
#         if newLine[-1][-1] == "\n":
#             newLine[-1] = newLine[-1][:-1:]
#         cutLines.append(newLine)
        
#     return cutLines


# """
# indices:
# capital, country, longitude, latitude
# takes in a list and returns a dictionary
# """
# def make_key_value_pair(string:list[str]) -> dict:
#     print("make_key_value_pair running \n")
#     print(string)

#     lat = directions_to_positives(string[2].rstrip())
#     long = directions_to_positives(string[3].rstrip())

#     new_dict = {
#         "capital" : string[0].rstrip(),
#         "country" : string[1].rstrip(),
#         "latitude" : lat,
#         "longitude" : long,
#         "lat and long" : lat + " " + long,
#     }

#     return new_dict


# def make_json(lines : list[list[str]]):
    

#     dictOfCountries = {}
#     dictOfCoords = {}
#     for line in lines:
#         formattedLine : dict = make_key_value_pair(line)
#         dictOfCountries[formattedLine.get("country")] = formattedLine
#         dictOfCoords[formattedLine.get("lat and long")] = formattedLine

#     namesFile.write(json.dumps(dictOfCountries))
#     coordsFile.write(json.dumps(dictOfCoords))


# make_json(parse_lines())


# readFile.close()
# coordsFile.close()
# namesFile.close()


import json
from countryinfo import CountryInfo

countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo (Congo-Brazzaville)", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic (Czechia)", "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor (Timor-Leste)", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini (Swaziland)", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, North (North Korea)", "Korea, South (South Korea)", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]


dictOfCountries = {}
dictOfCoords = {}

for country_name in countries:
    try:
        info = CountryInfo(country_name).info()
        capital = info.get("capital")
        latlng = info.get("latlng")
        if not capital or not latlng or len(latlng) != 2:
            print(f"Skipping {country_name}: missing data.")
            continue
        lat = str(round(latlng[0], 2))
        lon = str(round(latlng[1], 2))
        entry = {
            "capital": capital,
            "country": country_name,
            "latitude": lat,
            "longitude": lon,
            "lat and long": f"{lat} {lon}"
        }
        dictOfCountries[country_name] = entry
        dictOfCoords[f"{lat} {lon}"] = entry
        print(f"Added {country_name}: {capital} at {lat} {lon}")
    except Exception as e:
        print(f"Error with {country_name}: {e}")

with open("coordinates_creation/names.json", "w", encoding="utf-8") as namesFile:
    json.dump(dictOfCountries, namesFile, ensure_ascii=False, indent=4)

with open("coordinates_creation/coords.json", "w", encoding="utf-8") as coordsFile:
    json.dump(dictOfCoords, coordsFile, ensure_ascii=False, indent=4)