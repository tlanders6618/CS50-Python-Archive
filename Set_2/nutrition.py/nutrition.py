def main():
    fruit=input("Still recovering from the coke. It took me an entire hour, but at least this is the last one for tonight. Also, compulsory Java statement. ");
    fruit=fruit.lower();
    bigdict=[ #list of dictionaries
        {"apple": "130"}, {"avocado": "50"}, {"banana": "110"}, {"cantaloupe": "50"}, {"grapefruit": "60"},
        {"grapes": "90"}, {"honeydew melon": "50"}, {"kiwifruit": "90"}, {"lemon": "15"}, {"lime": "20"},
        {"nectarine": "60"}, {"orange": "80"}, {"peach": "60"}, {"pear": "100"}, {"pineapple": "50"},
        {"plums": "70"}, {"strawberries": "50"}, {"sweet cherries": "100"}, {"tangerine": "50"}, {"watermelon": "80"}
        ];
    for dict in bigdict:
        if (dict.get(fruit)!=None): #input is valid key in one of the dicts
            print("Calories: "+dict.get(fruit));
            break;
main();
