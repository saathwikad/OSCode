class Optimal:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pages = []

    def page_fault(self, page, future_pages):
        if page not in self.pages:
            if len(self.pages) == self.capacity:
                # Find the page that will not be used for the longest time in the future
                page_to_remove = max(self.pages, key=lambda p: future_pages.index(p) if p in future_pages else float('inf'))
                self.pages.remove(page_to_remove)
            self.pages.append(page)
            return True
        return False

# Example usage
optimal = Optimal(3)
pages_to_access = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]

for i, page in enumerate(pages_to_access):
    future_pages = pages_to_access[i+1:]
    if optimal.page_fault(page, future_pages):
        print(f"Page {page} caused a page fault. Pages in memory: {optimal.pages}")
    else:
        print(f"Page {page} is already in memory. Pages in memory: {optimal.pages}")
