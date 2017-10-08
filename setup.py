from setuptools import setup, find_packages


setup(
    name='i3tg',
    packages=find_packages(),
    install_requires=['telethon'],
    entry_points={
        'console_scripts': [
            'i3tg-auth = i3tg.__main__:auth',
            'i3tg-poll = i3tg.__main__:poll',
        ],
    },

)
