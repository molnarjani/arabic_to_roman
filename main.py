import argparse
from roman import RomanNumber

parser = argparse.ArgumentParser(description='Convert arabic numbers to roman')
parser.add_argument('-i', '--input-file', help='Input file with arabic numbers, each line containing one number, default is ARAB.IN',
                    metavar='file', default='ARAB.IN', type=argparse.FileType('r'))
parser.add_argument('-o', '--output-file', help='Name of the output file for converted numbers, default is ROMAN.OUT',
                    metavar='file', default='ROMAN.OUT', type=argparse.FileType('w'))
args = parser.parse_args()

def convert(input_file, output_file):

    try:
        numbers = list(map(int, input_file.read().splitlines()))
    except ValueError:
        print(f'Input file contains line that are not integers')
        exit(1)

    try:
        for num in numbers:
            output_file.write(f'{RomanNumber.from_arabic(num)}\n')
    except ValueError:
        print(f'Line cannot be converted to roman: {num}')
        exit(1)

if __name__ == '__main__':
    convert(args.input_file, args.output_file)
