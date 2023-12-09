"""
Formats notes taken in Obsidian to be compatible with Docusaurus.
"""

import re

def convert_inline_math(markdown_text):
    """
    Convert inline math in newline: '\t$' to '$\\'
    Constraint: the '$' cannot be followed by '\\\\' or '\n'
    """
    
    newline_pattern = r'(?<=\t\$)(?!\\\\|\n)'
    newline_replacement = r'\\\\ '
    markdown_text = re.sub(newline_pattern, newline_replacement, markdown_text)    

    return markdown_text

def convert_block_math_bullet(markdown_text):
    """
    Convert block math under bullet point: ' $$' to '\n\n\t$'
    """

    pattern = r' \$\$([^\$]+)\$\$'

    def replace_func(match):
        # Extracting the content inside $$
        content = match.group(1).strip()
        content = content.replace('flalign', 'aligned')
        return '\n\n\t$\n\t' + content + '\n\t$'

    modified_text = re.sub(pattern, replace_func, markdown_text)

    return modified_text

def convert_block_math_newline(markdown_text):
    """
    Convert block math in newline: '$$' to '$'
    """

    pattern = r'\$\$([^\$]+)\$\$'

    def replace_func(match):
        # Extracting the content inside $$
        content = match.group(1).strip()
        content = content.replace('flalign', 'aligned')
        return '\n$\n' + content + '\n$\n'

    modified_text = re.sub(pattern, replace_func, markdown_text)

    return modified_text

def convert_square_brackets_to_image_path(markdown_text):
    """
    Converts obsidian ![[IMAGE_NAME]] to 
     - ![Image](/static/attachments/IMAGE_NAME) OR
     - <Image src="/attachments/IMAGE_NAME" width="{WIDTH}px"/>
    depending on whether or not a width was provided.
    """

    pattern = r'!\[\[(.*?)\]\]'

    def replace_with_path(match):
        image_name = match.group(1)
        image_name = image_name.replace(' ', '%')

        image_name_parts = image_name.split('|')
        if (len(image_name_parts) > 1):
            return f'<Image src="/attachments/{image_name_parts[0]}" width="{image_name_parts[1]}px"/>'
        
        return f'![Image](/attachments/{image_name})'

    return re.sub(pattern, replace_with_path, markdown_text)

def convert_color_span_style(markdown_text):
    """
    Converts <span style="color:#f55656"> to <span style:{{ color: '#f55656' }}>
    """

    # Define the regex pattern to match the color style
    pattern = r'<span style="color:(.*?)">'

    # Function to replace the matched pattern
    def replace_with_new_style(match):
        color_code = match.group(1)
        return f'<span style={{{{ color: \'{color_code}\' }}}}>'

    # Use re.sub to replace all occurrences of the pattern
    return re.sub(pattern, replace_with_new_style, markdown_text)

def format(file_name):
    md_file = open(file_name)
    md_file_contents = md_file.read()
    md_file.close()

    md_file = open(file_name, 'w')
    formatted_content = convert_inline_math(md_file_contents)
    formatted_content = convert_block_math_bullet(formatted_content)
    formatted_content = convert_block_math_newline(formatted_content)
    formatted_content = convert_square_brackets_to_image_path(formatted_content)
    formatted_content = convert_color_span_style(formatted_content)
    md_file.write(formatted_content)

if __name__ == '__main__':
    file_name = "blah.md"
    format(file_name)
