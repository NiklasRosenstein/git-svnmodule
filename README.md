__NAME__

`git svnmodule` - track svn repositories as modules in git
[![PyPI Downloads](http://img.shields.io/pypi/dm/git-svnmodule.svg)](https://pypi.python.org/pypi/git-svnmodule)
[![PyPI Version](https://img.shields.io/pypi/v/git-svnmodule.svg)](https://pypi.python.org/pypi/git-svnmodule)

![UML Diagram](http://i.imgur.com/Yio0UuO.png)

__DESCRIPTION__

Git-svnmodule is a Git extension that allows you to track SVN repositories
like submodules in your project's history. Similar to git-submodules, the
SVN repository information is stored in a `.svnmodules` configuration file.
A slight difference in that regard however is that the SVN repository revision
numbers are stored in the same file.

You can edit the `.svnmodules` file manually or add SVN modules from the
command-line using the `git svnmodule add` command. Here's an example session
adding a repository and checking out the most recent revision.

    niklas@sunbird ~/project$ git svnmodule add svn://example.org/theproject/assets
    niklas@sunbird ~/project$ git svnmodule update
    svnmodule: update: assets = None
    A    assets\Scenes
    A    assets\Scenes\TestingTrack.unity
    A    assets\Scenes\Menu.unity
    A    assets\Scenes\Server.unity
    A    assets\Scenes\TestingTrack.unity.meta
    A    assets\Scenes\looping.unity
    A    assets\Scenes\Menu.unity.meta
    A    assets\Scenes\Server.unity.meta
    A    assets\Scenes\looping.unity.meta
    Checked out revision 3.
    niklas@sunbird ~/project$ cat .svnmodules
    [svnmodule="assets"]
    url = svn://example.org/theproject/assets
    revision = 3

__SYNOPSIS__

```
usage: git svnmodule [-h] {init,add,revsync,update,format-authorized-keys} ...

positional arguments:
  {init,add,revsync,update,format-authorized-keys}
    init                install Git post-checkout hook
    add                 add a svn module to `.svnmodules`
    revsync             synchronize the revision number of all or a specific
                        svn module and write them into `.svnmodules`
    update              check out all or a specific svn module/s at the
                        revisions tracked by Git
    format-authorized-keys
                        format an OpenSSH authorized_keys file for SSH+SVN
                        from a directory of public keys.

optional arguments:
  -h, --help            show this help message and exit
```

__INSTALLATION__

1. Goto https://python.org/ and follow the instructions to install
   Python 3 on your system (if it is not already installed)
2. On Windows, make sure you don't install Python to a path that
   contains whitespace! (see [pypa/pip#2783][]).
2. Run `pip install --user git-svnmodule` from the command-line
3. Run `python -c "import site; print(site.USER_BASE)"` and make sure
   the `bin` folder (Unix) or `Scripts` folder (Windows) inside the
   printed directory is on your `PATH` environment variable
4. Use `git svnmodule`

[pypa/pip#2783]: https://github.com/pypa/pip/issues/2783

__CHANGELOG__

v0.1.2

* add `git svnmodule format-authorized-keys` command
* #5 pip install: git-hooks data files not included

v0.1.1

* #3 make sure .svnmodules section/option order remains consistent
* #2 update command now updates revision numbers
