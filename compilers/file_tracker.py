import os
import subprocess
from obsidian_to_docusaurus import compile_obsidian_to_docusaurus
from docusaurus_to_obsidian import compile_docusaurus_to_obsidian

def get_changed_files(root_dir):
    modified = subprocess.check_output(['git', 'ls-files', '--modified', root_dir]).decode('utf-8').splitlines()
    deleted = subprocess.check_output(['git', 'ls-files', '--deleted', root_dir]).decode('utf-8').splitlines()
    untracked = subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard', root_dir]).decode('utf-8').splitlines()

    all_files = set(modified + untracked)

    return [f for f in all_files if f not in deleted and 
        (f.endswith('.md') or f.endswith('.md"'))]

def forward_compile(root_dir):
    """
    Converts .md files edited using Obsidian to Docusaurus format.
    """

    target_files = get_changed_files(root_dir)
    for target in target_files:
        compile_obsidian_to_docusaurus(target)

def backward_compile(root_dir):
    """
    Converts .md files rendered by Docusaurus to Obsidian format.
    """

    target_files = get_changed_files(root_dir)
    for target in target_files:
        compile_docusaurus_to_obsidian(target)

if __name__ == '__main__':
    # backward_compile('./blog')
    # backward_compile('./docs')

    forward_compile('./blog')
    forward_compile('./docs')