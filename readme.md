 # multtestlib

**multtestlib** is a library for running unit tests using processing parallel, written in Python.

![table](https://user-images.githubusercontent.com/16055876/222324613-78df26fa-1cf5-48ce-b8e8-4018d6a2224c.png)

## Example

**Code:**

    import multtestlib  
    def main():
    
    a = 90  
    b = 35  
    c = 12
    
    with multtestlib.Pool() as pool:
	    pool.starmap(multtestlib.test_equal,
		[(a, 90),
		 (b, 35),
		 (c, 12)])
    		 
    if __name__ == "__main__":  
        multtestlib.init()  
        multtestlib.freeze_support()  
        main()  
        multtestlib.end()

**Output:**

    test_equal - a: 35 b: 35 Result: Pass
    test_equal - a: 90 b: 90 Result: Pass
    test_equal - a: 12 b: 12 Result: Pass
    Total: 3
    Passed: 3

**Generated Files**

    filepass.txt -> Contains passed tests
    filefail.txt -> Contains failed tests
    filetot.txt -> Contains all tests
