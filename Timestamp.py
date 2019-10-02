class Timestamp(object):
    def __init__(self, s): # s = hh:mm:ss.ms
        self.hours = int(s[:2])
        self.minutes = int(s[3:5]) 
        self.seconds = int(float(s[6:]))


    def secondsConverter(self):
        hoursInSeconds = self.hours * 3600
        minutesInSeconds = self.minutes * 60

        return hoursInSeconds + minutesInSeconds + self.seconds
