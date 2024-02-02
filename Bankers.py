class BankerAlgorithm:
    def __init__(self, num_processes, num_resources):
        self.num_processes = num_processes
        self.num_resources = num_resources
        self.max_resources = []
        self.allocation = []
        self.available = []
        self.need = []

    def initialize_resources(self, max_resources, allocation):
        self.max_resources = max_resources
        self.allocation = allocation
        self.calculate_available()
        self.calculate_need()

    def calculate_available(self):
        total_resources = [sum(col) for col in zip(*self.allocation)]
        self.available = [max_res - alloc_res for max_res, alloc_res in zip(self.max_resources, total_resources)]

    def calculate_need(self):
        self.need = [[max_res - alloc_res for max_res, alloc_res in zip(max_row, alloc_row)]
                     for max_row, alloc_row in zip(self.max_resources, self.allocation)]

    def is_request_safe(self, process_id, request):
        # Try to allocate resources temporarily
        temp_allocation = [row.copy() for row in self.allocation]
        temp_available = self.available.copy()
        temp_need = self.need[process_id]

        for i in range(self.num_resources):
            if request[i] > temp_need[i] or request[i] > temp_available[i]:
                return False
            temp_allocation[process_id][i] += request[i]
            temp_available[i] -= request[i]
            temp_need[i] -= request[i]

        # Check if the temporary state is safe
        if self.is_safe_state(temp_allocation, temp_available, temp_need):
            return True
        else:
            return False

    def request_resources(self, process_id, request):
        if self.is_request_safe(process_id, request):
            # If the request is safe, allocate the resources
            for i in range(self.num_resources):
                self.allocation[process_id][i] += request[i]
                self.available[i] -= request[i]
                self.need[process_id][i] -= request[i]
            return True
        else:
            return False

    def release_resources(self, process_id, release):
        for i in range(self.num_resources):
            self.allocation[process_id][i] -= release[i]
            self.available[i] += release[i]
            self.need[process_id][i] += release[i]

    def is_safe_state(self, temp_allocation, temp_available, temp_need):
        work = temp_available.copy()
        finish = [False] * self.num_processes

        while True:
            found = False
            for i in range(self.num_processes):
                if not finish[i]:
                    if all(temp_need[i][j] <= work[j] for j in range(self.num_resources)):
                        work = [work[j] + temp_allocation[i][j] for j in range(self.num_resources)]
                        finish[i] = True
                        found = True

            if not found:
                break

        return all(finish)

# Example usage:
num_processes = 5
num_resources = 3

max_resources = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3],
]

allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2],
]

banker = BankerAlgorithm(num_processes, num_resources)
banker.initialize_resources(max_resources, allocation)

# Example request
process_id = 1
request = [1, 0, 2]

if banker.request_resources(process_id, request):
    print(f"Request from Process {process_id} for resources {request} granted.")
else:
    print(f"Request from Process {process_id} for resources {request} denied.")

# Example resource release
release = [0, 1, 0]
process_id_to_release = 2
banker.release_resources(process_id_to_release, release)

print(f"Resources released by Process {process_id_to_release}: {release}")
