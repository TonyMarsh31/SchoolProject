# NumPy的常用操作: 增删、分割、reshape、正态分布随机数
import numpy as np

# 创建一个一维数组
arr1 = np.array([5.90, 5.96, 5.23, 6.24])
# 追加元素
result = np.append(arr1, 5.85)
print(result)
# 追加列表
result = np.append(arr1, [5.52, 5.23])
print(result)
# 删除指定索引位置的元素
result = np.delete(arr1, 2)
print(result)
# 删除多个索引位置的元素
result = np.delete(arr1, [1, 2, 3])

# 创建一个一维数组
prices = np.array([[5.90, 5.96, 5.23, 6.24, 6.12, 6.63],
                   [5.50, 2.96, 5.33, 6.24, 6.12, 4.63]])
# 将价格数据进行reshape操作
result = np.reshape(prices, newshape=(3, 4))
# 输出结果
print(result)
# 将价格数据进行reshape操作
result = np.reshape(prices, newshape=(3, 6))
print(result)

# 生成服从二项分布的随机数
randoms = np.random.binomial(1, 0.5, (3, 2))
print(randoms)
# 生成服从均匀分布的随机浮点数，范围是[0,1)
randoms = np.random.rand(5)
print(randoms)
