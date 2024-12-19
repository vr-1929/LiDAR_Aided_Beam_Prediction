import matplotlib.pyplot as plt
import numpy as np

# Example Data (Replace with actual data if available)
operation_window = np.arange(2, 19, 2)  # Operation windows: 2 to 18
top1_beam_input_accuracy = np.linspace(1.0, 0.6, len(operation_window))
top5_beam_input_accuracy = np.linspace(1.0, 0.85, len(operation_window))
top1_lidar_input_accuracy = np.linspace(0.9, 0.7, len(operation_window))
top5_lidar_input_accuracy = np.linspace(0.9, 0.75, len(operation_window))

beam_measurements_baseline = np.linspace(64, 50, len(operation_window))
beam_measurements_lidar = np.linspace(10, 5, len(operation_window))

# Plot 1: Average Accuracy
plt.figure(figsize=(10, 12))

plt.subplot(2, 1, 1)
plt.plot(operation_window, top1_beam_input_accuracy, 'r-o', label='Top-1 Beam Input')
plt.plot(operation_window, top5_beam_input_accuracy, 'r-s', label='Top-5 Beam Input')
plt.plot(operation_window, top1_lidar_input_accuracy, 'b-o', label='Top-1 LiDAR Input')
plt.plot(operation_window, top5_lidar_input_accuracy, 'b-s', label='Top-5 LiDAR Input')
plt.title('Average Accuracy vs Operation Window')
plt.xlabel('Operation Window Before the Next Exhaustive Beam Search')
plt.ylabel('Average Accuracy')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.ylim(0.4, 1.0)

# Plot 2: Beam Measurements (Overhead)
plt.subplot(2, 1, 2)
plt.plot(operation_window, beam_measurements_baseline, 'r-o', label='Baseline (Top-5)')
plt.plot(operation_window, beam_measurements_lidar, 'b-o', label='LiDAR-aided (Top-5)')
plt.title('No. of Beam Measurements (Overhead) vs Operation Window')
plt.xlabel('Operation Window Before the Next Exhaustive Beam Search')
plt.ylabel('No. of Beam Measurements (Overhead)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

plt.tight_layout()
plt.show()
