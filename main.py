WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

DELIMITER = ";"

class TIMESTAMP:
    weekday = ""
    hour = 0
    consumption = 0.0
    price = 0.0

def readfile(PFilename, PRows):
    print("Reading file {}".format(PFilename))
    with open(PFilename) as File:
        File.readline()
        for Line in File:
            Line = Line.strip("\n")
            if Line == "":
                continue
            Line = Line.split(DELIMITER)
            PRows.append(Line)
    return None

def analyseTimestamps(Timestamps, PRows):
    for row in PRows:
        Timestamp = TIMESTAMP()
        Timestamp.weekday = row[0]
        Timestamp.hour = int(row[1])
        Timestamp.consumption = float(row[2])
        Timestamp.price = float(row[3])
        Timestamps.append(Timestamp)
    Usage = [0.0] * 7
    Cost = [0.0] * 7
    for Timestamp in Timestamps:
        for i in range(len(WEEKDAYS)):
            if Timestamp.weekday == WEEKDAYS[i]:
                Usage[i] += Timestamp.consumption
                Cost[i] += Timestamp.consumption * Timestamp.price
    return Usage, Cost

def displayResults(Usage, Cost):
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for i in range(len(WEEKDAYS)):
        print(" - {} usage {:.2f} kWh, cost {:.2f} €".format(WEEKDAYS[i], Usage[i], Cost[i]))
    print("### Electricity consumption summary ###")

def main():
    filename = input("Insert filename: ")
    PRows = []
    readfile(filename, PRows)
    Timestamps = []
    Usage, Cost = analyseTimestamps(Timestamps, PRows)
    displayResults(Usage, Cost)
    print("Program ending.")

main()