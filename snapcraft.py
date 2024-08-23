# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:27:37 2024

@author: leao2
"""

import yaml

def generate_snapcraft_yaml():
    snapcraft_config = {
        'name': 'your-snap-name',
        'version': '0.1',
        'summary': 'A brief summary of your snap.',
        'description': 'A longer description of your snap.',
        'apps': {
            'your-app-name': {
                'command': 'bin/your-binary'
            }
        },
        'parts': {
            'your-part-name': {
                'source': '.',
                'plugin': 'python',
                'python-packages': ['your-package']
            }
        }
    }

    with open('snapcraft.yaml', 'w') as file:
        yaml.dump(snapcraft_config, file, default_flow_style=False)

    print("Snapcraft YAML configuration created.")

generate_snapcraft_yaml()
