def sstf_disk_scheduling(requests, head_position):
    sorted_requests = sorted(requests, key=lambda x: abs(x - head_position))
    total_head_movement = 0

    for request in sorted_requests:
        total_head_movement += abs(head_position - request)
        head_position = request

    return total_head_movement

# Example usage
requests_sequence = [98, 183, 37, 122, 14, 124, 65, 67]
initial_head_position = 53

total_movement_sstf = sstf_disk_scheduling(requests_sequence, initial_head_position)
print("Total head movement using SSTF:", total_movement_sstf)
