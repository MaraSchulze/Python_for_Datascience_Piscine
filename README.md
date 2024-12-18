# 🐍 Python for Data Science Piscine 🐍
### Description
This is the 5 module course of the 42school for students interested in Python and data science.  
It introduces basic Python, Numpy, Pandas and Matplotlib.  
The descriptions of the exercises are found in the subject pdfs in the 5 module folders.  
### Modules
| Module Name       | Short Description of Exercises                       |
|-------------------|-----------------------------------------------------|
| Module 0: Starting  | First python script, datetime, First function, Forms of None and 0, Modulo and Assertions, First program, filter, dicts, tqdm, First package creation |
| Module 1: Arrays   | numpy, 2D arrays, load an image, slices, transpose, list comprehensions |
| Module 2: Data Tables  | pandas load_csv, matplotlib, matplotlib with 2 plots, scatter plots and simple data wrangling |
| Module 3: Oriented Object Programming | Simple class, Inheritance, Diamand Problem and MRO, magic functions and operator, abstractmethod decorator |
| Module 4: Data Oriented Design | statistics, closures, decorators, dataclass |
### Requirements
venv
### Usage
First set up the virtual environment (it takes a little while):
```
make
```
Then activate the virtual environment (if it works there appears "(venv)" as prompt):
```
source venv/bin/activate
```
  
Now cd into the module folder, then cd into the subfolder with the exercise:
```
cd Module_<n>
cd ex<0x>
```
then execute (according to the exercise):
```
python <programname>.py
```
or
```
python tester.py
```

If you want to leave the virtual environment, just type
```
deactivate
```
