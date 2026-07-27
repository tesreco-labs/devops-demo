# 📊 Monitoring with Prometheus & Grafana

> **Module 3 - TESRECO DevOps Labs**
>
> **Estimated Time:** 45 Minutes
>
> **Difficulty:** ⭐⭐ Beginner

---

# Objective

In this lab, you will

- Start the monitoring stack
- Verify Prometheus is scraping the application
- Connect Grafana to Prometheus
- Generate application traffic
- Visualize metrics in Grafana

---

# Architecture

```text
                   Browser
                      │
                      ▼
              Flask Application
              localhost:5000
                      │
            exposes /metrics
                      │
                      ▼
              Prometheus
             localhost:9090
                      │
            executes PromQL
                      │
                      ▼
                Grafana
             localhost:3000
```

---

# Step 1 - Start the Application

From the repository root

```bash
docker compose up -d
```

Verify

```bash
docker compose ps
```

Expected

```
NAME

app
prometheus
grafana
```

---

# Step 2 - Verify Application

Open

```
http://localhost:5000
```

Application should respond successfully.

---

# Step 3 - Verify Metrics Endpoint

Open

```
http://localhost:5000/metrics
```

You should see something similar to

```
# HELP python_gc_objects_collected_total

# TYPE python_gc_objects_collected_total counter

python_gc_objects_collected_total 520

process_cpu_seconds_total 1.56

process_resident_memory_bytes 35504128
```

If you can see text like above,

your application is exposing Prometheus metrics correctly.

---

# Step 4 - Open Prometheus

Open

```
http://localhost:9090
```

You should see the Prometheus dashboard.

---

# Step 5 - Verify Target

Navigate to

```
Status

↓

Targets
```

Expected

```
app

UP
```

If the target is **UP**,

Prometheus is successfully scraping the application.

---

# Step 6 - Test a Metric

Click

```
Graph
```

Run

```
up
```

Click

```
Execute
```

Expected

```
1
```

Meaning

Application is reachable.

---

Try another query

```
process_cpu_seconds_total
```

Click Execute.

---

# Step 7 - Open Grafana

Open

```
http://localhost:3000
```

Default Login

```
Username

admin

Password

admin
```

Change password if prompted.

---

# Step 8 - Add Prometheus Data Source

Navigate

```
Connections

↓

Data Sources

↓

Add data source

↓

Prometheus
```

---

Connection URL

Since Grafana and Prometheus run in Docker Compose,

use

```
http://prometheus:9090
```

NOT

```
localhost:9090
```

because containers communicate using **service names**.

---

Click

```
Save & Test
```

Expected

```
Data source is working
```

---

# Step 9 - Create Dashboard

Click

```
Dashboards

↓

New

↓

New Dashboard

↓

Add Visualization
```

Choose

```
Prometheus
```

---

# Step 10 - First Query

Use

```
up
```

Run Query.

Expected

```
1
```

Congratulations 🎉

Grafana is now reading data from Prometheus.

---

# Step 11 - Generate Application Traffic

Currently there isn't much activity.

Let's create some.

### Linux / macOS

```bash
while true
do
    curl http://localhost:5000 > /dev/null
    sleep 1
done
```

---

### Windows PowerShell

```powershell
while ($true) {
    Invoke-WebRequest http://localhost:5000 | Out-Null
    Start-Sleep -Seconds 1
}
```

---

### Faster Traffic

```bash
for i in {1..500}
do
    curl http://localhost:5000 > /dev/null
done
```

---

### Python Load Generator

Create

```
load.py
```

```python
import requests
import random
import time

while True:
    requests.get("http://localhost:5000")
    time.sleep(random.uniform(0.2,1.5))
```

Run

```bash
python load.py
```

---

# Step 12 - Watch Metrics Increase

Return to Prometheus.

Try

```
process_cpu_seconds_total
```

Execute several times.

Notice

```
Value increases
```

---

Also try

```
process_resident_memory_bytes
```

---

# Step 13 - View Same Metrics in Grafana

Open your dashboard.

Replace

```
up
```

with

```
process_cpu_seconds_total
```

Run Query.

Switch visualization

```
Time Series
```

You should now see a graph.

---

# Step 14 - Useful PromQL Queries

Application Status

```
up
```

---

CPU Usage

```
process_cpu_seconds_total
```

---

Memory Usage

```
process_resident_memory_bytes
```

---

Virtual Memory

```
process_virtual_memory_bytes
```

---

Python GC Collections

```
python_gc_objects_collected_total
```

---

Python GC Uncollectable Objects

```
python_gc_objects_uncollectable_total
```

---

Thread Count

```
process_threads
```

---

File Descriptors

```
process_open_fds
```

---

Maximum File Descriptors

```
process_max_fds
```

---

# Bonus Exercise

If your Flask app exposes custom metrics like

```
http_requests_total
```

Run

```
http_requests_total
```

Refresh the application several times.

Watch the counter increase.

---

# Common Problems

## Prometheus Target Down

Check

```
Status

↓

Targets
```

If DOWN,

verify

```
http://localhost:5000/metrics
```

---

## Grafana Cannot Connect

Wrong

```
localhost:9090
```

Correct

```
http://prometheus:9090
```

---

## No Data

Generate traffic

```bash
curl http://localhost:5000
```

several times.

---

## Dashboard Empty

Verify

```
up
```

returns

```
1
```

inside Prometheus first.

---

# Lab Completed

You have successfully

✅ Started Docker Compose

✅ Verified Prometheus scraping

✅ Connected Grafana

✅ Generated application traffic

✅ Created your first dashboard

---

# Challenge

Can you create a dashboard containing

- Application Status
- CPU Usage
- Memory Usage
- Thread Count

using four different panels?
