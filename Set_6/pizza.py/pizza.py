import csv, sys;
from tabulate import tabulate;

def main():
    if (len(sys.argv)>2):
        sys.exit("Too much pizza (arguments)! Overloading...ERROR. Please try again.");
    elif (len(sys.argv)<2):
        sys.exit("where the pizza (arguments)");
    length=len(sys.argv[1]);
    if (sys.argv[1][length-4:]!=".csv"): #pizza.csv len=9 so len-4=5
        sys.exit("Mamma mia! You've been permanently banned from Parmesan's Pizza, where every menu must be a valid CSV.");
    try:
        with open(sys.argv[1], "r") as file:
            reader=csv.DictReader(file);
            menu=[]; first=True;
            for row in reader:
                if (first==True):
                    menu.append(row.keys()); first=False; #to be used as headers
                list=[]; #each list is row in csv
                for key in row:
                    list.append(row.get(key));
                menu.append(list);
    except FileNotFoundError:
        sys.exit("Mamma mia! You've been permanently banned from Parmesan's Pizza, where every menu must be a valid CSV.");
    else:
        print(tabulate(menu, headers="firstrow", tablefmt="grid"));

if __name__=="__main__":
    main();
