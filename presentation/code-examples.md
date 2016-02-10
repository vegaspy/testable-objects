Testable Objects
================

Code Examples
-------------

### Bad Code

The file [bad_car.py](../testable_objects/bad_car.py) contains an example of basicaly untestable code. It is also
highly coupled to make matters worse.

### Good Code

The file [good_car.py](../testable_objects/good_car.py) contains an example of a fairly good set of objects
that adhere to the [good object blueprint](blueprint-to-a-good-object.md).

### Tests

There are examples of bad tests that do not use mocks in the ```GoodCarBadTest``` test class as well as
examples of fairly good tests using mocks and stubs in the ```GoodCarGoodTest``` test class in the
[good_car_tests.py](../tests/good_car_tests.py) test file.

[Prev](adams-rules.md)