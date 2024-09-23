def trap(n):
    password_ = ""
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:  # i + j - пара
                password_ += f"{i}{j}"
    return password_
print(trap(10))

#12 13 23 ...
