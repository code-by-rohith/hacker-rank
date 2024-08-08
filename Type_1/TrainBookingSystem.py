class User:
    def __init__(self, user_id, name, age):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.bookings = []

    def add_booking(self, booking):
        self.bookings.append(booking)


class Train:
    def __init__(self, train_id, name, source, destination, seats):
        self.train_id = train_id
        self.name = name
        self.source = source
        self.destination = destination
        self.seats = seats
        self.booked_seats = 0

    def book_seat(self):
        if self.booked_seats < self.seats:
            self.booked_seats += 1
            return True
        else:
            return False


class Booking:
    def __init__(self, booking_id, user_id, train_id):
        self.booking_id = booking_id
        self.user_id = user_id
        self.train_id = train_id


class RailwayReservationSystem:
    def __init__(self):
        self.users = {}
        self.trains = {}
        self.bookings = {}
        self.user_counter = 1
        self.train_counter = 1
        self.booking_counter = 1

    def add_user(self, name, age):
        user_id = self.user_counter
        self.users[user_id] = User(user_id, name, age)
        self.user_counter += 1
        return user_id

    def add_train(self, name, source, destination, seats):
        train_id = self.train_counter
        self.trains[train_id] = Train(train_id, name, source, destination, seats)
        self.train_counter += 1
        return train_id

    def book_ticket(self, user_id, train_id):
        if user_id in self.users and train_id in self.trains:
            train = self.trains[train_id]
            if train.book_seat():
                booking_id = self.booking_counter
                booking = Booking(booking_id, user_id, train_id)
                self.bookings[booking_id] = booking
                self.users[user_id].add_booking(booking)
                self.booking_counter += 1
                return booking_id
            else:
                return "No available seats"
        else:
            return "Invalid user or train ID"

    def view_bookings(self, user_id):
        if user_id in self.users:
            user = self.users[user_id]
            bookings_info = []
            for booking in user.bookings:
                train = self.trains[booking.train_id]
                bookings_info.append({
                    "booking_id": booking.booking_id,
                    "train_name": train.name,
                    "source": train.source,
                    "destination": train.destination
                })
            return bookings_info
        else:
            return "Invalid user ID"

    def view_trains(self):
        trains_info = []
        for train_id, train in self.trains.items():
            trains_info.append({
                "train_id": train_id,
                "name": train.name,
                "source": train.source,
                "destination": train.destination,
                "available_seats": train.seats - train.booked_seats
            })
        return trains_info

def main_menu():
    system = RailwayReservationSystem()
    while True:
        print("\nRailway Ticket Reservation System")
        print("1. Add User")
        print("2. Add Train")
        print("3. Book Ticket")
        print("4. View Bookings")
        print("5. View Trains")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            user_id = system.add_user(name, age)
            print(f"User added with ID: {user_id}")

        elif choice == "2":
            name = input("Enter train name: ")
            source = input("Enter source: ")
            destination = input("Enter destination: ")
            seats = int(input("Enter number of seats: "))
            train_id = system.add_train(name, source, destination, seats)
            print(f"Train added with ID: {train_id}")


        elif choice == "3":
            user_id = int(input("Enter user ID: "))
            train_id = int(input("Enter train ID: "))
            result = system.book_ticket(user_id, train_id)
            if isinstance(result, int):
                print(f"Ticket booked successfully with Booking ID: {result}")
            else:
                print(result)

        elif choice == "4":
            user_id = int(input("Enter user ID: "))
            bookings = system.view_bookings(user_id)
            if isinstance(bookings, str):
                print(bookings)
            else:
                for booking in bookings:
                    print(booking)

        elif choice == "5":
            trains = system.view_trains()
            for train in trains:
                print(train)

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
