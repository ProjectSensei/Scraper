# RegEx library
import re
import json

# RegEx patterns
def convert(a):
    pattern_for_title_and_episode = re.compile(r"^[^;]*?&title=|\W*&.*$")
    pattern_for_title = re.compile(r"^[^;]*?&title=|(?=\+episode).*$")
    pattern_for_episode = re.compile(r"^[^;]*?&title=|.+?(?=episode)|(?<=\+episode\+\d).*$", re.IGNORECASE)

# Target link (must be dynamic)

# Converters
    anime_title_and_episode_orig = pattern_for_title_and_episode.sub('', a) # RegEx
    anime_title_and_episode_formatted = anime_title_and_episode_orig.replace('+', ' ') # Remove + signs

    anime_title_orig = pattern_for_title.sub('', a) # RegEx
    anime_title_formatted = anime_title_orig.replace('+', ' ') # Remove + signs

    anime_episode_orig = pattern_for_episode.sub('', a) # RegEx
    anime_episode_formatted = anime_episode_orig.replace('+', ' ') # Remove + signs

    return anime_title_formatted, anime_episode_formatted
