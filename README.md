# README

## Description

Short Python script that takes an .xlsx file and generates an html table with Bootstrap classes.

## Usage

Place the cuddlyspork.py file in the directory of the files you wish to format. On the command line, import `cuddlyspork` then call the `cuddlyspork.table_to_html()` function.

```python

import cuddlyspork
cuddlyspork.table_to_html(file,table,ints)

```
Function parameters:

**file**: *str*, the file that holds tables

**table**: *str*, the table (`sheetname` argument in pandas' `read_excel` function) you wish to convert

**skiprows**: *int*, the number of rows to be skipped by pandas' `read_excel` function. Defaults to 0.

**ints**: *int,list*, a single integer or list of integers representing columns that read_excel converted from percentages to floats that need to be converted back or columns that need to be rounded, see *rounding* and *skip*. During string and *rounding* conversions, floats are always rounded to the tenth place. Defaults to `None`

**rounding**: *boolean*, a True or False value that indicates which columns need to be rounded. Defaults to `False`.

**skipconvert**: *int*, number of rows that needs to be skipped for either string or rounding conversions. Takes into account number of rows skipped when reading the data via pandas. Example, if your observations start on the fifth row and you need to skip the first three when reading the data in, **skiprows** will be 3 and **skipconvert** will be 5. Defaults to 0.

Sample:

```python

import cuddlyspork
cuddlyspork.table_to_html('sample.xlsx','Table 1',ints=[0,1,2], rounding=True, skiprows=2, skipconvert=4)

```

The html is deposited in a file in the root folder.

## License

MIT License

Copyright (c) 2016 Matt Sedlar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
