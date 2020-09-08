# -*- coding: utf-8 -*-

from setuptools import find_packages, setup


with open('README.md', 'r') as fh:
    readme = fh.read()

setup(
    name='WTForms-Ext',
    version='0.5',
    url='https://github.com/zengqiu/wtforms-ext',
    license='MIT',
    author='zengqiu',
    author_email='zengqiu@qq.com',
    description='Extensions of WTForms',
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    platforms='any',
    install_requires=[
        'WTForms',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)