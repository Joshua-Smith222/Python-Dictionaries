ticket_tracker = []

def open_ticket(ticket_id, customer_name, issue_description):
    ticket = {
        "Ticket ID": ticket_id,
        "Customer Name": customer_name,
        "Issue Description": issue_description,
        "Status": "Open"
    }
    ticket_tracker.append(ticket)
    print(f"Ticket {ticket_id} opened for {customer_name}.")

def update_ticket_status(ticket_id, new_status):
    for ticket in ticket_tracker:
        if ticket["Ticket ID"] == ticket_id:
            ticket["Status"] = new_status
            print(f"Ticket {ticket_id} status updated to {new_status}.")
            return
    print(f"Ticket ID {ticket_id} not found.")

def display_tickets(status=None):
    if status:
        filtered_tickets = [ticket for ticket in ticket_tracker if ticket["Status"] == status]
        if filtered_tickets:
            for ticket in filtered_tickets:
                print(ticket)
        else:
            print(f"No tickets with status '{status}' found.")
    else:
        for ticket in ticket_tracker:
            print(ticket)

 # Initialize with some sample tickets
open_ticket(1, "Jake", "Issue with login")
open_ticket(2, "Claudia", "lost photos")
open_ticket(3, "Ashley", "Page not loading")

# Example usage of the functions
display_tickets()  # Display all tickets
update_ticket_status(2, "Closed")  # Update status of ticket ID 2
display_tickets("Open")  # Display only open tickets
open_ticket(4, "David", "Unable to reset password")  # Open a new ticket
display_tickets()  # Display all tickets after the new ticket is added
