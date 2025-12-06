input_str = """
ADD INPUT
""".strip()

input_arr = input_str.split()

count = 0
pointer = 50
for line in input_arr:
    print(f"The dial starts by pointing at {pointer}")
    direction = line[0]
    number = int(line[1:])
    print(f"turning {direction} by {number}")
    while number >= 100:
        count += 1
        print("Seen 0")
        number -= 100
    if direction == "R":
        if pointer + number >= 100:
            print("Seen 0")
            count += 1
        pointer = (pointer + number) % 100
    else:
        if pointer - number <= 0 and pointer > 0:
            print("Seen 0")
            count += 1
        pointer = (pointer - number) % 100

print(count)
"""
The dial starts by pointing at 50.
The dial is rotated L68 to point at 82; during this rotation, it points at 0 (yes)once.
The dial is rotated L30 to point at 52. Y
The dial is rotated R48 to point at 0. Y
The dial is rotated L5 to point at 95.
The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
The dial is rotated L55 to point at 0.
The dial is rotated L1 to point at 99.
The dial is rotated L99 to point at 0.
The dial is rotated R14 to point at 14.
The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.
"""