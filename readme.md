 # multtestlib

**multtestlib** (2023.4) is a library for running unit tests using processing parallel, written in Python.

![table](https://github.com/alvarengaricardo/multtestlib/blob/main/table.png?raw=true.png)

## Example

**Code:**

    import multtestlib as mtl
    import library_to_test as ltt
    

    def main():
        # Specify the number of CPUs to be used.
        cpus = 4

        # Create one, or two, array with the input parameters.
        array_in1 = [a, b, c, d, e]
        array_in2 = [aa, bb, cc, dd, ee]

        # Create one, or two, array with the output parameters (expected values).
        array_out = [f, g, h, i, j]

        # Provide the parameters for the selected test function.
        # In this example "test_equal".
        mtl.test_equal(cpus, array_in1, array_in1, array_out, ltt.function_to_test)


    if __name__ == "__main__":
        mtl.init()
        main()
        mtl.end()


**Generated Files, with the results**

    filepass.txt -> Contains passed tests
    filefail.txt -> Contains failed tests
    filetot.txt -> Contains all tests
