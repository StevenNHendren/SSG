import re

def extract_markdown_images(text):
    #matches = re.findall(r"!\[([\w\s]+)\]\((https?://[\w\._/]+)\)", text)
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    #print(f"image matches: {matches}")
    return matches

def extract_markdown_links(text):
    #matches = re.findall(r"(?<!!)\[([\w\s]+)\]\((https?://[\w\._/]+)\)", text)
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    #print(f"link matches: {matches}")
    return matches
