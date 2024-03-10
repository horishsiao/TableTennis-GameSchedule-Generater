import random
import csv

def Csv_reader():
    with open("./系際盃表單.csv", newline="", encoding="utf-8") as csvfile:    
        rows = csv.reader(csvfile)
        parts = []
        for row in rows:
            parts.append(row)
    return parts

data = Csv_reader()
# 提取
timestamps = [row[0] for row in data[1:]]

# 提取負責人資訊
responsibles = [row[1].split('/') for row in data[1:]]


male_singles = [row[2] for row in data[1:] if row[2].strip()]
open_male_singles = [row[3] for row in data[1:] if row[3].strip()]
open_female_singles = [row[4] for row in data[1:] if row[4].strip()]
male_doubles = [row[5] for row in data[1:] if row[5].strip()]
female_doubles = [row[6] for row in data[1:] if row[6].strip()]
mixed_doubles = [row[7] for row in data[1:] if row[7].strip()]
team_competition = [row[8] for row in data[1:] if row[8].strip()]

print("時間戳記:", timestamps)
print("負責人資訊:", responsibles)
print("一般組男單報名:", male_singles)
print("公開組男單報名:", open_male_singles)
print("公開組女單報名:", open_female_singles)
print("男雙報名:", male_doubles)
print("女雙報名:", female_doubles)
print("混雙報名:", mixed_doubles)
print("團體賽報名:", team_competition)