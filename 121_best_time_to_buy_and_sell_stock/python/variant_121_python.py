def find_cheapest_tickets(departures, returns):
    MIND =  float('inf')
    MINR = float('inf')

    for i in range(len(departures)):
        if MIND > departures[i]:
            MIND = departures[i]
        elif MINR > returns[i]:
            MINR = min(abs(MIND+returns[i]),MINR)
    return MINR





    # min_departure_cost = departures[0]
    # min_cost = float('inf')
    
    # for i in range(1, len(departures)):
    #     min_cost = min(min_cost, min_departure_cost + returns[i])

    #     if departures[i] < min_departure_cost:
    #         min_departure_cost = departures[i]
    
    # return min_cost

if __name__ == "__main__":
    departures = [8, 3, 6, 10]
    returns = [10, 9, 5, 8]
    assert find_cheapest_tickets(departures, returns) == 8

    departures = [10, 3, 10, 9, 3]
    returns = [4, 20, 6, 7, 10]
    assert find_cheapest_tickets(departures, returns) == 9

    departures = [1, 3, 10, 9, 3]
    returns = [1, 20, 6, 7, 10]
    assert find_cheapest_tickets(departures, returns) == 7

    departures = [1, 3, 10, 9, 3]
    returns = [1, 1, 6, 7, 10]
    assert find_cheapest_tickets(departures, returns) == 2

    departures = [1, 3, 10, 9, 3]
    returns = [10, 9, 8, 7, 6]
    assert find_cheapest_tickets(departures, returns) == 7

    departures = [12, 33, 44, 9, 23]
    returns = [100, 90, 80, 70, 15]
    assert find_cheapest_tickets(departures, returns) == 24

    departures = [4, 3, 5, 11, 2]
    returns = [1, 6, 10, 2, 9]
    assert find_cheapest_tickets(departures, returns) == 5

    print('ALL Test Passed!!!')