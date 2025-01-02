vowels = {"a", "e", "i", "o", "u"}


def max_vowels(s: str, k: int) -> int:
    size = len(s)
    result = 0
    current_window = s[:k]
    for letter in current_window:
        if letter in vowels:
            result += 1
    i = 1
    current = result
    while i + k <= size:
        if s[i - 1] in vowels:
            current -= 1
        if s[i + k - 1] in vowels:
            current += 1
        result = max(result, current)
        i += 1
    return result


if __name__ == '__main__':
    string_input = "weallloveyou"
    window = 7
    print(max_vowels(string_input, window))
