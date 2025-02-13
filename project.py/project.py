import random; #don't forget to use mypy for compiling

demon=False; #global variable, in case the player activates the demonic pact

def main(name=None, size=None): #params solely to be used by test_project.py
    print("Welcome to Dungeon Adventure. Your objective is to explore all of a monster-infested, grid-like dungeon without dying.");
    if (name is None):
        name=getInput("What is your name?", True);
    print("\nDungeon sizes range from 3x3 to 10x10. Larger dungeons are more challenging to explore.");
    if (size is None):
        size=getInput("How large would you like the dungeon to be? Choose 1 number for both the length and width.", False);
    while (size<3 or size>10):
        size=getInput("Invalid number. Type one number between 3 and 10.", False);
    #create the player character
    if (size<=6): #starting health
        php=5+(size*5);
    else:
        php=35;
    player=Hero(name, php);
    dungeon=Dungeon(size, player); #create the dungeon
    print("\nYou descend into the dungeon, bringing nothing with you but your wits and will to survive.");
    print("What will you do next? (Type 'h' at any time for a list of commands.)");
    while (True):
        if (gameOver(player, dungeon)==False):
            dungeon.turn();
        else:
            global demon;
            print(""); #always print new line, regardless of what the specific game end message is
            if (demon==True):
                if (playerWon(player)==True):
                    print("Congratulations! You made it out of the dungeon alive.");
                    print("But victory comes at a cost.");
                else:
                    print("Demons come swarming out of the shadows to claim your fallen form.");
                print("With your adventure over, your infernal benefactors have come to collect what they are owed.");
                print("You are dragged below the earth to join them in eternal damnation...");
            else:
                if (playerWon(player)==False):
                    print("Their will was stronger. You have fallen, but do not despair. You can always rise again and explore another dungeon.");
                else:
                    print("Congratulations! You made it out of the dungeon alive.");
                    print("If you dare, there is always another out there, waiting to be explored...");
            break;

def getInput(message: str, type: bool): #returns valid string (true) or int (false) input from user
    if (message is not None):
        answer=input(message+" ").strip();
    else:
        answer=input().strip();
    while (True):
        if (type==True): #answer should be string
            if (betterIsAlpha(answer)==True and len(answer)>0):
                if (len(answer)>25):
                    print("Your input is too long!");
                else:
                    return answer; #must be between 1 and 25 characters
            else:
                print("Invalid input. Make sure you don't include any punctuation or numbers.");
        elif (type==False): #answer should be an int
            try:
                typecast=int(answer);
            except ValueError:
                print("Invalid input. You need to type an integer.");
            else:
                return typecast;
        #if nothing valid was returned, get another input to check the validity of
        answer=input().strip();

def gameOver(h, d):
    return (h.dead==True or d.explored==True);

def playerWon(h): #can't lose while they're alive, but must be alive to win (by leaving dungeon) so this is always accurate
    return (h.dead==False);

def betterIsAlpha(word: str)->bool: #only has letters or spaces, since str.isalpha is not useful
    for char in word:
        if (char.isalpha()==False and char!=" "):
            return False;
    return True;

class Attack: #special attacks, for both monsters and players
    def __init__(self, n: str):
        self.name=n;
        self.usable=True;
        self.stolen=None; #for steal

    @property #property means getter
    def name(self)->str:
        return self._name;

    @name.setter
    def name(self, title: str):
        if (title in ["Bleed", "Heal", "Leech", "Parry", "Deflect", "Steal", "Seal", "Stun"]):
            self._name=title;
        else:
            raise ValueError("Failed to make special attack due to invalid name: "+title);

    @property #property means getter
    def usable(self)->bool:
        return self._usable;

    @usable.setter
    def usable(self, title: bool):
        if (title==False or title==True):
            self._usable=title;
        else:
            raise TypeError("Failed to convert special attack used: "+str(title)+" to a boolean value.");

    @property #property means getter
    def stolen(self):
        return self._stolen;

    @stolen.setter
    def stolen(self, item): #store stolen item so it can be retrieved by player after fight ends
        self._stolen=item; #item is stored, not used

    def use(self, user, target): #target is always the user's enemy
        if ("Sealed" in user.status):
            print(user.name+"'s "+self.name+" could not be used due to being Sealed!");
            return;
        elif (self.usable==False):
            print("You may only use your special attack once per fight!");
            return;
        else:
            if (self.name=="Heal"):
                print(user.name+" used "+self.name+"!");
            else:
                print(user.name+" used "+self.name+" on "+target.name+"!");
        match self.name:
            case "Bleed": #defence ignoring damage
                self.usable=False;
                if ("Deflected" in target.status):
                    print("Deflect protected "+target.name+"!");
                    target.status.remove("Deflected");
                elif ("Unique: Doll" in target.status):
                    print(target.name+"'s Voodoo Doll took effect!");
                    user.takedamage(7, target, True);
                else:
                    target.takedamage(7, user, True);
            case "Heal":
                self.usable=False;
                if ("Unique: Doll" in target.status):
                    print(target.name+"'s Voodoo Doll took effect!");
                    target.HPGain(8, "none");
                else:
                    user.HPGain(8, "none");
            case "Parry": #ignore next attack
                self.usable=False;
                if ("Unique: Doll" in target.status):
                    print(target.name+"'s Voodoo Doll took effect!");
                    target.status.append("Parried");
                else:
                    user.status.append("Parried");
            case "Deflect": #ignore next special attack
                self.usable=False;
                if ("Unique: Doll" in target.status):
                    print(target.name+"'s Voodoo Doll took effect!");
                    target.status.append("Deflected");
                else:
                    user.status.append("Deflected");
            case "Steal": #disable item; only usable by monsters (who can't have items), so target will always be hero
                self.usable=False;
                length=len(target.inventory);
                if ("Deflected" in target.status):
                    print("Deflect protected "+target.name+"!");
                    target.status.remove("Deflected");
                elif ("Unique: Doll" in target.status):
                    print(target.name+"'s Voodoo Doll took effect!");
                    print(user.name+" has no items to Steal.");
                elif (length>0):
                    if (self.stolen is not None): #originally stolen item is forever lost; this is a feature, not a bug
                        print("The greedy goblin throws your "+self.stolen.name+" into the darkness to be lost forever, setting its sights on something shinier!");
                    index=random.randint(0,length-1);
                    item=target.inventory[index];
                    target.drop(item, True);
                    self.stolen=item;
                else:
                    print(target.name+" has no items to Steal.");
            case "Seal": #disable special
                self.usable=False;
                if ("Deflected" in target.status):
                    print("Deflect protected "+target.name+"!");
                    target.status.remove("Deflected");
                elif ("Unique: Doll" in target.status):
                    print(target.name+"'s Voodoo Doll took effect!");
                    user.status.append("Sealed");
                else:
                    target.status.append("Sealed");
            case "Stun": #skip turn
                self.usable=False;
                if ("Deflected" in target.status):
                    print("Deflect protected "+target.name+"!");
                    target.status.remove("Deflected");
                elif ("Unique: Doll" in target.status):
                    print(target.name+"'s Voodoo Doll took effect!");
                    user.status.append("Stunned");
                else:
                    target.status.append("Stunned");
            case "Leech": #health steal
                self.usable=False;
                if ("Deflected" in target.status):
                    print("Deflect protected "+target.name+"!");
                    target.status.remove("Deflected");
                elif ("Unique: Doll" in target.status):
                    print(target.name+"'s Voodoo Doll took effect!");
                    user.takedamage(5, target, True);
                    target.HPGain(5, "none");
                else:
                    target.takedamage(5, user, True);
                    user.HPGain(5, "none");
            case _:
                raise ValueError("Failed to use special attack due to invalid name: "+self.name);

    def __str__(self):
        return self.name;

