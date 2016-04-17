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

from argparse import ArgumentParser
from .config import normalize_path, read_svn_modules, write_svn_modules
from . import svn

import os
import shlex
import shutil
import sys

data_dir = os.path.dirname(__file__)


##
# Commands
##

def do_add(parser, args):
  path = args.path
  if not path:
    path = args.url.split('/')[-1]
  path = normalize_path(path)
  if not path:
    parser.error('empty path')

  modules = read_svn_modules()
  if path in modules:
    parser.error('svnmodule="{}" already used'.format(path))

  modules[path] = {'url': args.url}
  write_svn_modules(modules)


def do_init(parser, args):
  # Copy the Git hooks to the local Git repository.
  hooks = os.path.join(data_dir, 'git-hooks')
  for src in os.listdir(hooks):
    dst = os.path.join('.git', 'hooks', src)
    src = os.path.join(hooks, src)
    shutil.copyfile(src, dst)
  print('git hooks installed')


def do_update(parser, args):
  modules = read_svn_modules()
  target_modules = get_target_modules(parser, args, modules)

  for module in target_modules:
    # Checkout.
    url = modules[module]['url']
    revision = modules[module].get('revision')
    print('svnmodule: update: {} = {}'.format(module, revision))
    svn.checkout(module, url, revision)

    # Update tracked revision number.
    info = svn.get_info(module)
    modules[module]['revision'] = info['revision']

  write_svn_modules(modules)


def do_revsync(parser, args):
  modules = read_svn_modules()
  if not modules:
    print('svnmodule: revsync: no svn modules')
    return 0

  target_modules = get_target_modules(parser, args, modules)
  print('svnmodule: revsync: loading svn revisisions ...')
  for module in target_modules:
    # Read the repository information.
    try:
      info = svn.get_info(module)
    except svn.NotARepositoryException:
      print('svnmodule: revsync: warning: {!r} does not exist'.format(module))
    else:
      # Update the revision number.
      modules[module]['revision'] = info['revision']
      print('svnmodule: revsync: {} = {}'.format(module, info['revision']))

  write_svn_modules(modules)


def do_format_authorized_keys(parser, args):
  if not os.path.isdir(args.keys_directory):
    parser.error('not a directory: {!r}'.format(args.keys_directory))
  prefix = 'command="svnserve -t -r {root} --tunnel-user={{user}}", ' \
           'no-port-forwarding,no-agent-forwarding,no-X11-forwarding,' \
           'no-pty'.format(root=shlex.quote(args.root))
  for file in os.listdir(args.keys_directory):
    path = os.path.join(args.keys_directory, file)
    with open(path) as fp:
      for key in filter(bool, map(str.strip, fp.readlines())):
        print(prefix.format(user=file), key)


def get_target_modules(parser, args, modules):
  """
  Helper to get the list of modules that are targeted by the
  command-line parameters.
  """

  if args.module:
    args.module = normalize_path(args.module)
    if args.module not in modules:
      parser.error('unknown module: {!r}'.format(args.module))
    return [args.module]
  else:
    return modules.keys()


##
# Main
##

def exit_with_result(func):
  def decorator(*args, **kwargs):
    sys.exit(func(*args, **kwargs))
  return decorator


def get_parser():
  parser = ArgumentParser(prog='git svnmodule')
  action = parser.add_subparsers(dest='action')

  init = action.add_parser('init', help='install Git post-checkout hook')

  add = action.add_parser('add', help='add a svn module to `.svnmodules`')
  add.add_argument('url')
  add.add_argument('path', nargs='?')

  revsync = action.add_parser('revsync',
    help='synchronize the revision number of all or a specific svn '
         'module and write them into `.svnmodules`')
  revsync.add_argument('module', nargs='?')

  update = action.add_parser('update',
    help='check out all or a specific svn module/s at the revisions '
         'tracked by Git')
  update.add_argument('module', nargs='?')

  format_authorized_keys = action.add_parser('format-authorized-keys',
    help='format an OpenSSH authorized_keys file for SSH+SVN from a '
         'directory of public keys.')
  format_authorized_keys.add_argument('root',
    help='SVN repository root directory')
  format_authorized_keys.add_argument('keys_directory',
    help='directory listing user public keys')

  return parser


@exit_with_result
def main():
  parser = get_parser()
  args = parser.parse_args()
  if not args.action:
    parser.print_usage()
    return 0

  func = globals()['do_' + args.action.replace('-', '_')]
  return func(parser, args)
