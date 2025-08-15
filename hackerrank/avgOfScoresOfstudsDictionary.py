'''
Question - 
given a dictonary, access the scores of the names given in the dictionary and get the averga of those scores
'''

def get_average(student_marks, query_name):
    if query_name in student_marks:
        scores = student_marks[query_name]
        avg = sum(scores) / len(scores)
        return avg
    else:
        return None
    
student_marks = {
    "Karthik": [80, 90, 70],
    "Ravi": [65, 75, 85]
}
query_name = "Karthik"

result = get_average(student_marks, query_name)
print(f"{result:.2f}")

'''
TRACING : 

student_marks = {
    "Karthik": [80, 90, 70],
    "Ravi": [65, 75, 85]
}
query_name = "Karthik"

if query_name in student_marks:
"Karthik" in dictionary -> true
    scores = student_marks[query_name]
    here, I am accessing the list of scores of the query_name "Karthik" and storing it in a variable "scores"

    scores = [80, 90, 70]

    avg = sum(scores) / len(scores)
    sum(scores) = 80 + 90 + 70 = 240 
    len(scores) = 3
    avg = 240 / 3 -> 80

    Output = 80

    But if we need to get the output with two decimal places, then we can add 
    round(avg, 2) or print with f string literals

    and hence the output will be 80.00

'''