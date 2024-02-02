class MRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pages = []

    def page_fault(self, page):
        if page in self.pages:
            # Move the accessed page to the front to indicate it's the most recently used
            self.pages.remove(page)
            self.pages.insert(0, page)
            return False
        else:
            if len(self.pages) == self.capacity:
                # Remove the most recently used page (first item in the list)
                self.pages.pop(0)
            self.pages.insert(0, page)
            return True

# Example usage
mru = MRU(3)
pages_to_access = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]

for page in pages_to_access:
    if mru.page_fault(page):
        print(f"Page {page} caused a page fault. Pages in memory: {mru.pages}")
    else:
        print(f"Page {page} is already in memory. Pages in memory: {mru.pages}")
