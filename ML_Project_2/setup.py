# Run the build process by running the command 'python setup.py build'

import sys
from cx_Freeze import setup, Executable

options = {
    'build_exe': {
        'include_files': [
            'images/background.png',
            'sounds/shot_sound.wav',
            'sounds/background.wav',
            'images/aim_pointer.png',
            'images/gun_1.png',
            'images/zombie_1.png',
            'images/zombie_2.png',
            'images/zombie_3.png',
            'images/zombie_4.png'
        ],
        'path': sys.path + ['modules']
    }
}

executables = [
    Executable('game.py')
]

setup(name='Zombie Killer',
      version='0.1',
      description='Python Game Demo',
      options=options,
      executables=executables
      )
