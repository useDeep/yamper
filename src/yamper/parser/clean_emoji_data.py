import json
import os

cur_dir= os.path.dirname(__file__)
file_path= os.path.join(cur_dir, 'emoji_dict.py')

with open(file_path, 'r') as file:
    emoji_data= json.load(file)

url_prefix = "https://github.githubassets.com/images/icons/emoji/unicode/"
url_suffix = ".png?v8"

unicode_data= {}

for key, url in emoji_data.items():
    if url.startswith(url_prefix):
        unicode= url.replace(url_prefix, "").replace(url_suffix, "")
        if '-' in unicode:
            unicodes= unicode.split('-')
            unicode_data[key]= '-'.join([f"&#{part};" for part in unicodes])
        else:
            unicode_data[key]= f"&#x{unicode};"
    else:
        unicode_data[key]= url

with open(file_path, 'w') as file:
    json.dump(unicode_data, file, indent=4)
