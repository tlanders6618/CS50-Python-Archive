def main(): #semicolons because aesthetics
    print("Hello, it is I, the late and great Albert Einstein. Name any mass, and I will tell you its equivalent in energy!");
    mass=int(input());
    answer=300000000*300000000*mass;
    string=f"{answer:,}"; #f string to add commas so num is legible, as seen in the introduction lecture
    print(string);
    print("Abra-cadabra! "+str(mass)+" kilogram(s) is the same as "+string+" Joules! Pretty cool, huh?");

main();
