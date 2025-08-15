'''
Question - 
print the name(s) of the students with the second lowest score. 
'''

def secondlowestScoreAndName(name, score):
    records = list(zip(name, score))
                
    scores = sorted({score for name, score in records})
            
    if len(scores) >= 2:
        second_lowest = scores[1]
    else:
        second_lowest = scores[0]
                
    names = [name for name, score in records if score==second_lowest]
        
    return sorted(names)

for name in secondlowestScoreAndName(name=["chi", "beta", "alpha"], score=[20.0, 50.0, 50.0]):
    print(name)
# print(secondlowestScoreAndName(name=["chi", "beta", "alpha"], score=[20.0, 50.0, 50.0]))

'''
TRACING:

name = ["chi", "beta", "alpha"]
score=[20.0, 50.0, 50.0]

records = list(zip(name, scores))
=> zip(names, scores) = ("chi", 20.0), ("beta", 50.0), ("alpha", 50.0)
=> list(zip(names, scores)) = [("chi", 20.0), ("beta", 50.0), ("alpha", 50.0)]
=> records = ["chi", "beta", "alpha"], score=[20.0, 50.0, 50.0]

scores = sorted({score for name, score in records})
this means that I am accessing only the "score" in records and then sorting it.
the flower brackets {} because, I am treating it as a set
=> scores = [20.0, 50.0]

if len(scores) >= 2:
-> len(scores) = 2 -> true
    second_lowest = scores[1]
    second_lowest = 50.0

names = [name for name, score in records if score == slowest_score]
this means that I am checking the name in records whose score is eqaul to the second lowest score
names = ["beta", "alpha"]

return sorted(names)
this means that I am returning those names in alphabetical order
-> names = ["alpha", "beta"]

but to print them one line after another, 
I iterate through another loop by calling the function and passing the parameters and printing the name one by one

Output = 
alpha
beta
'''

