print(
    "Once upon a time, in a quaint little village, there lived a clever cat named Freak. "
    "One fine morning, you, a traveler seeking adventure, came upon this mysterious feline.\n"
    "'Greetings, dear friend,' said Freak with a gentle purr, 'I am the guardian of this town. "
    "Pray tell, what is thy name?'"
)

player_name = input("Enter your name, brave traveler: ")

print(f"'Ah, {player_name}, a name worthy of legend!'")

print(
    "Meow...I am Freak 🐱, the black cat. You have the choice: "
    "Either we go hunting mice, or you can pet me. What is it that you prefer?"
)

while True:
    choice = input("Type 'hunt' to go hunting, or 'pet' to pet me: ").lower()

    if choice == "hunt" or choice == "hunting mice":
        print(f"A true hunter must prove their courage. Tell me, brave {player_name}, what sound does a sneaky mouse make?")

        mouse_sound = input("Your answer: ").lower()
        if mouse_sound == "squeak":
            print("Purrfect! You're worthy. Let's catch some mice together!")
        else:
            print(f"Hmm, that doesn't sound quite right {player_name}... But we'll give it a try anyway!")
        break  # exit the loop after handling this choice

    elif choice == "pet" or choice == "pet me":
        print("Before you pet me, answer this:")
        print("If we catch 3 mice each day, how many mice will we catch in 4 days?")

        riddle_answer = input("Your answer: ")

        if riddle_answer == "12":
            print(f"Purrr... you got it right {player_name}! You may pet me now.")
        else:
            print("Hmph, that’s not quite right. Maybe next time!")
        break  # exit the loop after handling this choice

    else:
        print("Hmm, I don't understand that choice. Let's try again.")
