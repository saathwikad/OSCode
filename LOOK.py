def look_disk_scheduling(requests, head_position):
    sorted_requests = sorted(requests)
    total_head_movement = 0

    lower_requests = [request for request in sorted_requests if request < head_position]
    upper_requests = [request for request in sorted_requests if request > head_position]

    movement_sequence = lower_requests + upper_requests

    for request in movement_sequence:
        total_head_movement += abs(head_position - request)
        head_position = request

    return total_head_movement

# Example usage
total_movement_look = look_disk_scheduling(requests_sequence, initial_head_position)
print("Total head movement using LOOK:", total_movement_look)
