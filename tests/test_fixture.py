from unittest import TestCase

from assertpy import assert_that

from fixturepy import Fixture


class FixtureTest(TestCase):
    def test_fixture_should_create_string(self):
        value = Fixture().create(str)

        assert_that(value).is_not_empty()

    def test_fixture_should_create_integer(self):
        value = Fixture().create(int)

        assert_that(value).is_greater_than_or_equal_to(0)
