input_str = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124".split(",")

def check_chunk(num_str, size=1):
    chunk = num_str[:size]
    return chunk * (len(num_str) // size) == num_str


def is_invalid(num_str):
    if check_chunk(num_str):
        return True


    if len(num_str) % 2 == 0:
        for i in range(2, (len(num_str) // 2) + 1):
            if check_chunk(num_str, i):
                return True
    else:
        for i in range(3, (len(num_str) // 2) + 1):
            if check_chunk(num_str, i):
                return True

    return False

result = 0
for line in input_str:
    left, right = line.split("-")
    # print(left, right)
    for i in range(int(left), int(right) + 1):
        if is_invalid(str(i)):
            # print(i)
            result += i
print(result)

"""
123123123
chunks of 1
chunks of 3

check that the chunks are the same..

if it's odd we start at 1, 3, 5, etc

if it's 2, 4, 6, etc

can we break this string down into repeating parts
"""