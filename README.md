# AI-Powered Cloud Security Anomaly Detection

## Overview
This project demonstrates an AI-driven cloud security monitoring system that detects anomalous access patterns in cloud-style security logs using unsupervised machine learning. The system is designed to operate in headless cloud environments and produces security alerts and visual artifacts suitable for SOC analysis.

## Problem Statement
Modern cloud environments generate massive volumes of security logs. Traditional rule-based monitoring struggles to detect unknown or zero-day threats. This project addresses the challenge by using machine learning to automatically identify abnormal behavior without predefined rules.

## Architecture
Logs (Azure-style CSV)
        ↓
Feature Extraction (Requests, Failed Logins)
        ↓
Isolation Forest (Unsupervised ML)
        ↓
Anomaly Detection
        ↓
Security Alerts + Visual Evidence

## Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn (Isolation Forest)
- Matplotlib
- Linux (Headless Execution)

## Security Signals Analyzed
- Request volume anomalies
- Failed authentication attempts
- Correlated abnormal behavior

## How It Works
1. Cloud-style access logs are ingested
2. Relevant security features are extracted
3. Isolation Forest learns normal behavior
4. Anomalies are flagged as potential security incidents
5. Alerts and visual artifacts are generated

## Output Artifacts
- anomaly_detection.png (visual evidence)
- security_alerts.csv (incident record)

## Why Isolation Forest?
Isolation Forest is well-suited for security anomaly detection because it does not require labeled data and can identify rare abnormal events in large datasets.

## Enterprise Mapping
| Project Component | Real-World Equivalent |
|------------------|----------------------|
| logs.csv | Azure Monitor / Log Analytics |
| ML Model | Microsoft Sentinel Analytics Rule |
| Alerts CSV | SOC Incident |
| Visualization | Security Dashboard |

## Future Enhancements
- Azure Log Analytics integration
- Microsoft Sentinel correlation
- Real-time streaming support
- Containerized deployment
- Terraform-based infrastructure

## Author
Faseeh Fawaz  
Bachelor of Computer Science – University of Wollongong in Dubai  
Actively seeking Cloud Security / DevSecOps internship opportunities
