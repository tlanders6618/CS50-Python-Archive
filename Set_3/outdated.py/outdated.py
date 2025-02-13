def main():
    name_to_num={"January":"1", "February":"2", "March":"3", "April":"4", "May":"5", "June":"6", "July":"7",
                 "August":"8", "September":"9", "October":"10", "November":"11", "December":"12"};
    done=False;
    while(done==False): #ensures user input is #/#/# or # #, # before trying to print anything
        go=False; convert=False; #only convert july to 7 if format isn't #/#/#; if it is, dates should be all nums already
        date=input("All hail the mihty duck. Hail Java. ");
        date=date.title(); date=date.strip();
        if (date.count("/")>0): #if user has 7/7/2000, replace "/" with " " so dates are separate and .split works properly
            ndate="";
            for char in date:
                if (char=="/"):
                    ndate+=" ";
                else:
                    ndate+=char;
            date=ndate; go=True;
        elif (date.count(",")>0): # July 7, 2000 is already properly formatted; continue
                go=True; convert=True;
        if (go==True):
            values=date.split();
            if (len(values)!=3): #user didn't put in full date; not enough words, so retry
                continue;
            else:
                month, day, year=values;
                if (month.count(",")>0): #delete all commas
                    month=month.replace(",", "");
                if (day.count(",")>0):
                    day=day.replace(",", "");
                if (year.count(",")>0):
                    year=year.replace(",", "");
                if (day.isdigit()==True): #must be 7, not seven or gibberish or anything else
                    day=int(day);
                else:
                    continue; #restart loop
                if (year.isdigit()==True):
                    year=int(year);
                else:
                    continue;
                if (month.isdigit()==True):
                    month=int(month);
                elif (month in name_to_num and convert==True):
                    month=name_to_num[month];
                    month=int(month);
                else:
                    continue;
                if (day<32 and month<12 and month>0 and year>0): #check validity of date
                    if (len(str(day))==1): #fill blank spaces so # becomes ## or #### for all slots
                        day="0"+str(day);
                    if (len(str(month))==1):
                        month="0"+str(month);
                    if (len(str(year))<4):
                        for _ in range (4-(len(str(year)))):
                            year="0"+str(year);
                    print(str(year)+"-"+str(month)+"-"+str(day)); #print and then return true to break the loop and end program
                    done=True;
main();
