def harmonic(n):  #计算n阶调和数（1 + 1/2 + 1/3 + … + 1/n）
    total = 0.0
    for i in range(1, n+1):
        total += 1.0 / i
    return total
x=harmonic(10)
print(x)