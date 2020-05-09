# Blu GTA V

The world of AI is growing at an exponential rate in the real world, but what about a virtual world? I created 'Blu' to be a intelligent learning agent set inside the world of Grand Theft Auto V. I will be trying to see what is possible with deep/machine learning in the world of GTA V.

## Motivation

I wanted to research and develop my skills in reinforcement/machine/deep learning with neural nets. **Why** Grand Theft Auto V? Well GTA has a dynamic open world, with active AI and NPC simulations. This will create a great environment for Blu to learn and explore different implementations of deep learning and AI development. 

## People Puncher

The People Puncher model is a trained model that causes Blu to **mimic** training data to identify, move towards, and punch people in GTA V.


![People puncher in action](https://github.com/westpoint-neural-networks/final-project-treturner/blob/master/assets/people_puncher.gif)


By recording GTA V gameplay that is based on running around and punching people and recording the keyboard input at each frame. A convolutional neural network (CNN) can learn the representations necessary to replicate the data provided. I took this approach over reinforcement learning (RL) becuase it was challenging to label a punishment and reward through GTA V. Additionally, attempting to copy the dataset rather than use RL was a novel approach that I have not seen used often. 

---

## Getting Started 
Project requirements include:
* **[Python](https://www.python.org/downloads/release/python-356/)** - version 3.5.6
* **[Anaconda](https://www.anaconda.com/products/individual)** - *recomended, but not required*
* **[GTA V](https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/)** - You can reference the wiki page [GTA V Alternative](https://github.com/westpoint-neural-networks/final-project-treturner/wiki/GTA-V-Alternative) for an alternate way to test a 'person punching' model if a playable version of GTA V is unavailable. 


### Initial Setup

> **Using Anaconda**

By using **Anaconda** environments, you can create this project's environment with the code below.
```
conda env create -f environment.yml
```

This will create a conda environment called **'blu_gtav'** with python **3.5.6** and all the required packages. The **-n** or **--name** tag allows one to specify a specific name for the env other than **'blu_gtav.'**
```
conda env create -n environment_name -f environment.yml
```

> **Without using Anaconda**

Set your python version to 3.5.6, install the latest version of [pip](https://pip.pypa.io/en/stable/installing/) and run the following command to install all of the required packages.

`pip install opencv-python`

`pip install pywin32`

`pip install pandas`

`pip install scikit-learn`

`pip install keras`

`pip install tensorflow` ***tensorflow-gpu** or **tensorflow-cpu** can be substituted based on specific computer specifications.

### Setting up the screen input
Make sure you have GTA V downloaded and set to a **800 x 600** resolution. Put the games window in the top-left corner of your screen as this is where grab_screen will record pixel from.

### Usage
Simply execute the following python files in chronological order to prepare, train, and test a model that aims to punch people in GTA V:
* `python 1_collect_data.py` - a sample of training data is provided in '/training_data'
* `python 2_balance_data.py` - a sample of balanced training data is provided in '/training_data'
* `python 3_train_model.py` - the weights of trained models can be found in '/saved_models'
* `python 4_test_model.py` - loads the 'proportionate' model by default

> Running `python training_data/show_data.py` will display the training data saved at '/training_data/training_data.npy.' 

> Running `python training_data/show_balanced_data.py` will display the balanced training data saved at '/training_data/training_data_balanced.npy.' 

Additional documentation for each of these files can be found on this projects [wiki](https://github.com/westpoint-neural-networks/final-project-treturner/wiki) pages.

## Authors
* **Trevaun Turner** - *Initial work* - [treturner](https://github.com/treturner/)

## Contributors
* **Frannecklp** - for creating and optimizing *grab_screen.py* and it's functions.
* **Jake** - created *get_keys.py* for reading game input through the console while on the game window - [Box-Of-Hats](https://github.com/Box-Of-Hats)

## Acknowledgments
* **Harrison** - creator of [pythonprogramming.net](https://pythonprogramming.net) for inspiration and discovering that this was even remotely possible.
* **Dr. Kyle King** - my CS485 *Applied Neural Networks* instructor who influenced for my development and growth in deep learning/neural networks.

