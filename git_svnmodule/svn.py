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

from .subp import run
import os


class SvnException(Exception):
  pass


class NotARepositoryException(SvnException):
  pass


class UrlMismatchException(SvnException):

  def __init__(self, configured, expected):
    self.configured = configured
    self.expected = expected


def get_info(directory):
  """
  Runs the `svn info` command and returns a dictonary containing
  the results of the command. Keys in the dictionary are all lowercase
  and whitespace replace by underscores. Example result:

  ```python
  {
    'url': 'svn://example.org/theproject/assets',
    'repository_root': 'svn://example.org/theproject/assets',
    'repository_uuid': '3ff99ffb-19bb-487b-bb71-02f8d7be2fc4',
    'revision': 42,
    'node_kind': 'directory',
    'schedule': 'normal',
    'last changed rev': 32,
    'last changed date': '2016-04-16 12:48:02 +0200 (Sa, 16 Apr 2016)',
  }
  ```

  :raise NotARepositoryException:
  :raise SvnException:
  """

  if not os.path.isdir(os.path.join(directory, '.svn')):
    raise NotARepositoryException(directory)

  output = run(['svn', 'info'], cwd=directory, pipe=True).decode()
  result = {}
  for line in output.split('\n'):
    line = line.lower()
    if ':' not in line:
      continue

    parts = line.split(':', 1)
    if len(parts) != 2 or not all(parts):
      continue

    result[parts[0].replace(' ', '_')] = parts[1].strip()

  # Just check some of the expected result values.
  if not all(x in result for x in ['url', 'revision', 'node_kind']):
    raise SvnException('could not read info')

  return result


def checkout(directory, url, revision=None):
  """
  Checkout the SVN #directory with the specified #url and at
  #revision or at the most recent revision if None is passed.

  :param UrlMismatchException: if the #url does not match the
    configured SVN remote repository URl as configured in the
    local repository. This is a limitation currently.
  """

  if os.path.isdir(os.path.join(directory, '.svn')):
    # Repository exists, update revision.
    info = get_info(directory)
    if info['url'] != url:
      raise UrlMismatchException(info['url'], url)
    cwd = directory
    command = ['svn', 'update']
  else:
    cwd = None
    command = ['svn', 'checkout', url, directory]
  if revision:
    command += ['--revision', revision]
  run(command, cwd)
