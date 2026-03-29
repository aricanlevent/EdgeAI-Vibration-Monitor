# config.py

# Sensör veri simülasyon parametreleri
SAMPLING_RATE_HZ = 100         # Saniyede kaç veri okunacak
SIMULATION_DURATION_SEC = 5    # Simülasyon kaç saniye sürecek
NORMAL_VIBRATION_AMPLITUDE = 0.5
ANOMALY_VIBRATION_AMPLITUDE = 2.5 # Arıza anında beklenen sapma

# Edge AI Model Parametreleri
# (Hareketli ortalama için pencere boyutu)
WINDOW_SIZE = 20

# Anomali Tespiti Eşik Değeri (Z-Score threshold)
# Genellikle 3.0'dan büyük değerler anomali kabul edilir.
ANOMALY_THRESHOLD_Z_SCORE = 3.5
