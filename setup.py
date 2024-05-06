#!/usr/bin/env python3

from setuptools import setup

#read from requirements.txt
f = open('requirements.txt','r')
dep_list = []
for item in f.readlines():
    item = item.rstrip('\n')
    dep_list.append(item)
f.close()

setup(name='wireplumber-w31rd-hax',
      version='0.1.0',
      description='Collection of assorted workarounds and hacks for wireplumber, as well tools for enabling or disabling them',
      author='GI Jack',
      author_email='GI_Jack@hackermail.com',
      url='https://github.com/GIJack/wireplumber-w31rd-hax',
      packages=['wwh'],
      license='GPLv3',
      scripts=['wwh-cli.py'],
      #scripts=['wwh-cli.py', 'wwh-gui.py'],
      data_files=added_files,
      classifiers=[
          'Development Status :: 3 - Alpha ',
          'Environment :: Console',
          #'Environment :: X11 Applications :: Qt',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Operating System :: POSIX :: Linux',
          'Operating System :: POSIX :: BSD :: FreeBSD',
          'Operating System :: POSIX :: BSD :: OpenBSD',
          #'Operating System :: MacOS :: MacOS X',
          #'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 3',
          'Topic :: Utilities',
          'Topic :: System :: Networking',
      ],
      install_requires = dep_list
     )
