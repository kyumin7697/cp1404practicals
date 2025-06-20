"""
hex_colours.py
"""

COLOUR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}
print(COLOUR_TO_HEX)

COLOUR_CODE = {key.lower(): key for key in COLOUR_TO_HEX}

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    try:
        print(f"{colour_name.title()} has the code {COLOUR_CODE[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter a colour name: ").lower()