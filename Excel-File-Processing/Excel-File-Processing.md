---
marp: true
---

# Excel File Processing
## by Jibo He
清华大学社会科学学院心理学系
hejibolaboratory@pku.org.cn

---
# Python Modules for Excel Processing
## Xlrd
reading data and formatting from .xls files
• http://pypi.python.org/pypi/xlrd
##　Xlwt
writing data and formatting to .xls files
https://pypi.python.org/pypi/xlwt
## xlutils
 http://pypi.python.org/pypi/xlutils
• a collection of utilities using both xlrd and xlwt:
◦ copying data from a source to a target spreadsheet
◦ filtering data from a source to a target spreadsheet


---
# Python Modules for Excel Processing
## XlsxWriter
https://xlsxwriter.readthedocs.org/
XlsxWriter is a Python module that can be used to write text, numbers, formulas and hyperlinks to multiple worksheets in an Excel 2007+ XLSX file. It supports features such as formatting and many more, including:

---
# Install Python packages (1)
# Install using .exe 
xlrd-0.7.1.win32.exe
https://pypi.python.org/pypi/xlrd/0.7.1
# Install from source:
C:\> cd xlrd-0.7.1
C:\xlrd-0.7.1> python setup.py install


---
# Install Python packages (2)
# Install using pip
pip install xlrd
pip install xlwt
pip install xlutils
pip install xlsxwriter

---
# import modules 
## three types of import 
from xlrd import open_workbook
from xlrd import open_workbook as ow
Import xlrd # recommended way

---
# Open an Excel File

```python
import xlrd
from xlrd import open_workbook
## open file
wb = open_workbook('simple.xls')
## iterate the sheets
for s in wb.sheets():
    print 'Sheet:',s.name

    ## loop through all rows and columns
    for row in range(s.nrows):
        for col in range(s.ncols):
            print s.cell(row,col).value
```

---
# Open an Excel File

import xlrd
	- xlrd is the package to read excel files.
wb = open_workbook('simple.xls')
	- open a workbook
s.nrows, s.ncols
	- get the number of rows and columns
s.cell(row,col).value
	- get the value at cell location of (row,col)

---
# File Handle as a Sequence
 
```python
import xlwt

# create a workbook
book = xlwt.Workbook(encoding="utf-8")
 
sheet1 = book.add_sheet("ShowMeThePower")

# write something
sheet1.write(0, 0, "Python is Great!")
sheet1.write(1, 0, "Dominance")
sheet1.write(2, 0, "Test")

# save the excel file 
book.save("trial.xls")
print('-_-!')

```
---
# write a lot

import xlwt
	- python package to write an excel file
book = xlwt.Workbook(encoding="utf-8")
	- create a workbook
sheet1 = book.add_sheet("ShowMeThePower") 		- create a sheet called “ShowMeThePower”
sheet1.write(0, 0, "Python is Great!")
	- write at A1 of the excel 
book.save("trial.xls")	
	- save the excel file

---
# write a lot

```python
import xlwt
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("ShowMeThePower")
for row in xrange(1,10):
    for col in xrange(1,10):
        sheet1.write(row, col, row*col)
book.save("WriteAlot.xls")
print '-_-!'

```

---
# summary
Install python packages
Import a python package
    - import xlrd
Read an excel file
Write an excel file
