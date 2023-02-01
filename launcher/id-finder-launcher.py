class Launcher(): 
    id_number = input("What is your student ID number?\n")

    name = input("What is your name?\n")

    place = input("Where did you lose your ID?\n")

    first_user = id_storage(id_number, name, place)

    first_user.find_ID(id_number, name)
    
    def __init___(self, id_number, name, place):
        self.id_number = id_number
        self.name = name
        self.place = place
        
Launcher()