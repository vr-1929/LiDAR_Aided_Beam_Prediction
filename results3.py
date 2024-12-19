import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Example SNR values (in dB)
snr_values = np.arange(0, 21, 2)  # SNR from 0 dB to 20 dB in steps of 2

# Example accuracy values for different SNR levels
accuracy_model1 = np.array([0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.93, 0.95, 0.97, 0.98, 0.99])
accuracy_model2 = np.array([0.4, 0.55, 0.65, 0.75, 0.8, 0.85, 0.9, 0.92, 0.94, 0.96, 0.98])

# Create smoother curves using spline interpolation
new_snr = np.linspace(snr_values.min(), snr_values.max(), 300)  # More points for smoothness

spline_model1 = make_interp_spline(snr_values, accuracy_model1)(new_snr)
spline_model2 = make_interp_spline(snr_values, accuracy_model2)(new_snr)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(new_snr, spline_model1, 'b-', label='Model 1', linewidth=2)
plt.plot(new_snr, spline_model2, 'r--', label='Model 2', linewidth=2)

# Graph details
plt.title('Accuracy vs SNR (Signal-to-Noise Ratio)', fontsize=14)
plt.xlabel('SNR (dB)', fontsize=12)
plt.ylabel('Accuracy', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylim(0.3, 1.0)  # Y-axis limits
plt.legend(fontsize=12)
plt.tight_layout()

# Show plot
plt.show()
