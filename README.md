__NAME__

`git svnmodule` - use SVN repositories like Git submodules

__SYNOPSIS__

    git svnmodule {init,add,checkout,update}

__DESCRIPTION__

`git svnmodule` allows you to add SVN repositories and use them
similar to Git submodules. The modules are configured using a
`.svnmodules` file which is also used to track the respective
revision numbers.

This project was formed due to the need to manage large binary
files for the Unik game project, as it was decided that Git was
not appropriate for this task.

Example `.svnmodules` configuration:

    [svnmodule="Assets/"]
    url = svn://example.org/theproject/assets
    revision = 42

`git svnmodule init` intializes your local repository with Git
hooks and all checked out local SVN modules, installing convenient
hooks to make your life easier.

`git svnmodule add` allows you to add SVN modules from the command-line.

`git svnmodule checkout` checks out the SVN modules either at the most
recent commit if no revision is configured or at the configured revision

`git svnmodule update` updates the revision numbers in `.svnmodules`.

__INSTALLATION__
  
Via PyPI (not yet available):

    $ pip install git-svnmodule

Recent development version:

    $ git clone https://github.com/NiklasRosenstein/git-svnmodule.git
    $ cd git-svnmodule
    $ pip install .