class Character: #abstract superclass for players and monsters; they have mostly the same basic attributes
    def __init__(self, name: str, hp: int, off: int, deff: int):
        self._status=[]; #empty list to hold status effects from special attacks
        self.name=name;
        self.health=hp;
        self.offence=off;
        self.defence=deff;
        self.special=None;

    @property #property means getter
    def status(self)->list: #no setter, just use add and remove
        return self._status;

    @property #property means getter
    def name(self)->str:
        return self._name;

    @name.setter
    def name(self, title: str):
        if (betterIsAlpha(title)==True):
            self._name=title;
        else:
            raise TypeError("Invalid name.");

    @property #property means getter
    def health(self)-> int:
        return self._health;

    @health.setter
    def health(self, hp: int):
        global demon;
        if (hp<0):
            self._health=0;
        elif ("Unique: Bloodblade" in self.status and hp>30): #item lowers max health
            print(self.name+" has already reached the max health limit!");
            self._health=30;
        elif (demon==False and hp>45): #max health
            print(self.name+" has already reached the max health limit!");
            self._health=45;
        else:
            self._health=hp;

    def HPGain (self, hp: int, bonus: str):
        if (bonus=="rank"):
            print("Your experience in combat allows you to recover from your wounds faster. Bonus +1 HP.");
            hp=hp+1;
        elif (bonus=="strength"):
            print("Your triumph over such a powerful foe fills you with the resolve to push onwards. Bonus +1 HP.");
            hp=hp+1;
        elif (bonus=="subsidy"):
            print("You feel a rush as you emerge victorious in spite of your inexperience. Bonus +2 HP.");
            hp=hp+2;
        print(self.name+" gained "+str(hp)+" HP!");
        if ("Unique: Ointment" in self.status):
            print(self.name+"'s Healing Ointment took effect! +1 HP.");
            self.health=self.health+hp+1;
        else:
            self.health=self.health+hp;

    @property #property means getter
    def dead(self)-> bool: #don't need a setter for this
        return (self.health==0);

    @property #property means getter
    def offence(self):
        return self._offence;

    @offence.setter
    def offence(self, pow):
        if (pow>1):
            self._offence=pow;
        else:
            self._offence=1; #minimum damage an attack can do, or else fights would never end

    @property #property means getter
    def defence(self):
        return self._defence;

    @defence.setter
    def defence(self, pow):
        self._defence=pow; #negative defence is just damage vuln

    @property #property means getter
    def special(self):
        return self._special;

    @special.setter
    def special(self, attack: Attack):
        self._special=attack;

    def attacked(self, dmg: int, special: bool, attacker):
        if (special==False and "Parried" in self.status): #can only parry normal attacks, not special ones like leech
            if (attacker is not None):
                if ("Deflected" in attacker.status): #deflect prevents all specials (except heal), including parry
                    print("Deflect protected "+attacker.name+" from being Parried!");
                    attacker.status.remove("Deflected");
                    self.status.remove("Parried");
                    self.takedamage(dmg, attacker, special);
                else:
                    print("Parry protected "+self.name+" from "+attacker.name+"'s attack!");
                    self.status.remove("Parried"); #consumed after use
            else: #arrow trap
                print("Parry protected "+self.name+"!");
                self.status.remove("Parried"); #consumed after use
        else:
            self.takedamage(dmg, attacker, special);
        #then activate certain items after being attacked
        if (attacker is not None and attacker.dead==False):
            if ("Unique: Mask" in attacker.status):
                print(attacker.name+" reduced "+self.name+"'s Defence by 1!");
                self.defence=self.defence-1;

    def takedamage(self, dmg: int, attacker, special: bool):
        if ("Vulnerable" in self.status and special==False): #bleed cannot benefit from vulnerable
            dmg+=(dmg//2); #50% more damage, done before defence, since bonus should be based purely on attacker offence
            print(self.name+"'s vulnerability was exploited!");
            self.status.remove("Vulnerable"); #applies to one attack only, just like finisher attacks' damage boost
        dmg-=self.defence;
        if (dmg<0):
            dmg=0; #no negative damage; attacks should never heal target
        if (attacker is not None):
            print(self.name+" took "+str(dmg)+" damage from "+attacker.name+"'s attack!");
        else: #arrow trap
            print(self.name+" took "+str(dmg)+" damage!");
        #then activate certain items after being attacked
        if (special==False and "Unique: Spike" in self.status and attacker is not None):
            print(attacker.name+" took 2 damage from "+self.name+"'s Spiked Shield!");
            attacker.health=attacker.health-2; #spike only triggers from normal attacks, not special attacks
        self.health=self.health-dmg;

    def __str__(self):
        return "\n"+self.name+": "+str(self.health)+" HP, "+str(self.offence)+" Attack, "+str(self.defence)+" Defence"+"\nSpecial Attack: "+str(self.special);

class Item: #items are only for players, and have 5 levels instead of 10 (one for every 2 levels of the dungeon)
    def __init__(self, level: int, t: str):
        if (t=="Attack"):
            self.type=t;
            match (level):
                case 1: self.name="Wooden Club";
                case 2: self.name="Iron Mace";
                case 3: self.name="Haunted Mask";
                case 4: self.name="War Hammer";
                #no level 5 attack for balancing reasons; player stats are too high at level 3
                case _:
                    raise ValueError("Failed to create item due to invalid level: "+str(level));
        elif (t=="Defence"):
            self.type=t;
            match (level):
                case 1: self.name="Healing Ointment";
                case 2: self.name="Berserker Helm";
                case 3: self.name="Spiked Shield";
                case 4: self.name="Leech Totem";
                #no level 5 defence for same reasons as above; other items are already sufficient
                case _:
                    raise ValueError("Failed to create item due to invalid level: "+str(level));
        elif (t=="Utility"):
            self.type=t;
            match (level):
                case 1: self.name="Crystal Ball"; #parry
                case 2: self.name="Teleportation Ring"; #deflect
                case 3: self.name="Smoke Bomb"; #stunner
                case 4: self.name="Throwing Knife"; #bleed
                case 5: self.name="Black Book"; #leech
                case _:
                    raise ValueError("Failed to create item due to invalid level: "+str(level));
        elif (t=="Power"):
            self.type=t;
            match (level): #enchanted sack is power for balancing reasons, so the player has to choose between
                # 1 power item and 1 other, or the sack and 1 of each other
                case 1: self.name="Bloodblade"; #monster kills grant hp but lower max hp
                case 2: self.name="Enchanted Sack"; #gain extra item slot, but lose attack
                case 3: self.name="Double Edged Sword"; #gain attack but lose def
                case 4: self.name="Voodoo Doll"; #reflect opponent special attack but lose def
                case 5: self.name="Demonic Pact"; #no more defence or items, but gain big hp/attack boost
                case _:
                    raise ValueError("Failed to create item due to invalid level: "+str(level));
        else:
            raise ValueError("Failed to create item due to invalid type: "+t);

    @property #property means getter
    def name(self)->str:
        return self._name;

    @name.setter
    def name(self, title: str):
        if (betterIsAlpha(title)==True):
            self._name=title;
        else:
            raise ValueError("Failed to make item due to invalid item name: "+title);

    @property #property means getter
    def type(self)->str:
        return self._type;

    @type.setter
    def type(self, title: str):
        if (betterIsAlpha(title)==True):
            self._type=title;
        else:
            raise ValueError("Failed to make item due to invalid type: "+title);

    def use(self, target): #target is the hero using the item
        match (self.name):
            #level 1 items
            case "Wooden Club":
                target.offence+=1;
            case "Healing Ointment":
                target.status.append("Unique: Ointment");
            case "Bloodblade":
                target.status.append("Unique: Bloodblade"); #target.defence=target.defence-1;
                if (target.health>30):
                    target.health=30;
            case "Crystal Ball":
                target.special=Attack("Parry");
            #level 2 items
            case "Iron Mace":
                target.offence+=2;
            case "Berserker Helm":
                target.status.append("Unique: Berserk");
            case "Enchanted Sack":
                target.capacity=target.capacity+2; target.status.append("Unique: Sack");
            case "Teleportation Ring":
                target.special=Attack("Deflect");
            #level 3 items
            case "Haunted Mask":
                target.status.append("Unique: Mask");
            case "Spiked Shield":
                target.status.append("Unique: Spike");
            case "Double Edged Sword":
                target.offence+=3; target.defence-=1;
            case "Smoke Bomb":
                target.special=Attack("Stun");
            #level 4 items
            case "War Hammer":
                target.status.append("Unique: Hammer");
            case "Leech Totem":
                target.status.append("Unique: Totem");
            case "Voodoo Doll":
                target.status.append("Unique: Doll"); target.defence=target.defence-1;
            case "Throwing Knife":
                target.special=Attack("Bleed");
            #level 5 items
            case "Black Book":
                target.special=Attack("Leech");
            case "Demonic Pact":
                global demon; demon=True;
                concurrentmod=[];
                for item in target.inventory:
                    concurrentmod.append(item);
                for item in concurrentmod:
                    target.drop(item, False);
                target.capacity=0;
                print(target.name+" lost "+str(target.defence)+" Defence!");
                print(target.name+" gained 35 HP!");
                print(target.name+" gained 5 Attack!");
                target.health=target.health+35; target.offence=target.offence+5; target.defence=0;
            case _:
                raise ValueError("Failed to use item due to invalid item name: "+self.name);

    def undo(self, target): #target is the hero losing the item
        match (self.name):
            #level 1 items
            case "Wooden Club":
                target.offence-=1;
            case "Healing Ointment":
                target.status.remove("Unique: Ointment");
            case "Bloodblade":
                target.status.remove("Unique: Bloodblade"); #target.defence=target.defence+1;
            case "Crystal Ball":
                target.special=None;
            #level 2 items
            case "Iron Mace":
                target.offence-=2;
            case "Berserker Helm":
                target.status.remove("Unique: Berserk");
            case "Enchanted Sack":
                if (len(target.inventory)>2):
                    print("\nWith the Enchanted Sack gone, you no longer have room for so many items. Choose one to discard.");
                    names=[]; ezg=1;
                    print("Which item do you want to remove? Type its number.");
                    for item in target.inventory:
                        print(str(ezg)+". "+item.name); names.append(item.name); ezg=ezg+1;
                    while (True):
                        response=getInput(None, False);
                        if (int(response)>0 and int(response)<=ezg):
                            break;
                    tor=None; #avoiding concurrent modification
                    ezg=0;
                    for item in target.inventory:
                        ezg=ezg+1;
                        if (ezg==response):
                            tor=item; break;
                    target.drop(tor, False);
                #undo effects after clearing inventory
                target.capacity=target.capacity-2; target.status.remove("Unique: Sack");
            case "Teleportation Ring":
                target.special=None;
            #level 3 items
            case "Haunted Mask":
                target.status.remove("Unique: Mask");
            case "Spiked Shield":
                target.status.remove("Unique: Spike");
            case "Double Edged Sword":
                target.offence-=3; target.defence+=1;
            case "Smoke Bomb":
                target.special=None;
            #level 4 items
            case "War Hammer":
                target.status.remove("Unique: Hammer");
            case "Leech Totem":
                target.status.remove("Unique: Totem");
            case "Voodoo Doll":
                target.status.remove("Unique: Doll"); target.defence=target.defence+1;
            case "Throwing Knife":
                target.special=None;
            #level 5 items
            case "Black Book":
                target.special=None;
            case "Demonic Pact":
                pass; #if used, it cannot be undone
            case _:
                raise ValueError("Failed to undo item due to invalid item name: "+self.name);

    def getDesc(self)->str:
        desc="";
        match (self.name):
            #level 1 items
            case "Wooden Club":
                desc="Increase Attack by 1.";
            case "Healing Ointment":
                desc="You gain +1 HP from all sources.";
            case "Bloodblade":
                desc="On kill, gain 6 HP. Your HP cannot exceed 30." #equal to twice the slain monster's Attack + Defence.";
            case "Crystal Ball":
                desc="Gain Special Attack: Parry.";
            #level 2 items
            case "Iron Mace":
                desc="Increase Attack by 2.";
            case "Berserker Helm":
                desc="When attacked, increase Attack by 1. Resets on kill.";
            case "Enchanted Sack":
                desc="Gain two additional item slots. Lose 1 Attack while you have 4 items.";
            case "Teleportation Ring":
                desc="Gain Special Attack: Deflect.";
            #level 3 items
            case "Haunted Mask":
                desc="On attack, reduce your opponent's Defence by 1.";
            case "Spiked Shield":
                desc="Deal 2 Defence ignoring damage when attacked.";
            case "Double Edged Sword":
                desc="Lose 1 Defence. Increase Attack by 3.";
            case "Smoke Bomb":
                desc="Gain Special Attack: Stun.";
            #level 4 items
            case "War Hammer":
                desc="Finishers now do +150% damage instead of +50%.";
            case "Leech Totem":
                desc="After performing a finisher, you gain 2 HP. No longer gain bonus healing from fights.";
            case "Voodoo Doll":
                desc="Lose 1 Defence. When your enemy uses a special attack, you benefit from it instead of them.";
            case "Throwing Knife":
                desc="Gain Special Attack: Bleed.";
            #level 5 items
            case "Black Book":
                desc="Gain Special Attack: Leech.";
            case "Demonic Pact":
                desc="Lose all Defence and the ability to equip items in exchange for greatly increased HP and Attack.";
            case _:
                raise ValueError("Failed to use item due to invalid name: "+self.name);
        return desc;

    def __str__(self):
        return self.name+": "+self.getDesc()+" "+self.type+" item.";

class Hero(Character): #the player
    def __init__(self, name: str, h: int): #players always have the same starting stats
        super().__init__(name, h, 2, 0); #sets self.special to None
        self._rank=0; #level, but renamed to avoid confusion with dungeon/item/monster level, which is separate system
        self.XP=0;
        self.capacity=2; #players can have two items maximum by default
        self._inventory=[]; #empty list to hold player items

    @property #getter; has no setter since it's only increased by xp gain
    def rank(self)->int:
        return self._rank;

    def rankup(self):
    #3x3,4x4 is r0; (maybe 4 boss) 5x5 and 6x6 and 7x7 is r1; (maybe 7 boss) 8x8 and 9x9 is r2; (maybe 9 boss) 10x10 is r3
        oldie=self._rank;
        print("\n"+self.name+" leveled up!");
        if (oldie==0): #0 to 1 is just def boost
            self._rank=1;
            print(self.name+"'s Defence increased by 1!");
            self.defence=self.defence+1;
        elif (oldie==1): #1 to 2 is off and def boost
            self._rank=2;
            print(self.name+"'s Attack increased by 1!");
            self.offence=self.offence+1;
            print(self.name+"'s Defence increased by 1!");
            self.defence=self.defence+1;
        elif(oldie==2): #2 to 3 is just attack boost
            self._rank=3;
            print(self.name+"'s Attack increased by 1!");
            self.offence=self.offence+1;

    @property #getter
    def XP(self)->int:
        return self._XP;

    @XP.setter
    def XP (self, number: int): #gain 1 XP for each monster kill; 3 ranks total
        if (number<0):
            raise ValueError("Player XP cannot be negative.");
        else:
            self._XP=number;
        #check if enough XP to rank up
        if (self._rank==0 and self._XP==7):
            self.rankup();
            self._XP=0;
        elif (self._rank==1 and self._XP==9):
            self.rankup();
            self._XP=0;
        elif (self._rank==2 and self._XP==11):
            self.rankup();
            self._XP=0;

    @property #property means getter
    def capacity(self)->int:
        return self._capacity;

    @capacity.setter
    def capacity(self, num: int):
        if (num>=0): #no negative item slots
            self._capacity=num;
        else:
            raise ValueError("Player inventory capacity cannot be negative.");

    @property #property means getter
    def inventory(self):
        return self._inventory;

    @inventory.setter
    def inventory(self, thing): #only used to blank inventory for demonic pact; otherwise just use drop/add methods below
        if (isinstance(thing, list)):
            self._inventory=thing;
        else:
            raise TypeError("Player inventory must be a list.");

    def add(self, item: Item)->bool: #returns whether add was successful or not
        if (item.name!="Demonic Pact"): #deletes inventory, so ignore capacity/item types
            if (len(self.inventory)<self.capacity):
                for i in self.inventory:
                    if (i.type==item.type):
                        print("You cannot add that item. You may only have one item of each type!");
                        return False;
                self.inventory.append(item);
                item.use(self);
                print(self.name+" has equipped a(n) "+item.name+".");
                if ("Unique: Sack" in self.status and len(self.inventory)>3): #gained 4th item
                    print("Your shoulders sag under the weight of so many items. -1 Attack.");
                    self.offence=self.offence-1;
                return True;
            else:
                global demon;
                if (demon==True):
                    print("The pact may not be broken. You have made your choice.");
                else:
                    print("\nYou cannot add that item. Your inventory is already full!");
                return False;
        else:
            print(self.name+" has accepted the Demonic Pact. Actions have consequences...");
            item.use(self);
            return True;

    def drop(self, item: Item, stolen: bool):
        if (item in self.inventory):
            if (stolen==True):
                print("Goblin stole "+self.name+"'s "+item.name+"!")
            else:
                print(self.name+" removed "+item.name+" from their inventory.");
            if ("Unique: Sack" in self.status and len(self.inventory)>3): #losing 4th item
                print("With the extra item gone, you can feel a weight lifted off your shoulders. +1 Attack.");
                self.offence=self.offence+1;
            self.inventory.remove(item);
            item.undo(self);

    def __str__(self):
        appendage="\nItems (maximum of "+str(self.capacity)+"): ";
        if (len(self.inventory)>0):
            num=1;
            for item in self.inventory:
                appendage+="\n"+str(num)+". "+str(item);
                num+=1;
        else:
            appendage+="None.";
        status="\nLevel: "+str(self._rank)+"/3";
        progress="\nXP: "+str(self.XP);
        match (self._rank):
            case 0: progress=progress+"/7";
            case 1: progress=progress+"/9";
            case 2: progress=progress+"/11";
            case 3: pass; #the max, so any xp gained is just for show
            case _: raise AttributeError("Player's rank is invalid: "+str(self._rank));
        return super().__str__()+status+progress+appendage;

class Monster(Character):
    def __init__(self, level: int): #9 monsters of increasing strength for hero to fight
        match level: #level is based on size of dungeon; bigger dungeons spawn stronger monsters
            #hero has item level 1 (dungeon levels 1-3)
            case (1|2|3):
                match (random.randint(1,2)): #first three levels have equal chance of spawning zombies or ghouls
                    case 1:
                        super().__init__("Zombie", 5, 2, 1); #has no special attack
                    case 2:
                        super().__init__("Ghoul", 10, 3, 0); #still has no special attack
                    case _:
                        raise ValueError("Randint failed in monster constructor. Invalid level was: "+str(level));
            #hero has item level 2 (dungeon levels 4-7)
            case (4|5):
                super().__init__("Goblin", 15, 2, 0); #3x3 boss
                self.special=Attack("Steal");
            case (6|7):
                super().__init__("Witch", 15, 3, 0); #4x4 boss
                self.special=Attack("Seal");
            #hero has item level 3 (dungeon levels 8-11)
            case (8|9):
                super().__init__("Minotaur", 20, 4, 0); #5x5 boss
                self.special=Attack("Deflect");
            case (10|11):
                super().__init__("Gargoyle", 20, 4, 0); #6x6 boss
                self.special=Attack("Parry");
            #hero has item level 4 (dungeon levels 12-15)
            case (12|13):
                super().__init__("Vampire", 15, 5, 0); #7x7 boss
                self.special=Attack("Heal");
            case (14|15):
                super().__init__("Werewolf", 20, 4, 1); #8x8 boss
                self.special=Attack("Bleed");
            #hero has item level 5 (dungeon levels 16-18)
            case (16|17):
                super().__init__("Fallen Hero", 20, 5, 1); #9x9 boss
                self.special=Attack("Stun");
            case 18: #only spawns as final boss of 10x10 due to high stats
                super().__init__("Mirror Image", 1, 0, 0);
                #stats and special attack are set when encountered by player
            case _:
                raise ValueError("Failed to make Monster due to unrecognised level: "+str(level));

    def __str__(self):
        return "\nEnemy status:"+super().__str__();

class Dungeon: #constructor should work properly now; tested hundreds of times without error
    def __init__(self, size: int, p: Hero):
        self.dungeon=[["null"]*size for _ in range(size)]; #dungeon is a 2d array, aka a list of lists
        self.player=p;
        self.pp=[0,0]; #player position
        #level measures both distance from the start (which is always 0,0), and difficulty
        #row index + column index is always the distance from 0,0 to [row index][column index]
        #e.g. in a 4x4 grid, the last square is at 3,3, and is always a minimum of 6 moves away from the start
        #this is because only orthogonal movement is allowed; therefore the final square in a 4x4 grid is level 6
        #the current level is always found via 'level=i+j', where i and j are coordinates dungeon[i][j]; e.g. 3+3 is 6
        #the number of levels always equals the dungeon's (size-1)*2, e.g. a 4x4 (size is 4) goes up to level 6
        #level matters for balancing reasons, so the difficulty increases gradually and consistently
        #the dungeon is randomly generated, but always meets three conditions
        self.idone=[False]*(size-1+size-1); #each level needs at least one item appropriate for that level
        self.mdone=[False]*(size-1+size-1); #each level needs at least one monster appropriate for that level
        #finally, the last square in the dungeon should always be a monster to serve as a final boss
        #since there's only one spot of the max level in every dungeon, idone must be marked to avoid infinite looping
        self.idone[(size-1+size-1)-1]=True;
        #loop through each level to guarantee the above conditions
        for lev in range(1, (size-1)+(size-1)+1, 1): #plus one to ensure final level is made because range is exclusive
            while (True): #choose two random spots in that level to hold a monster and item
                #randints ranges both avoid errors and ensure efficiency by only generating ints in the level's range
                if (lev==1): #only two spots are 0,1 and 1,0
                    index1=random.randint(0, 1);
                elif (lev<size): #starts at 1 to avoid index errors like 0,4 when size is 4
                    index1=random.randint(0,lev-1);
                elif(lev==(size-1)+(size-1)): #final level in dungeon always has doubled coordinate like 4,4 or 9,9
                    index1=size-1;
                elif (lev>=size): #to avoid index errors like 1,5 when size is 4
                    index1=random.randint(1+(lev-size),size-1);
                #since level always equals index1+index2
                #so in order to generate something for the current level, index1+index2 must equal it
                index2=abs(lev-index1);
                #print("Trying for level: "+str(lev));
                #print(str(index1)+", "+str(index2));
                #if (self.dungeon[index1][index2]!="null"):
                    #print("Spot occupied by: "+str(self.dungeon[index1][index2]));
                #if statement ensures level of index is correct and item and monster don't overwrite each other
                if (index1+index2==lev and self.dungeon[index1][index2]=="null"):
                    if (self.idone[lev-1]==False):
                        self.idone[lev-1]=True;
                        self.dungeon[index1][index2]=self.makeItem(lev);
                        #print("Made item for level: "+str(lev));
                    elif (self.mdone[lev-1]==False):
                        self.mdone[lev-1]=True;
                        self.dungeon[index1][index2]=Monster(lev);
                        #print("Made monster for level: "+str(lev));
                        #print("Done with level: "+str(lev));
                        break; #done with the level, since monsters are made after items
                elif (self.idone[lev-1]==True and self.mdone[lev-1]==True):
                    #print("Done with level: "+str(lev));
                    break; #done with this level
        #once done, randomly fill out the rest of the dungeon
        for r in range(size):
            for c in range(size):
                if (self.dungeon[r][c]=="null"): #do not overwrite already filled spots
                    self.dungeon[r][c]=self.makeEvent(r+c);

    def makeEvent(self, level: int): #in addition to enemies and items, the dungeon has empty spaces, traps, and boosts
        end=(len(self.dungeon[0])-1)*2; #last level in dungeon; if size is 5x5, last spot is 4,4, so (5-1)*2=8=4+4
        #print("Level: "+str(level)+" last level is "+str(end))
        match (level):
            case 0: #player always starts at 0,0
                return self.player.name; #just the player's name, to be used as a location marker
            case _ if level==end:
                return Monster(level); #the very last spot should always be a strong enemy, to act as the final boss
            case _ : #all other spaces are randomly generated
                gamble=random.randint(0,3);
                if (gamble==0): #free space
                    return "Empty"; #uppercase so it shows as ? in tostring; lowercase empty is spot player visited
                elif (gamble==1): #spawn monster
                    return Monster(level);
                elif (gamble==2): #spawn item
                    return self.makeItem(level);
                elif (gamble==3): #random event
                    match (random.randint(0,4)):
                        case (0|1|2):
                            return "Event: campfire"; #health gain
                        case (3):
                            return "Event: arrow trap"; #health loss
                        case (4):
                            return "Event: mysterious potion"; #permanently gain or lose attack, health, or defence
                else:
                    raise ValueError("Randint isn't working properly for event creation.");

    def makeItem(self, Level: int)->Item: #returns randomly generated item based on given level
        if (1<=Level<=3): #items only have 5 levels, but dungeon has 18
            Level=1;
        elif (4<=Level<=7):
            Level=2;
        elif (8<=Level<=11):
            Level=3;
        elif (12<=Level<=15):
            Level=4;
        elif (16<=Level<=18):
            Level=5;
        else:
            raise ValueError("Failed to make Item due to unrecognised level: "+str(Level));
        if (Level==1): #crystal ball has lower drop rate since it's least useful at this level
            if (len(self.dungeon)<5): #bloodblade is overpowered in 3x3 and 4x4, so it will never spawn
                rando=random.randint(20,22);
            else: #5x5 and bigger, crystal ball is underpowered, so lower its drop rate so player can get more useful items and not die
                rando=random.randint(10,16); #lower crystal ball drop rate to ~14% and increase other drop rates to ~29%
        elif(Level==5): #there's only 2 level 5 items (for balancing reasons)
            rando=random.randint(50,51);
        else: #equal drop rates after above problem fixed; 25% for each item
            rando=random.randint(1,4);
        match (rando):
            case (1|10|11|20):
                return Item(Level, "Attack");
            case (2|12|13|21):
                return Item(Level, "Defence");
            case (3|14|22|50):
                return Item(Level, "Utility");
            case (4|15|16|51):
                return Item(Level, "Power");
            case _:
                raise ValueError("Randint isn't working properly for item creation. Invalid int: "+str(rando));

    @property #property means getter
    def dungeon(self):
        return self._dungeon;

    @dungeon.setter
    def dungeon(self, list):
        self._dungeon=list;

    @property #property means getter
    def player(self)->Hero:
        return self._player;

    @player.setter
    def player(self, hero: Hero):
        if (isinstance(hero, Hero)):
            self._player=hero;

    @property #property means getter
    def pp(self):
        return self._pp;

    @pp.setter
    def pp(self, l):
        if (isinstance(l, list)):
            self._pp=l;
        else:
            raise ValueError(str(l)+" is not a valid player coordinate.");

    @property #property means getter
    def explored(self)->bool: #if all spaces are empty, then the dungeon has been fully explored
        for r in range(len(self.dungeon[0])):
            for c in range(len(self.dungeon[0])):
                if (self.dungeon[r][c]!="empty" and self.dungeon[r][c]!=self.player.name):
                    return False;
        return True;

    def turn(self): #take turn and then return to main to check win condition
        print(self);
        pr=""; do=False;
        while (pr in ["a", "f", "s", "m", "h", "i", "k"]==False or do==False):
            pr=getInput(None, True).lower();
            do=self.parsePR(pr, None);
            if (do==False):
                print(self);
        return;

    def parsePR(self, pr: str, monster: Monster)->bool: #pr is player response; all valid ones handled here
        match (pr): #return true only if player takes turn; 'free actions' don't end turn after use
            case "a":
                if (monster==None): #out of combat
                    print("You swing wildly, hitting only the air in front of you. There are no monsters here...yet.");
                    return False;
                else:
                    print(""); #new line
                    monster.attacked(self.player.offence, False, self.player);
                    return True;
            case "s":
                if (self.player.special is None):
                    print("You have no special attack to use.");
                else:
                    if (monster==None): #out of combat
                        print("You must save your special attack for when the time is right. Such power is not to be squandered.");
                    else:
                        self.player.special.use(self.player, monster);
                return False;
            case "f":
                if (monster==None): #out of combat
                    print("You nearly lose a limb from attempting such a brutal attack with no target. Perhaps you should be more careful in the future.");
                    return False;
                else:
                    print(""); #new line
                    if ("Unique: Hammer" in self.player.status):
                        monster.attacked((self.player.offence*2)+(self.player.offence//2), False, self.player);
                    else:
                        monster.attacked(self.player.offence+(self.player.offence//2), False, self.player);
                    if (self.player.dead==False and "Unique: Totem" in self.player.status):
                        self.player.HPGain(2, "none");
                    print(self.player.name+" has become vulnerable!");
                    self.player.status.append("Vulnerable");
                    return True;
            case "m":
                if (monster==None):
                    self.move();
                    return True;
                else:
                    print("You cannot turn your back upon an enemy! You are both in this to the bitter end.");
                    return False;
            case "h":
                print("a: Attack your opponent.");
                print("f: Use a finisher attacker, doing 50% bonus damage, but making your enemy's next attack do 50% bonus damage to you.");
                print("s: Use your special attack, if you have one.");
                print("m: Move through the dungeon.");
                print("h: Display this list of commands.");
                print("i: Check your inventory and stats.");
                print("k: Explanation of special attacks.");
                return False;
            case "i":
                print(self.player);
                return False;
            case "k":
                print("Special attacks are gained by equipping utility items, though some can only be used by monsters.");
                print("Using a special attack does not prevent you from attacking, but it may only be used once per fight.");
                print("The special attacks are:");
                print("Bleed: Your opponent takes 7 damage.");
                print("Deflect: Your opponent's next special attack has no effect on you.");
                print("Heal: Gain 8 HP.");
                print("Leech: Your opponent takes 5 damage and you gain 5 HP.");
                print("Parry: Your opponent's next attack has no effect on you.");
                print("Seal: Your opponent cannot use their special attack for the rest of the fight.");
                print("Steal: Your opponent loses a random item until the end of the fight.");
                print("Stun: Your opponent skips their next turn.");
                return False;
            case _:
                print("Invalid command");
                return False;

    def move (self):
        r=getInput("Which way will you venture? Left, right, up, or down?", True).lower();
        while (True):
            while (r not in ["left", "right", "up", "down"]):
                r=getInput("Invalid response.", True).lower();
            coord=self.getCoords(r);
            try:
                event=self.dungeon[coord[0]][coord[1]];
            except IndexError:
                print("You cannot move that way! You are already at the dungeon's boundary.");
                r=getInput(None, True).lower();
            else:
                if (coord[0]<0 or coord[1]<0): #apparently negative indexes are valid, but I don't like that
                    print("You cannot move that way! You are already at the dungeon's boundary.");
                    r=getInput(None, True).lower();
                else:
                    self.dungeon[self.pp[0]][self.pp[1]]="empty"; #player's old location becomes empty
                    self.dungeon[coord[0]][coord[1]]=self.player.name; #player saved to new location
                    self.pp=coord; #and coords of new location saved
                    #then trigger event
                    print(""); #new line regardless of event
                    if (isinstance(event, Monster)):
                        self.battle(event);
                    elif (isinstance(event, Item)):
                        self.itemDrop(event, False);
                    elif(event[:5]=="Event"):
                        self.triggerEvent(event);
                    else:
                        print("There is nothing here. You are safe, for now...");
                    break;

    def getCoords(self, direction: str):
        match (direction): #row and then column
            case "left":
                c1=self.pp[0]; c2=int(self.pp[1])-1;
                return [c1,c2];
            case "right":
                c1=self.pp[0]; c2=int(self.pp[1])+1;
                return [c1,c2];
            case "up": #0,0 is top left corner
                c1=int(self.pp[0])-1; c2=self.pp[1];
                return [c1,c2];
            case "down":
                c1=int(self.pp[0])+1; c2=self.pp[1];
                return [c1,c2];

    def triggerEvent(self, event: str):
        match (event[7:]):
            case "campfire":
                print("You discover the remains of a campsite left behind by another adventurer. An old pack of rations allows you to recover your strength.");
                self.player.HPGain(5, "none");
            case "arrow trap":
                print("You trigger an old booby trap, unleashing a hail of arrows upon you!");
                self.player.attacked(6, False, None);
            case "mysterious potion":
                ans=getInput("You discover a mysterious vial of faintly glowing liquid. Do you dare drink it?", True).lower();
                while (ans not in ["yes", "no"]):
                    ans=getInput("This question requires a 'yes' or 'no' response, adventurer.", True).lower();
                if (ans=="no"):
                    print("You decide not to risk it, and leave the vial where you found it.");
                    return;
                else:
                    print("Bold choice, adventurer...");
                    match (random.randint(0,5)):
                        case 0: #gain hp
                            print("The vial turns out to be an old healing potion, yet is still highly effective.");
                            self.player.HPGain(10, "none");
                        case 1: #lose hp
                            print("But the vial was discarded for a reason. It turns out to be a defective healing potion, and makes you sick.");
                            self.player.health=self.player.health-5;
                        case 2: #gain strength/attack
                            print("After drinking the vial, your equipment suddenly feels lighter. You permanently gain +1 Attack.");
                            self.player.offence=self.player.offence+1;
                        case 3: #lose strength/attack
                            print("After drinking the vial, your equipment suddenly feels heavier. You permanently lose 1 Attack.");
                            self.player.offence=self.player.offence-1;
                        case 4: #gain focus/defence
                            print("The vial grants you a sudden burst of focus that never fully fades. You permanently gain 1 Defence.");
                            self.player.defence=self.player.defence+1;
                        case 5: #lose focus/defence
                            print("The vial grants you a sudden splitting headache that never fully fades. You permanently lose 1 Defence.");
                            self.player.defence=self.player.defence-1;

    def itemDrop(self, item: Item, stolen: bool):
        if (stolen==False):
            print("You discover something left behind by another adventurer, a(n) "+str(item));
        else:
            print("Additionally, your stolen "+item.name+" falls to the floor.");
        ans=getInput("Do you want to equip it?", True).lower();
        while (ans not in ["yes", "no"]):
            ans=getInput("This question requires a 'yes' or 'no' response, adventurer.", True).lower();
        if (ans=="yes"):
            global demon; #player wanted to equip new item but couldn't bc either it's duplicate or inventory full (not bc pact)
            if (self.player.add(item)==False and demon==False):
                print("Do you want to remove one of your items so you can add this one? Your items are: ");
                for it in self.player.inventory:
                    print(str(it));
                ans=getInput(None, True).lower();
                while (ans not in ["yes", "no"]):
                    ans=getInput("This question requires a 'yes' or 'no' response, adventurer.", True).lower();
                if (ans=="no"):
                    print("You leave the item behind for another adventurer to find.");
                else: #player is willing to remove an item
                    dupe=None; #see if player wants to equip an item of the type they already have
                    counter=1;
                    for it in self.player.inventory:
                        if (it.type==item.type):
                            dupe=it; break;
                        counter=counter+1; #keep track of dupe's index in player inventory
                    if (dupe is not None): #if so, ask to directly remove it
                        print("\nYou may only have one item of each type!");
                        ans=getInput("Remove your "+dupe.name+" so you can equip the "+item.name+"?", True);
                        while (ans not in ["yes", "no"]):
                            ans=getInput("This question requires a 'yes' or 'no' response, adventurer.", True).lower();
                        if (ans=="yes"):
                            self.player.drop(self.player.inventory[counter-1], False);
                            #to fix having full inventory when trying to replace sack with different power item
                            if (dupe.name=="Enchanted Sack" and len(self.player.inventory)>1):
                                print("\nWith the Enchanted Sack gone, you no longer have room for so many items. Choose one to discard.");
                                print("Which item do you want to remove? Type its number.");
                                counter=1;
                                numbers=[];
                                for it in self.player.inventory:
                                    print(str(counter)+". "+str(it));
                                    numbers.append(counter);
                                    counter+=1;
                                ans=getInput(None, False);
                                while (ans not in numbers):
                                    ans=getInput(None, False);
                                self.player.drop(self.player.inventory[ans-1], False);
                            self.player.add(item);
                        else:
                            print("You leave the item behind for another adventurer to find.");
                    else: #if not, they choose what to remove
                        print("\nWhich item do you want to remove? Type its number.");
                        counter=1;
                        numbers=[];
                        for it in self.player.inventory:
                            print(str(counter)+". "+str(it));
                            numbers.append(counter);
                            counter+=1;
                        ans=getInput(None, False);
                        while (ans not in numbers):
                            ans=getInput(None, False);
                        self.player.drop(self.player.inventory[ans-1], False);
                        self.player.add(item);
        else:
            print("You leave the item behind for another adventurer to find.");

    def battle(self, foe: Monster):
        #hero special attacks are used once per fight, but monsters can use them multiple times in fight
        #using special attacks does not cost a turn
        if (self.pp[0]==self.pp[1] and self.pp[0]==len(self.dungeon[0])-1): #last square in dungeon
            print("You've reached the end of the dungeon, but a monster stands in your way!");
            if (self.pp[0]==9): #9,9 is final square in 10x10, and is only one that contains mirror image
                print("As you conquer the foe, so you conquer yourself...");
                # as name suggests, mirror image copies player stats
                foe.health=self.player.health;
                if (foe.health>45): #but still has max health limit like player does
                    foe._health=45; #ensures demonic pact players can still win if they have enough health
                foe.offence=self.player.offence;
                foe.defence=self.player.defence;
                if (self.player.special is not None):
                    foe.special=Attack(self.player.special.name);
            if (foe.name!="Goblin"): #all other bosses get boosted stats; goblin boss in 3x3 is strong enough as is
                foe.offence=foe.offence+1;
                foe.defence=foe.defence+1;
        else:
            print("You encounter a monster! Prepare for battle!");
        print("The first move, as always, is yours.");
        turns=1; buff=0;
        while (self.player.dead==False and foe.dead==False):
            print(foe);
            if ("Stunned" not in self.player.status): #player always goes first
                good=False;
                while (good==False): #only end turn after player attacks
                    res=getInput(None, True).lower();
                    if (res in ["a", "f", "s", "m", "h", "i", "k"]):
                        good=self.parsePR(res, foe);
                    if (good==False):
                        print(foe);
            else:
                print("\nStill Stunned from your enemy's last attack, you are unable to attack!");
                self.player.status.remove("Stunned");
            if (foe.dead==False): #then enemy turn
                if ("Stunned" not in foe.status):
                    if (foe.special is not None and foe.special.usable==True):
                        foe.special.use(foe, self.player);
                    self.player.attacked(foe.offence, False, foe);
                    if (self.player.dead==False and "Unique: Berserk" in self.player.status):
                        buff=buff+1;
                        self.player.offence=self.player.offence+1;
                        print(self.player.name+" had their Attack increased by 1!");
                    if (turns%4==0 and foe.special is not None and foe.special.usable==False):
                        foe.special.usable=True; #can use special first turn, and then every fourth turn
                else:
                    print(foe.name+" skips its turn due to being Stunned!");
                    foe.status.remove("Stunned");
            turns+=1;
        if (foe.dead==True and self.player.dead==False):
            print(foe.name+" has died.");
            #totem healing + bonus is too strong; effectively prevents any health loss, which trivialises the game
            if (self.pp[0]+self.pp[1]>13 and "Unique: Totem" not in self.player.status): #fighting a werewolf or stronger
                bonus="strength"; #6 hp because werewolf/fallen hero do a little too much dmg
            elif (self.player.rank==3 and "Unique: Totem" not in self.player.status):
                bonus="rank"; #6 hp at level 3 to mitigate large hp loss over time in bigger dungeons
            elif (self.pp[0]+self.pp[1]>9 and self.player.rank<2 and "Unique: Totem" not in self.player.status):
                bonus="subsidy"; #7 hp; players lose too much health if fighting gargoyles or stronger at low levels
            else:
                bonus="none"; #default 5 hp recovery after kill
            print("\nWith your enemy slain, you recall what you've learned from the fight while your wounds slowly heal. +1 XP.");
            self.player.HPGain(5, bonus);
            self.player.XP=self.player.XP+1;
            if (buff>0):
                print("Your berserker rage has been sated. -"+str(buff)+" Attack.");
            self.player.offence=self.player.offence-buff;
            if ("Unique: Bloodblade" in self.player.status):
                vamp=6;
                #if (foe.defence<0): #haunted mask
                    #vamp=2*(foe.offence);
                #else:
                    #vamp=2*(foe.offence+foe.defence);
                print("\nYour Bloodblade emits a scarlet glow at your foe's defeat.");
                self.player.HPGain(vamp, "none");
            #also return stolen item and reset status
            if (foe.special is not None and foe.special.stolen is not None):
                self.itemDrop(foe.special.stolen, True);
            if (self.player.special is not None):
                self.player.special.usable=True;
            boogaloo=[];
            for thing in self.player.status: #non-unique status effects (e.g. parry) don't persist across fights
                if (thing[:6]!="Unique"):
                    boogaloo.append(thing);
            for thing in boogaloo:
                self.player.status.remove(thing); #remove them all, avoiding concurrent mod exception
        else:
            print("You have died.");

    def __str__(self): #visual representation of dungeon
        text="";
        print("\nDungeon progress:");
        for r in range(len(self.dungeon[0])):
            for c in range(len(self.dungeon[0])):
                if (self.dungeon[r][c]=="empty"):
                    text+=". "; #explored space
                elif(self.dungeon[r][c]==self.player.name):
                    text+="H ";
                #elif(isinstance(self.dungeon[r][c], Item)): #to check for fair distribution when debugging
                    #text+="I ";
                #elif(isinstance(self.dungeon[r][c], Monster)):
                    #text+="M ";
                #elif("Event" in self.dungeon[r][c]):
                    #text+="E ";
                else:
                    text+="? "; #unexplored space
            text=text+"\n";
        return text;

if __name__ == "__main__":
    main();
