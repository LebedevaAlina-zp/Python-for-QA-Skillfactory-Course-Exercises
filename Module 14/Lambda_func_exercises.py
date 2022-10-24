# Ex 14.6.3. Sort the list of people's mass and height data based on one's body mass index (mass in kg divided by height in m).
data = [
   (82, 191),
   (68, 174),
   (90, 189),
   (73, 179),
   (76, 184)
]

print(sorted(data, key = lambda x: x[0] / (x[1]/100)**2))

# Ex 14.6.4. Find the tuple with the least body mass index from the previous exercise.

print(min(data, key = lambda x: x[0] / (x[1]/100)**2))

# Ex. 14.6.5. Find the length of each element in the list.

a = ["asd", "bbd", "ddfa", "mcsa"]

print(list(map(len, a)))
