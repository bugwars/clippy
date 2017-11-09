## Introduction
A collection of Python scripts to generate test data for testing e.g. text fields. It is based on [PerlClip](http://www.satisfice.com/tools.shtml) and the blog post [counterstring: Self-Describing Test Data](http://www.satisfice.com/blog/archives/22) by James Bach.

> Sometimes you need to test a text field or document with different kinds of stressful inputs. But, it can be a pain to prepare the text data. PerlClip is a tool that helps you do that.

## Setup
This script requires the Python module [pyperclip](https://pypi.python.org/pypi/pyperclip).

Recommended way for installation is: `pip install pyperclip`

Tested with:
- Windows 10 & Python 3.6
- Linux Mint 18.2 & Python 2.7.12

## Usage
```
usage: counterstring.py [-h] [-l LENGTH] [-m MARKER_CHAR] [-v]

A tool for generating counterstring.

optional arguments:
  -h, --help            show this help message and exit
  -l LENGTH, --length LENGTH
                        maximum length to be generated. Minimum value is: 2
  -m MARKER_CHAR, --marker MARKER_CHAR
                        use a custom marker character. Make sure to escape
                        certain characters! Default: *
  -v, --version         shows version information
  ```
## Examples
`python counterstring.py -l 56` will generate the following string and paste it to your clipboard:  
`2*4*6*8*11*14*17*20*23*26*29*32*35*38*41*44*47*50*53*56*`

The last asterisk represents the end of a 56 character long string.

Whereas `python counterstring.py -l 18 -m \#` will generate:  
`2#4#6#8#11#14#17#2`

## How To Contribute
Open an issue (bug, feature request, whatever) for discussion.

Or add your code:
1. Fork this repository.
2. Create a new feature branch: `git checkout -b my-feature`
3. Commit your changes: `git commit -am "Add my feature"`
4. Push back: `git push origin my-feature`
5. Open a pull request.


## Known Issues
Please check the [issue list](https://github.com/straurob/pycounterstring/issues).
