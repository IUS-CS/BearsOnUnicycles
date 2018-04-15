# Testing Overview

## Engine Tests
The engine that this project runs on is tested using the `pytest` unit test library.
The files for the tests are located in src/engine/test and there are 37 at last count.
These tests consist of unit tests and function tests to ensure the base mechanics of the engine are functioning properly.
An example of a function test that verifies the `get_children_with_component` function can be found below.
It tests the interaction with the `GameObject` and `Component` classes.
```python
    #This is a sample test from the test_gameObject unit test module

    def test_get_children_with_component(self):
        g = game_object.GameObject("Test1")
        g2 = game_object.GameObject("Test2")
        g.add_child(g2)
        g2.add_component(component.Component())
        assert g2.parent is g
        try:
            l = g.get_children_with_component(component.Component)
        except game_object.GameObjectError:
            assert False
        assert l[0] is g2

```

## System Tests
Due to the nature of the pygame library as well as the nature of the software (heavily graphical), automated system tests are near impossible.
Thus, manual play-testing must be done in order to accommodate this gap in our testing.
A sample test document is included `docs/res` to give an example of a play-test.

## Travis CI
As noted in the README, this project utilizes Travis CI to provide continuous integration.
It runs all of the unit tests for this project automatically any time a pull request against master is made.
This has sped up workflow tremendously and eliminated the need for tests to be ran and verified before pushing branches. 