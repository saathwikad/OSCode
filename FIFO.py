class FIFO:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pages = []

    def page_fault(self, page):
        if page not in self.pages:
            if len(self.pages) == self.capacity:
                self.pages.pop(0)
            self.pages.append(page)
            return True
        return False

# Example usage
fifo = FIFO(3)
pages_to_access = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]

for page in pages_to_access:
    if fifo.page_fault(page):
        print(f"Page {page} caused a page fault. Pages in memory: {fifo.pages}")
    else:
        print(f"Page {page} is already in memory. Pages in memory: {fifo.pages}")
