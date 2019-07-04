"""
    Hour Clock
"""


class HourClock:
    """
        Hour clock

        Args :
            initial_hour (int) : hour to initialize with
        Attributes :
            actual_hour (int) : actual hour
    """
    actual_hour: int

    def __init__(self, initial_hour: int = 6):
        self.actual_hour = initial_hour

    def __repr__(self):
        return str(self.actual_hour)

    def __add__(self, other):
        if type(other) == HourClock:
            other = other.actual_hour
        temp_hour = self.actual_hour + other

        # If we pass a "day", we go to the other "day"
        if temp_hour >= 24:
            temp_hour -= 24
        return temp_hour

    def __int__(self):
        return self.actual_hour

    def get_hour(self):
        """
            Get actual time of clock
            :return: actual hour
        """
        return self.actual_hour

    def add(self, other):
        """
            Adds an hour
            :param other: (clock or int) hour to add
            :return self:
        """
        self.actual_hour = self.__add__(other)
        return self

    def delta(self, other) -> int:
        """
            Return positive difference from self to other
            :param other: (clock or int) hour to compare to
            :return: (int) difference
        """
        if type(other) == HourClock:
            other = other.actual_hour
        standard_diff = other - self.actual_hour

        # If the other hour is from another "day", the difference is negative, and so we add 1 "day"
        if standard_diff < 0:
            standard_diff += 24
        return standard_diff

    def between(self, x, y) -> bool:
        """
            Returns if the clock is between hour x and hour y
            :param x: (clock) first hour of interval
            :param y: (clock) second hour of interval
        """
        return x.delta(y) > self.delta(y)
