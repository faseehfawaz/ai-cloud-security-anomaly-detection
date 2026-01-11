import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

data = pd.read_csv("data/logs.csv")

model = IsolationForest(contamination=0.1)
data["anomaly"] = model.fit_predict(data[["requests"]])

alerts = data[data["anomaly"] == -1]

if not alerts.empty:
    print("SECURITY ALERT: Suspicious activity detected")
    print(alerts)
    alerts.to_csv("security_alerts.csv", index=False)

normal = data[data["anomaly"] == 1]
anomaly = data[data["anomaly"] == -1]

plt.figure()
plt.scatter(normal.index, normal["requests"], label="Normal")
plt.scatter(anomaly.index, anomaly["requests"], label="Anomaly")
plt.xlabel("Time Index")
plt.ylabel("Number of Requests")
plt.title("AI-Based Anomaly Detection in Cloud Logs")
plt.legend()

plt.savefig("anomaly_detection.png")
