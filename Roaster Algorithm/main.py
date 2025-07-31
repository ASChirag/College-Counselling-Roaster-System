import random

class Student:
    def __init__(self, name, rank):
        self.name = str(name)
        self.rank = int(rank)
        random_number = random.randint(101, 999)
        self.register_number = f"DCET392025{random_number}"
    
    def display_details(self):
        print(f"\n Register Number : {self.register_number} \n Name : {self.name} \n Rank: {self.rank} \n ")

class Option:
    def __init__(self, college, department, priority):
        self.college = str(college)
        self.department = str(department)
        self.priority = int(priority)

class Option_entry:
    def __init__(self):
        self.option_entry = []
    
    def add_option_entry(self, option):
        self.option_entry.insert(option.priority, option)
        self.option_entry.sort(key=lambda option: option.priority)
    
    def remove_option_entry(self, option):
        if option.prioirty not in self.option_entry:
            print("Option not in Option Entry")
        else:
            self.option_entry.remove(option.priority)
    
    def display_option_entry(self):
        for i in range(len(self.option_entry)):
            print(f"Priority {i} College: {self.option_entry[i].college} Department: {self.option_entry[i].department}")

    def clear_option_entry(self):
        self.option_entry.clear()

    def retrieve_option_entry(self):
        option_entry_list = []
        for item in self.option_entry:
            option = f"{item.college}_{item.department}"
            option_entry_list.append(option)
        return option_entry_list

    def length(self):
        return len(self.option_entry)

class Roaster_Mechanism:
    def __init__(self):
        pass

    def allote_college(self, student, option_entry, College_seats):
        College_seats = College_seats
        option_entry_list = option_entry.retrieve_option_entry()
        print("Allocation Started")
        if option_entry_list is None or len(option_entry_list) == 0:
            print("No option entry")
            print(option_entry_list)
            return f"Register Number : {student.register_number} \n Name : {student.name} \n Rank: {student.rank} \n No College has been alloted to you..."
    
        else:
            print(f"\nOption entry list: {option_entry_list}")
            for i in range (0, len(option_entry_list)):
                student_college_name = option_entry_list[i]
                print(f"\nChecking for {student_college_name} for student {student.name}")
                print(f"\nChecking seats availability, {College_seats[student_college_name]}")
                if College_seats[student_college_name] > 0:
                    College_seats[student_college_name] -= 1
                    return print(f"\nRegister Number : {student.register_number} \n Name : {student.name} \n Rank: {student.rank} \n Congratulations !!! \n {student_college_name} has been alloted to you...")


College_seats = {
    "R V College of Engineering_Computer Science": int(3),
    "R V College of Engineering_Artificial Intelligence": int(2),
    "R V College of Engineering_Data Science & AI": int(1),
    "PES Campus_Computer Science": int(4),
    "PES Campus_Artificial Intelligence": int(5),
    "PES Campus_Data Science & AI": int(6),
    "BMS College of Engineering_Computer Science": int(2),
    "BMS College of Engineering_Artificial Intelligence": int(3),
    "BMS College of Engineering_Data Science & AI": int(4)
}


# option1 = Option("R V College of Engineering", "Computer Science", 1)
# option2 = Option("PES Campus", "Computer Science", 4)
# option3 = Option("R V College of Engineering", "Artificial Intelligence", 2)
# option4 = Option("PES Campus", "Artificial Intelligence", 5)
# option5 = Option("R V College of Engineering", "Data Science & AI", 3)
option_entry1 = Option_entry()
Roaster_system = Roaster_Mechanism()
student1 = Student("Kushal", 1)

option1 = Option("R V College of Engineering", "Computer Science", 5)
option2 = Option("PES Campus", "Computer Science", 7)
option3 = Option("R V College of Engineering", "Artificial Intelligence", 4)
option4 = Option("PES Campus", "Artificial Intelligence", 8)
option5 = Option("R V College of Engineering", "Data Science & AI", 6)
option6 = Option("BMS College of Engineering", "Computer Science", 2)
option7 = Option("BMS College of Engineering", "Artificial Intelligence", 1)
option8 = Option("R V College of Engineering", "Data Science & AI", 3)
option_entry1.add_option_entry(option1)
option_entry1.add_option_entry(option2)
option_entry1.add_option_entry(option3)
option_entry1.add_option_entry(option4)
option_entry1.add_option_entry(option5)
option_entry1.add_option_entry(option6)
option_entry1.add_option_entry(option7)
option_entry1.add_option_entry(option8)

Roaster_system.allote_college(student=student1, option_entry=option_entry1, College_seats=College_seats)

# student1.display_details()
# option_entry1.display_option_entry()

student2 = Student("Kishore", 2)

option_entry2 = Option_entry()

option1 = Option("R V College of Engineering", "Computer Science", 1)
option2 = Option("PES Campus", "Computer Science", 4)
option3 = Option("R V College of Engineering", "Artificial Intelligence", 2)
option4 = Option("PES Campus", "Artificial Intelligence", 5)
option5 = Option("R V College of Engineering", "Data Science & AI", 3)
option6 = Option("BMS College of Engineering", "Computer Science", 6)
option7 = Option("BMS College of Engineering", "Artificial Intelligence", 7)

option_entry2.add_option_entry(option1)
option_entry2.add_option_entry(option2)
option_entry2.add_option_entry(option3)
option_entry2.add_option_entry(option4)
option_entry2.add_option_entry(option5)
option_entry2.add_option_entry(option6)
option_entry2.add_option_entry(option7)

student2.display_details()
Roaster_system.allote_college(student=student2, option_entry=option_entry2, College_seats=College_seats)