class ID: 
    numbers_names_dict = {}
   
    def __init__(self, name, ID_number, place): 
        self.name = name
        self.ID_number = ID_number
        self.place = place
        ID.numbers_names_dict[ID_number] = name

    def find_ID(self, ID_number, name=None,): 
        if self.ID_number in ID.numbers_names_dict: 
            return print("Your ID is currently located at " + str(self.place) + " !")
        else: 
            return print("Sorry, your ID could not be found!")
    