def optimal_page_algorithm(pages, frame):
    s = set()
    fault = 0
    hit = 0

    for i, page in enumerate(pages):
        if page not in s:
            print("Fault")
            fault += 1
            if len(s) < frame:
                s.add(page)
            else:
                future_pages = pages[i:].copy()
                maxindex = []
                for pagein in s:
                    try:
                        maxindex.append(future_pages.index(pagein))
                    except:
                        s.remove(pagein)
                        break
                    print(maxindex)
                else:
                    s.remove(future_pages[max(maxindex)])
                s.add(page)
        else:
            print("HIT")
            hit += 1
        print(s)
    return hit, fault


# Driver Code
page_references = [7, 0, 1, 1, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_count = 4
print("hit : ",optimal_page_algorithm(page_references, frame_count)[0])
