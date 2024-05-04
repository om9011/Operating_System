def pageFaults(pages, capacity):
    s = set()
    indexes = {}
    page_faults = 0

    for i, page in enumerate(pages):
        if len(s) < capacity and page not in s:
            s.add(page)
            page_faults += 1

        elif page not in s:
            lru_page = min(s, key=indexes.get)
            s.remove(lru_page)
            s.add(page)
            page_faults += 1

        indexes[page] = i

    return page_faults

# Driver code
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 4
print(pageFaults(pages, capacity))
