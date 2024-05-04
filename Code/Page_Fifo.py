from queue import Queue


def pageFaults(pages, capacity):
    s = set()
    indexes = Queue()
    page_faults = 0

    for page in pages:
        if len(s) < capacity and page not in s:
            s.add(page)
            page_faults += 1
            indexes.put(page)
        elif page not in s:
            val = indexes.get()
            s.remove(val)
            s.add(page)
            indexes.put(page)
            page_faults += 1

    return page_faults


if __name__ == '__main__':
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    capacity = 4
    print(pageFaults(pages, capacity))
