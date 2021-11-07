import random
NAMES = ["AIBEK", "JOOMART", "ADINAI", "ERMEK", "ATAI", "ASLAN", "LYAZAT", "SALAVAT",
    "DANIYAR", "BOLOTBEK", "ALYMBEK", "DASTAN", "MAKSAT"]

team1 = random.choices(NAMES, k=3)
team2 = random.choices(NAMES, k=3)
team3 = random.choices(NAMES, k=3)
team4 = random.choices(NAMES, k=4)
print(team1)
print(team2)
print(team3)
print(team4)