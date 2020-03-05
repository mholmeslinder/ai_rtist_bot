import os

def cleaner():
    dir = "./raw" # real
    data_file = open("./raw/artist_names.txt", 'r') # real

    # make list out of dataset, so we can check against it
    dataset =[]
    for line in data_file:
        dataset.append(line.strip())

    # make list from all names in all raw gpt2 output files
    raw_list = []
    for dir, subdir, files in os.walk(dir):
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(dir, file), 'r') as raw_file:
                    for line in raw_file:
                        # this '===...' weirdness comes from a 
                        # weird quirk of gpt2 output
                        if '====================' not in line:  
                            raw_list.append(line.strip())

    # compare each item in GPT-2 output to see if it is in dataset
    # if it's NOT in dataset, write to new list/file
    # TODO implement casefold or some other method to check for near-matches?
    new_artists = set([x for x in raw_list if x not in dataset])
    with open("./new_artist_names.txt", '+a') as dump_file:
        for item in new_artists:
            dump_file.write(item + '\n')

    data_file.close()

if __name__ == '__main__':
    cleaner()
