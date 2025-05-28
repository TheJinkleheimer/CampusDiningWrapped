try: h = open(input("Input full file path of your dining plan history: ").strip('"'))
except: print(f"Bad input!!! Follow the readme >:(") # "C:\Users\ilumi\Documents\History.txt"
else:
    places = [
        {
            "place" : "Subway Dexter",
            "spent" : 0.00,
            "times" : 0,
            "area" : "Other"
        },
        {
            "place" : "Subway PCV",
            "spent": 0.00,
            "times": 0,
            "area": "PCV"
        },
        {
            "place" : "Panda Express",
            "spent": 0.00,
            "times": 0,
            "area" : "1901"
        },
        {
            "place" : "Chick-Fil-A",
            "spent": 0.00,
            "times": 0,
            "area" : "1901"
        },
        {
            "place" : "Mingle & Nosh",
            "spent": 0.00,
            "times": 0,
            "area" : "Vista Grande"
        },
        {
            "place" : "Balance",
            "spent": 0.00,
            "times": 0,
            "area" : "Vista Grande"
        },
        {
            "place" : "Pico's",
            "spent": 0.00,
            "times": 0,
            "area" : "1901"
        },
        {
            "place" : "Streats",
            "spent": 0.00,
            "times": 0,
            "area" : "Vista Grande"
        },
        {
            "place" : "Noodles",
            "spent": 0.00,
            "times": 0,
            "area" : "Vista Grande"
        },
        {
            "place" : "Village Market",
            "spent": 0.00,
            "times": 0,
            "area" : "PCV"
        },
        {
            "place" : "Grand Ave Market",
            "spent": 0.00,
            "times": 0,
            "area" : "Vista Grande"
        },
        {
            "place" : "Hearth",
            "spent": 0.00,
            "times": 0,
            "area" : "Vista Grande"
        },
        {
            "place" : "Jewel of India",
            "spent": 0.00,
            "times": 0,
            "area" : "Other"
        },
        {
            "place" : "Jamba Juice",
            "spent": 0.00,
            "times": 0,
            "area" : "Vista Grande"
        },
        {
            "place" : "Scout Coffee",
            "spent": 0.00,
            "times": 0,
            "area" : "Other"
        },
        {
            "place" : "Poly Deli",
            "spent": 0.00,
            "times": 0,
            "area" : "1901"
        },
        {
            "place" : "Pom & Honey",
            "spent": 0.00,
            "times": 0,
            "area" : "1901"
        },
        {
            "place" : "Einstein's Bagels",
            "spent": 0.00,
            "times": 0,
            "area" : "PCV"
        },
        {
            "place" : "Brunch",
            "spent": 0.00,
            "times": 0,
            "area" : "Vista Grande"
        },
        {
            "place" : "1901 Kitchen",
            "spent": 0.00,
            "times": 0,
            "area" : "1901"
        },
        {
            "place" : "Taco Bell",
            "spent": 0.00,
            "times": 0,
            "area" : "PCV"
        },
        {
            "place" : "Campus Market",
            "spent": 0.00,
            "times": 0,
            "area" : "Other"
        }
    ]

    areas = [
        {
            "area" : "PCV",
            "spent" : 0.00,
            "times" : 0
        },
        {
            "area" : "1901",
            "spent" : 0.00,
            "times" : 0
        },
        {
            "area" : "Vista Grande",
            "spent" : 0.00,
            "times" : 0
        },
        {
            "area" : "Other",
            "spent" : 0.00,
            "times" : 0
        },
        {
            "area" : "Unknown",
            "spent" : 0.00,
            "times" : 0
        }
    ]
    hours = [[0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0],
             [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0]]
    days = [[[0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0]],
            [[0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0]],
            [[0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0]],
            [[0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0]],
            [[0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0]],
            [[0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0]],
            [[0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0]],
            [[0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0]],
            [[0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0]],
            [[0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0]],
            [[0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0]],
            [[0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0]]]
    quarters = [1, [0, 0.0, 0.0], [0, 0.0, 0.0], [0, 0.0, 0.0], [0, 0.0, 0.0], [0, 0.0, 0.0], [0, 0.0, 0.0], [0, 0.0, 0.0], [0, 0.0, 0.0], [0, 0.0, 0.0], [0, 0.0, 0.0], [0, 0.0, 0.0], [0, 0.0, 0.0], [0, 0.0, 0.0], [0, 0.0, 0.0]]
    months = [[0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0], [0,0.0]]

    highest = 0
    lowest = 6000

    h.readline()
    first = h.readline().strip("\n").split("\t")
    total = 0
    available = 3*float(first[4].strip("$"))

    for x in h:
        #get line
        line = x.strip("\n").split("\t")[0:4]

        #make it nice
        dnt = line[0].split(" ")
        dnt = [dnt[0].split("/"), dnt[1].split(":")]
        line[0] = [int(dnt[0][0]), int(dnt[0][1])]
        line.insert(1, [int(dnt[1][0]), int(dnt[1][1])])
        line[4] = float(line[4].strip("$"))

        #CRUNCH IT [[9, 17], [19, 22], 'Mingle & Nosh Micros 782', 'First Year Plus', 7.35]

        if line[2] == "PatronImport Location":
            line = [[0,0],[0,0], 'PatronImport Location', 'First Year Plus', 0]
            quarters[0] += 1

        #by place
        placeKeys = [x["place"] for x in places]
        placeKey = ""
        for k in placeKeys:
            if "PCV" in line[2].upper():
                placeKey = "Subway PCV"
            elif "SUBWAY" in line[2].upper():
                placeKey = "Subway Dexter"
            elif k.upper() in line[2].upper():
                placeKey = k

        if placeKey == "": # if place not accounted for, add it
            places.append({
                "place" : line[2],
                "spent": line[4],
                "times": 1,
                "area": "Unknown"
            })
            placeKeys.append(line[2])
            placeKey = line[2] # update key for area stuff
        else:
            places[placeKeys.index(placeKey)]["spent"] += line[4] # update place data
            places[placeKeys.index(placeKey)]["times"] += 1

        if placeKey != "PatronImport Location":
            areaKeys = [x["area"] for x in areas]
            areaIndex = areaKeys.index(places[placeKeys.index(placeKey)]["area"])

            areas[areaIndex]["spent"] += line[4] # update area data
            areas[areaIndex]["times"] += 1

        # by quarter
        quarters[quarters[0]][0] += 1
        quarters[quarters[0]][1] += line[4]

        #by month
        months[line[0][0]-1][0] += 1
        months[line[0][0]-1][1] += line[4]

        # by day
        days[line[0][0]-1][line[0][1]-1][0] += 1
        days[line[0][0]-1][line[0][1]-1][1] += line[4]

        # by time
        hours[line[1][0]][0] += 1
        hours[line[1][0]][1] += line[4]

        #by spending amount
        if 0.5 < line[4] < lowest: lowest = line[4]
        if line[4] > highest: highest = line[4]

        total += line[4]

    for a in areas:
        try:
            a["average"] = a["spent"] / a["times"]
        except:
            a["average"] = 0.0
    for p in places:
        try:
            p["average"] = p["spent"] / p["times"]
        except:
            p["average"] = 0.0

    def dictBySpent(e):
        return -e["spent"]
    def dictByTimes(e):
        return -e["times"]
    def dictByAvg(e):
        return -e["average"]

    aBySpent = sorted(areas, key=dictBySpent)
    aByTimes = sorted(areas, key=dictByTimes)
    aByAvg = sorted(areas, key=dictByAvg)

    pBySpent = sorted(places, key=dictBySpent)
    pByTimes = sorted(places, key=dictByTimes)
    pByAvg = sorted(places, key=dictByAvg)
    
    parsedDays = []
    for i in range(len(days)):
        for j in range(len(days[i])):
            if days[i][j][0] > 0:
                parsedDays.append({
                    "date" : str(i + 1) + "/" + str(j + 1),
                    "times" : days[i][j][0],
                    "spent": days[i][j][1],
                    "average" : days[i][j][1]/days[i][j][0]
                })

    for d in parsedDays:
        try:
            d["average"] = d["spent"] / d["times"]
        except:
            d["average"] = 0.0

    dBySpent = sorted(parsedDays, key=dictBySpent)
    dByTimes = sorted(parsedDays, key=dictByTimes)
    dByAvg = sorted(parsedDays, key=dictByAvg)

    mt = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    parsedMonths = []
    for i in range(len(months)):
        if months[i][0] > 0:
            parsedMonths.append({
                "month": mt[i],
                "times": months[i][0],
                "spent": months[i][1],
                "average": months[i][1] / months[i][0]
            })

    mBySpent = sorted(parsedMonths, key=dictBySpent)
    mByTimes = sorted(parsedMonths, key=dictByTimes)
    mByAvg = sorted(parsedMonths, key=dictByAvg)

    parsedHours = []
    for i in range(len(hours)):
        parsedHours.append({
            "hour" : str(i),
            "times": hours[i][0],
            "spent": hours[i][1],
        })
        try: parsedHours[-1]["average"] = hours[i][1] / hours[i][0]
        except: parsedHours[-1]["average"] = 0

    hBySpent = sorted(parsedHours, key=dictBySpent)
    hByTimes = sorted(parsedHours, key=dictByTimes)
    hByAvg = sorted(parsedHours, key=dictByAvg)

    utilization = total/available

    print("\n\nHere is your Campus Dining Wrapped!\n")

    print("\nList of places by total spent:")
    for i in range(len(pBySpent)): print(f"{i + 1}." + (21 - len(pBySpent[i]["place"]) - len( # PLACE
        str(i + 1))) * " " + f"{pBySpent[i]["place"]} ${pBySpent[i]["spent"]:.2f}")

    print("\nList of places by number of transactions:")
    for i in range(len(pByTimes)): print(f"{i + 1}." + (21 - len(pByTimes[i]["place"]) - len(
        str(i + 1))) * " " + f"{pByTimes[i]["place"]} {pByTimes[i]["times"]:.0f}")

    print("\nList of places by average transaction cost:")
    for i in range(len(pByAvg)): print(f"{i + 1}." + (21 - len(pByAvg[i]["place"]) - len(
        str(i + 1))) * " " + f"{pByAvg[i]["place"]} ${pByAvg[i]["average"]:.2f}")

    print("\nList of areas by total spent:")
    for i in range(len(areas)): print(f"{i + 1}." + (15 - len(aBySpent[i]["area"]) - len( # AREA
        str(i + 1))) * " " + f"{aBySpent[i]["area"]} ${aBySpent[i]["spent"]:.2f}")

    print("\nList of areas by number of transactions:")
    for i in range(len(areas)): print(f"{i + 1}." + (15 - len(aByTimes[i]["area"]) - len(
        str(i + 1))) * " " + f"{aByTimes[i]["area"]} {aByTimes[i]["times"]:.0f}")

    print("\nList of areas by average transaction cost:")
    for i in range(len(areas)): print(f"{i + 1}." + (15 - len(aByAvg[i]["area"]) - len(
        str(i + 1))) * " " + f"{aByAvg[i]["area"]} ${aByAvg[i]["average"]:.2f}")

    print("\nList of months by total spent:")
    for i in range(len(parsedMonths)): print(f"{i + 1}." + (13 - len(mBySpent[i]["month"]) - len(  # MONTH
        str(i + 1))) * " " + f"{mBySpent[i]["month"]} ${mBySpent[i]["spent"]:.2f}")

    print("\nList of months by number of transactions:")
    for i in range(len(parsedMonths)): print(f"{i + 1}." + (13 - len(mByTimes[i]["month"]) - len(
        str(i + 1))) * " " + f"{mByTimes[i]["month"]} {mByTimes[i]["times"]:.0f}")

    print("\nList of months by average transaction cost:")
    for i in range(len(parsedMonths)): print(f"{i + 1}." + (13 - len(mByAvg[i]["month"]) - len(
        str(i + 1))) * " " + f"{mByAvg[i]["month"]} ${mByAvg[i]["average"]:.2f}")

    print("\nList of top days by total spent:")
    for i in range(10): print(f"{i + 1}." + (8 - len(dBySpent[i]["date"]) - len(  # DAY
        str(i + 1))) * " " + f"{dBySpent[i]["date"]} ${dBySpent[i]["spent"]:.2f}")

    print("\nList of top days by number of transactions:")
    for i in range(10): print(f"{i + 1}." + (8 - len(dByTimes[i]["date"]) - len(
        str(i + 1))) * " " + f"{dByTimes[i]["date"]} {dByTimes[i]["times"]:.0f}")

    print("\nList of top days by average transaction cost:")
    for i in range(10): print(f"{i + 1}." + (8 - len(dByAvg[i]["date"]) - len(
        str(i + 1))) * " " + f"{dByAvg[i]["date"]} ${dByAvg[i]["average"]:.2f}")

    print("\nList of hours of the day by total spent (Military Time):")
    for i in range(len(parsedHours)): print(f"{i + 1}." + (5 - len(hBySpent[i]["hour"]) - len(  # DAY
        str(i + 1))) * " " + f"{hBySpent[i]["hour"]} ${hBySpent[i]["spent"]:.2f}")

    print("\nList of hours of the day by number of transactions (Military Time):")
    for i in range(len(parsedHours)): print(f"{i + 1}." + (5 - len(hByTimes[i]["hour"]) - len(
        str(i + 1))) * " " + f"{hByTimes[i]["hour"]} {hByTimes[i]["times"]:.0f}")

    print("\nList of hours of the day by average transaction cost (Military Time):")
    for i in range(len(parsedHours)): print(f"{i + 1}." + (5 - len(hByAvg[i]["hour"]) - len(
        str(i + 1))) * " " + f"{hByAvg[i]["hour"]} ${hByAvg[i]["average"]:.2f}")

    print(f"\nStats by Quarter (may only work for first years):")
    for q in range(1, quarters[0] + 1):
        quarters[q][2] = quarters[q][1] / quarters[q][0]
        print(f"Quarter {q + 1} - Spent: ${quarters[q][1]:.2f}\t Transactions: {quarters[q][0]}\t Average: ${(quarters[q][1] / quarters[q][0]):.2f}")

    print(f"\nMost Spent in one transaction: ${highest:.2f}")
    print(f"\nLeast Spent in one transaction: ${lowest:.2f}")
    print(f"\nTotal dining plan utilization (only works for first years): {100 * total/available:.2f}%")

    print(f"\n\n\nThank you for using Jinkleheimer's Dining Wrapped!")
