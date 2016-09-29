# parser
This is an example of html parser that uses xpath expressions (Python 2.7).  

##### Before usage

        pip install lxml

##### How to use

Input data stores in the file `input`.  
The first line is `url` for parsing.  
Each other line consists from description of xpath expression (what it try to find)  
and `xpath` for searching.
(See an example in this repository.)  

##### Running

    python parser.py

Results will be display in the console and will be write in the file `out`.  
Data in the file `out` will be rewritten each time when you run this script.  