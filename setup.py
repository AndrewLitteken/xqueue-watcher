from setuptools import setup

f = open('requirements/production.txt', 'r')

text = ""
for line in f:
    text += line

setup(
    name='xqueue_watcher',
    version='0.2',
    description='XQueue Pull Grader',
    packages=[
        'xqueue_watcher',
    ],
    install_requires=text
)
