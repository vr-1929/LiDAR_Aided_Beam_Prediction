import pandas as pd

# Data
data = {
    'Timestamps': ['Present', 'Future1', 'Future2', 'Future3'],
    'Top-1 Accuracy': [0.56776557, 0.55860806, 0.5018315, 0.45604396],
    'Top-5 Accuracy': [0.94322344, 0.94322344, 0.93040293, 0.92307692]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Displaying the table
print(df)


import matplotlib.pyplot as plt
import numpy as np

# Data
timestamps = ['Present', 'Future1', 'Future2', 'Future3']
top1_accuracies = [0.56776557, 0.55860806, 0.5018315, 0.45604396]
top5_accuracies = [0.94322344, 0.94322344, 0.93040293, 0.92307692]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(timestamps, top1_accuracies, marker='o', label='Top-1 Accuracy', color='blue')
plt.plot(timestamps, top5_accuracies, marker='o', label='Top-5 Accuracy', color='green')

# Adding Data Point Annotations
for i, (t, t1, t5) in enumerate(zip(timestamps, top1_accuracies, top5_accuracies)):
    plt.text(t, t1, f"{t1:.2f}", color='blue', ha='center', va='bottom', fontsize=10)
    plt.text(t, t5, f"{t5:.2f}", color='green', ha='center', va='bottom', fontsize=10)

# Graph details
plt.title('Top-1 and Top-5 Accuracies Over Timestamps')
plt.xlabel('Timestamps')
plt.ylabel('Accuracy')
plt.ylim(0.4, 1.0)  # Set y-axis range for better visualization
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()

