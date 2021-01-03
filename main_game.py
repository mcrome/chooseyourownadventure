print("Welcome to Choose Your Own Adventure!")
name = input("What is your name?")
color = input("What is your favorite color?")
# I do not know that!
age = int(input("What is your age?"))
print("Hello", name, "you are", age, "years old.")

health = 15
level = 1
weapon = input("Choose a weapon: rifle, blade, or spear.").lower()

if age >= 18:
    print("You are old enough to play!")
    wants_to_play = input("Do you want to play?").lower()
    if wants_to_play == "yes":
        print(f"You are starting with {health} health and on level {level}, with a {weapon} as a weapon, let's play!")

        hay_or_straw = input("First Choice... hay foot or straw foot?(hay/straw)").lower()

        if hay_or_straw == "hay":
            health -= 3
            print("You were attacked by a bear and lost 3 health")

            rock_or_tree = input(
                "You look for shelter and find a rock and a tree. Which one do you choose?(rock/tree)").lower()

            if rock_or_tree == "rock":
                health -= 5
                print("The rock fell on you and you lost 5 health. Be Careful!")
                if weapon == "spear":
                    fishing_or_hunting = input(
                        "You're getting hungry. You can choose to go fishing or hunting with your spear.").lower

            elif rock_or_tree == "tree":
                health += 3
                print("The tree nurtured you and you gained 3 health points!")
                stream_bridge = input(
                    "You find a stream. "
                    "You can build a bridge of either sticks or mud. Which do you choose?(sticks/mud)").lower()
                if stream_bridge == "sticks":
                    level += 2
                    print("You went up two levels")
                elif stream_bridge == "mud":
                    health -= 5
                    print("Your soul was lost IN THE RIVER! You lost 5 health")
                    if health == 0:
                        print("You ran out of health and have lost the game! Try Again")
                    elif health <= 5:
                        print(f"You are running low on health! Your health is only {health}!")
                else:
                    print("Invalid Input! Try Again")
            else:
                print("Invalid Input! Try Again")

        elif hay_or_straw == "straw":
            level += 0.5
            print("You went up half a level")
            rock_or_tree = input(
                "You look for shelter and find a rock and a tree. Which one do you choose?(rock/tree)").lower()

            if rock_or_tree == "rock":
                health -= 5
                print("The rock fell on you and you lost 5 health. Be Careful!")
                if weapon == "spear":
                    fishing_or_hunting = input(
                        "You're getting hungry. You can choose to go fishing or hunting with your spear.(fish/hunt)").lower()
                    if fishing_or_hunting == "fish":
                        health -= 2
                        print("Your spear slipped and you didn't catch the fish. You lost 2 health.")
                    elif fishing_or_hunting == "hunt":
                        health += 3
                        level += 1
                        print("You caught the fish! You have gained 3 health and went up one level.")
                    else:
                        print("Invalid Input! Try Again")

            elif rock_or_tree == "tree":
                health += 3
                print("The tree nurtured you and you gained 3 health points!")

        else:
            print("Invalid Input! Try Again")
    else:
        print("See ya...")


elif age >= 14:
    print("You can play with supervision, let an adult confirm their age and whether they want to play")
else:
    print("You are not old enough to play")
