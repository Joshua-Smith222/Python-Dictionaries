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
