def scan_disk_scheduling(requests, head_position):
    sorted_requests = sorted(requests)
    total_head_movement = 0

    lower_requests = [request for request in sorted_requests if request < head_position]
    upper_requests = [request for request in sorted_requests if request >= head_position]

    upper_requests.sort(reverse=True)

    movement_sequence = lower_requests + upper_requests

    for request in movement_sequence:
        total_head_movement += abs(head_position - request)
        head_position = request

    return total_head_movement

# Example usage
total_movement_scan = scan_disk_scheduling(requests_sequence, initial_head_position)
print("Total head movement using SCAN:", total_movement_scan)
