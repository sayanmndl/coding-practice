import heapq

"""
N = 3
requests = [
  {id: 1, pickup: 0, return: 5},
  {id: 2, pickup: 2, return: 7},
  {id: 3, pickup: 5, return: 9}
]
"""

def assign_cars(N, requests):
    requests.sort(key = lambda x: (x['pickup'], x['return']))
    
    # busy = (return_time, car_id) - minheap
    busy = []

    # IDs of cars that have become available.
    available = []
    next_car_id = 0
    result = []

    for req in requests:
        pickup = req['pickup']

        while busy and busy[0][0] <= pickup: # car returned at or before pickup can be reused
            _, car_id = heapq.heappop(busy)
            heapq.heappush(available, car_id)

        if available: # reuse existing car
            car_id = heapq.heappop(available)
        else:
            # need new car
            if next_car_id >= N:
                raise ValueError('not enough car')
            car_id = next_car_id
            next_car_id+=1

        result.append({
            'requestID': req['id'], 'carID': car_id
        })

        heapq.heappush(busy, (req['return'], car_id))
    return result


N = 3

requests = [
    {"id": 1, "pickup": 0, "return": 5},
    {"id": 2, "pickup": 2, "return": 7},
    {"id": 3, "pickup": 5, "return": 9},
]

print(assign_cars(N, requests))