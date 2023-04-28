from textwrap import fill
import time
from images import*
character_array = ["The Mage", "The Knight", "Generic Dude"]
mage_actions = ["Run", "Fireball", "Beat with Stick", "Call Dragon Slayer"]
knight_actions = ["Run", "Slash", "Remove Helmet", "Call Dragon Slayer"]
generic_dude_actions = ["Run", "Punch", "Serenade", "Release Donkey"]
user_input = "\n> "
general_intro = "Congratulations! The King has selected you to go on a quest to slay a mighty dragon! " \
                "What class will you choose? "
choose_character = "\nChoose your character (Enter corresponding number):" \
                   "\n\t1. The Mage\n\t2. The Knight\n\t3. Generic Dude"
farm_intro = "The sun shines hard against your back as you work, picking the weeds from the base of your field. " \
             "It's hard work, but work you’ve grown accustomed to, enough to even find some joy in its simplicity. " \
             "You know what the next day will bring, and that gives you a sense of blissful security. The only worry " \
             "that plagues you is the harvest, which depending on the weather, can be bountiful or completely " \
             "obismisal. Last harvest was modest, and the thought of empty pockets gnaws at the back of your mind. " \
             "Suddenly, the sound of hooves beats echoes in the distance, pulling you from your thoughts. You fear " \
             "for the worst, the tax collector, though you’re surprised to see a lone knight upon a decorated steed. " \
             "He bends towards you, offering a single letter addressed to you. With trepidation, you open the letter " \
             "and find that you have been summoned to the castle for mandatory royal service. Your heart sinks as " \
             "you read your assignment: to slay the spine-chilling dragon deep within Skull Cavern. Do you accept" \
             " the king's wishes?"
castle_intro = "While wandering the great marketplace, looking for interesting artifacts and delectable food to fill " \
               "your basket, you’re approached by a knight, barring a single letter addressed to you. Written inside" \
               " an invitation to meet with the king to discuss an urgent matter is written. A matter that takes " \
               "both bravery and skill inorder to complete, but which is not detailed out in the letter. Although " \
               "not all is shrouded in mystery, promised is both fame and wealth, something that you are in " \
               "desperate need of. You take the letter, sparred on by  dreams of rewards, and make haste the caste " \
               "gates. As you approach the towering castle gates, you feel a sense of awe and reverence for the " \
               "grandeur of the structure before you. The gates themselves are immense, made of solid iron, and " \
               "guarded by stern-faced knights dressed in full regalia. You present your invitation to the guards, " \
               "who nod in recognition and swing open the gates, allowing you passage into the castle's inner " \
               "courtyard. You make your way through the bustling courtyard, following the directions given to you " \
               "by the guards. The path leads you through a series of elaborately decorated halls and corridors, " \
               "each more ornate than the last. Finally, you arrive at the throne room, where the king sits upon a " \
               "magnificent throne of gold and jewels. I, the king, come to you with grave news. You have been " \
               "chosen for this great quest, for only you have the courage and strength to face this perilous foe. " \
               "The dragon is cunning and powerful, and its icy breath can freeze a man solid in an instant. " \
               "Nevertheless, I believe in you, and I trust that you will do all that is necessary to protect " \
               "our realm from this dangerous threat. Will you accept this challenge and become the hero that our " \
               "kingdom needs?"
accept_deny = "\n\t1. Accept\n\t2. Deny"


# Formats all the text the same length
def format_text(sentences):
    sentences = str(fill(sentences, 150))
    print(sentences)
    # for char in sentences:
    #     print(char, end="")
    #     time.sleep(.03)
    # print("\n")


# Function to call when character dies but takes potion into consideration
def death(potion):
    cave_decision = -1
    if potion:
        text = "Right before you take your dying breath you remember you have a health potion in your inventory. "
        format_text(text)
        while cave_decision != "1" and cave_decision != "2":
            cave_decision = input("Would you like to use it?\n\t1.  Yes\n\t2. No" + user_input)
        cave_decision = int(cave_decision)
        if cave_decision == 1:
            print("Your health has been replenished.")
        else:
            print("YOU DIED!")
            death_img()
    else:
        death_img()


# Running away always leads to death
def run_away():
    text = "Unable to master the courage to continue, you turn quickly, and run down the path you came. Stumbling " \
           "through the dark, you become hopelessly lost in the narrow tunnels of the cave. Without help, and no one " \
           "to call to, you sit down defeated. Your supplies dwindle and soon you find yourself in a permanent " \
           "slumber, forever resting in this cave."
    format_text(text)
    death(False)


