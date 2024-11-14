from bs4 import BeautifulSoup
#soup_title = soup.findAll("td",{"class":"main_entry"})
#f.write(str(soup_title))

range_start = 1
range_end = 20

for i in range(range_start, range_end + 1):
    with open(f"data/result{i}.txt", "r", encoding='utf-8') as input_file:
        initial_content = BeautifulSoup(input_file, "html.parser")
        found_classes = initial_content.findAll("td", {"class": "main_entry"})
        initial_result = []
        for element in found_classes:
            prettified_element = BeautifulSoup(str(element), "html.parser").prettify()
            initial_result.append(prettified_element)
            
        #initial result now contains extracted classes for each artist.
        
        artists = "".join(initial_result).split("</td>")[:-1]

        with open(f"extracted_data/result{i}.txt", "w", encoding='utf-8', errors='replace') as output_file:
            output_file.write('''['name', 'date_of_death', 'birthplace', 'deathplace', 'cause_of_death', 'musical_skills']''')
            for artist in artists:
                soup = BeautifulSoup(artist, "html.parser")

                filtered = ['']
                my_list = soup.get_text().splitlines()
                my_list = [x.strip() for x in my_list if x.strip() not in filtered]
                
                if my_list[2] == "a.k.a:":
                    my_list = my_list[:2] + my_list[4:]
                    
                
                #print(my_list)
                try:
                    artist_name = my_list[1]
                    date_of_death = my_list[2].split(":")[1].strip()
                    
                    birthplace_details = my_list[4].replace('\xa0', ' ').split(" ")
                    birthplace = birthplace_details[len(birthplace_details) - 1]
                    
                    deathplace_details = my_list[6].replace('\xa0', ' ').split(" ")
                    deathplace = deathplace_details[len(deathplace_details) - 1]
                    
                    cause_of_death = my_list[8].replace('\xa0', ' ')
                    
                    musical_skills_position = my_list.index("musical skill:")
                    musical_skills = my_list[musical_skills_position + 1].replace('\xa0', ' ')
                    
                except IndexError:
                    continue
                
                result_to_write = [artist_name, date_of_death, birthplace, deathplace, cause_of_death, musical_skills]
                output_file.write(f"\n{result_to_write}")
                
