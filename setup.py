from setuptools import setup

setup(
    name = 'webhooker',
    version = '0.0.1',

    author = 'Leonard Kinday',
    author_email = 'leonard@kinday.ru',
    license = 'MIT',
    url = 'http://github.com/kinday/webhooker.py',

    install_requires = [
        'netaddr',
        'web.py',
    ],
    packages = ['webhooker'],

    tests_require=['nose'],
    test_suite='nose.collector',
)
