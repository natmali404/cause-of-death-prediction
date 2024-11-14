output_file = open("unified_data/valid_unified_data.txt", "w", encoding="utf-8")
range_start = 1
range_end = 20

output_file.write('''['name', 'date_of_death', 'birthplace', 'deathplace', 'cause_of_death', 'musical_skills']''')

total_lines = 0

for i in range(range_start, range_end + 1):
    with open(f"extracted_data/result{i}.txt", "r", encoding='utf-8') as input_file:
        lines = input_file.readlines()[1:]
        filtered_lines = [line for line in lines if "n.a." not in line]
        total_lines += len(filtered_lines)
        output_file.write("\n")
        output_file.writelines(filtered_lines)
        
print(f"A total of {total_lines} lines have been written to the valid_unified_data.txt file.")