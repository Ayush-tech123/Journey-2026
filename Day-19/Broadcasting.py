import numpy as np

data = np.array([
    [53, 65, 96],
    [63, 64, 85],
    [26, 90, 38]
])

print(data)
print(data.shape)

feature_mean = np.mean(data, axis=0)
print("Output of feature mean")
print(feature_mean)

centered = data - feature_mean
print("Output of centered")
print(centered)

feature_std = np.std(data, axis = 0)
print("Output of feature_std")
print(feature_std)

scaled = (data - feature_mean) / feature_std
print("Output of scaled")
print(scaled)