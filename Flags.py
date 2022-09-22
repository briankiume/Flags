def get_flags(a):
    peaks = []
    for x in range(1, len(a) - 1):
        if (a[x] > a[x - 1]) & (a[x] > a[x + 1]):
            peaks.append(x)

    flags = peaks
    k = len(peaks)
    for x in range(len(flags)):
        try:
            diff = abs(flags[x] - flags[x + 1])
        except IndexError:
            continue
        if diff < k:
            flags.remove(flags[x + 1])

    return len(flags)


print(get_flags([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))
