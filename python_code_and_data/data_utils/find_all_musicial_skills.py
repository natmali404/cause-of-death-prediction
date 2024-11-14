data_file = open("simplified_data.txt", "r", encoding="utf-8").readlines()[1:]
output = open("all_skills.txt", "w", encoding="utf-8")

data = []

for line in data_file:
    new_line = line.strip()[1:-1].strip("'").split("','")
    data.append(new_line)
    
    
skills = {}


for element in data:
    artist_skills = element[5].split(",")
    for i in range(len(artist_skills)):
        artist_skills[i] = artist_skills[i].strip()
    for skill in artist_skills:
        if skill not in skills:
            skills[skill] = 1
        else:
            skills[skill] += 1

            

sorted_skills = sorted(skills.items(), key=lambda item: item[1], reverse=True)

for skill, count in sorted_skills:
    output.write(f"{skill}: {count}\n")