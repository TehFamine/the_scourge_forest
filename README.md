# Welcome to The Scourge Forest

The Scourge Forest is a Multi-User Dungeon (MUD) built upon the Evennia game engine 
set in a RPI world with a mixture of action-adventure and hack-n-slash gameplay.

## Features

* Dungeons & Dragons (D&D) 5E Game Systems (d20)
  * All Backgrounds/Classes/Races/Skills
* Level Progression System
  * 30 levels across the core D&D 5E classes (no multi-classing)
* Unique Story Driven Content
  * Experience a new story and set of adventures with The Scourge Forest
  * Hundreds of items, armor, weapons, and monsters all heavily influenced from 5E
* Instanced Areas & Adventure System
  * Play adventures entirely solo without disruption from others
  * Content scales to your level and to your group
* Rogue-like Gameplay
  * Adventures, combat, quests, and story delivered through old school menu-style screens
* Powered by Evennia
  * *Evennia* is a modern library for creating [online multiplayer text
games][wikimudpage] (MUD, MUSH, MUX, MUCK, MOO etc) in pure Python. It
allows game creators to design and flesh out their ideas with great
freedom.

## Getting Started

To get started, you must first install the following prerequisites.

### Prerequisites

* Linux/Unix
* Windows (Vista, Win7, Win8, Win10)
* Mac OSX (>=10.5 recommended)
* [Python](http://www.python.org) (v3.7, 3.8 are tested)
   * [virtualenv](http://pypi.python.org/pypi/virtualenv) for making isolated Python environments.
   * [Twisted](http://twistedmatrix.com) (v19.0+)
   * [ZopeInterface](http://www.zope.org/Products/ZopeInterface) (v3.0+)  - usually included in Twisted packages
   * Linux/Mac users may need the `gcc` and `python-dev` packages or equivalent.
   * Windows users need [MS Visual C++](https://aka.ms/vs/16/release/vs_buildtools.exe) and *maybe* [pypiwin32](https://pypi.python.org/pypi/pypiwin32).
   * [Django](http://www.djangoproject.com) (v2.2.x), latest dev version is usually untested with Evennia
* [GIT](http://git-scm.com/) - version control software

### Installation

Choose the installation path that best fits your environment.

#### Linux Installation

If you run into any issues during the installation and first start, please
check out [Linux Troubleshooting](#linux-troubleshooting).

For Debian-derived systems (like Ubuntu, Mint etc), start a terminal and
install the [dependencies](#requirements):

```
sudo apt-get update
sudo apt-get install python3 python3-pip python3-dev python3-setuptools python3-git python3-virtualenv gcc

# If you are using an Ubuntu version that defaults to Python3, like 18.04+, use this instead:
sudo apt-get update
sudo apt-get install python3.7 python3-pip python3.7-dev python3-setuptools virtualenv gcc

```
Note that, the default Python version for your distribution may still not be Python3.7 after this. This is ok - we'll specify exactly which Python to use later. 
You should make sure to *not* be `root` after this step, running as `root` is a
security risk. Now create a folder where you want to do all your Evennia
development.

Find a location or mkdir a folder to clone The Scourge Forest.

```
git clone https://github.com/TehFamine/the_scourge_forest.git
```

A new folder `the_scourge_forest` will appear containing the source code for the game. To isolate the the game code install and its dependencies from the rest of the system, it is good
Python practice to install into a _virtualenv_. Then `cd the_scourge_forest` and run the following:

Run `python -V` to see which version of Python your system defaults to.

```
# If your Linux defaults to Python3.7+:
virtualenv tsfv

# If your Linux defaults to Python2 or an older version 
# of Python3, you must instead point to Python3.7+ explicitly:
virtualenv -p /usr/bin/python3.7 tsfv
```

A new folder `tsfv` will appear (we could have called it anything). This
folder will hold a self-contained setup of Python packages without interfering
with default Python packages on your system (or the Linux distro lagging behind
on Python package versions). It will also always use the right version of Python. 
Activate the virtualenv:

```
source tsfv/bin/activate
```

The text `(tsfv)` should appear next to your prompt to show that the virtual
environment is active.

> Remember that you need to activate the virtualenv like this *every time* you
> start a new terminal to get access to the Python packages (notably the
> important `evennia` program) we are about to install.

Let's go one hop outside the game folder to snag Evennia.

```
cd ../
git clone https://github.com/evennia/evennia.git
```

A new folder `evennia` will appear containing the Evennia library. This only
contains the source code though, it is not *installed* yet. (so you see the `evennia/` and `the_scourge_forest/`
folders) and go back into the game source

```
cd the_scourge_forest
pip install -e ../evennia
```

Your final folder structure should look like this:
```
./the_scourge_forest
    commands/
    server/
    typeclasses
    tsfv/
    etc..
```

Once you install Evennia, it should install all the dependancies for the game. These
dependancies will be stored in that virtual environment `tsfv` everytime you activate it. To
activate and start the MUD, simply type:

```
evennia migrate      # (this creates the database)
evennia start        # (create a superuser when asked. Email is optional.)
```

> Server logs are found in `the_scourge_forest/server/logs/`. To easily view server logs
> live in the terminal, use `evennia -l` (exit the log-view with Ctrl-C).
>

Your game should now be running! Open a web browser at `http://localhost:4001`
or point a telnet client to `localhost:4000` and log in with the user you
created. Check out [where to go next](#where-to-go-next).

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Evennia](https://github.com/evennia/evennia)
