from setuptools import setup

setup(
    name='thebot-instagram',
    version='0.1.0',
    description='Prints a new popular photo from the instagram each hour.',
    keywords='thebot instagram plugin',
    license = 'New BSD License',
    author="Alexander Artemenko",
    author_email='svetlyak.40wt@gmail.com',
    url='http://github.com/svetlyak40wt/thebot-instagram/',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Server',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
    py_modules=['thebot_instagram'],
    install_requires=[
        'thebot',
        'python-instagram',
    ],
)
