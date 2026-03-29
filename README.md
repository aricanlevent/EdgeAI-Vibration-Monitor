# Edge AI Anomaly Detection for Predictive Maintenance

This project implements a lightweight **TinyML** engine for real-time anomaly detection in industrial motors or defense systems (e.g., UAV engine vibration monitoring, gimbal stability analysis).

### The Problem it Solves
Mechanical systems often fail due to vibrations that precede a catastrophic breakdown. In mission-critical defense applications, predicting these failures is crucial. Traditional cloud-based AI cannot handle high-frequency sensor data due to latency and bandwidth constraints.

This project simulates an **Edge AI solution** that processes raw time-series vibration data directly at the source (the sensor node) to identify impending failures instantly.

### Technical Architecture (Multi-File Python)
Designed with professional software engineering practices for modularity and scalability:

1.  **Configuration (`config.py`):** Centralizes sampling rates, detection thresholds, and model parameters.
2.  **Data Generator (`data_generator.py`):** Simulates a "Mock Sensor" by generating synthetic raw vibration data. It creates two scenarios: Normal Operating data and Anomaly data (containing periodic spikes).
3.  **Edge AI Model (`edge_model.py`):** The core intelligence. It implements a **Moving Average Z-Score** methodology with a **Sliding Window** buffer. This approach is highly optimized for Edge devices with limited RAM and CPU resources.
4.  **Application Main (`main.py`):** Orchestrates the data flow, executes inference, and simulates the system's "ALERT" response when anomalies are detected.

### Edge AI / TinyML Characteristics
- **Resource Efficient:** The model utilizes basic statistics (mean, standard deviation) suitable for execution on microcontrollers or resource-constrained Edge gateways.
- **Real-Time Inference:** Data is processed in a streaming fashion (simulated), minimizing latency.
- **Local Autonomy:** Decisions are made without relying on external cloud connectivity.

### Prerequisites to Run (Simulation)
- Python 3.x
- NumPy library (`pip install numpy`)
- `git clone https://github.com/yourusername/EdgeAI-Vibration-Monitor.git`
- `python main.py`
