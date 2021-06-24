# Python-CI-Example
An example Action/Workflow for Python CI

# What's happening?
The repo contains two Python files:

  1. some_basic_code.py
  2. some_basic_tests.py

If we were to clone and run this repo using the command:

```python -m unittest some_basic_tests.py```

We would expect to get the following output:

```
F.
======================================================================
FAIL: test_my_basic_function_fails (some_basic_tests.TestStringMethods)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/ue0meq/GITHUBACTIONTEST_2/some_basic_tests.py", line 11, in test_my_basic_function_fails
    self.assertEqual(my_basic_function(), "")
AssertionError: 'Hi from my basic function!' != ''
- Hi from my basic function!
+ 


----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
```
