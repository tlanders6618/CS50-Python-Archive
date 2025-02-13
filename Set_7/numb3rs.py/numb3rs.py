import re;

def main():
    print(validate(input("IPv4 Address: ")));

def validate(ip):
    Range="(?:[2][5][0-5]|[2][0-4][0-9]|[1][0-9][0-9]|[1-9][0-9]|[0-9])";
    #1-9 instead of 0-9 bc first digit of multi-digit number is never 0
    #if 250+, cannot end in anything >5, but if <250, can end in 9, e.g. 249
    #everything <200 can end in 9
    if(re.search(r"^"+Range+"\."+Range+"\."+Range+"\."+Range+"$", ip.strip())==None):
        return False;
    else:
        return True;

if __name__ == "__main__":
    main();
