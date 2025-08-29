def count_substring(string, sub_string):
    count = 0
    n = len(sub_string)

    for i in range(len(string) - n + 1):
        if string[i:i + n] == sub_string:
            count = count + 1

    return count

print(count_substring(string="ABCDCDC", sub_string="CDC"))

'''
TRACING - 

string = "ABCDCDC"
sub_string = "CDC"

count = 0
n = len(sub_string)
n = 3

for i in range(len(string) - n + 1):
    len(string) = 7
    len(string) - n + 1 -> 7 - 3 + 1
    loop runs until 5

    -> i = 0
    if string[i : i + n] == sub_string:
    string[0 : 0 + 3] -> string[0: 3] -> 'ABC' == 'CDC' -> false

    -> i = 1
    if string[i : i + n] == sub_string:
    string[1 : 1 + 3] -> string[1 : 4] -> 'BCD' == 'CDC' -> false

    -> i = 2
    if string[i : i + n] == sub_string:
    string[2: 2 + 3] -> string[2: 5] -> 'CDC' == 'CDC' -> true
        count = count + 1
        count = 1

    -> i = 3
    if string[i : i + n] == sub_string:
    string[3 : 3 + 3] -> string[3: 6] -> 'DCD' == 'CDC' -> false

    -> i = 4
    if string[i : i + n] == sub_string:
    string[4: 4 + 3] -> string[4: 7] -> 'CDC' == 'CDC -> true
        count = count + 1
        count = 2

Output = 2



'''