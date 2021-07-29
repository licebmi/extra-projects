# number printer

## About
This is just a small test project

## Requirements
This project requires python3 and makes use of the standard library.
For testing purposes you will need GNU Make and BATS

A `shell.nix` file is included to create a quick testing environment with nix on both Linux or MACOS. Else, you can follow the instructions as below.

### MACOS
Python 3 is still shipped with the latest version at the moment of writing (11.5)
Else you might use homebrew or nix to install it.
``` sh
# Homebrew
brew install python@3 make

# nix
nix -iA nixpkgs.python3 nixpkgs.make
```

### Linux
Most standard linux distributions will ship python 3.
If this is not installed, you can install it using your package manager
``` sh
# apt
sudo apt install python3 make

# Yum
sudo yum install python3 make

# emerge
sudo emerge --ask dev-lang/python:3.8

# nix
nix -iA nixpkgs.python3 make
```

## Running

Just executing the script will return a randomized range of numbers from 1 to 10, a couple of bonus features are added:
 - Specify the ammount of numbers to be returned
 - Specify the start of the range
 - Return the ordered range instead of a random one

``` sh
./number-printer.py -h

# usage: number-printer.py [-h] [-o] [-s START] [ammount]

# Generate a range of random integers

# positional arguments:
#   ammount               Specify the ammount of digits to return

# optional arguments:
#   -h, --help            show this help message and exit
#   -o, --ordered         Returns an ordered range
#   -s START, --start START
#                         Specify the start of the range
```

``` sh
./number-printer.py

#7
#5
#9
#6
#1
#4
#8
#3
#10
#2
```
