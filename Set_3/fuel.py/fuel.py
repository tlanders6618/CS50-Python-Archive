def main():
    while (True):
        fraction=input("Input "); fraction=fraction.strip(); top=""; bottom=""; go=False;
        if (fraction.count("/")>0):
            try:
                top, dash, bottom=fraction.partition("/");
            except ValueError:
                pass;
        else:
            continue;
        go=check(top, bottom); #make sure fraction is proper
        if (go==True): #only print if so
            java(top, bottom); break;

def check(top, bottom):
    if (top.isdigit()==False or bottom.isdigit()==False):
        return False;
    if (bottom=="0"):
        return False;
    if (int(top)>int(bottom)):
        return False;
    if (int(top)<0 or int(bottom)<0):
        return False;
    return True;

def java(top, bottom):
    ans=int(top)/int(bottom);
    ans*=100; #convert from decimal to percent; 0.5*100=50
    if (ans>=99):
        print("F");
    elif (ans<=1):
        print("E");
    else:
        ans=int(ans);
        print(str(ans)+"%", end="");

main();
