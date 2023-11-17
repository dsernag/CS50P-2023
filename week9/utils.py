import re

def replace_double_space(string : str) -> str:
    return re.sub(r'\s+', ' ', string)

def parse_song_name(input_entry : dict):
    return replace_double_space(input_entry["song"]) + "-" + replace_double_space(input_entry["artist"])
