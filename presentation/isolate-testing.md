Testable Objects
================

Isolate Testing
---------------

Isolating testing is crucial at the object, method, and functionality level. This will increase the reliability
of tests and reduce the complexity of modifying tested code.

### Test only one object at a time

In order to isolate testing on an object, you need to test only that object. A failure on a dependent should
not make the object you are testing fail. This leads to a false failure and creates doubts in your tests
and frustration with your devdeopment.

### Only test functionality once

Further isolation is performed and the functionlity level. Each test should only test a single piece of functionality.
This isolation prevents false failures and allows you to quickly identify the source of the unintended side effect.

### Inject mock objects that perform external functionality

As you are using [good objects](blueprint-to-a-good-object.md), you are building simple objects that have
functionality injected via other objects. Use [mock objects](https://en.wikipedia.org/wiki/Mock_object) to
isolate object being tested from dependent objects. This will ensure that the dependent object functionality
will behave in a expdected manner regardless of the actual state on that object in the codebase.

When dealing with [mock objects](https://en.wikipedia.org/wiki/Mock_object), there are some rules of thumb to help
use mock objects effectively.

#### Stub methods to return expected results

Be sure to stub your happy path in the test setup. Do not rely on the happy path if your test requires a specific
response. The stubs created in the setup are only for tests that do not rely on a specific behavior of stubbed methods.

#### Use spies to verify correct method calls against injected mocks

Do not assume you are making the correct call to a stub on a mocked object simply because the return value was correct.
Verify the calls with a spy. In [unittest's mock library](https://docs.python.org/dev/library/unittest.mock.html), stubs
are inherently spies. This is not always the case.

#### Use generic stubs and verify calls before assertions

Using generic stubs is preferred over call specific stubs. The validation of the call against the stub can be made in
spy assertions. In [unittest's mock library](https://docs.python.org/dev/library/unittest.mock.html), stubs
are inherently spies. This is not always the case. When using call specific stubs, if the correct parameters are not
met when calling the stub, there is no return value defined and ```None``` will be returned default. This will prevent
your test from identifying the failure in your code as it will likely error with the following:

    AttributeError: 'NoneType' object has no attribute 'get_object'

When a generic stub is used, an object will be returned and the test will a diagnosable failure message instead of an
error with a stack trace.

It is also important to verify stub calls before making response assertions. Even with a generic stub, response
assertions can give you unintelligible responses that are of no help. This is one of my favorite.

    AssertionError: False is not true

It is very obvious to nearly everyone that ```False``` is not true. The issue lies elsewhere in the code. If we
would have validated our mack call, we could have seen the real problem that we called the stub with the incorrect
attributes. That would fail with a descriptive error like this:

    AssertionError: Expected call: get_object('expected')
    Actual call: get_object('other')

Python does not provided for making certain tesrts dependent on others but you can use sub-tests to isolate testing
without re-testing functionality. The prior example could be handled like this:

    def test_method_call(self):
        self.main_object.run()
        result = self.dependant_object.get_object.assert_called_once_with('expected')

        with self.subTest(val=result):
            assertTrue(val)


[Prev](blueprint-to-a-good-object.md) [Next](adams-rules.md)