import timeit
import pandas as pd


def boyer_moore_search(text, pattern):
    shift_table = {}
    for index, char in enumerate(pattern[:-1]):
        shift_table[char] = len(pattern) - index - 1
    shift_table.setdefault(pattern[-1], len(pattern))

    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        char_shift = shift_table.get(text[i + len(pattern) - 1], len(pattern))
        i += char_shift
    return -1


def __polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def rabin_karp_search(main_string, substring):
    substring_length = len(substring)
    main_string_length = len(main_string)

    base = 256
    modulus = 101

    substring_hash = __polynomial_hash(substring, base, modulus)
    current_slice_hash = __polynomial_hash(main_string[:substring_length], base, modulus)

    h_multiplier = pow(base, substring_length - 1) % modulus

    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i + substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1


def __compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
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


def kmp_search(main_string, pattern):
    lps = __compute_lps(pattern)

    i = j = 0

    while i < len(main_string):
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == len(pattern):
            return i - j

    return -1


def measure_time(search_function, text, pattern):
    setup_code = f"from __main__ import {search_function.__name__}"
    stmt = f"{search_function.__name__}({repr(text)}, {repr(pattern)})"
    times = timeit.repeat(stmt, setup=setup_code, repeat=3, number=10)
    return min(times)


def load_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        return file.read()


def main():
    article1 = load_file('article_01.txt')
    article2 = load_file('article_02.txt')

    search_string = "пошук"
    non_existing = "fake string to search"
    results_article = {
        "Article": ["1", "2"],
        "Boyer-Moore": [measure_time(boyer_moore_search, article1, search_string), measure_time(boyer_moore_search, article2, search_string)],
        "Boyer-Moore no str": [measure_time(boyer_moore_search, article1, non_existing), measure_time(boyer_moore_search, article2, non_existing)],
        "Knuth-Morris-Pratt": [measure_time(kmp_search, article1, search_string), measure_time(kmp_search, article2, search_string)],
        "Knuth-Morris-Pratt  no str": [measure_time(kmp_search, article1, non_existing), measure_time(kmp_search, article2, non_existing)],
        "Rabin-Karp": [measure_time(rabin_karp_search, article1, search_string), measure_time(rabin_karp_search, article2, search_string)],
        "Rabin-Karp no str": [measure_time(rabin_karp_search, article1, non_existing), measure_time(rabin_karp_search, article2, non_existing)]
        #"Boyer-Moore": [measure_time(boyer_moore_search, article2, search_string)],
       # "Boyer-Moore  no str": [measure_time(boyer_moore_search, article2, non_existing)],
        #"Knuth-Morris-Pratt": [measure_time(kmp_search, article2, search_string)],
        #"Knuth-Morris-Pratt  no str": [measure_time(kmp_search, article2, non_existing)],
        #"Rabin-Karp": [measure_time(rabin_karp_search, article2, search_string)],
        #"Rabin-Karp no str": [measure_time(rabin_karp_search, article2, non_existing)]
    }
    df = pd.DataFrame(results_article)
    print(df.to_markdown(index=False))


if __name__ == "__main__":
    main()
