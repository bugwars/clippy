## Introduction
A Python tool to generate "counterstrings" for testing e.g. text fields. It is based on [PerlClip](http://www.satisfice.com/tools.shtml) and the blog post [Counterstrings: Self-Describing Test Data](http://www.satisfice.com/blog/archives/22) by James Bach.

> Sometimes you need to test a text field or document with different kinds of stressful inputs. But, it can be a pain to prepare the text data. PerlClip is a tool that helps you do that.

## Usage
```
usage: counterstrings.py [-h] [-l LENGTH] [-v]

A tool for generating counterstrings.

optional arguments:
  -h, --help            show this help message and exit
  -l LENGTH, --length LENGTH
                        maximum length to be generated
  -v, --version         shows version information
  ```
## Example
`python counterstrings.py -l 56` will generate the following string and paste it to your clipboard:  
`2*4*6*8*11*14*17*20*23*26*29*32*35*38*41*44*47*50*53*56*`

The last asterisk represents the end of a 56 character long string.

Whereas `python counterstrings.py -l 18` will generate:  
`2*4*6*8*11*14*17*2`

## Known Issues
Please check the [issue list](https://github.com/straurob/pycounterstrings/issues).
