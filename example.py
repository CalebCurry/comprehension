#loop way

data = [1, 2, 3, 4]

squares = []
for i in data:
    if i != 3:
        squares.append(i*i)

print(squares)

#1
squares = [i*i for i in data if i != 3]
print(squares)

#2
names = ['caleb', 'amanda', 'jerry']
backwards = [name[::-1] for name in names]
print(backwards)

#3

import math
data = [1, 34, 3, 23, 234, 65, 12, 23, 3, 545, 12, 54, 6, 8, 878, 3, 5, 867, 3, 5, 2, 4, 4, 4, 9, 6]
qualified = [d for d in data if d%2==0]
print(qualified)

fav_numbers = [4, 33, 12]
qualified = [d for d in data if d in fav_numbers]
print(qualified)


#4 flatten 
student_scores = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
flat = [score for scores in student_scores for score in scores]
print(flat)

#5 replace values - https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator
#when else put it on left
memberships = ['gold', 'silver', 'silver', 'bronze', 'free', 'bronze', None, None, 'bronze', None]
cleaned = [('free' if m is None else m) for m in memberships]
print(cleaned)

#6 
flavors = ['c', 's', 'v']
cones = [[scoop1, scoop2, scoop3] for scoop1 in flavors for scoop2 in flavors for scoop3 in flavors]
print(len(cones))
print(cones)
cones = [f'{scoop1}{scoop2}{scoop3}' for scoop1 in flavors for scoop2 in flavors for scoop3 in flavors]
print(cones)

#7 set comp 
cones = {f'{scoop1}{scoop2}{scoop3}' for scoop1 in flavors for scoop2 in flavors for scoop3 in flavors}
print(cones)

#dict comprehension
#8 key value pairs
names = ['chocolate', 'strawberry', 'vanilla']
result = {flavor:name for flavor, name in zip(flavors, names)}
print(result)

#simple, but limited:
result = dict(zip(flavors, names))
print(result)

#example of why limited
result = {flavor:name for flavor, name in zip(flavors, names) if name != 'chocolate'}
print(result)

#9
users = [('caleb', 124), ('john', 342), ('ashley', 43)]
flipped = [(user[1], user[0].capitalize()) for user in users]
print(flipped)

#simple, no capitalization:
flipped = [user[::-1] for user in users]
print(flipped)

#10  flipping dict keys, i think flipped in vid
users = {user[0]: user[1] for user in flipped}
print(users)

flipped = {val:key for key, val in users.items()}
print(flipped)

#not flawless as dict keys cannot have duplicates 
