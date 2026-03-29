# main.py
from data_generator.py import VibrationDataGenerator
from edge_model.py import TinyMLAnomalyDetector
import config
import numpy as np

def run_simulation(scenario_name, data):
    print(f"\n--- Scenario: {scenario_name} ---")
    
    detector = TinyMLAnomalyDetector()
    results = detector.run_inference(data)
    
    total_samples = len(data)
    anomalies_count = len(results)
    
    print(f"[RESULTS] Processed {total_samples} samples.")
    print(f"[RESULTS] Detected {anomalies_count} anomalies.")
    
    if anomalies_count > 0:
        print("[ALERT] Motor requires IMMEDIATE inspection! Anomalies found:")
        # İlk 3 anomaliyi detaylandır
        for idx, val, z in results[:3]:
            print(f"  -> Sample {idx}: Value={val:.2f}, Z-Score={z:.2f}")
    else:
        print("[STATUS] Motor is operating within normal parameters.")

if __name__ == "__main__":
    print("\n=========================================")
    print("Edge AI Vibration Monitoring Simulation")
    print("=========================================\n")
    
    # Veri üretim motorunu başlat
    generator = VibrationDataGenerator()
    
    # 1. Senaryo: Normal Çalışma
    normal_vibration_data = generator.generate_normal_data()
    run_simulation("Normal Operation", normal_vibration_data)
    
    # 2. Senaryo: Arıza Durumu (Anomalili)
    anomaly_vibration_data = generator.generate_anomaly_data()
    run_simulation("Predictive Maintenance Alert", anomaly_vibration_data)
    
    print("\n--- Simulation Complete ---")
