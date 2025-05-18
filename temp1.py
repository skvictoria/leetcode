# import matplotlib.pyplot as plt
# import numpy as np

# # 데이터 설정
# x_labels = ["Trained on 20%", "Trained on 30%", "Trained on 40%", "Trained on 50%", 
#             "Trained on 60%", "Trained on 70%", "Trained on 80%", "Trained on 90%"]

# short_term = [47.373, 40.826, 43.75, 49.142, 47.647, 47.881, 46.373, 50.147]
# long_term = [22.303, 19.73, 22.794, 21.568, 21.568, 24.632, 24.019, 27.328]

# # X 축 위치 설정
# x = np.arange(len(x_labels))

# # 그래프 그리기
# plt.figure(figsize=(10, 5))
# plt.plot(x, short_term, marker='o', label="Short-horizon action anticipation")
# plt.plot(x, long_term, marker='o', label="Long-horizon action anticipation")

# # 축 설정
# plt.xticks(x, x_labels, rotation=10, fontsize=10)
# plt.yticks(np.arange(0, 61, 10))  # 세로축을 0에서 60까지 설정 (10 단위)
# plt.ylim(0, 60)  # y축 범위 지정
# plt.ylabel("Action Anticipation Accuracy")
# plt.xlabel("Observation rate")
# plt.title("L2 level (Action level) action anticipation", fontweight="bold")
# plt.legend()
# plt.grid(True, linestyle='--', alpha=0.5)

# # 그래프 출력
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

# 데이터 설정
x_labels = ["Trained on 20%", "Trained on 30%", "Trained on 40%", "Trained on 50%", 
            "Trained on 60%", "Trained on 70%", "Trained on 80%", "Trained on 90%"]

short_term = [34.313, 29.534, 27.083, 24.754, 29.534, 32.948, 30.318, 26.146]
long_term = [36.274, 32.72, 30.637, 30.024, 34.751, 39.46, 44.905, 46.025]

# X 축 위치 설정
x = np.arange(len(x_labels))

# 그래프 그리기
plt.figure(figsize=(10, 4))
plt.plot(x, short_term, marker='o', label="Short-horizon action anticipation")
plt.plot(x, long_term, marker='o', label="Long-horizon action anticipation")

# 축 설정
plt.xticks(x, x_labels, rotation=10,fontsize=10)
plt.yticks(np.arange(0, 61, 10))  # 세로축을 0에서 60까지 설정 (10 단위)
plt.ylim(0, 60)  # y축 범위 지정
plt.ylabel("Action Anticipation Accuracy")
plt.xlabel("Observation rate")
plt.title("L3 level (Procedure level) action anticipation", fontweight="bold")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

# 그래프 출력
plt.show()
