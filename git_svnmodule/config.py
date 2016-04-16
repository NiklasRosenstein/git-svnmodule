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
"""
Reader and writer for `.svn-module` configuration files.
"""

import collections
import configparser


def normalize_path(path):
  """
  Normalizes a path, mainly for the purpose of stripping redundant
  path separators from it.
  """

  # Who the fuck would do something like path\/\ ?? Keep it simple
  return path.strip('\\').strip('/')


def read_svn_modules(file='.svnmodules'):
  """
  Read a `.svn-modules` file and return a dictionary mapping the
  relative module path to its configuration data. Example result:

  ```python
  {
    "Assets": {
      "url": "svn://example.org/theproject/assets"
    }
  }
  ```

  :param file: can be a string or file-like object.
  :raise ValueError: if the file contains an invalid section or a
    section contains an invalid or misses an option.
  :return: #collections.OrderedDict
  """

  config = configparser.ConfigParser()
  if isinstance(file, str):
    config.read(file)
  else:
    config.read_file(file)

  result = collections.OrderedDict()
  for section in config.sections():
    if not section.startswith('svnmodule="') or not section.endswith('"'):
      raise ValueError('invalid section: {}'.format(section))
    path = normalize_path(section[11:-1])
    values = collections.OrderedDict(config.items(section))
    if not path:
      raise ValueError('empty svnmodule path encountered')
    if path in result:
      raise ValueError('duplicate [{}]'.format(section))
    if 'url' not in values:
      raise ValueError('missing option: [{}].key'.format(section))
    result[path] = values

  return result


def write_svn_modules(modules, file='.svnmodules'):
  """
  Writes the configuration in the dictionary #config to the
  specified #file.

  :param file: can be a string or file-like object.
  :raise ValueError: if #config has an incorrect structure.
  """

  config = configparser.ConfigParser()
  for path, values in modules.items():
    section = 'svnmodule="' + path + '"'
    if not isinstance(values, dict):
      raise ValueError('section values must be a dictionary')
    if not 'url' in values:
      raise ValueError('missing option: [{}].key'.format(section))
    config[section] = values

  if isinstance(file, str):
    with open(file, 'w') as fp:
      config.write(fp)
  else:
    config.write(file)
