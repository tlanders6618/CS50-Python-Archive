import project, random;
from project import playerWon, betterIsAlpha, gameOver;

def test_playerWon():
    a=project.Hero("Prince Akazani", 50); #alive
    assert playerWon(a)==True;
    a.health=0;
    assert playerWon(a)==False;

def test_gameOver():
    j=project.Hero("Jimmy Two Eyes", 50); #alive
    d=project.Dungeon(2, j); #unexplored
    assert gameOver(j,d)==False;
    j.health=0; #dead
    assert gameOver(j,d)==True;
    j.health=1; #alive
    for r in range(len(d.dungeon[0])): #"exploring" it, since explored has no setter
        for c in range(len(d.dungeon[0])):
            if (d.dungeon[r][c]!="empty" and d.dungeon[r][c]!=j.name):
                d.dungeon[r][c]="empty";
    assert gameOver(j,d)==True;

def test_betterIsAlpha(): #true if input is alphabet letter or space
    assert betterIsAlpha(" ")==True;
    assert betterIsAlpha("please")==True;
    assert betterIsAlpha("sw Or D")==True;
    assert betterIsAlpha("!")==False;
    assert betterIsAlpha("2")==False;
    assert betterIsAlpha(",")==False;

def main():
    project.main(size=10, name="Jimmy Two Shoes"); #starts the game faster
    #personaltest(); #certified fair and balanced: all levels ^_^

def personaltest(): #ctrl c to cancel
    #make the hero
    j=project.Hero("Jimbocles the Mighty", 23);
    #j.defence=j.defence+1;
    j.rankup();
    j.rankup();
    j.rankup();
    #j.add(project.Item(4, "Power"));
    j.add(project.Item(2, "Attack"));
    j.add(project.Item(3, "Defence"));
    #j.add(project.Item(4, "Utility"));
    # make and populate dungeon
    d=project.Dungeon(3, j); #3x3
    d.dungeon[0][1]="empty";
    d.dungeon[0][2]="empty";
    d.dungeon[1][0]=project.Monster(17);
    d.dungeon[1][1]=project.Monster(13);
    d.dungeon[1][2]="empty";
    d.dungeon[2][0]=project.Monster(17);#"empty";
    d.dungeon[2][1]=project.Monster(15)#"empty";
    # choose a boss monster to fight
    d.dungeon[2][2]=project.Monster(17);
    while (True):
        if (project.gameOver(j, d)==False):
            d.turn();
        else:
            if (project.playerWon(j)==False):
                print("\nYou lose lmao");
            else:
                print("\nCongratulations!");
            break;

if __name__ == "__main__":
    main();
