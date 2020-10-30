import requests
from bs4 import BeautifulSoup
import os

source_files = []

for subdir, dirs, files in os.walk('../data/2019'):
    for filename in files:
        filepath = "/" + subdir.split("\\")[1] + "/" + filename
        source_files.append(filepath)


# for x in range(0, len(source_files)):
#     fr = open("../data/2019/" + source_files[x], "r")
#     lines = fr.readlines()

#     for i in range(0, len(lines)):
#         if "<!--" in lines[i]:
#             lines[i] = "\n"
#         elif "-->" in lines[i]:
#             lines[i] = "\n"

#     a_file = open("../data/2019/" + source_files[x], "w")
#     a_file.writelines(lines)
#     a_file.close()
#     fr.close()

for x in range(0, len(source_files)):
    fr = open("../data/2019/" + source_files[x], "r")
    lines = fr.readlines()

    for i in range(0, len(lines)):
        if "kick failed" in lines[i]:
            lines[i] = "\n"

    a_file = open("../data/2019/" + source_files[x], "w")
    a_file.writelines(lines)
    a_file.close()
    fr.close()
