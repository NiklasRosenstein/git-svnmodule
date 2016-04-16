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

import os
import subprocess
import sys


class CalledProcessError(Exception):

  def __init__(self, command, process, cwd):
    self.command = command
    self.process = process
    self.cwd = cwd

  def __str__(self):
    return 'program {!r} exited with status-code {}'.format(
      self.command[0], self.process.returncode)


def run(command, cwd=None, pipe=False):
  """
  Run the system command specified by the list of arguments in #command.
  If #cwd is specified, it overrides the current working directory for
  the command. If #pipe is True, the output of the command is directed
  into a pipe and returned from the function.

  :raise CalledProcessError: if the command exits with a non-zero
    status code.
  :return: #bytes if #pipe is True, None otherwise
  """

  if not pipe:
    sys.stdout.flush()
    sys.stderr.flush()
    stdout = None
    stderr = None
  else:
    stdout = subprocess.PIPE
    stderr = subprocess.STDOUT
  if not cwd:
    cwd = os.getcwd()

  process = subprocess.Popen(command, cwd=cwd, stdout=stdout, stderr=stderr)
  process.wait()
  if process.returncode != 0:
    raise CalledProcessError(command, process, cwd)
  if pipe:
    return process.communicate()[0]
  else:
    return None
