def main(): #using semicolons bc java training
    dollars = dollarsconv(input("How much did your meal cost? "));
    percent = percentconv(input("What percentage would you like to tip? "));
    tip = (dollars*percent);
    print(f"Leave ${tip:.2f}");

def dollarsconv(doll):
    doll=doll.replace("$",""); #delete $ from value, leaving only num, e.g. 40.00
    return float(doll);

def percentconv(perstring):
    perstring=perstring.replace("%",""); #delete % from percent, leaving only num, e.g. 7.9
    if (perstring=="0" or perstring=="0.00"): #practising if statements, as seen in the variables short
        print("For shame, good sir or madame. Think of the children!");
        return 0;
    else:
        return float(perstring)/100;

main();
