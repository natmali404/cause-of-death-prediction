import requests
import time


def search_artist(artist_name):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Referer': 'https://www.google.com/'
}
    base_url = "https://musicbrainz.org/ws/2/"
    
    
    #first api call - for artist data
    search_url = base_url + "artist" #endpoint
    params = {
        "query": artist_name,
        "fmt": "json",
    }

    response = requests.get(search_url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()

        if "artists" in data:
            try:
                if data["artists"][0]["type"] == "Person":
                    artist_data = data["artists"][0]
                else:
                    artist_data = data["artists"][1] if data["artists"][1] else None
                    #print(artist_data)
            except KeyError or TypeError:
                return None, None
        else:
            artist_data = None
    else:
        print("Primary error:", response.status_code)
        return None, None
    
    
    time.sleep(1)
    #second api call - for specific genre data
    try:
        id = artist_data["id"]
    except KeyError or TypeError:
        return None, None
    search_url = base_url + "artist/" + id #endpoint
    params = {
        "fmt": "json",
        "inc": "genres"
    }
    response = requests.get(search_url, params=params, headers=headers)
    
    if response.status_code == 200:
        genre_data = response.json()["genres"]
    else:
        print("Secondary error:", response.status_code)
        genre_data = None

    return artist_data, genre_data
    


def retrieve_names(filepath):
    names = []
    with open(filepath, "r", encoding="utf-8") as file:
        lines = file.readlines()[1:]
        for line in lines:
            line = line.strip()[1:-1]
            first_element = line.split(",")[0].strip()
            names.append(first_element)
    return names



if __name__ == "__main__":
    names = retrieve_names("../rateyourmusic_data/unified_data/valid_unified_data.txt")
    partial_result_file = open("artist_data.txt", "w", encoding="utf-8")
    full_result_file = open("artist_data_full.txt", "w", encoding="utf-8")
    partial_result_file.write(f'''['name', 'birthday', 'gender', 'genres']''')
    full_result_file.write(f'''['name', 'birthday', 'gender', 'genres']''')
    ordinal = 1
    full_successes = 0
    partial_successes = 0
    failures = 0
    for name in names:
        time.sleep(1)
        artist_data, genre_data = search_artist(name)
        if artist_data:
            begin_date = artist_data.get("life-span", {}).get("begin", "n.a.")
            gender = artist_data.get("gender", "n.a.")
            if genre_data:
                genre_names = ", ".join([genre["name"] for genre in genre_data])
                line = f"\n[{name}, '{begin_date}', '{gender}', '{genre_names}']"
                full_result_file.write(line)
                full_successes += 1
            else:
                genre_names = ""
                line = f"\n[{name}, '{begin_date}', '{gender}', '{genre_names}']"
                partial_result_file.write(line)
                partial_successes += 1
            
        else:
            print(f"Artist {name} not found.")
            failures += 1
        print(f"{ordinal}. Searched for {name}. Number of full successes: {full_successes}, number of partial successes: {partial_successes}, number of failures: {failures}.")
        ordinal += 1
