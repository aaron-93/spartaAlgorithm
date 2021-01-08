
import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    idx = 0
    q = []

    while stock <k:
        for i in range(idx, len(dates)):
            if stock < dates[i]:
                break
            heapq.heappush(q, -supplies[i])
            idx = i +1

        stock += (heapq.heappop(q)*-1)
        answer += 1

    return answer

print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
