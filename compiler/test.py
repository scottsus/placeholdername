import re

md = """
### Power
- Instantaneous power
\t$p(t) = v(t)i(t) = V_{supply}i(t)$
- Peak power
    $P_{peak} = V_{supply} i_{peak}$
- Average power
    $P_{ave} = \frac 1T \int_t^{t+T} p(t) dt$
    $= \frac {V_{supply}}T \int_t^{t+T} i_{supply}(t) dt$
"""

def convert_inline_math(markdown_text):
    """
    Convert inline math in newline: '\t$' to '$\\'
    Constraint: the '$' cannot be followed by '\\\\' or '\n'
    """
    
    newline_pattern = r'(?<=\t\$)(?!\\\\|\n|\$)'
    newline_replacement = r'\\\\ '
    markdown_text = re.sub(newline_pattern, newline_replacement, markdown_text)    

    return markdown_text

print(convert_inline_math(md))