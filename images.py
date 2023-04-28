from textwrap import fill
import time
from graphics import *


# Formats all text the same
def format_text(sentences):
    sentences = str(fill(sentences, 150))
    for char in sentences:
        print(char, end="")
        time.sleep(.03)
    print("\n")


# You die
def death_img():
    win2 = GraphWin("Window2", 550, 550)
    win2.setBackground('black')
    death = Image(Point(250, 250), "img/death.gif")
    death.draw(win2)
    win2.getMouse()
    win2.close()


# Victory
def victory_img():
    win2 = GraphWin("Window2", 550, 550)
    win2.setBackground('black')
    victory = Image(Point(250, 250), "img/you_win.gif")
    victory.draw(win2)
    win2.getMouse()
    win2.close()


# Character Selection
def mage_img():
    win1 = GraphWin("Window1", 500, 500)
    win1.setBackground(color_rgb(0, 0, 0))
    img = Image(Point(250, 250), "img/mage.gif")
    img.draw(win1)
    txt = Text(Point(250, 420), "You have chosen the Mage!\nClick anywhere to continue")
    txt.setTextColor('white')
    txt.draw(win1)
    win1.getMouse()
    win1.close()


def knight_img():
    win1 = GraphWin("Window1", 500, 500)
    win1.setBackground(color_rgb(0, 0, 0))
    img = Image(Point(250, 250), "img/knight.gif")
    img.draw(win1)
    txt = Text(Point(250, 420), "You have chosen the Knight!\nClick anywhere to continue")
    txt.setTextColor('white')
    txt.draw(win1)
    win1.getMouse()
    win1.close()


def generic_dude_img():
    win1 = GraphWin("Window1", 500, 500)
    win1.setBackground(color_rgb(0, 0, 0))
    img = Image(Point(250, 250), "img/generic_dude.gif")
    img.draw(win1)
    txt = Text(Point(250, 420), "You have chosen the Generic Dude!\nClick anywhere to continue")
    txt.setTextColor('white')
    txt.draw(win1)
    win1.getMouse()
    win1.close()


# Shop time
def shop_img(version):
    items_bought_array = []
    counter = 0
    money = 100
    # Image Background
    win2 = GraphWin("Window2", 600, 600)
    win2.setBackground('black')

    # Shopkeeper
    shopkeeper = Image(Point(400, 150), "img/shopkeeper.gif")
    shopkeeper.draw(win2)
    shopkeeper_prompt = Text(Point(150, 150),
                             "Welcome Traveller! \n\nWhat would you like to purchase \nfor your travels?")
    shopkeeper_prompt.setTextColor('white')
    shopkeeper_prompt.draw(win2)

    # Health Potion section
    healthPotion = Image(Point(100, 420), "img/health.gif")
    healthPotion.draw(win2)
    health_prompt = Text(Point(100, 500), "Health Potion (50g)\nType 1 to Purchase")
    health_prompt.setTextColor('white')
    health_prompt.draw(win2)

    # Map
    map = Image(Point(300, 420), "img/map2.gif")
    map.draw(win2)
    map_prompt = Text(Point(300, 500), "Map (50g)\nType 2 to Purchase")
    map_prompt.setTextColor('white')
    map_prompt.draw(win2)

    # Display total amount of gold
    total_gold = Text(Point(300, 570), "You Have:" + str(money) + "g")
    total_gold.setTextColor('gray')
    total_gold.draw(win2)

    # Donkey
    if version == 3:
        donkeyimg = Image(Point(500, 420), "img/donkey.gif")
        donkeyimg.draw(win2)
        donkey_prompt = Text(Point(500, 500), "Donkey (100g)\nType 3 to Purchase")
        donkey_prompt.setTextColor('white')
        donkey_prompt.draw(win2)
        items = {
            1: "Health Potion",
            2: "Map",
            3: "Donkey"
        }
    # Dragon Contract
    else:
        dragonContractImg = Image(Point(500, 420), "img/contract.gif")
        dragonContractImg.draw(win2)
        dragonContractImgPrompt = Text(Point(500, 500), "Dragon Slayer Contract (100g)\nType 3 to Purchase")
        dragonContractImgPrompt.setTextColor('white')
        dragonContractImgPrompt.draw(win2)
        items = {
            1: "Health Potion",
            2: "Map",
            3: "Contract with Dragon Slayer",
        }
    prices = [50, 50, 100]
    # Quits shop when you run out of money
    while money > 0:
        for cost, num_item, item in zip(prices, items.keys(), items.values()):
            print(str(num_item) + ".", item, "(" + str(cost) + " Gold)")
        items_bought = int(input("\n>"))
        while items[items_bought] == "Out of Stock":
            counter += 1
            if counter == 3:
                format_text("You imbecile. Stop!")
            elif counter == 5:
                format_text("I will make you stop!")
                death_img()
            else:
                format_text("YOU already bought that you greedy piece of garbage! Ahem sorry we are currently "
                            "out of stock. Would you like to buy anything else?")
            for cost, num_item, item in zip(prices, items.keys(), items.values()):
                print(str(num_item) + ".", item, "(" + str(cost) + " Gold)")
            items_bought = int(input("\n>"))
        # Keeps track of which items are bought
        items_bought_array.append(items[items_bought])
        items[items_bought] = "Out of Stock"
        if items_bought == 1:
            # Removes potion
            total_gold.setText("You Have: " + str(money) + "g")
            shop_confirm = Text(Point(300, 545), "You Have purchased a Health Potion! Click to continue")
            shop_confirm.setTextColor('white')
            shop_confirm.draw(win2)
            healthPotion.undraw()
            health_prompt.undraw()
            # Out of stock
            outOfStockImg = Image(Point(100, 420), "img/out_of_stock.gif")
            outOfStockImg.draw(win2)
            outOfStockTxt = Text(Point(100, 500), "Out of Stock")
            outOfStockTxt.setTextColor('white')
            outOfStockTxt.draw(win2)
            # Total Gold
            total_gold = Text(Point(300, 570), "You Have:" + str(money) + "g")
            total_gold.setTextColor('gray')
            total_gold.draw(win2)
        elif items_bought == 2:
            # Removes map
            total_gold.setText("You Have: " + str(money) + "g")
            shop_confirm = Text(Point(300, 545), "You Have purchased a Map! Click to continue")
            shop_confirm.setTextColor('white')
            shop_confirm.draw(win2)
            map.undraw()
            map_prompt.undraw()
            # Out of stock
            outOfStockImg = Image(Point(300, 420), "img/out_of_stock.gif")
            outOfStockImg.draw(win2)
            outOfStockTxt = Text(Point(300, 500), "Out of Stock")
            outOfStockTxt.setTextColor('white')
            outOfStockTxt.draw(win2)
            # Total Gold
            total_gold = Text(Point(300, 570), "You Have:" + str(money) + "g")
            total_gold.setTextColor('gray')
            total_gold.draw(win2)
        if items_bought == 3:
            total_gold.setText("You Have: " + str(money) + "g")
            # Remove Donkey
            if version == 3:
                shop_confirm = Text(Point(300, 545), "You Have purchased a Donkey! Click to continue")
                shop_confirm.setTextColor('white')
                shop_confirm.draw(win2)
                donkeyimg.undraw()
                donkey_prompt.undraw()
            # Remove Dragon
            else:
                shop_confirm = Text(Point(300, 545), "You Have purchased a Contract! Click to continue")
                shop_confirm.setTextColor('white')
                shop_confirm.draw(win2)
                dragonContractImg.undraw()
                dragonContractImgPrompt.undraw()
            # Out of stock
            outOfStockImg = Image(Point(500, 420), "img/out_of_stock.gif")
            outOfStockImg.draw(win2)
            outOfStockTxt = Text(Point(500, 500), "Out of Stock")
            outOfStockTxt.setTextColor('white')
            outOfStockTxt.draw(win2)
            # Total Gold
            total_gold = Text(Point(300, 570), "You Have:" + str(money) + "g")
            total_gold.setTextColor('gray')
            total_gold.draw(win2)
        money -= prices[items_bought - 1]
        if money != 0:
            format_text("Wise choice. Would you like to buy something else?")
        else:
            format_text("Wise decision. Best of luck to you on your journey, and don't forget who helped you with this "
                        "journey when you slay the dragon.")
    win2.getMouse()
    win2.close()
    return items_bought_array


