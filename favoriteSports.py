fav_sports = {}

while True:
    print("What are your favorite sports")
    sport = input()
    if sport == '':
        break

    print(f"What do you like about {sport}?")
    info = input()

    fav_sports[sport] = info

print("Your favorite sport and what you like about it:")
for sport, info in fav_sports.items():

    print(f"{sport}: {info}")
