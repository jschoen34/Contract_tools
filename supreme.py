import csv

filename = "SCDB_2019_01_justiceCentered_Citation.csv"
fp = open(filename, encoding="ISO-8859-1")

justices = {}
reader = csv.DictReader(fp)

for row in reader:

    jid = row["justice"]
    name = row["justiceName"]
    date = row["dateDecision"]
    case = row ["caseName"]

    #print ("justice" + name + "has ID = " + jid)

    justice.setdefault({jid, name, "first_case": case, "first date": date, "last_case": case, "last_date": date})
    justices[jid]["last_case"] = case
    justice[jid]["last_date"] = date

print (justices)

fp.close()
