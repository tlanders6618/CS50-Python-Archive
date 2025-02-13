def main():
    while (True):
        fraction=input("Input ");
        ans=convert(fraction);
        if (ans != -1): #valid fraction
            ans=gauge(ans);
            print(ans);
            break;

def convert(fraction):
    fraction=fraction.strip(); top=""; bottom="";
    if (fraction.count("/")>0):
        try:
            top, dash, bottom=fraction.partition("/");
        except ValueError:
            return -1;
        else:
            good=check(top, bottom);
            if (good==True):
                ans=int(top)/int(bottom);
                ans*=100; #convert from decimal to percent; 0.5*100=50
                return ans;
    else:
        return -1;

def check(top, bottom):
    if (top.isdigit()==False or bottom.isdigit()==False):
        raise ValueError("Improper fraction.");
    if (bottom=="0"):
        raise ZeroDivisionError;
    if (int(top)>int(bottom)):
        raise ValueError("Improper fraction.");
    if (int(top)<0 or int(bottom)<0):
        return False;
    return True;

def gauge(percent):
    if (percent>=99):
        return "F";
    elif (percent<=1):
        return "E";
    else:
        percent=int(percent);
        return str(percent)+"%";

if __name__=="__main__":
    main();
