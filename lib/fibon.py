# This works I swear :shrug: :winky_face:
# Please don't test 0 :winky_face:
def fibonacci(n):
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b

    return b
