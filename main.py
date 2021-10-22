import re

# 1 ############################################

largestCities = "2019_largest_cities.txt"
readFile = open(largestCities, 'r')

postalCities = "us_postal_codes.csv"
readFile2 = open(postalCities, 'r')

cities_name = dict()
boolArray = [True for i in range(30)]
i = 0
for line in readFile:
    res = (re.search(r"[A-Z]+[a-z]+[' ']+[A-Z]+[a-z]+", line))
    res2 = (re.search(r"[A-Z]+[a-z]+[A-Z]", line))
    if res:
        cities_name[i] = res.group()
        boolArray[i] = False
        i += 1

    if res2 and not res:
        res3 = re.search(r'[A-Z]+[a-z]+', res2.group())
        cities_name[i] = res3.group()
        boolArray[i] = False
        i += 1

for line in readFile2:
    for index in range(len(cities_name)):
        if re.search(cities_name[index], line) and boolArray[index] == False:
            boolArray[index] = True
            print(cities_name[index], re.search(r"([0-9]{4})", line).group())

readFile.close()
readFile2.close()

# 2 #####################################################################

atoms = "atoms2.log"
readFile3 = open(atoms, 'r')
output = open("output", 'w')

for line in readFile3:
    res = re.search(r"([A-Z]{3})+[' ']+([0-9]{6})+[' ']+([A-Z]{9})+\.+[' ']+([A-Z]+[' ']+[A-Z]+[' ']+[A-Z]+[' ']+[a-z]+\.+[a-z]{3})+\.+[' ']+[0-9]+\.", line)
    if res:
        output.write(res.group(2) + '\n')

readFile3.close()
output.close()