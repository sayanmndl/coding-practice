import heapq

'''
orders = [
    {"name": "Alice", "amount": 5, "type": "Fizz", "cost": 10},
    {"name": "Catherine", "amount": 3, "type": "Fizz", "cost": 5},
    {"name": "Bob", "amount": 6, "type": "Buzz"}
]

Output:

[
    ["Catherine", "Bob", 3, 5],
    ["Alice", "Bob", 3, 10]
]
'''


def process_orders(orders):
    # (cost, order_id, supplier_name, remaining_amount)
    fizz_heap = []
    fulfilled = []

    order_id = 0

    for order  in orders:
        name = order['name']
        amount = order['amount']

        if order['type'] == 'Fizz':
            heapq.heappush(fizz_heap, (order['cost'], order_id, name, amount))
            order_id += 1
        else: # Buzz
            remaining = amount
            while remaining > 0 and fizz_heap:
                cost, idx, supplier, available = heapq.heappop(fizz_heap)
                # amount we can match
                matched = min(remaining, available)
                fulfilled.append(
                    (supplier, name, matched, cost)
                )
                remaining -= matched
                available -= matched

                if available > 0:
                    heapq.heappush(fizz_heap, (cost, idx, supplier, available))

    return fulfilled
