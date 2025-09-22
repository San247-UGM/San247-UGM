import numpy as np
import matplotlib.pyplot as plt

# Interval waktu
t = np.linspace(-8, 8, 1000)

# Input sinyal dari output S2
x1 = (np.sin(2*t)) * (t+1)        # y1 dari S2
x2 = (np.sin(2*t)**2) - (t+1)     # y2 dari S2

# Output Sistem S3
y = np.where(t >= 0, x1 + 2, -x2)   # aturan sesuai soal

# Plot output
plt.figure(figsize=(8,5))
plt.plot(t, y, color='purple', label='$y(t)$')
plt.title("Respon Sistem S3 (Output Akhir)")
plt.xlabel("t")
plt.ylabel("Output")
plt.legend()
plt.grid(True)
plt.show()