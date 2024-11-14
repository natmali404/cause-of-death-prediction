import random

data_file = open("final_data_fix3.txt", "r", encoding="utf-8").readlines()[1:]
output = open("simplified_data.txt", "w", encoding="utf-8")
overall_output = open("simplified_data_overall.txt", "w", encoding="utf-8")
genre_output = open("simplified_data_genres.txt", "w", encoding="utf-8")
skills_output = open("simplified_data_skills.txt", "w", encoding="utf-8")

new_column_names = "['gender','age','birth_place','death_place','cause_of_death','musicial_skills','genres']"

overall_output.write("['gender','age','birth_place','death_place','cause_of_death','musical_skills','genres']")
skills_output.write("['gender','age','birth_place','death_place','cause_of_death','musical_skills']")
genre_output.write("['gender','age','birth_place','death_place','cause_of_death','genres']")

data = []

for line in data_file:
    new_line = line.strip()[1:-1].strip("'").split("','")
    data.append(new_line)
    
gender_count = 0
age_count = 0
for line in data:
    if line[1] == "n.a.":
        gender_count += 1
    if line[4] == "n.a.":
        age_count +=1 
        
print(f"Empty age count: {age_count}")
print(f"Empty gender count: {gender_count}")


death_causes_dictionary = {
    "suicide": ["suicide"],
    "AIDS": ["AIDS"],
    "overdose": ["cocaine", "heroin", "overdose","Fentanyl","drugs","narcotics","drug","drug-induced","drug-related","alcohol", "alcoholism"],
    "natural causes": ["natural", "sleep", "age", "aged"],
    "cancer": ["cancer", "tumor", "tumour"],
    "diabetes": ["diabetes"],
    "heart attack": ["heart attack", "heart failure", "heart disease", "heat attack", "heart problems", "heart thrombosis", "cardiac", "seizure"],
    "pneumonia": ["pneumonia"],
    "tuberculosis": ["tuberculosis"],
    "accident": ["car accident", "struck by", "single-car accident", "crash", "accident", "fire", "collapse", "stairs", "drowned","sea","drown", "falling", "electrocution"],
    "stroke": ["stroke", "brain aneurysm", "strokes","aneurysm"],
    "organ failure": ["liver failure", "liver disease","kidney failure", "kidney disease", "failure", "brain", "organ"],
    "murder": ["murder", "murdered", "shot", "fight"],
    "illness": ["infection", "complications", "asthma", "peritonitis", "AIDS", "ALS", "cirrhosis", "multiple myeloma", "progressive supranuclear palsy", "dimentia", "cardiomegaly", "multiple sclerosis", "tuberculosis", "sepsis", "hepatitis", "COPD", "emphysema", "illness", "pneumonia", "COVID-19", "diabetes", "lymphoma", "Alzheimer", "pulmonary embolism", "leukemia", "bronchiectasis", "myeloma", "following","polio", "meningitis", "spondylosis", "declining", "surgery"]
    
}

skills_dictionary = {
    "vocals": ["vocals","singer","voice", "Vocal", "vocal", "Voice", "Vocals", "Lyrics","narrator", "sopran", "whistle"],
    "guitar": ["guitar", "banjo", "mandolin", "sitar", "fiddle", "dobro", "pedal steel", "ukulele",
        "lavta", "baglama", "qanun", "cura", "sanzur", "dombra", "komuz", "oud",
        "tambur", "bouzuki", "kora", "dulcimer", "autoharp", "harp", "Guitar",
        "cellist"],
    "drums": ["drums", "percussion", "vibraphone", "vibes", "maracas", "congas", "tambourine", "bongos",
        "bells", "gong", "tubular bells", "timbal", "slapsticks", "orchestra bells",
        "handclapsandfingasnaps", "brush trap", "wind chimes", "tree bell", "finga Cymbals",
        "woodblocks", "spoons", "tabor", "conga drum", "BooBams", "timpany", "mallets",
        "table", "percussian", "marimba"],
    "bass": ["bass","Bass"],
    "rapper": ["rapper", "rapping"],
    "piano": ["piano", "e-piano", "organ", "synthesizer", "keyboards", "keyboard", "mellotron", "harpsichord", "keybords", "melodica", "harmonium", "clavinet",
        "mini-moog", "Oberheim", "Moog Synthesizer", "keys"],
    "trumpet": ["trumpet", "trombone", "horn","Horn", "pipes"],
    "flute": ["flute", "clarinet", "oboe", "didgeridoo"],
    "leadership": ["conductor", "bandleader", "producer","composer"],
    "saxophone": ["saxophone","Saxophone","sax", "harmonica"],
    "strings": ["violin", "cello", "viola", "strings"]
}

