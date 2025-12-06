input_str = """
ADD INPUT
""".strip()

input_arr = input_str.split()

count = 0
pointer = 50
for line in input_arr:
    direction = line[0]
    number = int(line[1:])
    if direction == "R":
        pointer = (pointer + number) % 100
    else:
        pointer = (pointer - number) % 100
    
    if pointer == 0:
        count += 1

print(count)