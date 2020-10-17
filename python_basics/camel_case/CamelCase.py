# ================ BlackBISS ================
# Author: Daniel Cohen Hillel, ID: 212553804

import re

def seperate_camel(s: str) -> str:
    return re.sub(r'(\w)([A-Z])', r'\1 \2', s)

if __name__ == '__main__':
    print(seperate_camel('''This is a test of CamelCase.
    My name is DanielCohenHillel. GerryHamburgary'''))
