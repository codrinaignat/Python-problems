def test_square(num):
    root = int(num ** 0.5)
    if num == root * root:
        print(num, " is a perfect square (",
            root, " * ", root, ").", sep="")
    else:
        print(num, "is not a perfect square.")

print(test_square(49))
