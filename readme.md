# multtestlib: A package developed for performing unit tests in Python using parallel processing.

---

Multtestlib has been devised to aid Python testers in expediting their testing processes through non-distributed parallel processing. This approach allows customizable utilization of the computer's available processor cores, facilitating workload distribution and consequent reduction in the overall execution time of the test suite.

---

## Installation

Multtestlib is available on PyPi and can be installed using the pip command:
    
    pip install multtestlib

---

## Requirements

Multtestlib requires Python 3.7 or later to run.

---

## Usage

For parallel processing usage, the input parameters of the test functions and their respective expected values must be stored in lists. During the test processing, multtestlib will take care of distributing and managing the data contained in the lists - and functions - among the processor cores indicated in the test program.

Next, we will see an example of a unit test for the **myfunction(a, b)** being submitted for execution using parallel processing:

    import multtestlib as mtl
    import functions

    def main():
        cpus = 8 # Specify the number of CPUs to be used.
        input_values1 = []
	    input_values2 = []
	    return_values = []
		
        # It is necessary to store the input data and
	    # expected values in their respective lists.

        mtl.test_equal(cpus, input_values1, input_values2, return_values, functions.myfunction)
    
	
    if __name__ == "__main__":
        mtl.init()
        main()
        mtl.end()
---

## Output Files

During the execution of the unit tests, three output files are generated containing the results of the tests performed.

    filepass.txt -> Contains passed tests
    filefail.txt -> Contains failed tests
    filetot.txt -> Contains all tests

---

## List of testing commands

![table](https://github.com/alvarengaricardo/multtestlib/blob/main/table.png?raw=true.png)

---
