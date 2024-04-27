# multtestlib: A package developed for performing unit tests in Python using multiprocessing.

Multtestlib has been devised to aid Python testers in expediting their testing processes through multiprocessing. This approach allows customizable utilization of the computer's available processor cores, facilitating workload distribution and consequent reduction in the overall execution time of the test suite.

---

## Installation

Multtestlib is available on PyPi and can be installed using the pip command:
    
    pip install multtestlib

---

## Requirements

Multtestlib requires Python 3.7 or later to run.

---

## Usage

For multiprocessing usage, the input parameters of the test functions and their respective expected values must be stored in lists. During the test processing, multtestlib will take care of distributing and managing the data contained in the lists - and functions - among the processor cores indicated in the test program.

Next, we will see an example of a unit test for the **myfunction(a, b)** being submitted for execution using multiprocessing:

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
## MIT License

Copyright (c) 2022-2024 Ricardo Ribeiro de Alvarenga

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