# BUY ITEMS!!
def shop():
    shop_decision = -1
    map = False
    potion = False
    string = "Halt! You can't go empty handed! Before you depart, do you want to visit the shop?"
    format_text(string)
    # Validation Check
    while shop_decision != "1" and shop_decision != "2":
        shop_decision = input("\t1. Yes\n\t2. No" + user_input)
    shop_decision = int(shop_decision)
    if shop_decision == 2:
        death_img()
    # Keeps track of which items are bought, removes items from arrays accordingly
    items_bought_array = shop_img(character)
    if "Donkey" not in items_bought_array:
        generic_dude_actions.pop(3)
    if "Health Potion" in items_bought_array:
        potion = True
    if "Map" in items_bought_array:
        map = True
    if "Contract with Dragon Slayer" not in items_bought_array:
        mage_actions.pop(3)
        knight_actions.pop(3)
    items_string = "Currently in your inventory is "
    for i in items_bought_array:
        items_string += "a " + i + ", "
    items_string = items_string[:len(items_string) - 2]
    if len(items_bought_array) > 1:
        items_string = items_string[:items_string.rfind(",") + 1] + " and " + items_string[items_string.rfind(",") + 2:]
    print(items_string)
    entry_path(map, potion)


# Forked path
def entry_path(map, potion):
    pathChoice = -1
    format_text("On your journey, you come across a fork in the road.\n")
    # Having map reveals a new path one can take
    if map:
        format_text("You suddenly remember that you bought a map at the store. You look at the map in hopes of "
                    "discovering secrets. You notice that the map tells you to walk into the forest of trees. "
                    "Where do you want to go?")
        # Validation Check
        while pathChoice != "1" and pathChoice != "2" and pathChoice != "3":
            pathChoice = input("\t1. Go left\n\t2. Go right\n\t3. Go through forest of trees" + "\n>")
    else:
        while pathChoice != "1" and pathChoice != "2" and pathChoice != "3":
            pathChoice = input("\t1. Go left\n\t2. Go right" + "\n>")
    pathChoice = int(pathChoice)
    path_img()
    # Player goes left, leads to Monster Cave
    if pathChoice == 1:
        cave_entrance_img()
        monster_cave(potion)
    # Player goes right (Death)
    elif pathChoice == 2:
        cave_entrance_img()
        cave2_img()
        text = "As you cautiously make your way down the right path, a sense of excitement mixed with apprehension " \
               "fills your heart. Suddenly, without warning, a loud rumbling fills the cave as rocks begin to fall " \
               "from the ceiling. You try to dodge the falling debris, but it’s too late. You become trapped beneath " \
               "the weight of the rocks, and in a split second, your life is extinguished. The cave went silent once " \
               "more, and the tragic and sudden end to your daring journey will never be forgotten."
        format_text(text)
        death(False)
    elif pathChoice == 3 and map:
        dragons_lair(potion)


