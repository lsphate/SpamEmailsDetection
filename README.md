#README

##1. File Structure & Environment
- All ___*.py___ and ___*.m___ applications must be placed in the same directory.

- Because of the constraint of file size, we cannot submit our partition of the dataset. The partition of the raw e-mail text file we used is:

	- **Training** part includes:

		- **ham**: *0001.1999-12-10.farmer.ham.txt* ~ *4100.2001-03-29.farmer.ham.txt*, total 2903 files.
	
		- **spam**: *0006.2003-12-18.GP.spam.txt* ~ *4198.2005-04-05.GP.spam.txt*, total 1198 files.

	- **Testing** part includes:

		- **ham**: *4103.2001-03-29.farmer.ham.txt* ~ *5172.2002-01-11.farmer.ham.txt*, total 742 files.

		- **spam**: *4201.2005-04-05.GP.spam.txt* ~ *5171.2005-09-06.GP.spam.txt*, total 302 files.

- Programming in **Mac OSX 10.10.3 64-bit**, **Matlab R2015a**, and **Python 2.7.9** with:
	- snowballstemmer ver. 1.2.0
	- stop-words ver 2015.2.23.1

##2. Pre-processing

We'll briefly introduce our codes in this part. Please be advised that we **DO NOT** encourage you to run you own version of parameters because this would directly affect the accuracy of the prediction model.

1. **hw3p4ipre1.py**: The Python application used to create the dictionary of the bag-of-words, generate the corresponding vectors of the e-mails data set. It well create 4 CSV files in current directory, named by *trainS.csv*, *trainH.csv*, *testS.csv* and *testH.csv*.

2. **hw3p4ipre2.m**: The MATLAB script used to load the 4 CSV files above into MATLAB, and dump the workspace to *vector.mat*.

	- **vector.mat**: This is the most important file that provides the parameters we need in building the model. We attach our own version of this file so please **DO** use this version while grading.


##3. Usage
Please put your custom test data sets in the **TAtest** folder, with each raw e-mail as a single text file. (Just like the professor provides.)

Use **hw3p4_1.py** to generate the corresponding vector of the your e-mail data sets. The output bag-of-words vector will be named by ***testTA.csv*** and placed in the same directory.

Then run **hw3p4_2.m** in MATLAB, it well call **classification.m**, which is the main function of building model and do testing. The output the result of test in the format of:

```
	Final =

     	0     0     0     0     1     1     1  ...
```

Where 0 represents hams and 1 represents spams.

##4. Developer & Citation

####Developer
Hao-Hsiang Chuang (hc2751)

Sun-Yi Lin (sl3833)

####Python Package
https://pypi.python.org/pypi/snowballstemmer

https://pypi.python.org/pypi/stop-words/2015.2.23.1


####Logic Regression
http://cs229.stanford.edu/notes/cs229-notes1.pdf
