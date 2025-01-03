from collections import deque


def assert_true(txt):
    if not is_palindrome(txt):
        print("Assertion error: " + txt)


def assert_false(txt):
    if is_palindrome(txt):
        print("Assertion error: " + txt)


def is_palindrome(possible_palindrome):
    normalized = possible_palindrome.replace(" ", "").lower()
    if len(normalized) < 2:
        return False

    deq = deque(normalized)
    for i in range(len(normalized) % 2):
        if deq.popleft() != deq.pop():
            return False
    return True


assert_false("asd")
assert_false("a sd")
assert_false("aSd")
assert_false("")
assert_false(" ")

assert_true("assa")
assert_true("as sa")
assert_true("ass a")
assert_true("asSa")
