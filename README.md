# README

## Description
Short Python script that takes an .xlsx file and generates an html table with Bootstrap classes

## Usage

Place the cuddlyspork.py file in the directory of the files you wish to format. On the command line, import `cuddlyspork` then call the `cuddlyspork.table_to_html()` function. The function's parameters are the file and the table (assuming each table is on its own sheet in the Excel file) you wish to format.

```python

import cuddlyspork
cuddlyspork.table_to_html('file','Table #')

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
