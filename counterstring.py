import argparse
import pyperclip

version_info = "0.2.0"

# Checks if length parameter is an integer greater or equal 2
def positive_ge_2(x):
    try:
        x = int(x)
    except Exception as e:
        raise argparse.ArgumentTypeError("Value must be an integer!")
    if x < 2:
        raise argparse.ArgumentTypeError("Minimum value for length is: 2")
    return x

# Initializes argument parser.        
parser = argparse.ArgumentParser(description="A tool for generating counterstrings.")
parser.add_argument("-l", "--length", dest="length", type=positive_ge_2, help="maximum length to be generated. Minimum value is: 2")
parser.add_argument("-m", "--marker", dest="marker_char", default="*", help="use a custom marker character. Make sure to escape certain characters! Default: *")
parser.add_argument("-v", "--version", action="store_true", dest="version", help="shows version information")
args = parser.parse_args()

# Checks for required parameters.
if not (args.length or args.version):
    parser.print_help()
    exit()

if len(args.marker_char) != 1:
    exit("Marker must be a single character!")

# Prints version.
if args.version:
    print(version_info)
    exit(0)

# Init
marker_char = args.marker_char
length = args.length
counterstring = "2" + marker_char
last_position = 2

# Creates counterstring.
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

# Copies output to clipboard.
pyperclip.copy(counterstring)
print("Ready to paste!")
