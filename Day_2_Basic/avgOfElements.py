'''
Write a program to find the average of elements in an 
array without using sum() or len() functions

Example, let the array be a list of heights of students.
'''


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
  total_height += height

number_of_students = 0
for student in student_heights:
  number_of_students += 1

average_height = round(total_height / number_of_students)
print(average_height)


# Sample testcase: 

# student_heights = [180, 124, 165, 173, 189, 169, 146]
# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
# There are a total of 7 heights in student_heights
# 1146 ÷ 7 = 163.71428571428572
# Average height rounded to the nearest whole number = 164