from unittest import TestCase

from assertpy import assert_that
from email_validator import validate_email

from fixturepy import Fixture, Email


class FixtureTest(TestCase):
    fixture = Fixture()

    def test_fixture_should_create_string(self):
        value = self.fixture(str)

        assert_that(value).is_not_empty()

    def test_fixture_should_create_integer(self):
        value = self.fixture(int)

        assert_that(value).is_greater_than_or_equal_to(0)

    def test_fixture_should_create_email(self):
        value = self.fixture(Email)

        validate_email(value, check_deliverability=False)
