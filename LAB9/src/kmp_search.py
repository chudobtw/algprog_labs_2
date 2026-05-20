def compute_lps_array(needle: str) -> list[int]:
    length = 0
    lps = [0] * len(needle)
    i = 1

    while i < len(needle):
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(haystack: str, needle: str) -> list[int]:
    if not needle:
        return []

    lps = compute_lps_array(needle)
    i = 0
    j = 0
    result = []

    while i < len(haystack):
        if needle[j] == haystack[i]:
            i += 1
            j += 1

        if j == len(needle):
            result.append(i - j)
            j = lps[j - 1]
        elif i < len(haystack) and needle[j] != haystack[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return result

if __name__ == "__main__":
    haystack_text = "We write code, we test code, we deploy code"
    needle_text = "code"
    
    indexes = kmp_search(haystack_text, needle_text)
    
    print(f"Текст: {haystack_text}")
    print(f"Шукаємо: {needle_text}")
    print(f"Знайдено на індексах: {indexes}")