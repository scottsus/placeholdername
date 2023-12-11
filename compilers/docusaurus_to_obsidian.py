"""
Formats Docusaurus notes to be compatible with Obsidian.
"""

import sys
import re

def convert_inline_math(markdown_text):
    """
    Convert inline math: '$\\ ' to '$'
    """

    pattern = r'\$\\{2}\s?'
    replacement = '$'
    markdown_text = re.sub(pattern, replacement, markdown_text)

    return markdown_text

def convert_block_math_bullet(markdown_text):
    """
    Convert block math under bullet point: '\n\n\t$\n' to ' $$'
    """

    pattern = r'\n\n\t\$\n([^\$]+)\$'

    def replace_func(match):
        # Extracting the content inside $$
        content = match.group(1).strip()
        content = content.replace('aligned', 'flalign')
        return ' $$\n\t' + content + '\n\t$$'

    modified_text = re.sub(pattern, replace_func, markdown_text)

    return modified_text

def convert_block_math_newline(markdown_text):
    """
    Convert block math in newline: '\n$\n' to '$$\n'
    """

    pattern = r'\n\$\n([^\$]+)\$\n'

    def replace_func(match):
        # Extracting the content inside $$
        content = match.group(1).strip()
        content = content.replace('aligned', 'flalign')
        return '$$\n' + content + '\n$$'

    modified_text = re.sub(pattern, replace_func, markdown_text)

    return modified_text

def convert_image_path_to_square_brackets(markdown_text):
    """
    Converts Docusaurus:
     - ![Image](/attachments/IMAGE_NAME) OR
     - <Image src="/attachments/IMAGE_NAME" width="{WIDTH}px"/>
    to Obsidian ![[IMAGE_NAME|WIDTH]]
    """

    # Pattern for ![Image](/attachments/IMAGE_NAME)
    # Replace with Obsidian format ![[IMAGE_NAME]]
    pattern1 = r'!\[.*?\]\(/attachments/(.*?)\)'
    markdown_text = re.sub(pattern1, r'![[\1]]', markdown_text)

    # Pattern for <Image src="/attachments/IMAGE_NAME" width="{WIDTH}px"/>
    # Replace with Obsidian format ![[IMAGE_NAME|WIDTH]]
    pattern2 = r'<Image src="/attachments/(.*?)" width="\{(\d+)px\}"/>'
    markdown_text = re.sub(pattern2, r'![[\1|\2]]', markdown_text)

    return markdown_text

def compile_docusaurus_to_obsidian(file_name):
    md_file = open(file_name)
    md_file_contents = md_file.read()
    md_file.close()

    md_file = open(file_name, 'w')
    formatted_content = convert_inline_math(md_file_contents)
    formatted_content = convert_block_math_bullet(formatted_content)
    formatted_content = convert_block_math_newline(formatted_content)
    formatted_content = convert_image_path_to_square_brackets(formatted_content)
    md_file.write(formatted_content)

    print(f'Docusaurus -> Obsidian {file_name}')