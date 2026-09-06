import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("Time to sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 10

    def to_work(self):
        print("Time to work")
        self.money += 20
        self.gladness -= 5
        self.progress -= 0.05

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.money < 0:
            print("Bankruptcy...")
            self.alive = False
        elif self.progress > 5:
            print("Passed...")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {self.progress}")
        print(f"Money = {self.money}")

    def choise(self):
        if self.money < 30:
            return self.to_work
        elif self.progress < 1:
            return self.to_study
        elif self.gladness < 20:
            return self.to_sleep
        else:
            live_cube = random.randint(1, 4)
            if live_cube == 1:
                return self.to_study
            elif live_cube == 2:
                return self.to_sleep
            elif live_cube == 3:
                return self.to_chill
            else:
                return self.to_work

    def live(self, day):
        day = f"Day {day} of {self.name} life"
        print(f"{day:=^50}")
        if self.money < 30:
            self.to_work()
        elif self.progress < 1:
            self.to_study()
        elif self.gladness < 20:
            self.to_sleep()
        else:
            live_cude = random.randint(1, 4)
            if live_cude == 1:
                self.to_study()
            elif live_cude == 2:
                self.to_sleep()
            elif live_cude == 3:
                self.to_chill()
            elif live_cude == 4:
                self.to_work()
        self.end_of_day()
        self.is_alive()


student1 = Student(name="Gerundy")

for day in range(365):
    if student1.alive == False:
        break
    student1.live(day)
