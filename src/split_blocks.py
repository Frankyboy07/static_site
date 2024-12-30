with open("example_block.md",'r') as file:
    file_contents = file.read()
import re
def markdown_to_blocks(markdown):
    current_block = []
    blocks = []
    for line in markdown.split("\n"):
        if line != "":
            current_block.append(line.strip())
        else:
            if len(current_block) > 0:
                blocks.append("\n".join(current_block))
                current_block = []
    if current_block:        
        blocks.append("\n".join(current_block))
    return blocks

def block_to_block_type(markdown_block):
    if check_for_heading(markdown_block):
        return "heading"
    elif check_for_code(markdown_block):
        return "code"
    elif check_for_ordered_list(markdown_block):
        return "ordered_list"
    elif check_for_unorded_list(markdown_block):
        return "unordered_list"
    elif check_for_quote(markdown_block):
        return "quote"
    else:
        return "normal text"
    

def check_for_heading(markdown_block):
    if len(markdown_block) < 2:
        return None
    hash_count = markdown_block[0:6].count("#")
    first_chars = markdown_block[:hash_count]
    if hash_count < 1 or hash_count > 6 or len(markdown_block) <= hash_count:
        return None
        
    if first_chars != "#" * hash_count:
        return None
    elif markdown_block[hash_count] == " ":
        return True

def check_for_quote(markdown_block):
    lines = markdown_block.split("\n")
    results = []
    for line in lines:
        results.append(line.startswith(">"))
    if all(results):
        return True
    else:
        return None
    
def check_for_code(markdown_block):
        if len(markdown_block) < 6:
            return None
        if markdown_block.startswith("```") and markdown_block.endswith("```"):
            return True

def check_for_unorded_list(markdown_block):
    if len(markdown_block) < 2:
        return None
    results = []
    marker = None
    lines = markdown_block.split("\n")
    if lines[0][0:2] == "* ":
        marker = "*"
    if lines[0][0:2] == "- ":
        marker = "-"
    for line in lines:
        if marker is not None: 
            if line.startswith(f"{marker} "):
                results.append(True)
            else:
                results.append(False)
        if not line.startswith(f"{marker} "):
            results.append(False)
           
    if all(results):
        return True
    
def check_for_ordered_list(markdown_block):
    lines = markdown_block.split("\n")
    for index, line in enumerate(lines):
        if not line.startswith(f"{index + 1}. "):
            return None  # Not an ordered list
    return True
    


test_header = "### Header"
test_cases = [
    "# Heading",
    "### Bigger Heading",
    "#Not a heading",  # (no space after #)
    "# # Not a heading",  # (non-consecutive #)
    "#######Too many",  # (more than 6 #)
    "# This is a heading with a # in it",  # Should be a heading
    "####### Too many #s",  # Should not be a heading
    "#This isn't a heading",  # Should not be a heading
]

test_cases2 = [
    "# Heading",              # Should be heading
    "## Heading",             # Should be heading
    "# # Heading",           # Should not be heading
    "#",                     # Should not be heading (no space after)
    "####### Heading",       # Should not be heading (too many #)
    "Regular paragraph"      # Should not be heading
]

test_cases_quotes = [
    ">This is a quote",                    # Should be quote
    ">Line 1\n>Line 2",                    # Should be quote
    ">Line 1\n>Line 2\n>Line 3",          # Should be quote
    ">Line 1\nThis is not a quote",        # Should NOT be quote
    "This is not a quote",                 # Should NOT be quote
    "> Line 1\n>Line 2",                   # Should be quote (space after > is okay)
    "",                                    # Should NOT be quote (empty string)
    ">",                                   # Should be quote (single >)
]

test_cases_code = [
    "```\ncode here\n```",              # Should be code
    "```\nmulti\nline\ncode\n```",      # Should be code
    "```code```",                       # Should be code
    "```incomplete",                    # Should NOT be code
    "not code```",                      # Should NOT be code
    "`not code`",                       # Should NOT be code
    "``not code``",                     # Should NOT be code
    "",                                 # Should NOT be code
    "```\n```",                         # Should be code (empty code block)
]


test_cases_unordered_list = [
    "* Item 1\n* Item 2",              # Should be unordered_list
    "- Item 1\n- Item 2",              # Should be unordered_list
    "* Item 1\n- Item 2",              # Should NOT be unordered_list (mixed markers)
    "*Not a list",                     # Should NOT be unordered_list (no space after *)
    "-Not a list",                     # Should NOT be unordered_list (no space after -)
    "* Item 1\nNot a list",           # Should NOT be unordered_list (inconsistent)
    "",                               # Should NOT be unordered_list (empty)
    "* ",                             # Should be unordered_list (single empty item)
    "* Item 1\n* Item 2\n* Item 3",   # Should be unordered_list (three items)
    "*",                              # Should NOT be unordered_list (no space)
    "- Item 1\n-Item 2"               # Should NOT be unordered_list (missing space)
]

test_cases_ordered_list = [
    "1. First item\n2. Second item",         # Should be ordered_list
    "1. First item\n3. Second item",         # Should NOT be ordered_list
    "1. First item\n2. Second item\n3. Third item",  # Should be ordered_list
    "1. First item\n- A dashed item\n2. Second item",# Should NOT be ordered_list
    "1. First item\n- A break",              # Should NOT be ordered_list
    "1. Only one item",                      # Should be ordered_list
    "",                                      # Should NOT be ordered_list
    "1. First item\n2. Second item\n4. Fourth item", # Should NOT be ordered_list
]

test_cases = [
    "## Heading Example",                # Should be "heading"
    "```\nCode block\n```",              # Should be "code"
    "> This is a quote\n> More quote",   # Should be "quote"
    "* Unordered list item 1\n* Unordered list item 2",  # Should be "unordered_list"
    "- Another unordered list item\n- Yet another item", # Also "unordered_list"
    "1. Ordered list item 1\n2. Ordered list item 2",    # Should be "ordered_list"
    "Just a simple text paragraph.",     # Should be "normal text"
    "Hello World!",                      # Should be "normal text"
    "## Heading\n\n- List item\n\n1. Ordered item", # First line is "heading", Subsequent checks apply per block
    "Invalid **Markdown** text",         # Should be "normal text"
]

# Sample usage
for case in test_cases:
    block_type = block_to_block_type(case)
    print(f"Input: {case}\nDetected Block Type: {block_type}\n")
