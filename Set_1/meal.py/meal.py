def main(): #semicolon supremacy, says the superior software shaper
    flunk=convert(input("What time is it? "));
    if (flunk>=7 and flunk<=8):
        print("breakfast time");
    elif (flunk>=12 and flunk<=13):
        print("lunch time");
    elif (flunk>=18 and flunk<=19):
        print("dinner time");

def convert(time):
    hour, ignore, min=time.partition(":"); #since time is written as #:##, hour is #, ignore is :, and min is ##
    Hour=float(hour);
    Min=float(min); Min=Min/60;
    #print (Hour+Min); #works as intended
    return Hour+Min;

if __name__ == "__main__": #idk what this means, but check50 doesn't work without it for some reason
    main();
