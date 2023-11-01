NAME_TO_CODE = {"DarkOrchid4": "68228b", "DarkSlateGray": "2f4f4f", "Deep Peach": "ffcba4", "DeepPink2": "ee1289",
                "Ferrari Red": "ff2800", "Bitter Lime": "bfff00", "Caribbean Green": "00cc99", "Cordovan": "893f45",
                "Daffodil": "ffff31", "DarkSeaGreen1": "c1ffc1"}

colour_name = input("Enter name: ")
while colour_name != "":
    try:
        print(f"{colour_name} is {NAME_TO_CODE[colour_name]}")
    except KeyError:
        print("Invalid name")
    colour_name = input("Enter name: ")
