def c_scan_disk_scheduling(requests, head_position, max_cylinder):
    sorted_requests = sorted(requests)
    total_head_movement = 0

    upper_requests = [request for request in sorted_requests if request >= head_position]
    lower_requests = [request for request in sorted_requests if request < head_position]

    upper_requests.sort()

    movement_sequence = upper_requests + lower_requests + [max_cylinder]

    for request in movement_sequence:
        total_head_movement += abs(head_position - request)
        head_position = request

    return total_head_movement

# Example usage
max_cylinder = 200
total_movement_cscan = c_scan_disk_scheduling(requests_sequence, initial_head_position, max_cylinder)
print("Total head movement using C-SCAN:", total_movement_cscan)
