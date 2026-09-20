import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 50
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

    def live(self, day):
        day = f"Day {day} of {self.name} life"
        print(f"{day:=^50}")
        if self.money < 5:
            self.to_work()
        elif self.progress < 1:
            self.to_study()
        elif self.gladness < 10:
            self.to_sleep()
        else:
            cube = random.randint(1, 4)
            if cube == 1:
                self.to_study()
            elif cube == 2:
                self.to_sleep()
            elif cube == 3:
                self.to_chill()
            elif cube == 4:
                self.to_work()
        self.end_of_day()
        self.is_alive()


student1 = Student(name="Gerundy")

for day in range(365):
    if student1.alive == False:
        break
    student1.live(day)
