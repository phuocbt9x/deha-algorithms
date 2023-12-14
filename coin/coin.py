import time

class Coin:
    def __init__(self, N, S, v):
        self.N = N
        self.S = S
        self.v = v
        self.dp = [float('inf')] * (S + 1)
        self.dp[0] = 0
        self.start_time = 0
        self.end_time = 0

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self):
        self.end_time = time.time()

    def get_elapsed_time(self):
        return self.end_time - self.start_time

    def calculate_min_coins(self):
        self.start_timer()
        #Duyệt qua tất cả các giá trị trừ 1 -> tổng S
        for i in range(1, self.S + 1):
            # Duyệt qua tất cả các loại đồng xu
            for j in range(self.N):
                # Nếu giá trị đồng xu nhỏ hơn hoặc bằng i
                if self.v[j] <= i:
                    # Cập nhật giá trị tối ưu
                    self.dp[i] = min(self.dp[i], self.dp[i - self.v[j]] + 1)
 
        self.stop_timer()
        
        # Kiểm tra nếu không tồn tại đồng xu nào có tổng giá trị là S
        if self.dp[self.S] == float('inf'):
            return -1
        else:
            return self.dp[self.S]

