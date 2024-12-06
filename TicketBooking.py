class TicketBooking:
    def __init__(self):
        self.events = {}

    def add_event(self, event_name, total_seats):

        self.events[event_name] = {f"Seat-{i + 1}": "Available" for i in range(total_seats)}

    def book_ticket(self, event, seat_number):

        if event not in self.events:
            return f"Event {event} not found."

        if seat_number not in self.events[event]:
            return f"Seat {seat_number} not found for event {event}."

        if self.events[event][seat_number] == "Booked":
            return f"Seat {seat_number} is already booked."


        self.events[event][seat_number] = "Booked"
        return f"Ticket booked for {event} at {seat_number}."

    def cancel_booking(self, event, seat_number):

        if event not in self.events:
            return f"Event {event} not found."

        if seat_number not in self.events[event]:
            return f"Seat {seat_number} not found for event {event}."

        if self.events[event][seat_number] == "Available":
            return f"Seat {seat_number} is not booked."


        self.events[event][seat_number] = "Available"
        return f"Booking for seat {seat_number} at {event} has been canceled."

    def view_booked_tickets(self):

        booked_tickets = []
        for event, seats in self.events.items():
            for seat, status in seats.items():
                if status == "Booked":
                    booked_tickets.append((event, seat))
        return booked_tickets

    def view_available_seats(self, event):

        if event not in self.events:
            return f"Event {event} not found."

        available_seats = [seat for seat, status in self.events[event].items() if status == "Available"]
        return available_seats

    def get_booking_details(self, seat_number):

        for event, seats in self.events.items():
            if seat_number in seats:
                status = seats[seat_number]
                return {"event": event, "seat_number": seat_number, "status": status}
        return f"Seat {seat_number} not found."

    def change_seat(self, event, old_seat, new_seat):

        if event not in self.events:
            return f"Event {event} not found."

        if old_seat not in self.events[event]:
            return f"Old seat {old_seat} not found for event {event}."

        if new_seat not in self.events[event]:
            return f"New seat {new_seat} not found for event {event}."

        if self.events[event][old_seat] != "Booked":
            return f"Old seat {old_seat} is not booked."

        if self.events[event][new_seat] == "Booked":
            return f"New seat {new_seat} is already booked."


        self.events[event][old_seat] = "Available"
        self.events[event][new_seat] = "Booked"
        return f"Seat changed from {old_seat} to {new_seat} for event {event}."



ticket_system = TicketBooking()

ticket_system.add_event("Concert", 5)

print(ticket_system.book_ticket("Concert", "Seat-1"))
print(ticket_system.book_ticket("Concert", "Seat-2"))

print(ticket_system.view_booked_tickets())

print(ticket_system.view_available_seats("Concert"))

print(ticket_system.get_booking_details("Seat-1"))

print(ticket_system.change_seat("Concert", "Seat-1", "Seat-3"))

print(ticket_system.cancel_booking("Concert", "Seat-2"))

print(ticket_system.view_available_seats("Concert"))
