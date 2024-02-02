from collections import OrderedDict

class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pages = OrderedDict()

    def page_fault(self, page):
        if page in self.pages:
            # Move the accessed page to the end to indicate it's the most recently used
            self.pages.move_to_end(page)
            return False
        else:
            if len(self.pages) == self.capacity:
                # Remove the least recently used page (first item in OrderedDict)
                self.pages.popitem(last=False)
            self.pages[page] = None
            return True

# Example usage
lru = LRU(3)
pages_to_access = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]

for page in pages_to_access:
    if lru.page_fault(page):
        print(f"Page {page} caused a page fault. Pages in memory: {list(lru.pages.keys())}")
    else:
        print(f"Page {page} is already in memory. Pages in memory: {list(lru.pages.keys())}")
