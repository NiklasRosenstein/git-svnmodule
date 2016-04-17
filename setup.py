# Copyright (C) 2016  Niklas Rosenstein
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import setuptools
import sys

if sys.version < '3.0':
  sys.exit('requires Python 3.0 or newer (current: {0})'.format(sys.version[:5]))

setuptools.setup(
  name = 'git-svnmodule',
  version = '0.1.2',
  description = 'use SVN repositories like Git submodules',
  author = 'Niklas Rosenstein',
  author_email = 'rosensteinniklas@gmail.com',
  url = 'https://github.com/NiklasRosenstein/git-svnmodule',

  packages = ['git_svnmodule'],
  entry_points = {
    'console_scripts': [
      'git-svnmodule = git_svnmodule:main',
    ]
  },
  keywords = 'git submodules svn',
  classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Version Control',
  ]
)
