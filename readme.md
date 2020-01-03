# botdelaradio

This bot tweets periodically radio broadcasting information.

## Requirements:

*   python3
*   tweepy
*   a twitter developer account

## Example of installation using git and conda

1.  Clone the repository in the directory of your choice:

    `$ git clone https://github.com/Bielorusse/botdelaradio.git`

2.  Create a new conda environment with the dependencies:

    `$ conda create -n botdelaradio python=3 tweepy`

3.  Activate the newly created environment:

    `$ conda activate botdelaradio`

4.  Create a duplicate of the example config with the filename `config.ini` and
    fill this file with your twitter developer account credentials.

## Usage

`python botdelaradio.py`
