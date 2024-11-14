#data_file = open("final_data_fix3.txt", "r", encoding="utf-8").readlines()[1:]
data_file = open("simplified_data.txt", "r", encoding="utf-8").readlines()[1:]
output = open("all_death_causes.txt", "w", encoding="utf-8")

data = []

for line in data_file:
    new_line = line.strip()[1:-1].strip("'").split("','")
    data.append(new_line)
    
    
death_causes = {}


for element in data:
    artist_death_causes = element[4].split(", ")
    for cause in artist_death_causes:
        if cause not in death_causes:
            death_causes[cause] = 1
        else:    
            death_causes[cause] += 1
            

sorted_death_causes = sorted(death_causes.items(), key=lambda item: item[1], reverse=True)

for cause, count in sorted_death_causes:
    output.write(f"{cause}: {count}\n")