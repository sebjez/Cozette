# Given a script log file, find characters missing from the font

from argparse import ArgumentParser
from unicodedata import category
from pathlib import Path

default_path = Path(__file__).parent.parent / "img" / "characters.txt"
# Unicode categories excluded from search
# (control chars, whitespace)
excluded = {"Cc", "Cf", "Zs", "Zl", "Zc"}


# read file and return a set of characters
def file_to_charset(path):
    charset = set()
    with open(path, "r") as f:
        for line in f:
            for c in line:
                charset.add(c)
    return charset


# parsing cli arguments
parser = ArgumentParser(
    description="Search given file for characters missing from the font and \
    list them",
)
parser.add_argument("input_file", help="file to search for missing characters")
parser.add_argument(
    "-c",
    "--chars",
    help="file with a list of characters in the font",
    default=default_path,
)
args = parser.parse_args()


# build character sets from files
fontset = file_to_charset(args.chars)
logset = file_to_charset(args.input_file)

logset.difference_update(fontset)

for ch in logset:
    # filter out whitespace
    if category(ch) not in excluded:
        print(f"{ch}\t{hex(ord(ch))}")
