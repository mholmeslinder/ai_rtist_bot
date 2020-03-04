# generate_artist.py
import random

artist_names = "./data/artist_names.txt"
new_artist_names = "./data/new_artist_names.txt"


def get_tweet():
    choices = get_choices()
    return f''''One of these two is a real life recording artist, and one was generated by a neural network:

{choices[0]} or {choices[1]} 
    
- which one is real?? Reply with your guess.'''


# generate a choice between two artists: which one is real?
def get_choices():
    # real_artist -get random line from artist_names that's NOT in used_artists
    real_artist = random_name(artist_names)
    # fake_artist - same process for new_artist_names
    fake_artist = random_name(new_artist_names)
    choices = [real_artist, fake_artist]
    random.shuffle(choices)
    return choices


def random_name(fname):
    with open("./data/used_artist_file.txt", "+a") as used_artist_file:
        names = open(fname).read().splitlines()
        used_names = used_artist_file.read().splitlines()
        name = random.choice(names)  

        if name not in used_names:
            used_artist_file.write(f'{name}\n')
            return name
        else:     
            random_name(fname)

# for testing
if __name__ == '__main__':
    print(get_tweet())
