class Star_Cinema:
    _hall_list = []  # Protected attribute
    
    def entry_hall(self):
        self._hall_list.append(self)  # Accessing protected attribute within the class


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        super().__init__()  
        self._seats_dict = {}  # Protected attribute for storing seats information
        self._show_list = []   # Protected attribute for storing show information
        self.rows = rows  # Number of rows in the hall
        self.cols = cols  # Number of columns in the hall
        self.hall_no = hall_no  # Hall number
    
    def entry_show(self, id, movie_name, time):

        # Method to add a show with its details to the hall
        show_info_tup = (id, movie_name, time)
        self._show_list.append(show_info_tup)  # Accessing protected attribute within the class

        # Creating seats with given rows and columns of the hall for the particular show
        seats = [[0] * self.cols for _ in range(self.rows)]  
        self._seats_dict[id] = seats  # Accessing protected attribute within the class

    def book_seats(self, id, row, col):
        
        # Method to book seats for a particular show.
        if id not in self._seats_dict:  # Accessing protected attribute within the class
            print("Invalid Show-ID. Please try again")
            return False
        seats = self._seats_dict[id]  # Accessing protected attribute within the class
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            print(f"Invalid seat: ({row}, {col}). Please try again")
            return False
        if seats[row][col] == 1:
            print(f"Seat ({row}, {col}) is already booked. Please try again")
            return  False
        seats[row][col] = 1  # Marking the seat as booked
        print("Seat booked successfully.")
        return True

    def view_show_list(self):

        # Method to view the list of shows available in the hall.
        for show in self._show_list:  # Accessing protected attribute within the class
            print(f'SHOW-ID: {show[0]} SHOW-NAME: {show[1]} SHOW-TIME: {show[2]}')

    def view_available_seats(self, id):
        
        # Method to view the available seats for a particular show.
        seats = self._seats_dict.get(id)  # Accessing protected attribute within the class
        if seats is None:
            print("Invalid Show-ID.")
            return False
        for row in range(self.rows):
            for col in range(self.cols):
                print(seats[row][col], end=', ')  
            print() 
        return True 

# Creating an instance of the Hall class
dhaka_hall = Hall(20, 20, 1)

# Adding shows to the hall
dhaka_hall.entry_show("111", "Spiderman", "10th february 10.00 pm")
dhaka_hall.entry_show("112", "Superman", "10th february 8.00 pm")
dhaka_hall.entry_show("113", "Batman", "10th february 6.00 pm")
dhaka_hall.entry_show("114", "Powerman", "10th february 4.00 pm")

# interface for the counter
while True:
    print("1: View all show today")
    print("2: View available seats")
    print("3: Book tickets")
    print("4: Exit")

    ch = int(input("\nEnter Option:"))

    if ch == 1:
        dhaka_hall.view_show_list()
    elif ch == 2:
        id = input("\nSHOW ID: ")
        while not dhaka_hall.view_available_seats(id):
            id = input(f'Please enter a valid SHOW ID: ')
        
    elif ch == 3:
        tickets = int(input("\nEnter number of tickets: "))
        
        for t in range(1, tickets + 1):
            id = input(f'\nEnter SHOW ID for ticket-{t}: ')
            row = int(input(f'\nEnter row for ticket-{t}: '))
            col = int(input(f'\nEnter col for ticket-{t}: '))
            while not dhaka_hall.book_seats(id, row, col):
                id = input(f'\nEnter SHOW ID for ticket-{t} again: ')
                row = int(input(f'\nEnter row for ticket-{t} again: '))
                col = int(input(f'\nEnter col for ticket-{t} again: '))

        print("View updated seats: ")
        dhaka_hall.view_available_seats(id)  
    else:
        break
