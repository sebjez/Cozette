import requests
from pathlib import Path
import json
import unicodedata

_json_path = Path(__file__).parent / "glyphnames.json"
_download_url = "https://raw.githubusercontent.com/ryanoasis/nerd-fonts/refs/heads/master/glyphnames.json"


def _download_json():
    print("Downloading glyphnames.json from nerd-fonts repo")
    r = requests.get(_download_url)
    r.raise_for_status()
    with open(_json_path, "w") as file:
        file.write(r.text)
    return r.json()


if _json_path.exists():
    with open(_json_path, "r") as file:
        _j = json.load(file)
else:
    _j = _download_json()


_nerd_glyphs_dict = {}

for name, data in _j.items():
    try:
        char = data["char"]
        _nerd_glyphs_dict[char] = name
    except KeyError:
        continue


def char_name(char):
    try:
        n = _nerd_glyphs_dict[char]
    except KeyError:
        n = unicodedata.name(char, "<NO NAME FOUND>")
    return n
