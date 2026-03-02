class RegistrationQueue:
    def __init__(self):
        self.queue = []

    def add_student(self, student_name):
        self.queue.append(student_name)
        print(f"{student_name} is now in line.")

    def process_next(self):
        if len(self.queue) > 0:

            student = self.queue.pop(0)
            print(f"Processing: {student}. {len(self.queue)} people still waiting.")
        else:
            print("The line is empty!")

support = RegistrationQueue()

support.add_student("Alice")
support.add_student("Bob")
support.add_student("Charlie")

support.process_next()