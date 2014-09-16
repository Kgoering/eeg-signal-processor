from distutils.core import setup

setup(
	name = "EEG-Processor",
	packages = ["EEG-Processor"],
	version = "1.0.0",
	author = "Bryan Burkett, Jonathan Coup, Kaleb Goering, Joshua Marple",
	author_email = "eeg-signal-processor@googlegroups.com",
	url = "",
	decription = "Uses machine learning algorithms to predict what is thought",
	long_description = "Takes either a transformed EEG signal or a raw EEG signal and can either learn it or predict its value. It can use a SVM, LDA, or QDA for the learning algorithm. The libraries needed: PyWavelets, Numpy, CSV, Scikit-Learn"
	classifiers = [
		"Programming Language :: Python",
	        "Programming Language :: Python :: 3",
	        "Development Status :: 1.0.0",
	        "Intended Audience :: Developers",
	        "License :: OSI Approved :: Apache",
	        "Operating System :: OS Independent",
		]
	)
