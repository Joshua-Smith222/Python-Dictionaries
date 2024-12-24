ticket_tracker = []

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
