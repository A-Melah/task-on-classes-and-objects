from tkinter import scrolledtext


class Student:
     
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, new_name):
        self.name = new_name
        return new_name

    def change_age(self, new_age):
        self.age = int(new_age)
        return new_age

    def add_track(self, new_track):
        self.track = new_track
        return new_track

    def get_score(self):
        return self.score

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)



print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_track("UI/UX"))
Bob.get_score()
