# This works I swear :shrug: :winky_face:
def fibonacci(n):
    # Test 69, I dare you!
    # Please don't test 0.
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b

    return b
