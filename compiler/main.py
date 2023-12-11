import os
import argparse
import subprocess
from obsidian_to_docusaurus import compile_obsidian_to_docusaurus
from docusaurus_to_obsidian import compile_docusaurus_to_obsidian

def get_changed_files(root_dir):
    initial_quote_path = subprocess.check_output(['git', 'config', 'core.quotePath']).decode('utf-8').strip()
    subprocess.run(['git', 'config', 'core.quotePath', 'false'])

    modified = subprocess.check_output(['git', 'ls-files', '--modified', root_dir]).decode('utf-8').splitlines()
    deleted = subprocess.check_output(['git', 'ls-files', '--deleted', root_dir]).decode('utf-8').splitlines()
    untracked = subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard', root_dir]).decode('utf-8').splitlines()

    all_files = set(modified + untracked)

    subprocess.run(['git', 'config', 'core.quotePath', initial_quote_path])

    return [f for f in all_files if f not in deleted and 
        (f.endswith('.md') or f.endswith('.md"'))]

def forward_compile(root_dir):
    """
    Converts .md files edited using Obsidian to Docusaurus format.
    """

    target_files = get_changed_files(root_dir)
    for target in target_files:
        compile_obsidian_to_docusaurus(target)

def get_all_files(root_dir):
    all_files = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                all_files.append(os.path.join(root, file))
    
    return all_files

def backward_compile(root_dir):
    """
    Converts .md files rendered by Docusaurus to Obsidian format.
    """

    target_files = get_all_files(root_dir)
    for target in target_files:
        compile_docusaurus_to_obsidian(target)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Compile Obsidian <-> Docusaurus markdown files.'
    )
    parser.add_argument('--forward', action='store_true', help='Compile Obsidian -> Docusaurus')
    parser.add_argument('--backward', action='store_true', help='Compile Docusaurus -> Obsidian')
    args = parser.parse_args()

    if args.forward and args.backward:
        raise Exception('Cannot compile both ways')
    
    # Always compile backwards
    backward_compile('./blog')
    backward_compile('./docs')
    
    if not args.backward:
        forward_compile('./blog')
        forward_compile('./docs')
        