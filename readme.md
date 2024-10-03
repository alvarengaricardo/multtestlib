# multtestlib: A package developed for performing unit tests in Python using multiprocessing.

Multtestlib has been devised to aid Python testers in expediting their testing processes through multiprocessing. This approach allows customizable utilization of the computer's available processor cores, facilitating workload distribution and consequent reduction in the overall execution time of the test suite.

---
![GitHub release](https://img.shields.io/github/release/alvarengaricardo/multtestlib.svg) [![Python](https://img.shields.io/badge/Python-%3E%3D%203.7-blue.svg)](https://www.python.org/downloads/) [![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) [![Downloads](https://pepy.tech/badge/multtestlib)](https://pepy.tech/project/multtestlib)
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

Here are some code snippets illustrating the usage of multtestlib:

    # It is strongly recommended to create a test function to be called by the main() function.
    
    import multtestlib as mtl


    # Class to be tested
    class Cube:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_volume(self):
        return self.side_length ** 3


    # Functions to be tested
    def add(a, b):
        return (a + b)


    def subtract(a, b):
        return a - b


    # Wrapper function to test a class method
    # When testing methods of a class, create a function (outside of the class)
    # to invoke it:
    # def method(object):
    #     return object.method()
    def calculate_volume(cube):
        return cube.calculate_volume()


    # The tester function
    def tester():
        argument_list_a = [1, 2, 3, 5, 7, 9]
        argument_list_b = [2, 3, 4, 4, 3, 6]
        expected_list = [3, 5, 7, 1, 4, 2]
        functions_list = [add, add, add, subtract, subtract, subtract]
        argument_list_cube = [Cube(3), Cube(4), Cube(5)]
        expected_list_cube = [27, 64, 125]
        functions_list_cube = [calculate_volume, calculate_volume, calculate_volume]
        cpu = 1
        mtl.test_equal(cpu, argument_list_a, argument_list_b, expected_list, functions_list)
        mtl.test_equal(cpu, argument_list_cube, "", expected_list_cube, functions_list_cube)


    if __name__ == "__main__":
        mtl.init()
        tester()
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
