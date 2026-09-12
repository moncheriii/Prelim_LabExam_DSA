
class Student:
    def __init__(self, student_id: str, student_name: str, course: str, year_level: int):
        self.student_id = student_id
        self.student_name = student_name
        self.course = course
        self.year_level = year_level

    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.student_name} | Course: {self.course} | Year Level: {self.year_level}"


class DynamicArray:
    def __init__(self):
        self._capacity = 5  # Initial capacity of 5
        self._count = 0
        # Initialize internal fixed-size storage with None
        self._array = [None] * self._capacity

    def _resize(self):
        new_capacity = self._capacity * 2
        new_array = [None] * new_capacity
        for i in range(self._count):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity
        print(f"-> Array capacity automatically increased to {new_capacity}")

    def add(self, student: Student):
        if self._count == self._capacity:
            self._resize()
        self._array[self._count] = student
        self._count += 1
        print("Student added successfully.")

    def display(self):
        if self._count == 0:
            print("No student records found.")
            return
        print("\n--- STUDENT LIST ---")
        for i in range(self._count):
            print(self._array[i])

    def search(self, student_id: str) -> int:
        for i in range(self._count):
            if self._array[i].student_id.lower() == student_id.lower():
                return i
        return -1

    def get(self, index: int):
        if 0 <= index < self._count:
            return self._array[index]
        return None

    def remove(self, student_id: str):
        index = self.search(student_id)
        if index == -1:
            print(f"Error: Student with ID {student_id} not found.")
            return
        
        for i in range(index, self._count - 1):
            self._array[i] = self._array[i + 1]
        self._array[self._count - 1] = None
        self._count -= 1
        print("Student removed successfully.")

    def size(self) -> int:
        return self._count

    def get_capacity(self) -> int:
        return self._capacity


def main():
    list_adt = DynamicArray()
    choice = -1

    while choice != 7:  
        print("\n==================================")
        print("      STUDENT RECORD MANAGER      ")
        print("==================================")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Remove Student")
        print("6. Display Array Information")
        print("7. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 7.")
            continue

        if choice == 1:
            sid = input("Enter Student ID: ")
            sname = input("Enter Student Name: ")
            scourse = input("Enter Course: ")
            try:
                syear = int(input("Enter Year Level: "))
                list_adt.add(Student(sid, sname, scourse, syear))
            except ValueError:
                print("Invalid input for year level. Operation cancelled.")
        elif choice == 2:
            list_adt.display()
        elif choice == 3:
            sid = input("Enter Student ID to search: ")
            idx = list_adt.search(sid)
            if idx != -1:
                print(f"Student Found: {list_adt.get(idx)}")
            else:
                print(f"Student with ID {sid} not found.")
        elif choice == 4:
            sid = input("Enter Student ID to update: ")
            idx = list_adt.search(sid)
            if idx != -1:
                st = list_adt.get(idx)
                st.student_name = input("Enter New Name: ")
                st.course = input("Enter New Course: ")
                try:
                    st.year_level = int(input("Enter New Year Level: "))
                    print("Student record updated successfully.")
                except ValueError:
                    print("Invalid year level input. Update aborted.")
            else:
                print(f"Student with ID {sid} not found.")
        elif choice == 5:
            sid = input("Enter Student ID to remove: ")
            list_adt.remove(sid)
        elif choice == 6:
            print(f"Current Number of Students: {list_adt.size()}")
            print(f"Current Array Capacity: {list_adt.get_capacity()}")
        elif choice == 7:
            print("Thank you for using Student Record Manager. Goodbye!")
        else:
            print("Invalid option. Please choose between 1 and 7.")


if __name__ == "__main__":
    main()