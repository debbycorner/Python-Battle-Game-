
import random
pips = random.randint(1, 6)

weapon_list = ["Exploding Milk Bottles", "Candy Canes", "Snowballs"]
weapon_list2 ={"Exploding Milk Bottles": 50, "Candy Canes": 20, "Snowballs": 10}

big_baby = "Big Baby"



elf = "Elf"
monster_health = 100

character_name_health = 100
character_gold = 100

monster_list = [elf, big_baby]

print("In a land far far away a brave warrior goes to fight against a mysterious monster. The warrior must choose carefully a weapon they believe will aid them in defeating this mysterious monster.")
character_name = input("What is your characters name?: ")
print(f"Welcome to the adventure! {character_name} \n You start the game with 100 gold pieces")


print("You roll the dice...it lands with", pips)
if pips <= 3:
    monster_picked = big_baby
    print(f"You will battle {big_baby}\n the {big_baby} has a health of {monster_health}")
elif pips >=4:
    monster_picked = elf
    print(f"You will now fight {elf}\n the {elf} has a health of {monster_health}.")

buy_weapon = input("Would you like to pick a weapon? ")
if buy_weapon == "Yes":
    picked_weapon = input(f"Please pick from the following list: {weapon_list} : ")
    print(f"You have picked {picked_weapon}\n 50 pieces of gold have been taken. You now have {character_gold} left.\n Reaminging weapons in shop {weapon_list}")
    weapon_list.remove(picked_weapon)
    if picked_weapon == "Snowballs":
        attack_level = weapon_list2["Snowballs"]
        print(f"Your attack level is: {attack_level}")
    elif picked_weapon == "Candy Canes":
        attack_level = weapon_list2["Candy Canes"]
        print(f"Your attack level is: {attack_level}")
    elif picked_weapon == "Exploding Milk Bottles":
        attack_level = weapon_list2["Exploding Milk Bottles"]
        print(f"Your attack level is: {attack_level}")
    character_gold = character_gold - 50
    print(f"You have picked {picked_weapon}\n 50 pieces of gold have been taken. You now have {character_gold} left.\n Reaminging weapons in shop {weapon_list}")
elif buy_weapon == "No":
    print(f"You do not have a weapon and you haven't spent any of your gold. You still have {character_gold} pieces of gold left. Good luck in your battle!")
else:
    print("Invalid selection")

while True: 
    if buy_weapon == "Yes": 
        if monster_health > 0:
            print(f"The {monster_picked} has a health of {monster_health}. {character_name} strikes the {monster_picked} with their weapon")
            monster_health = monster_health - attack_level
        if monster_health <= 0:
            print("You won!")
            break
    if buy_weapon == "No":
        print(f"Oh NOOOOO! You didn't hurt the {monster_picked}")
        haracter_name_health = character_name_health - 100
        print(f"The {monster_picked} has hurt you! You are now dead")
        break



