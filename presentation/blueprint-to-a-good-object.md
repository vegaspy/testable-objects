Testable Objects
================

Blueprint to a Good Object
--------------------------

There is a definite blueprint to designing a goot object that can be well tested in a faily simple manner.

### Simple

Simple objects are the easiest to read, modify, and test. Push for simple objects that do one thing and one thing only.
This is commonly known as the
[single responsibility principle](https://en.wikipedia.org/wiki/Single_responsibility_principle).

### Contained

Objects should be as private as possible only exposing what is required. This is known as
[Encapsulation](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)).

### Composed

In order to provide objects that complete complex operations, you must compose objects that are
[facades](https://en.wikipedia.org/wiki/Facade_pattern) to the underlying complexity.
[Dependency injection](https://en.wikipedia.org/wiki/Dependency_injection) is the vehicle with which you
implement [composition](https://en.wikipedia.org/wiki/Object_composition). Inheritance is to be avoided where
possible. Even though Pythom allows for
[multiple inheritance](https://docs.python.org/2/tutorial/classes.html#multiple-inheritance),
[composition should be preferred over inheritence](https://en.wikipedia.org/wiki/Composition_over_inheritance).
[Factory](https://en.wikipedia.org/wiki/Factory_(object-oriented_programming)) objects and methods can be used
to handle complex compositions in a practical manner. Composed objects let you isolate the tests to the objects
providing the pieces of functionality. You simply need to test the proper interaction with the injected objects.

### Very Loosely Coupled

Even well [encapsulated](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)) objects can be
coupled with other objects by the means that they communicate. All too often objects that are not directly related
are dependent on each other in order to communicate. To make objects more loosely coupled, consider utilizing
[mediator](https://en.wikipedia.org/wiki/Mediator_pattern), [observer](https://en.wikipedia.org/wiki/Observer_pattern),
or [publish/subscribe](https://en.wikipedia.org/wiki/Publish/subscribe) design patterns to facilitate communication
between objects. Design patterns such as
[chain of responsibility](https://en.wikipedia.org/wiki/Chain_of_responsibility_pattern),
[comamnd](https://en.wikipedia.org/wiki/Command_pattern), and
[strategy](https://en.wikipedia.org/wiki/Strategy_pattern) can be used to abstract functionality to a manner similar to
[middleware](https://en.wikipedia.org/wiki/Middleware).

[Prev](why-focus-on-objects-not-tests.md) [Next](isolate-testing.md)