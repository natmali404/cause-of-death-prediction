data_file = open("simplified_data.txt", "r", encoding="utf-8").readlines()[1:]
output = open("all_genres.txt", "w", encoding="utf-8")

data = []

for line in data_file:
    new_line = line.strip()[1:-1].strip("'").split("','")
    data.append(new_line)
    
    
genres = {}


for element in data:
    artist_genres = element[6].split(",")
    artist_genres = [elem.strip() for elem in artist_genres]
    for genre in artist_genres:
        if genre not in genres:
            genres[genre] = 1
        else:    
            genres[genre] += 1

            

sorted_genres = sorted(genres.items(), key=lambda item: item[1], reverse=True)

for genre, count in sorted_genres:
    output.write(f"{genre}: {count}\n")