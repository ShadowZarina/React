# Weather Data Simulator

import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
num_days = 365
mean_annual_temp = 15  # Celsius
annual_temp_amplitude = 10 # Celsius
daily_temp_std = 2 # Celsius (for random fluctuations)

# Generate time series (in days)
days = np.arange(num_days)

# Simulate seasonal temperature trend (sine wave)
seasonal_temp = mean_annual_temp + annual_temp_amplitude * np.sin(2 * np.pi * days / num_days)

# Add daily random fluctuations
daily_fluctuations = np.random.normal(loc=0, scale=daily_temp_std, size=num_days)

# Combine to get simulated temperature
simulated_temperature = seasonal_temp + daily_fluctuations

# Plot the simulated data
plt.plot(days, simulated_temperature)
plt.xlabel("Day of Year")
plt.ylabel("Temperature (°C)")
plt.title("Simulated Daily Temperature")
plt.grid(True)
plt.show()


