#pragma once

#include <cassert>
#include <vector>

// VARIANT: What if you had to return the minimum cost to buy a roundtrip flight?
// Note you cannot fly somewhere and back on the same day.
int FindCheapestTickets(std::vector<int>& departures,
                        std::vector<int>& returns) {
    int min_departure_cost = departures[0];
    int min_cost = INT_MAX;
    for (int i = 1; i < departures.size(); i++) {
        min_cost = std::min(min_cost, returns[i] + min_departure_cost);

        min_departure_cost = std::min(min_departure_cost, departures[i]);
    }

    return min_cost;
}

void FindCheapestTickets() {
    std::vector<int> departures = {8, 3, 6, 10};
    std::vector<int> returns = {10, 9, 5, 8};
    assert(8 == FindCheapestTickets(departures, returns));

    departures = {10, 3, 10, 9, 3};
    returns = {4, 20, 6, 7, 10};
    assert(9 == FindCheapestTickets(departures, returns));

    departures = {1, 3, 10, 9, 3};
    returns = {1, 20, 6, 7, 10};
    assert(7 == FindCheapestTickets(departures, returns));

    departures = {1, 3, 10, 9, 3};
    returns = {1, 1, 6, 7, 10};
    assert(2 == FindCheapestTickets(departures, returns));

    departures = {1, 3, 10, 9, 3};
    returns = {10, 9, 8, 7, 6};
    assert(7 == FindCheapestTickets(departures, returns));

    departures = {12, 33, 44, 9, 23};
    returns = {100, 90, 80, 70, 15};
    assert(24 == FindCheapestTickets(departures, returns));

    departures = {4, 3, 5, 11, 2};
    returns = {1, 6, 10, 2, 9};
    assert(5 == FindCheapestTickets(departures, returns));
}