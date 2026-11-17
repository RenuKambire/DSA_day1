
class Hospital:
    def __init__(self):
        self.patients = []

    # Add patient (Enqueue)
    def add_patient(self):
        pid = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        priority = int(input("Enter Priority (1-Critical, 2-Serious, 3-Normal): "))

        if priority not in [1, 2, 3]:
            print("Invalid Priority!")
            return

        patient = (priority, pid, name)
        self.patients.append(patient)

        # Sort patients according to priority
        self.patients.sort()

        print("Patient added successfully!")

    # Display Next patient
    def display_next(self):
        if not self.patients:
            print("No patients waiting.")
        else:
            priority, pid, name = self.patients[0]

            print("\nNext Patient to be Treated:")
            print("Patient ID:", pid)
            print("Patient Name:", name)
            print("Priority:", priority)

    # Remove patient (Dequeue)
    def dequeue(self):
        if not self.patients:
            print("No patients to remove.")
        else:
            patient = self.patients.pop(0)

            print("Patient treated and removed:")
            print("Patient ID:", patient[1])
            print("Patient Name:", patient[2])

    # Display all waiting patients
    def display_all(self):
        if not self.patients:
            print("No waiting patients.")
        else:
            print("\nWaiting Patients in Priority Order:")
            for priority, pid, name in self.patients:
                print("Patient ID:", pid,
                      "| Name:", name,
                      "| Priority:", priority)



h = Hospital()

while True:
    print("\n--- Hospital Emergency Management ---")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient")
    print("4. Display All Patients")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        h.add_patient()

    elif choice == 2:
        h.display_next()

    elif choice == 3:
        h.dequeue()

    elif choice == 4:
        h.display_all()

    elif choice == 5:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please try again.")
