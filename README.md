# Blu GTA V

The world of AI is growing at an exponential rate in the real world, but what about a virtual world? I created 'Blu' to be a intelligent learning agent set inside the world of Grand Theft Auto V. I will be trying to see what is possible with deep/machine learning in the world of GTA V.

## Motivation

I wanted to research and develop my skills in reinforcement/machine/deep learning with neural nets. **Why** Grand Theft Auto V? Well GTA has a dynamic open world, with active AI and NPC simulations. This will create a great environment for Blu to learn and explore different implementations of deep learning and AI development. Also the use of mods in GTA allow me to control certain variables like time of day, weather, ect.

## Getting Started
If you use **Anaconda** environments, you can create this projects environment with the code below. The --name tag allows you to specify the desired name for the environment:

```
conda env create --name insert_env_name -f environment.yml
```

This will create a conda environment called 'blu-gtav' with python **3.5.2** and all the required packages.

### Setting up the screen input
Make sure you have GTA V downloaded and set to a **800 x 600** resolution. Put the games window in the top-left corner of your screen as this is where grabscreen is set to.

## Dependencies without Anaconda
Set your python version to 3.5.2 and install these packages manually.

### Use pip to install these whl
* [OpenCV](http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv) - download the version 'cp35' with your desired architecture.
* [pypiwin32](https://pypi.python.org/pypi/pypiwin32/219) - download the version 'cp35' with your desired architecture.

### pip/conda install
* numpy
* time

## Authors
* **Trevaun Turner** - *Initial work* - [treturner](https://bitbucket.com/treturner/)

## Contributors
* **Frannecklp** - for creating and optimizing *grabscreen.py* and it's functions.
* **Jake** - created *getkeys.py* for reading game input through the console while on the game window - [Box-Of-Hats](https://github.com/Box-Of-Hats)

## Acknowledgments
* Harrison - creator of [pythonprogramming.net](https://pythonprogramming.net) for inspiration and discovering that this was even remotely possible.
