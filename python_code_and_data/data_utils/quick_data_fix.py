data_file = open("final_data_fix2.txt", "r", encoding="utf-8").readlines()[1:]
output = open("final_data_fix3.txt", "w", encoding="utf-8")

data = []

for line in data_file:
    new_line = line.strip()[1:-1].strip("'").split("','")
    data.append(new_line)

 

additional_data_file = open("musicbrainz_data/artist_data.txt", "r", encoding="utf-8").readlines()[1:]
additional_data = []
for line in additional_data_file:
    new_line = line.strip()[1:-1].strip("'").split("', '")
    additional_data.append(new_line)

additional_data_and_genre_file = open("musicbrainz_data/artist_data_full.txt", "r", encoding="utf-8").readlines()[1:]
additional_data_and_genre = []
for line in additional_data_and_genre_file:
    new_line = line.strip()[1:-1].strip("'").split("', '")
    additional_data_and_genre.append(new_line)







new_column_names = "['name','gender','birth_date','death_date','age','birth_place','death_place','cause_of_death','musicial_skills','genres']"
output.write(new_column_names)

# for line in data:
#     print(line)
#     if line == "" or line == "\n":
#         continue
#     name = line[0]
#     data_found = False
#     for additional_line in additional_data_and_genre:
#         if name == additional_line[0]:
#             data_found = True
#             gender = additional_line[2].replace("'","").replace(",","").replace(" ","")
#             break
#     if not data_found:
#         for additional_line in additional_data:
#                 if name == additional_line[0]:
#                     data_found = True
#                     gender = additional_line[2].replace("'","").replace(",","").replace(" ","")
#     if not data_found:
#         gender = "n.a."
    

#     #new_column_names = "['name','gender','birth_date','death_date','age','birth_place','death_place','cause_of_death','musicial_skills','genres']"
#     print(f"Gender: {gender}")
#     print(f"Bday: {line[1]}")
#     print(f"['{line[0]}','{gender}','{line[1]}','{line[2]}','{line[3]}','{line[4]}','{line[5]}','{line[6]}','{line[7]}','{line[8]}']\n\n")
#     output.write(f"\n['{line[0]}','{gender}','{line[1]}','{line[2]}','{line[3]}','{line[4]}','{line[5]}','{line[6]}','{line[7]}','{line[8]}']")

for line in data:
    print(line)
    gender = line[1].replace("'","").replace(",","").replace(" ","")
    

    #new_column_names = "['name','gender','birth_date','death_date','age','birth_place','death_place','cause_of_death','musicial_skills','genres']"
    print(f"Gender: {gender}")
    print(f"Bday: {line[1]}")
    print(f"['{line[0]}','{gender}','{line[2]}','{line[3]}','{line[4]}','{line[5]}','{line[6]}','{line[7]}','{line[8]}','{line[9]}']\n\n")
    output.write(f"\n['{line[0]}','{gender}','{line[2]}','{line[3]}','{line[4]}','{line[5]}','{line[6]}','{line[7]}','{line[8]}','{line[9]}']")
