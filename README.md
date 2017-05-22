# sqlinpython
Connect to Sqlserver database from Python code and perform CRUD Operations

Steps to follow to connect to SQL Server 

Install python and follow the below steps :

1.Add  Path in  environment variables : example-add c:\python34\;c:\python34\script

The above are the python installed paths
python34-version

neccessary paths:
c:\python34\;c:\python34\script


2.Download pymssql  module  to  import in our program in order to connect to database

Install through exe

pymssql-2.1.1.win32-py3.4.exe


https://pypi.python.org/simple/pymssql/--download  required exe  from  this site and  run

or
Install with PIP:
copy the whl file in python34 folder and in cmd-go to python34 folder and  run

pip install pymssql-2.1.2-cp34-cp34m-win32.whl

Select the correct whl file with respect to 32/64 bit python version installed and machine configuration 

Another way  through pip : pip install https://pypi.python.org/packages/cp26/p/pymssql/pymssql-2.1.1-cp26-none-win32.whl

3.Now  we can import the pymssql  module in our code and connect to sql server
