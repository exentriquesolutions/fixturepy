from datetime import datetime, timezone, date
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

    def test_fixture_should_create_integer_range(self):
        value = self.fixture(int, fixture_range=(10, 20))

        assert_that(value).is_less_than_or_equal_to(20)
        assert_that(value).is_greater_than_or_equal_to(10)

    def test_fixture_should_create_email(self):
        value = self.fixture(Email)

        validate_email(value, check_deliverability=False)

    def test_fixture_should_create_floating_point_number(self):
        value = self.fixture(float)

        assert_that(value).is_greater_than_or_equal_to(0)
        assert_that(value).is_less_than_or_equal_to(1)

    def test_fixture_should_create_floating_point_number_range(self):
        value = self.fixture(float, fixture_range=(5, 10))

        assert_that(value).is_greater_than_or_equal_to(5)
        assert_that(value).is_less_than_or_equal_to(10)

    def test_fixture_should_create_datetime(self):
        value = self.fixture(datetime)

        assert_that(value).is_type_of(datetime)
        assert_that(value.tzinfo).is_equal_to(timezone.utc)
        assert_that(value.year).is_greater_than_or_equal_to(1970)
        assert_that(value.year).is_less_than_or_equal_to(2100)

    def test_fixture_should_create_date(self):
        value = self.fixture(date)

        assert_that(value).is_type_of(date)
        assert_that(value.year).is_greater_than_or_equal_to(1970)
        assert_that(value.year).is_less_than_or_equal_to(2100)
