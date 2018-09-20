# Convert files from arabic to roman
## Converts all arabic number in input file (default is ARAB.IN) to roman and write to output file (default is ROMAN.OUT)


Files:
  - main.py             -- script to conver all arabic numbers in input file to romans and write to output file
  - roman/roman.py      -- contains RomanNumber class that is used to represent roman numbers
  - roman/test_roman.py -- tests for RomanNumber class
  
# Setup
Script works with python3
For running tests:
```bash
pip install -r requirements.txt
pytest
```


# Usage
```
usage: main.py [-h] [-i file] [-o file]

Convert arabic numbers to roman

optional arguments:
  -h, --help            show this help message and exit
  -i file, --input-file file
                        Input file with arabic numbers, each line containing
                        one number, default is ARAB.IN
  -o file, --output-file file
                        Name of the output file for converted numbers, default
                        is ROMAN.OUT
```

# Example:
```bash
cat ARAB.IN
3
4
5

python main.py

cat ROMAN.OUT
III
IV
V
--------------------
Alternatively:
python main.py -i SOMEFILE.IN -o CUSTOM_FILE.OUT
python main.py --input-file SOMEFILE.IN --output-file OUTFILE.OUT
```
