import math


def f(z):
    log_x = math.log10(z)
    return ((z ** (2 * log_x ** 2)) - (10 * z ** 3)) ** 2

x, x_0 = 0, 0
step = 0.01
end_x = 0.4
min_f = f(step)

while x <= end_x:
    x += step
    current_f = f(x)
    if current_f < min_f:
        min_f = current_f
        x_0 = x

print(round(x_0, 2))
