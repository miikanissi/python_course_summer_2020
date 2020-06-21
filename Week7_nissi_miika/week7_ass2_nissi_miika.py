class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.alarm = AlarmClock()

    def ticking(self):
        if self.seconds < 59:
            self.seconds += 1
        else:
            self.seconds = 0
            if self.minutes < 59:
                self.minutes += 1
            else:
                self.minutes = 0
                if self.hours < 23:
                    self.hours +=1
                else:
                    self.hours = 0

        if self.alarm.isActive():
            if (self.hours == self.alarm.hour and self.minutes == self.alarm.minute and self.seconds == 0):
                self.alarm.onWakeUp()

    def getTime(self):
        info = str(self.hours) +  ":" + str(self.minutes) + ":" + str(self.seconds)
        return info

    def getAlarm(self):
        return self.alarm

class AlarmClock():
    def __init__(self, hour = 0, minute = 0):
        self.hour = hour
        self.minute = minute
        self.active = False

    def setAlarm(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def isActive(self):
        return self.active
    
    def onWakeUp(self):
        print("BZZZZZ Wake up!!!")

myClock = Clock(22,59,58)
print(myClock.getTime())

myClock.getAlarm().setAlarm(23,4)
myClock.getAlarm().activate()

for i in range(2000):
    myClock.ticking()
print(myClock.getTime())

myClock.getAlarm().deactivate()
for i in range(100000):
    myClock.ticking()
print(myClock.getTime())
