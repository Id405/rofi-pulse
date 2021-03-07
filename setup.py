from setuptools import setup

setup(
    name='rofi_pulse',
    version='1.0.0',    
    description='Control pulseaudio with rofi',
    url='https://github.com/id405/rofi-pulse',
    author='Id405',
    license='GPL V3.0',
    install_requires=['pulsectl', 'python-rofi'],
    packages=['rofi_pulse'],

    entry_points = {
        "console_scripts": ['rofi_pulse = rofi_pulse:main']
    },

    classifiers=[
        'Operating System :: Linux',
        'Programming Languge :: Python :: 3',
    ],
)
