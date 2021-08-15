def my_sort(slist):
    if len(slist) <= 1:
        return slist
    pilot = slist[0]
    less_then = []
    more_then = []
    equal = []
    for elem in slist:
        if elem > pilot:
            more_then.append(elem)
        elif elem < pilot:
            less_then.append(elem)
        else:
            equal.append(elem)

    return my_sort(less_then) + equal + my_sort(more_then)