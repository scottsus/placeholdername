"""
Formats Docusaurus notes to be compatible with Obsidian.
"""

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
    Converts Docusaurus <Image src="/attachments/IMAGE_NAME" width="{WIDTH}px"/> to 
    Obsidian ![[/static/attachments/IMAGE_NAME|WIDTH]]
    """

    pattern = r'<Image src="/attachments/(.*?)"(?: width="(\d+)px")? alt="Image"/>'
    replacement = r'![[\1' + (r'|\2' if '\2' in markdown_text else '') + r']]'
    markdown_text = re.sub(pattern, replacement, markdown_text)

    return markdown_text

def convert_color_span_style(markdown_text):
    """
    Converts Docusaurus <span style={{ color: #COLOR }}> to 
    Obsidian <span style="color: #COLOR">
    """

    pattern = r'<span style={{ color: \'#(.*?)\' }}>'

    def replace_func(match):
        color_code = match.group(1)
        return f'<span style="color: #{color_code}">'
    
    return re.sub(pattern, replace_func, markdown_text)

def compile_docusaurus_to_obsidian(file_name):
    md_file = open(file_name)
    md_file_contents = md_file.read()
    md_file.close()

    md_file = open(file_name, 'w')
    formatted_content = convert_inline_math(md_file_contents)
    formatted_content = convert_block_math_bullet(formatted_content)
    formatted_content = convert_block_math_newline(formatted_content)
    formatted_content = convert_image_path_to_square_brackets(formatted_content)
    formatted_content = convert_color_span_style(formatted_content)
    md_file.write(formatted_content)

    print(f'Docusaurus -> Obsidian {file_name}')