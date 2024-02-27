from collections import Counter


def checkInclusion(s1, s2):
    s1c = Counter(s1)
    window = Counter(s2[: len(s1)])

    if s1c == window:
        return True

    for i in range(len(s1), len(s2)):
        window[s2[i - len(s1)]] -= 1
        if window[s2[i - len(s1)]] == 0:
            del window[s2[i - len(s1)]]
        window[s2[i]] += 1

        if s1c == window:
            return True
    return False


print(checkInclusion("ab", "eidbaooo"))
print(checkInclusion("ab", "eidboaooa"))
