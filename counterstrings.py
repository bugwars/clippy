import argparse
import pyperclip

version_info = "0.2.0"
    
parser = argparse.ArgumentParser(description="A tool for generating counterstrings.")
parser.add_argument("-l", "--length", dest="length", type=int, help="maximum length to be generated")
parser.add_argument("-v", "--version", action="store_true", dest="version", help="shows version information")
args = parser.parse_args()

if not (args.length or args.version):
  parser.print_help()
  exit()

if args.version:
  print(version_info)
  exit(0)

marker_char = "*"
length = args.length

# Init
counterstring = "2" + marker_char
last_position = 2

while len(counterstring) < length:
    position = len(counterstring) + (len(str(last_position)) + 1)
    if len(str(position)) > len(str(last_position)):
        position += 1
    token = str(position) + marker_char
    remaining_length = length - len(counterstring)
    if remaining_length < (len(token) + len(counterstring)):
        token = token[0:remaining_length]
    counterstring += token
    last_position = position

pyperclip.copy(counterstring)
print("Ready to paste!")