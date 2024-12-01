
file_path = "input.txt"
list_left = []
list_right = []
distance = 0

with open(file_path, 'r') as file:
    for line in file:   
        left,right  = map(int, line.split())
        list_left.append(left)
        list_right.append(right)

list_left.sort()
list_right.sort()

print(len(list_left))
print(len(list_right))

for i in range(len(list_left)):
    distance = distance + abs(list_left[i] - list_right[i])

print(distance)

sim_score = 0
for i in list_left:
    sim_score = sim_score  + (i * list_right.count(i))

print(sim_score)


    