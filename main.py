class id_storage: 
    numbers_names_dict = {}
   
    def __init__(self, name, id_number, place): 
        self.name = name
        self.id_number = id_number
        self.place = place
        id_storage.numbers_names_dict[id_number] = name

    def find_ID(self, id_number, name=None,): 
        if self.id_number in id_storage.numbers_names_dict: 
            return print("Your ID is currently located at " + str(self.place) + " !")
        else: 
            return print("Sorry, your ID could not be found")
        
id_number = input("What is your student ID number?\n")
name = input("What is your name?\n")
place = input("Where did you lose your ID?\n")
first_user = id_storage(id_number, name, place)

first_user.find_ID(id_number, name)
    