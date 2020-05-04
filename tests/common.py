"""Common test code."""
from datetime import tzinfo
from typing import Final, cast

from dateutil import tz

TIMEZONE_STR0: Final = "Europe/London"
TIMEZONE_STR1: Final = "America/Los_Angeles"
TIMEZONE0: Final = cast(tzinfo, tz.gettz(TIMEZONE_STR0))
TIMEZONE1: Final = cast(tzinfo, tz.gettz(TIMEZONE_STR1))