# Fight or DiE
def monster_cave(potion):
    cave_decision = -1
    text = "As you step into the cave room, the dim light reveals shadowy figures lurking in the corners. " \
           "Suddenly, a group of monsters jump out, their eyes fixed on you as they attack. You draw your weapon " \
           "and brace for the upcoming fight."
    format_text(text)
    cave_img()
    monster_img()
    # Validation Check
    while cave_decision != "1" and cave_decision != "2" and cave_decision != "3":
        if character == 1:
            for i in range(len(mage_actions)):
                if mage_actions[i] == "Call Dragon Slayer":
                    continue
                print(str(i + 1) + ". " + mage_actions[i])
        elif character == 2:
            for i in range(len(knight_actions)):
                if knight_actions[i] == "Call Dragon Slayer":
                    continue
                print(str(i + 1) + ". " + knight_actions[i])
        else:
            for i in range(len(generic_dude_actions)):
                if generic_dude_actions[i] == "Release Donkey":
                    continue
                print(str(i + 1) + ". " + generic_dude_actions[i])
        cave_decision = input("What will you do?" + user_input)
    cave_decision = int(cave_decision)
    # Player runs
    if cave_decision == 1:
        run_away()
    # Player attacks
    if cave_decision == 2:
        # Mage Fireball
        if character == 1:
            text = "You unleash a flurry of fireballs, striking the monsters with deadly accuracy. With each flick " \
                   "of your wand, the monsters stumble and reel, unable to withstand your mastery of the arcane " \
                   "arts. Once all the monsters are defeated, you quickly make your way down the next corridor of " \
                   "this ever winding cave."
            format_text(text)
            exploration_cave(potion)
        # Knight Slash
        elif character == 2:
            text = "You charge into battle, your sword striking with deadly precision. Despite being outnumbered, " \
                   "your skill with a blade allows you to hold your own against the monster horde. Once all the " \
                   "monsters are defeated, you quickly make your way down the next corridor of this ever winding cave."
            format_text(text)
            exploration_cave(potion)
        # Generic Dude Punch
        else:
            text = "While your punches initially confused the dragon, it quickly realized just how weak you are!"
            format_text(text)
            death(potion)
            potion = False
    # Player chooses funny action
    if cave_decision == 3:
        # Mage Beat with Stick
        if character == 1:
            text = "Despite your best efforts, your stick could not penetrate the monster’s armor."
            format_text(text)
            death(potion)
            potion = False
        # Knight Remove Helmet
        elif character == 2:
            text = "While you were removing your helmet like an idiot, the monster took the opportunity to " \
                   "slice your head off!"
            format_text(text)
            death(potion)
            potion = False
        # Generic Dude Serenade
        else:
            text = "You scared the monsters away with your singing, and you happily make your way to the next area."
            format_text(text)
            exploration_cave(potion)
    if cave_decision == 3:
        exit()


# It's dangerous out there
def exploration_cave(potion):
    cave_decision = -1
    cave_decisions = {
        1: "Continue down main path",
        2: "Explore",
        3: "Run away"
    }
    text = "Entering the next cave room, you stumble as you step into a large clawed animal track. As you trace " \
           "the tracks you notice they lead to a path deeper into the cave. The path is straightforward, but you " \
           "notice other cavern paths, some with strange writing or glittering rocks. Could there be treasure in " \
           "these parts of the cave?"
    format_text(text)
    # Validation Check
    while cave_decision != "1" and cave_decision != "2":
        for num, decisions in cave_decisions.items():
            print(str(num) + ". ", decisions)
        cave_decision = input("What will you do?" + user_input)
    cave_decision = int(cave_decision)
    if cave_decision == 1:
        dragons_lair(potion)
    elif cave_decision == 2:
        text = "You choose a path at random, spurred on by the hope of treasure. Maybe there will be an item that " \
               "can help you defeat the dragon? But before you can find any treasure, your foot sinks deep into a " \
               "muddy pit. You struggle to pull your foot out, but it only sinks deeper. After a few minutes you are " \
               "up to your waist in mud, and after a few more only your head remains. You sink under the mud, unable " \
               "to complete your quest. "
        format_text(text)
        death(False)
    else:
        run_away()


