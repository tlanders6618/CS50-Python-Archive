def main(phrase): #obligatory java comment
    phrase=phrase.strip();
    first, op, sec=phrase.split(None, 2);
    num1=float(first);
    num2=float(sec);
    match (op):
        case "+": return num1+num2;
        case "-": return num1-num2;
        case "*": return num1*num2;
        case "/": return num1/num2;

an=main(input("Oh yeah, it's calculating time. Hit me up. ")); #formatted as x + y
print(f"{an:.1f}");
