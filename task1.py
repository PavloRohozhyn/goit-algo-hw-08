import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)
    total_cost = 0
    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        combined_length = first + second
        total_cost += combined_length
        heapq.heappush(cables, combined_length)
    return total_cost

# Main
if __name__ == '__main__':
    try:
        # cables
        cables = [4, 3, 2, 6]
        print(f"Cables : {cables}")
        # result
        print(f"Minimum costs for connecting cables: {min_cost_to_connect_cables(cables)}")
    except (ValueError) as e:
        print(f'Something went wrong, {e}')
        sys.exit(0)
