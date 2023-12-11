import re

markdown_text = '<Image src="/attachments/IMG-20231207175829.png" width="300px"/>'

pattern2 = r'<Image src="/attachments/(.*?)" width="(\d+)px"/>'
markdown_text = re.sub(pattern2, r'![[\1|\2]]', markdown_text)

print(markdown_text)