genres_dictionary = {
    "hip hop": ["rap", "emo rap", "gangsta rap", "hip hop"],
    "pop": ["pop", "easy listening", "pop rock", "brill building"],
    "rock": ["symphonic prog", "neo-psychedelia", "neue deutsche welle", "metal", "rock", "post-punk","new-wave","punk", "new wave", "grunge", "new age", "avant-garde", "aor"],
    "jazz": ["jazz", "swing", "big band", "dixieland", "honky tonk", "jam band"],
    "soul": ["soul", "funk", "blues","bop","r&b","R&B", "doo-wop", "quiet storm", "reggae", "afrobeat", "ska", "dub", "boogie-woogie"],
    "electronic": ["bassline", "trance", "psychedelic", "modern creative", "berlin school", "production music", "electronic","electro","disco", "experimental", "DJ", "ambient", "dance"],
    "folk": ["guaracha", "Tejano","latin", "salsa", "flamenco", "minneapolis sound", "tex-mex", "boogie", "nashville sound", "americana", "schlager","gospel","folk","country", "christmas music","ballad", "bluegrass", "spoken word", "poetry"],
    "classical": ["classical", "opera", "orchestra", "symphony", "chamber music"]
    
}


for line in data:
    #simplify death causes
    death_causes = line[7].split(",")
    found = False
    for cause in death_causes_dictionary:
        for fragment in death_causes_dictionary[cause]:
            for singular_cause in death_causes:
                if fragment in singular_cause:
                    line[7] = cause
                    found = True
                    break
    if not found:
        line[7] = "n.a."
    
    #simplify musicial skills
    skills = line[8].split(",")
    for i in range(len(skills)):
        skills[i] = skills[i].strip()
    simplified_skills = []
    for skill in skills:
        found = False
        for category, items in skills_dictionary.items():
            for item in items:
                if item in skill:
                    simplified_skills.append(category)
                    found = True
                    break
            if found:
                break
    if not found and simplified_skills == []:
        simplified_skills.append("n.a.")
    line[8] = ",".join(set(simplified_skills))  #remove duplicates
    

    #simplify genres
    genres = line[9].split(",")
    for i in range(len(genres)):
        genres[i] = genres[i].strip()
    simplified_genres = []
    for genre in genres:
        found = False
        for category, items in genres_dictionary.items():
            for item in items:
                if item in genre:
                    simplified_genres.append(category)
                    found = True
                    break
            if found:
                break
    if not found and simplified_genres == []:
        simplified_genres.append("n.a.")
    line[9] = ",".join(set(simplified_genres))  #remove duplicates


output.write(f"['gender','age','birth_place','death_place','cause_of_death','musical_skills','genres']")

genders = [0,0]
total_counter = 0 
genre_counter = 0
for line in data:
    if line[7] == "n.a." or line[8] == "n.a.":
        continue
    if line[1] == "male" :
        genders[0] = genders[0] + 1
    elif line[1] == "female":
        genders[1] = genders[1] + 1
    else:
        line[1] = random.choice(["male","female"])
    if line[4] == "n.a." or len(line[4]) > 2 or int(line[4]) > 90 or int(line[4]) < 20:
        line[4] = random.randint(30,70)
    #print(f"['{line[1]}','{line[4]}','{line[5]}','{line[6]}','{line[7]}','{line[8]}','{line[9]}']\n\n")
    output.write(f"\n['{line[1]}','{line[4]}','{line[5]}','{line[6]}','{line[7]}','{line[8]}','{line[9]}']")
    #new_column_names = "['gender','age','birth_place','death_place','cause_of_death','musicial_skills','genres']"
    skills = line[8].split(",")
    genres = line[9].split(",")
    for skill in skills:
        if skill == "n.a.":
            continue
        total_counter += 1
        #skills_output.write(f"\n['{line[1]}','{line[4]}','{line[5]}','{line[6]}','{line[7]}','{skill}']")   
        for genre in genres:
            #total_counter += 1
            if genre != "n.a.":
                genre_counter += 1
                overall_output.write(f"\n['{line[1]}','{line[4]}','{line[5]}','{line[6]}','{line[7]}','{skill}','{genre}']")
        skills_output.write(f"\n['{line[1]}','{line[4]}','{line[5]}','{line[6]}','{line[7]}','{skill}']")
    for genre in genres:
        if genre != "n.a.":
            genre_output.write(f"\n['{line[1]}','{line[4]}','{line[5]}','{line[6]}','{line[7]}','{genre}']")

    
    #output.write(f"\n['{line[1]}','{line[4]}','{line[5]}','{line[6]}','{line[7]}','{line[8]}','{line[9]}']")
        

print(f"Total data written: {total_counter}, including data with genres: {genre_counter}.")
print(f"Males: {genders[0]}, females: {genders[1]}.")
