import sys, csv;

def main():
    if (len(sys.argv)>3):
        sys.exit("Abra kadabra! That's too many arguments!");
    elif(len(sys.argv)<3):
        sys.exit("Not enough arguments. Hocus pocus!");
    #else
    names=[];
    try:
        with open(sys.argv[1], "r") as before:
            CSV=csv.DictReader(before);
            for dict in CSV:
                sur, fore=dict["name"].split(",");
                student={"first": fore.strip(), "last": sur, "house": dict["house"]}; #strip bc space in ", Harry"
                names.append(student);
        with open(sys.argv[2], "w") as after:
            newCSV=csv.DictWriter(after, ["first", "last", "house"]);
            newCSV.writeheader();
            for dict in names:
                newCSV.writerow(dict);
    except FileNotFoundError:
        sys.exit("Alah kazam! Your file could not be accessed!");

if __name__=="__main__":
    main();
