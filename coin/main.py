from coin import Coin  

n = 6
S = 25
v = [2, 3, 5, 7, 11, 13]

calculator = Coin(n, S, v)
result = calculator.calculate_min_coins()

print("Kết quả:", result)
print("Thời gian thực hiện:", calculator.get_elapsed_time(), "giây")
