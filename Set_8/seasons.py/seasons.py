from datetime import datetime, date;
import re, inflect, sys;

def main():
    time=input("When were you born? "); #format YYYY-MM-DD
    if (validdate(time)==True):
        result=convert(time);
        print(result.capitalize()+" minutes");

def convert(time):
    today=date.today();
    today=datetime(today.year, today.month, today.day); #date with time of midnight (00:00)
    try: #date constructor already makes sure the date actually exists, so make use of it
        year, month, day=time.split("-");
        given=datetime(int(year), int(month), int(day)); #default time is also midnight
    except (ValueError):
        sys.exit("Invalid date.");
    else:
        dif=today-given; #provides a timedelta object
        seconds=dif.total_seconds();
        seconds=abs(seconds/60); #future dates would have negative time until them
        seconds=round(seconds);
        engine=inflect.engine();
        minutes=engine.number_to_words(seconds);
        minutes=minutes.replace(" and ", " "); #remove and
        return minutes;

def validdate(time): #checks if format is correct, not if date actually exists, e.g. Feb. 31st would past
    string="^[0-9][0-9][0-9][0-9]-(?:[0][1-9]|[1][0-2])-(?:[0][1-9]|[1-2][0-9]|[3][0-1])$";
    if (re.search(r""+string, time.strip(), re.IGNORECASE)==None):
        sys.exit("Invalid date.");
    else:
        return True;

if __name__ == "__main__":
    main();
