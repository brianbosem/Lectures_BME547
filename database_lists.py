class Patient:

    def __init__(self, name, id_no, age):
        self.name = name
        self.id_no = id_no
        self.age = age
        self.tests = []
    
    def __repr__(self):
        return "{}: {}".format(self.id_no, self.name)


def class_work():
    new_patient = Patient("Ann Ables", 120, 36)
    print(new_patient.id_no)
    print(new_patient.name)
    x = Patient("Bob Boyles", 24, 33)
    print(x.name)
    print(x)


def create_database_entry(patient_name, id_no, age):
    new_patient = Patient(patient_name, id_no, age)
    # new_patient = {"name": patient_name, "id_no": id_no, "age": age, "tests": [],}
    # new_patient = [patient_name, id_no, age, []]
    return new_patient

def print_database(db):
    for patient in db:
        print(patient[0][0])

def print_database2(db): # this is something that python can do better (done below)
    for i in range(len(db)):
        print("{} - {}".format(i, db[i]))

def print_database3(db):
    for i, patient in enumerate(db):
        print("{} - {}".format(i, patient))

def print_database4(db): 
    locations = ["Room 1", "Room 4", "ER", "Post-Op"]
    for i, patient in enumerate(db):
        print("{} - {} - {}".format(i, patient, locations[i]))

def print_database5(db): 
    locations = ["Room 1", "Room 4", "ER", "Post-Op"]
    for patient, locations in zip(db, locations):
        print("{} - {}".format(patient, locations))

def print_elders(db, age_limit):
    for patient in db:
        if patient["age"] > age_limit:
            print(patient["name"])

def get_patient(db, id):
    patient = db[id]
    return patient

    # for patient in db:
    #    if patient["id_no"] == id:
    #        return patient

def main():
    # class_work()

    # return


    db = {}
    x = create_database_entry("Ann Ables", 120, 30)
    db[x.id_no] = x
    x = create_database_entry("Bob Boyles", 24, 31)
    db[x.id_no] = x
    x = create_database_entry("Chris Chou", 33, 33)
    db[x.id_no] = x
    x = create_database_entry("David Dinkins", 14, 34)
    db[x.id_no] = x
    print(db)

    patient_id_tested = 24
    test_done = ("HDL", 65)

    patient = get_patient(db, patient_id_tested)
    patient.tests.append(test_done)
    print(db)

    #print_database5(db)
    # y = db[len[db]-1] old way of finding last entry
    # y = db[-1] # python way of finding last entry, can get second to last etc. 
    # y = db[1:3]
    # print(y)
    #bobsname = db[1][0]
    #print(bobsname)
    #print_database(db)
    #print_elders(db, 32)
    #found_patient = get_patient(db, 3)
    #print(found_patient)
    #print_database2(db)
    #print_database3(db) # same as above, uses enumerate command
    #print_database4(db)
    #print_database5(db)

if __name__ == "__main__":
    main()