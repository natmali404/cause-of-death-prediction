from datetime import datetime
import pandas as pd

def calculate_age(birth_date_str, death_date_str):
    #print(f"{birth_date_str}, {death_date_str}")
    birth_date_format = "%Y-%m-%d"
    death_date_format = "%d.%m.%Y"
    if(len(death_date_str) == 4 and len(birth_date_str) == 4):
        birth_date = int(birth_date_str)
        death_date = int(death_date_str)
        age = death_date - birth_date
        return age
    elif(len(birth_date_str) == 4):
        birth_date = int(birth_date_str)
        death_date = datetime.strptime(death_date_str, death_date_format)
        age = death_date.year - birth_date
        return age
    elif(len(birth_date_str) == 7):
        birth_date = int(birth_date_str[:-3])
        death_date = datetime.strptime(death_date_str, death_date_format)
        age = death_date.year - birth_date
        return age
    elif(len(death_date_str) == 4):
        birth_date = datetime.strptime(birth_date_str, birth_date_format)
        death_date = int(death_date_str)
        age = death_date - birth_date.year
        return age
    elif(len(death_date_str) == 7):
        birth_date = datetime.strptime(birth_date_str, birth_date_format)
        death_date = int(death_date_str[4:])
        age = death_date - birth_date.year
        return age
    else:
        birth_date = datetime.strptime(birth_date_str, birth_date_format)
        death_date = datetime.strptime(death_date_str, death_date_format)
        
        age = death_date.year - birth_date.year
        
        if (death_date.month, death_date.day) < (birth_date.month, birth_date.day):
            age -= 1
        
        return age





column_names = "['name','birth_date','death_date','age','birth_place','death_place','cause_of_death','musicial_skills','genres']"


valid_data = open("rateyourmusic_data/unified_data/valid_unified_data.txt", "r", encoding="utf-8").readlines()[1:]



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


##
# excel


excel_columns = ['name','birth_date','death_date','age','birth_place','death_place','cause_of_death','musicial_skills','genres']
excel_data = []

##



#print(genre_data)

result = open("final_data.txt", "w", encoding="utf-8")
result.write(column_names)
idx = 1
for line in valid_data:
    if line == "" or line == "\n":
        continue
    #print(f"{idx}. Analysing line {line}")
    idx += 1
    line = line.strip()[1:-1].replace('"',"'").strip("'").split("', '")
    #print(line)
    name = line[0]
    death_date = line[1].replace("Ocbtober","").replace("June","").replace(" ","").replace("[/b]","")
    birth_place = line[2].replace("xa0"," ")
    death_place = line[3]
    cause_of_death = line[4]
    musicial_skills = line[5]
    #search additional genre data, if not, make genre n.a. 
    data_found = False
    #print(line)
    for additional_line in additional_data_and_genre:
        if name == additional_line[0]:
            data_found = True
            birth_date = additional_line[1].replace(" ","")
            gender = additional_line[2]
            genres = additional_line[3]
            break
    if not data_found:
        for additional_line in additional_data:
                if name == additional_line[0]:
                    #print(additional_line)
                    data_found = True
                    birth_date = additional_line[1].replace(" ","")
                    gender = additional_line[2]
                    genres = "n.a."
    if not data_found:
        birth_date = "n.a."
        gender = "n.a."
        genres = "n.a."
    
    if(birth_date == "n.a." or death_date == "n.a."):
        age = "n.a."
    else:
        age = calculate_age(birth_date, death_date)

    #column_names = "['name','birth_date','death_date','age','birth_place','death_place','cause_of_death','musicial_skills','genres']"
    excel_data.append([name, birth_date, death_date, age, birth_place, death_place, cause_of_death, musicial_skills, genres])
    result.write(f"\n['{name}', '{birth_date}', '{death_date}', '{age}', '{birth_place}', '{death_place}', '{cause_of_death}', '{musicial_skills}', '{genres}']")
    if "n.a." in (birth_date, death_date, age, birth_place, death_place):
        print(f"\n['{name}', '{birth_date}', '{death_date}', '{age}', '{birth_place}', '{death_place}', '{cause_of_death}', '{musicial_skills}', '{genres}']")

    
df = pd.DataFrame(excel_data, columns=excel_columns)
df.to_excel("musicians.xlsx", index=False)
