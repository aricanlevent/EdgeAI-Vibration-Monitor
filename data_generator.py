# data_generator.py
import numpy as np
import config

class VibrationDataGenerator:
    """Simulates raw vibration sensor data from an industrial motor."""
    
    def __init__(self):
        self.num_samples = config.SAMPLING_RATE_HZ * config.SIMULATION_DURATION_SEC
        self.time = np.linspace(0, config.SIMULATION_DURATION_SEC, self.num_samples)
    
    def generate_normal_data(self):
        """Generates standard operating vibration data (Sine wave + Noise)."""
        print("[DATA_GEN] Generating Normal Operating Data...")
        # Ana titreşim frekansı (örneğin 10Hz)
        base_signal = config.NORMAL_VIBRATION_AMPLITUDE * np.sin(2 * np.pi * 10 * self.time)
        # Gerçek dünya gürültüsü ekle
        noise = np.random.normal(0, 0.1, self.num_samples)
        return base_signal + noise

    def generate_anomaly_data(self):
        """Generates operating data with periodic extreme anomalies."""
        print("[DATA_GEN] Generating Data with Abnormal Spikes...")
        data = self.generate_normal_data()
        
        # Simülasyonun ortasında rastgele noktalara 5 adet şok/spike ekle
        anomaly_indices = np.random.choice(range(len(data)), 5, replace=False)
        for idx in anomaly_indices:
            # Rastgele yönde (pozitif veya negatif) büyük sapma ekle
            direction = 1 if np.random.random() > 0.5 else -1
            data[idx] += direction * config.ANOMALY_VIBRATION_AMPLITUDE
            
        return data
