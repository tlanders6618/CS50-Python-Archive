import re;

def main():
    print(convert(input("Hours: ")));

def convert(time):
    if (time==""):
        time="12:00 PM to 6 AM";
    time=time.strip();
    k=re.search(r"(?:[1][0-2]|[1-9])(?::[0-5][0-9])? (?:AM|PM) to (?:[1][0-2]|[1-9])(?::[0-5][0-9])? (?:AM|PM)", time);
    if (k==None):
        raise ValueError();
    #else
    time=k.group();
    first, last=time.split("to"); #has extra spaces due to there being ones before and after "to"
    first=translate(first.strip()); #so strip when sending
    last=translate(last.strip());
    return (first+" to "+last);

def translate(time): #12pm is fine but 12am is not; otherwise anything am is fine as is
    if ((time[len(time)-2:]=="AM" and time[0:2]!="12") or (time[len(time)-2:]=="PM" and time[0:2]=="12")):
        if (":" not in time): #just need to add :00 to end
            if (len(time)==4): #one digit, space, and am; must add 0 to start
                #print("No translation needed: "+"0"+time[0:len(time)-2].strip())
                return "0"+time[0:len(time)-2].strip()+":00";
            elif(len(time)==5): #two digits, space, and am
                #print("No translation needed: "+time[0:len(time)-2].strip())
                return time[0:len(time)-2].strip()+":00";
        else: #fine as is
            if (time.find(":")==2): #double digits before colon; fine as is
                #print("No translation needed: "+time[0:len(time)-2].strip());
                return time[0:len(time)-2].strip(); #just return time with AM gone
            elif (time.find(":")==1): #single digit before colon; must be returned with 0 in front
                #print("No translation needed: "+"0"+time[0:len(time)-2].strip());
                return "0"+time[0:len(time)-2].strip(); #just return time with AM gone
    else:
        time=time[0:len(time)-2].strip(); #remove PM/AM from time and proceed to translation
    if (":" in time): # has numbers after colon; only replace number before it
        index=time.find(":");
        if (index==2): #double digits before colon, e.g. 11
            digit=time[0:2]; #slice from 0-1
            #print("Case: "+digit);
            match (digit):
                case "10": return "22"+time[2:]; #print("Translation complete: "+"22"+time[2:]);
                case "11": return "23"+time[2:]; #print("Translation complete: "+"23"+time[2:]);
                case "12": return "00"+time[2:]; #converting 12 AM #print("Translation complete: "+"0"+time[2:]);
                case _: print("I made a mistake somewhere."); #default case
        elif (index==1): #single digit before colon, e.g. 9
            digit=time[0:1]; #slice 0
            match (digit):
                case "1": return "13"+time[1:]; #print("Translation complete: "+"13"+time[2:]);
                case "2": return "14"+time[1:]; #print("Translation complete: "+"14"+time[2:]);
                case "3": return "15"+time[1:]; #print("Translation complete: "+"15"+time[2:]);
                case "4": return "16"+time[1:]; #print("Translation complete: "+"16"+time[2:]);
                case "5": return "17"+time[1:]; #print("Translation complete: "+"17"+time[2:]);
                case "6": return "18"+time[1:]; #print("Translation complete: "+"18"+time[2:]);
                case "7": return "19"+time[1:]; #print("Translation complete: "+"19"+time[2:]);
                case "8": return "20"+time[1:]; #print("Translation complete: "+"20"+time[2:]);
                case "9": return "21"+time[1:]; #print("Translation complete: "+"21"+time[2:]);
                case _: print("I made a mistake."); #default case
    else: # time is just a colonless digit, so return converted digit
        match (time[0:2].strip()): #slice from 0-1, either one digit with a space or two digits
            case "1": return "13:00"; #print("Translation complete: "+"13");
            case "2": return "14:00"; #print("Translation complete: "+"14");
            case "3": return "15:00"; #print("Translation complete: "+"15");
            case "4": return "16:00"; #print("Translation complete: "+"16");
            case "5": return "17:00"; #print("Translation complete: "+"17");
            case "6": return "18:00"; #print("Translation complete: "+"18");
            case "7": return "19:00"; #print("Translation complete: "+"19");
            case "8": return "20:00"; #print("Translation complete: "+"20");
            case "9": return "21:00"; #print("Translation complete: "+"21");
            case "10": return "22:00"; #print("Translation complete: "+"22");
            case "11": return "23:00"; #print("Translation complete: "+"23");
            case "12": return "00:00"; #for converting 12AM #print("Translation complete: "+"0");
            case _: print("I made a mistake somewhere."); #default case

if __name__ == "__main__":
    main();
