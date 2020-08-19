#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    ticket_cache = {}
    for ticket in tickets:
        ticket_cache[ticket.source] = ticket.destination

    route = []
    cur_dest = ticket_cache["NONE"]
    while cur_dest != "NONE":
        route.append(cur_dest)
        cur_dest = ticket_cache[cur_dest]

    route.append(cur_dest)
    return route
