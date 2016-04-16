__NAME__

`git svnmodule` - use svn repositories like Git submodules

__SYNOPSIS__

    git svnmodule [-h] {init,add,revsync,update} ...

__DESCRIPTION__

Git-svnmodule allows you to use svn repositories similar to Git submodules.
The svn url and revision tracking happens in the `.svnmodules` file.
Git-svnmodule will automatically automatically update this file with some
of its subcommands. Below you find an example configuration:

    [svnmodule="Assets/"]
    url = svn://example.org/theproject/assets
    revision = 42

*Subcommands*

* `init` - install Git post-checkout hook
* `add` - add a svn module to `.svnmodule` from the command-line
* `update` - check out all or a specific svn module/s at the revisions tracked by Git
* `revsync` - synchronize the revision number of all or a specific svn
  module and write them into `.svnmodule`

*Why?*

This project was formed due to the need to manage large binary files for
the Unik game project, as it was decided that Git was not appropriate for
this task.

__INSTALLATION__
  
Via PyPI

    $ pip install git-svnmodule

Recent development version:

    $ git clone https://github.com/NiklasRosenstein/git-svnmodule.git
    $ cd git-svnmodule
    $ pip install .

__EXAMPLE__

    $ git svnmodule init
    git hooks installed
    $ git svnmodule add svn://example.org/theproject/assets Assets
    $ git svnmodule update
    svnmodule: update: 'Assets' ...
    svnmodule: update:
    A    Assets\README.md
    Checked out revision 2.
