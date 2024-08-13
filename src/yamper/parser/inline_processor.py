import re
from .emoji_dict import EMOJI_DICT

def process_inline_text(text):
    text = re.sub(r'(\*\*(.+?)\*\*)|(__(.+?)__)', r'<strong>\2\4</strong>', text)
    text = re.sub(r'(\*(.+?)\*)|(_(.+?)_)', r'<em>\2\4</em>', text)
    text= re.sub(r'~~(\s*[\s\S]*?\s*)~~', r'<s>\1</s>', text)
    text = re.sub(r'<!--[\s\S]*?-->', '', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r':([a-zA-Z0-9_+-]+):', replace_emoji, text)
    text = re.sub(r'!\[(?P<alt>[^\]]*)\]\((?P<src>[^\s]+)(?:\s+"(?P<title>[^"]*)")?\)', r'<img src="\g<src>" alt="\g<alt>" title="\g<title>" />', text)
    text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', text)
    return text

def replace_emoji(match):
    shortcode = match.group(1)
    emoji_value = EMOJI_DICT.get(shortcode)
    
    if emoji_value is None:
        return f":{shortcode}:"
    elif emoji_value.startswith('http'):
        return f'<img src="{emoji_value}" alt="{shortcode}" />'
    else:
        return emoji_value