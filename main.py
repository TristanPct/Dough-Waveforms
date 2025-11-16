import os
import json

def generate_json():
    pitch = "d2"
    data = {
        "_base": "https://raw.githubusercontent.com/Bubobubobubobubo/Dough-Waveforms/main/"
    }
    
    # Iterate through each directory in the current folder
    for dir_name, _, file_list in os.walk('.'):
        dir_name = dir_name[2:] # Remove the './' from the directory name
        if not dir_name.startswith('wt_'): # Keep only WaveTables directories
            continue
        data[dir_name] = {pitch: []}
        for file_name in file_list:
            if file_name.lower().endswith('.wav'):
                data[dir_name][pitch].append(f"{dir_name}/{file_name}")
    with open('strudel.json', 'w') as json_file:
        # Minify if possible
        json.dump(data, json_file, separators=(',', ':'))

if __name__ == "__main__":
    generate_json()

