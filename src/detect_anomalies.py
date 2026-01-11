import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

data = pd.read_csv("data/logs.csv")

features = data[["requests", "failed_logins"]]

model = IsolationForest(contamination=0.15)
data["anomaly"] = model.fit_predict(features)

alerts = data[data["anomaly"] == -1]

if not alerts.empty:
    print("SECURITY ALERT: Potential attack detected")
    print(alerts)
    alerts.to_csv("security_alerts.csv", index=False)

normal = data[data["anomaly"] == 1]
anomaly = data[data["anomaly"] == -1]

plt.figure()
plt.scatter(normal.index, normal["requests"], label="Normal")
plt.scatter(anomaly.index, anomaly["requests"], label="Anomaly")
plt.xlabel("Log Event Index")
plt.ylabel("Request Count")
plt.title("AI-Based Cloud Security Anomaly Detection")
plt.legend()
plt.savefig("anomaly_detection.png")
