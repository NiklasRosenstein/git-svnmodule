__NAME__

`git svnmodule` - use svn repositories like Git submodules

__SYNOPSIS__

    git svnmodule {init,add,checkout,update}

__DESCRIPTION__

`git svnmodule` allows you to add svn repositories and use them
similar to Git submodules. The modules are configured using a
`.svnmodules` file which is also used to track the respective
revision numbers.

Note that in all places, `git svnmodule` tries to keep the naming
conventions of Git. For example, the term "update" means something
different for original Git submodules as compared to svn repositories.
Here, `git svnmodule update` means the same as `git submodule update`,
thus this will checkout the svn submodules at the revisions that are
currently tracked by Git. While this is not completely different from
svn, some might think that "update" would cause the svn submodules to
be updated to the most recent revision. This is NOT the case!

Example `.svnmodules` configuration:

    [svnmodule="Assets/"]
    url = svn://example.org/theproject/assets
    revision = 42

Subcommands:

`init` - install Git post-checkout hook

`add` - add a svn module to `.svnmodule` from the command-line

`update` - check out all or a specific svn module/s at the revisions tracked by Git

`revsync` - synchronize the revision number of all or a specific svn
module and write them into `.svnmodule`

> This project was formed due to the need to manage large binary
> files for the Unik game project, as it was decided that Git was
> not appropriate for this task.

__INSTALLATION__
  
Via PyPI (not yet available):

    $ pip install git-svnmodule

Recent development version:

    $ git clone https://github.com/NiklasRosenstein/git-svnmodule.git
    $ cd git-svnmodule
    $ pip install .

__EXAMPLES__

    $ git svnmodule init
    git hooks installed
    $ git svnmodule add svn://example.org/theproject/assets Assets
    $ git svnmodule update
    svnmodule: update: 'Assets' ...
    svnmodule: update:
    A    Assets\README.md
    Checked out revision 2.
