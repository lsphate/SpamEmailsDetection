#README

##1. File Structure
- All applications are in the same directory: ___*.py___, ___*.m___

- Because of the constraint of file size, we cannot submit our partition of the dataset. The partition of the raw e-mail text file we used is:

	- The folder **Training** includes the raw e-mail text tile. 

		- **/Training/ham** for 		***0001.1999-12-10.farmer.ham.txt*** ~ ***4100.2001-03-29.farmer.ham.txt***, total 2903 files
	
		- **/Training/spam** for ***0006.2003-12-18.GP.spam.txt*** ~ ***4198.2005-04-05.GP.spam.txt***, total 1198 files

	- The folder **Testing** includes the raw e-mail text tile.

		- **/Testing/ham** for ***4103.2001-03-29.farmer.ham.txt*** ~ ***5172.2002-01-11.farmer.ham.txt***, total 742 files

		- **/Testing/spam** for ***4201.2005-04-05.GP.spam.txt*** ~ ***5171.2005-09-06.GP.spam.txt***, total 302 files
		
- Please put you custom test data set in **TAtest** folder, with each raw e-mail as single text file. (Just like the professor provides.)

- Programming in **Mac OSX 10.10.3 64-bit** and **Matlab R2015a**.

##2. Introduction

1. **hw3p4ipre1.py**: The Python application used to create the dictionary of the bag-of-words, and generate the corresponding vector of the e-mails data set.
2. **hw3p4ipre2.m**: The Python application used to load the vectors in to MATLAB, and dump the workspace to ***vector.mat***.
3. **vector.mat**: The training vectors of our model.
4. **classification.m**: The MATLAB function of training the model and testing the input vector.


##3. Usage
Use **hw3p4_1.py** to generate the corresponding vector of the **TEST** mails set.

Put all the test raw e-mail text files into **TAtest** folder in the same directory, then run **hw3p4i_2.py**. The output bag-of-words vector will be named by ***testTA.csv*** and placed in the sam directory.

Then run **hw3p4_2.m** in MATLAB, it well output the result of test in the format of:

```
	Final =

     	0     0     0     0     1     1     1  ...
```

Where 0 represents hams and 1 represents spams.

##4. Citation

####Python Package
https://pypi.python.org/pypi/snowballstemmer
https://pypi.python.org/pypi/stop-words/2015.2.23.1


####Logic Regression
http://cs229.stanford.edu/notes/cs229-notes1.pdf
