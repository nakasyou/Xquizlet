import csv
import re

config_key_regex = re.compile(r"__.+__")

def get_config():
    with open("./xquizlet.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        setting = {}
        words = {}
        for row in reader:
            if len(row) != 2: continue
            (setting if config_key_regex.sub("",row[0]) == "" else words)[row[0]] = row[1]
    return setting, words

if __name__ == "__main__":
    print(get_config())