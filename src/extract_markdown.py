import re


def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)" # matches alt text and url
    matches = re.findall(pattern,text)
    results = []
    if matches:
        for match in matches:
            touple = (match[0],match[1])
            results.append(touple)
        return results
    else:
        raise Exception(f"No matches found in your input\n Input: {text}")

def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)" #matches aanchor text and link
    matches = re.findall(pattern,text)
    results = []
    if matches:
        for match in matches:
            touple = (match[0],match[1])
            results.append(touple)
        return results
    else:
        raise Exception(f"No matches found in your input\n Input: {text}")


text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
text2 = "This is text with a [link to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

print(extract_markdown_links(text2))