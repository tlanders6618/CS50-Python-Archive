import sys;
import requests;
import json;

def main():
    jason=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json");
    jason=jason.json(); #jason is a giant dict containing several other dicts
    #print(json.dumps(jason, indent=2));
    bpi=jason["bpi"]; #the bpi key in jason returns a dict containing 3 keys: USD, GBP, and EUR
    usd=bpi["USD"]; #access the USD dict, which contains 5 keys, one of which is rate_float
    cash=usd["rate_float"]; #rate_float returns the rate as a float (rate only returns a string), with 4 decimal places
    if (len(sys.argv)==2):
        try:
            fly=float(sys.argv[1]);
        except ValueError:
            sys.exit("You need to type a number -_-");
        else:
            pryce=cash*fly;
            print(f"${pryce:,.4f}");
    else:
        sys.exit("You're supposed to give me one argument, no more, no less >_<");

if __name__=="__main__":
    main();
