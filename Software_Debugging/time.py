class Time(object):
    def __init__(self, h=0, m=0, s=0):
        self._hours  = int(h)
        self._minutes = int(m)
        self._seconds = int(s)
        self.checkRep()

    def checkRep(self):
        assert 0 <= self.hours() <= 23
        assert 0 <= self.minutes() <= 59
        assert 0 <= self.seconds() <= 60

    def hours(self):
        return self._hours

    def minutes(self):
        return self._minutes

    def seconds(self):
        return self._seconds

    def __repr__(self):
        return '{:02d}:{:02d}:{:02d}'.format(self.hours(),
                                             self.minutes(),
                                             self.seconds())

    def seconds_since_midnight():
        return self.hours() * 3600 + self.minutes() * 60 + self.seconds()
    
    def advance(self, s):
        self.checkRep()
        old_seconds = self.seconds_since_midnight()

        self.checkRep()
        assert (self.seconds_since_midnight() ==
                (self.seconds() + seconds_offset) % (24 * 60 * 60))


if __name__ == '__main__':
    t = Time(3.14, 0, 0)
    print t
