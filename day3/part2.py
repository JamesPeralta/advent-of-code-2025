f = open("test.txt", "r")   # open for reading
input_str = f.read()
f.close()

def back_track(input_str, pointer, curr_arr, res=[]):
    if len(curr_arr) == 12:
        res.append(int("".join(curr_arr)))
        return
    
    for i in range(pointer, len(input_str)):
        curr_arr.append(input_str[i])
        back_track(input_str, i + 1, curr_arr, res)
        curr_arr.pop()

    return

input_str = input_str.split("\n")
result = 0
for line in input_str:
    res = []
    back_track(line, 0, [], res)
    max_res = max(res)

    result += max_res

print(result)
