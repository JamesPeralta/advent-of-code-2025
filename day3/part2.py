f = open("actual.txt", "r")   # open for reading
input_str = f.read()
f.close()


def find_largest(input_str):
    arr = []
    index = 0
    num_left = 12
    while num_left > 0:
        left_part = input_str[index:len(input_str) - num_left + 1]
        max_res = max(left_part)
        index = index + left_part.find(max_res) + 1
        arr.append(max_res)
        num_left -= 1

    return int("".join(arr))
    


input_str = input_str.split("\n")
result = 0
for line in input_str:
    result += find_largest(line)

print(result)

"""
987654321111
811111111119
434234234278
888911112111 = 3121910778619.
"""