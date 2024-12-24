ticket_tracker = []

def update_ticket_status(ticket_id, new_status):
    for ticket in ticket_tracker:
        if ticket["Ticket ID"] == ticket_id:
            ticket["Status"] = new_status
            print(f"Ticket {ticket_id} status updated to {new_status}.")
            return
    print(f"Ticket ID {ticket_id} not found.")
