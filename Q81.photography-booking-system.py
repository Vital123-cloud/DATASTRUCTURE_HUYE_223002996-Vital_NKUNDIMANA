from collections import deque

# Photography Booking System Class
class PhotographyBookingSystem:
    def __init__(self):
        self.available_photographers = []  
        self.scheduled_photoshoots = deque()  
        self.booking_history = []  
    
    def add_photographer(self, photographer_name):
        self.available_photographers.append(photographer_name)
        print(f"Photographer {photographer_name} has been added.")
    
    def remove_photographer(self, photographer_name):
        if photographer_name in self.available_photographers:
            self.available_photographers.remove(photographer_name)
            print(f"Photographer {photographer_name} has been removed.")
        else:
            print(f"Photographer {photographer_name} is not available.")
    
    
    def schedule_photoshoot(self, client_name):
        if self.available_photographers:
            photographer = self.available_photographers.pop(0)  
            self.scheduled_photoshoots.append((client_name, photographer))
            self.booking_history.append((client_name, photographer))  
            print(f"Photo shoot for {client_name} has been scheduled with {photographer}.")
        else:
            print("No photographers available to schedule the photo shoot.")
    

    def undo_last_booking(self):
        if self.booking_history:
            last_booking = self.booking_history.pop()  
            client_name, photographer = last_booking
            self.scheduled_photoshoots.remove(last_booking)
        
            self.available_photographers.insert(0, photographer)
            print(f"Last booking for {client_name} with {photographer} has been undone.")
        else:
            print("No bookings to undo.")
    
    
    def show_available_photographers(self):
        if self.available_photographers:
            print("Available photographers:", self.available_photographers)
        else:
            print("No photographers available.")
    
    
    def show_scheduled_photoshoots(self):
        if self.scheduled_photoshoots:
            print("Scheduled photo shoots:")
            for shoot in self.scheduled_photoshoots:
                print(f"Client: {shoot[0]}, Photographer: {shoot[1]}")
        else:
            print("No photo shoots scheduled.")


photography_system = PhotographyBookingSystem()

photography_system.add_photographer("Alice")
photography_system.add_photographer("Bob")


photography_system.show_available_photographers()


photography_system.schedule_photoshoot("Client1")
photography_system.schedule_photoshoot("Client2")

photography_system.show_scheduled_photoshoots()

photography_system.undo_last_booking()

photography_system.show_available_photographers()

photography_system.show_scheduled_photoshoots()
