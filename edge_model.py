# edge_model.py
import numpy as np
import config

class TinyMLAnomalyDetector:
    """
    Lightweight anomaly detection model designed for Edge devices.
    Uses Moving Average and Z-Score methodology for real-time inference.
    """
    
    def __init__(self):
        self.window_size = config.WINDOW_SIZE
        self.threshold = config.ANOMALY_THRESHOLD_Z_SCORE
    
    def run_inference(self, live_data_stream):
        """
        Processes a data stream and detects anomalies in real-time.
        (Simulates streaming by iterating over the array)
        """
        print(f"[EDGE_MODEL] Inference started (Model: Z-Score, Threshold: {self.threshold})")
        
        anomalies_detected = []
        data_buffer = [] # Simulates raw hardware buffer
        
        # Stream over data (like a live sensor feed)
        for i, current_value in enumerate(live_data_stream):
            data_buffer.append(current_value)
            
            # Yeterli veri birikmeden analiz yapma (ısıtma süresi)
            if len(data_buffer) < self.window_size:
                continue
            
            # Son WINDOW_SIZE kadar veriyi al (Sliding Window)
            current_window = np.array(data_buffer[-self.window_size:])
            
            # İstatisiksel Hesaplamalar
            mean = np.mean(current_window)
            std_dev = np.std(current_window)
            
            # Standart sapma 0 ise (veri sabit), Z-Score hesaplanamaz
            if std_dev == 0:
                z_score = 0
            else:
                # Mevcut değerin ortalamadan ne kadar saptığını hesapla
                z_score = abs((current_value - mean) / std_dev)
            
            # Anomali Kararı
            if z_score > self.threshold:
                # Anomali tespit edildi! (Verinin indeksini ve değerini kaydet)
                anomalies_detected.append((i, current_value, z_score))
                
        return anomalies_detected
