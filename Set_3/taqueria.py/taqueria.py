def main():
    menu= {"Taco": 3.00, "Baja Taco": 4.25, "Burrito": 7.50, "Super Burrito": 8.50, "Tortilla Salad": 8.00,
           "Bowl": 8.50, "Quesadilla": 8.50, "Super Quesadilla": 9.50, "Nachos": 11.00};
    print("Welcome to Felipe's Taqueria, where every taco is muy delicious-o. My name is Java. May I take your order? ");
    total=0.0;
    while (True):
        try:
            order=input();
            order=order.title(); order=order.strip();
            if (order in menu):
                total+=menu[order];
                print(f"${total:.2f}");
            else:
                print("Sir or ma'am, this is a taqueria. We only have what's on the menu, and a \""+order+"\" is not.");
        except EOFError:
            print(f"Thank you for ordering. Your total will be ${total:.2f}. Please proceed to the end of the drivethrough.");
            break;

main();
