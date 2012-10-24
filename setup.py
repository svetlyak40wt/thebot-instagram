from setuptools import setup

setup(
    name='thebot-instagram',
    version='0.1.1',
    description='Posts a new popular photo from the instagram each hour.',
    keywords='thebot instagram plugin',
    license = 'New BSD License',
    author="Alexander Artemenko",
    author_email='svetlyak.40wt@gmail.com',
    url='http://github.com/svetlyak40wt/thebot-instagram/',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
    py_modules=['thebot_instagram'],
    install_requires=[
        'thebot>=0.2.0',
        'python-instagram',
    ],
)
