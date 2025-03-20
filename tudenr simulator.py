import random as r

class Student:
    def __init__(self, name):
        self.name = name
        self.happy = r.randint(50, 100)
        self.progress = r.randint(0, 10)
        self.alive = True
        self.money = money

    def study(self):
        print("Час для навчання")
        self.progress += r.randint(1, 5)
        self.happy -= r.randint(1, 5)

    def sleep(self):
        print("Час для сну")
        self.happy += r.randint(1, 10)

    def chill(self):
        print("Час для відпочинку")
        self.happy += r.randint(5, 10)
        self.progress -= r.randint(1, 5)
        self.money -= r.randint(50, 75)
    def work(selfself):
        print("час для работи")
        self.money += r.randint(100, 200)

    def is_alive(self):
        if self.progress < 5:
            print("Ти на грані відрахування, починай навчатися")
            self.alive = False
        elif self.progress <= 1:
            print("Відрахування з Інституту")
            self.alive = False
        elif self.progress >= 5:
            print("Відмінно навчаєшся")
            self.alive = False
        elif self.money = 0:
            print("иди работай")

            def live(self, days):
                for day in range(days):
                    if not self.alive:
                        break

                    dice = r.randint(1, 4)

                    if self.progress < 5:
                        self.study()
                    elif self.money < 50:
                        self.work()
                    elif dice == 1:
                        self.study()
                    elif dice == 2:
                        self.sleep()
                    elif dice == 3:
                        self.chill()
                    else:
                        self.work()
                    self.is_alive()
                    self.end_of_day()

            def end_of_day(self):
                print(f"День закінчився. Щастя: {self.happy}, Успішність: {self.progress}, Гроші: {self.money}")


        student = Student("Остап")


        student.live(365)

        if not student.alive:
            print("Студент не зміг прожити рік.")
        else:
            print("Студент успішно прожив рік!")

stl = Student("Oner")