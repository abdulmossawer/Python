import numpy as np
import statistics as stats

baked_food = [200, 150, 150, 130, 200, 220, 170, 188]

# a = np.array(baked_food)
# print(np.mean(a))
# print(np.median(a))
# print(stats.mode(a))
# print(np.std(a))
# print(np.var(a))


# -1 represent inversely proportional relationship
# 1 represents proportional relationship
# 0 means no relationship

tC = [30, 50, 10, 30, 50,40]
deaths = [100, 120, 70, 100, 120, 112]
print(np.corrcoef(tC, deaths))