# It's that time; The finale
def dragons_lair(potion):
    # Initializes health points and attack points
    cave_decision = -1
    dragon_health = 150
    dragon_attack = 50
    mage_health = 100
    mage_attack = 25
    knight_health = 100
    knight_attack = 25
    generic_dude_health = 50
    generic_dude_attack = 10
    text = "As you cautiously enter the dragon's lair, you ready yourself to fight. Your eyes widen in amazement " \
           "at the vast treasure hoard that surrounds you. Piles of glittering jewels, gold and silver coins, and " \
           "ancient artifacts lay before you. Though your heart yearns to claim the treasure, you know that your " \
           "primary objective is to slay the dragon and emerge victorious. The dragon lays asleep atop its vast " \
           "wealth, now is your time to strike!"
    format_text(text)
    dragon_img()
    while mage_health > 0 and knight_health > 0 and generic_dude_health > 0:
        format_text("What will you do?")
        if character == 1:
            for i in range(len(mage_actions)):
                print(str(i + 1) + ". " + mage_actions[i])
        elif character == 2:
            for i in range(len(knight_actions)):
                print(str(i + 1) + ". " + knight_actions[i])
        else:
            for i in range(len(generic_dude_actions)):
                print(str(i + 1) + ". " + generic_dude_actions[i])
        while cave_decision != "1" and cave_decision != "2" and cave_decision != "3" and cave_decision != "4":
            cave_decision = input(user_input)
        cave_decision = int(cave_decision)
        # Player runs away
        if cave_decision == 1:
            run_away()
        elif cave_decision == 2:
            # Mage Fireball
            if character == 1:
                text = "The dragon reels in pain, but retaliates with its own attack. The dragon lost 25 HP, and " \
                       "you are suffering from a mere swipe of the dragon's claws! You lose 50 HP"
                dragon_health -= mage_attack
                mage_health -= dragon_attack
            # Knight Slash
            elif character == 2:
                text = "Your sword manages to cut the dragon deep, but it angers the dragon and " \
                       "he burns you! The dragon lost 25 HP! You lost 50 HP!"
                dragon_health -= knight_attack
                knight_health -= dragon_attack
            format_text(text)
            if mage_health <= 0 or knight_health <= 0:
                death(potion)
                potion = False
                knight_health = 100
                mage_health = 100
            if dragon_health <= 0:
                format_text("You successfully kill the dragon and return home to receive your reward."
                            "The king is very gracious with his gift and you stay as his loyal servant "
                            "for the rest of your life!")
                exit()
            elif character == 3:
                # Generic Dude Punch
                text = "While your punches initially confused the dragon, it quickly realized just how weak you are!" \
                       " The dragon lost 10 HP!"
                dragon_health -= generic_dude_attack
                format(text)
        # Player chooses funny action
        elif cave_decision == 3:
            # Mage Beat with Stick
            if character == 1:
                text = "Despite your best efforts, your stick would not penetrate the dragon’s scales."
            # Knight Remove Helmet
            elif character == 2:
                text = "While you were removing your helmet like an idiot, the dragon took the opportunity to bite " \
                       "your head off!"
            # Generic Dude Serenade
            elif character == 3:
                text = "Your music wooed the dragon successfully! Unfortunately, it accidentally burned you to a " \
                       "crisp by trying to kiss you."
            format_text(text)
            death(potion)
            potion = False
        # Special Actions
        if cave_decision == 4:
            # Player calls dragon slayer
            if character != 3:
                text = "The dragon slayer runs forward, charging at the sleeping dragon. His thunderous footsteps " \
                       "startle the dragon awake, who turns to the charging dragon slayer and breathes a powerful " \
                       "breath of fire leaving no remains of you or the dragon slayer."
                format_text(text)
                death(False)
            # Player serenades
            elif character == 3:
                text = "The dragon instantly falls in love with your donkey! They go on to live a happy life together" \
                       " with many children. The king, not knowing the dragon is still alive, rewards you handsomely!"
                format_text(text)
                exit()


# Beginning
def start():
    character = -1
    approve_character = -1
    format_text(general_intro)
    # Validation Check
    while character != "1" and character != "2" and character != "3":
        character = input(choose_character + user_input)
    character = int(character)
    if character == 1:
        mage_img()
    elif character == 2:
        knight_img()
    else:
        generic_dude_img()
    time.sleep(.5)
    if character == 1 or character == 2:
        format_text(castle_intro)
        # Validation Check
        while approve_character != "1" and approve_character != "2":
            approve_character = input(accept_deny + user_input)
        approve_character = int(approve_character)
        if approve_character == 1:
            response = "This is marvelous news! I offer you a generous sum of 100 gold to aid you on your journey." \
                        "Be sure to pay a visit to the shopkeeper before you depart, and stock up on any supplies " \
                        "you may need to vanquish the beast. You will find the dragon in its lair, Skull Cavern. " \
                        "May the luck of a thousand blazing suns guide you on your treacherous trail!\n"
        else:
            response = "The kingdom is in dire peril and my heart is heavy with sadness. The treacherous " \
                        "dragon looms on the horizon, and it seems there is little hope for our survival. " \
                        "Pack your belongings and inform your loved ones. There will be nothing left in a few " \
                        "weeks' time, only ruins of this once prosperous kingdom.\n"
        format_text(response)
        if approve_character == 2:
            exit()
        else:
            return character
    else:
        format_text(farm_intro)
        approve_character = int(input(accept_deny + user_input))
        # Validation Check
        while approve_character != "1" and approve_character != "2":
            approve_character = input(accept_deny + user_input)
        approve_character = int(approve_character)
        if approve_character == 1:
            response = "You dreadfully think about the journey ahead, but you are full of much joy for being " \
                        "chosen personally by the king!\n"
        else:
            response = "Too fearful to follow the king's wishes you go back to your daily life working in fields" \
                       " knowing you will die soon for your disobedience.\n"
        format_text(response)
        if approve_character == 2:
            exit()
        else:
            return character


character = start()
shop()