# First Cave
def cave_img():
    cave1Window = GraphWin("First Cave", 700, 500)
    cave1Window.setBackground('black')
    cave1Prompt = Text(Point(350, 450), "The dark cavern welcomes you")
    cave1Prompt.setTextColor('white')
    cave1Prompt.draw(cave1Window)
    cave1Image = Image(Point(350, 250), "img/cave.gif")
    cave1Image.draw(cave1Window)
    cave1Window.getMouse()
    cave1Window.close()


# 2nd Cave
def cave2_img():
    cave2Window = GraphWin("2nd Cave", 450, 450)
    cave2Window.setBackground('black')
    cave2Prompt = Text(Point(225, 425), "cave text (idk what)")
    cave2Prompt.setTextColor('white')
    cave2Prompt.draw(cave2Window)
    cave2Image = Image(Point(225, 210), "img/cave2.gif")
    cave2Image.draw(cave2Window)
    cave2Window.getMouse()
    cave2Window.close()


# Dragon
def dragon_img():
    dragonWindow = GraphWin("Dragon", 500, 460)
    dragonWindow.setBackground('black')
    dragonPrompt = Text(Point(250, 425), "oh a dragon das crazy")
    dragonPrompt.setTextColor('white')
    dragonPrompt.draw(dragonWindow)
    dragonImage = Image(Point(250, 200), "img/dragon.gif")
    dragonImage.draw(dragonWindow)
    dragonWindow.getMouse()
    dragonWindow.close()


# Cave Entrance
def cave_entrance_img():
    cave_entranceWindow = GraphWin("Cave_Entrance", 500, 400)
    cave_entranceWindow.setBackground('black')
    cave_entracePrompt = Text(Point(250, 320), "The path seems to lead here.\nClick to continue")
    cave_entracePrompt.setTextColor('white')
    cave_entracePrompt.draw(cave_entranceWindow)
    cave_entraceImage = Image(Point(250, 175), "img/cave_entrance.gif")
    cave_entraceImage.draw(cave_entranceWindow)
    cave_entranceWindow.getMouse()
    cave_entranceWindow.close()


# Monster
def monster_img():
    monsterWindow = GraphWin("Monster", 500, 500)
    monsterWindow.setBackground('black')
    monsterImg = Image(Point(250, 250), "img/monster.gif")
    monsterImg.draw(monsterWindow)
    monsterPrompt = Text(Point(250, 420), "A monster was guarding the entrance to the cave! \nWhat do you want to do?")
    monsterPrompt.setTextColor('white')
    monsterWindow.getMouse()
    monsterWindow.close()


# Path
def path_img():
    pathWindow = GraphWin("Path", 500, 470)
    pathWindow.setBackground('black')
    pathImg = Image(Point(250, 250), "img/path.gif")
    pathImg.draw(pathWindow)
    pathWindow.getMouse()
    pathWindow.close()
