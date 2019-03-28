class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def createWork(work, duration):
        return Work(work, duration)

class Chum(Student):
    def __init__(self, name, age):
        Student.__init__(self, name, age)
        self.works = ["stampGame", "smallBeadFrame", "timeLineOfLife", "bigBang", "earlyHumans"]
        tempwork = {"stampGame":30, "smallBeadFrame":60, "timeLineOfLife":20, "bigBang":120, "earlyHumans":80}
        # for key,val in tempwork.items():
        #     self.works.append(Work(key, val))

    def does(self, work):
        if work in self.works:
            self.works.remove(work)
        else:
            print("{0} is not an available work.".format(work))

    def addWork(self, work):
        self.works.append(work)

class Work:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
