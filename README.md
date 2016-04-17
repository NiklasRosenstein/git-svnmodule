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
  
Via PyPI

    $ pip install git-svnmodule

Get the latest development version (editable installation updatable with `git pull`)

    $ git clone https://github.com/NiklasRosenstein/git-svnmodule.git
    $ pip install -e git-svnmodule

__CHANGELOG__

v0.1.2

* add `git svnmodule format-authorized-keys` command
