# 🚀 Environment Setup Guide

> **Module 0 - TESRECO DevOps Labs**
>
> **Estimated Time:** 20-30 Minutes
>
> **Difficulty:** ⭐ Beginner

---

# Welcome

Welcome to the **TESRECO DevOps Demo Labs**.

This repository is designed to introduce you to modern DevOps practices through a hands-on monitoring application.

Throughout these labs, you will learn:

- Docker
- Docker Compose
- Container Networking
- Prometheus
- Grafana
- Application Monitoring
- Observability Fundamentals

By the end of this course, you'll have deployed a multi-container application and visualized real-time application metrics.

---

# Repository Architecture

```text
                    Browser
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
   localhost:5000  localhost:9090  localhost:3000
      Flask App      Prometheus       Grafana
           │
           ▼
      /metrics endpoint
```

---

# Prerequisites

Before starting, ensure the following software is installed.

| Software | Version |
|----------|----------|
| Git | Latest |
| Docker Desktop | Latest |
| Docker Compose | Included with Docker Desktop |
| VS Code (Recommended) | Latest |
| Web Browser | Chrome / Edge / Firefox |

---

# System Requirements

Minimum

- Windows 10/11
- macOS
- Ubuntu 22.04+

Recommended

- 8 GB RAM
- Dual Core CPU
- 10 GB Free Disk Space

---

# Install Git

Download

https://git-scm.com/downloads

Verify

```bash
git --version
```

Example

```
git version 2.48.1
```

---

# Install Docker Desktop

Download

https://www.docker.com/products/docker-desktop/

During installation

✔ Enable WSL2 (Windows)

✔ Restart system if prompted

---

Verify Installation

```bash
docker version
```

Expected

```
Client:
 Version: xx.xx.xx

Server:
 Engine:
 Version: xx.xx.xx
```

---

Verify Docker Compose

```bash
docker compose version
```

Expected

```
Docker Compose version v2.x.x
```

---

# Verify Docker is Running

Run

```bash
docker info
```

If Docker Desktop is not running,

start Docker Desktop first.

---

# Clone the Repository

```bash
git clone https://github.com/tesreco-labs/devops-demo.git
```

Move inside the project

```bash
cd devops-demo
```

---

# Repository Structure

Your project should look similar to:

```text
devops-demo/

├── app.py
├── Dockerfile
├── docker-compose.yml
├── prometheus.yml
├── requirements.txt
├── README.md
└── docs/
```

---

# Verify Project Files

Check

```bash
ls
```

or on Windows

```powershell
dir
```

Ensure these files exist

- Dockerfile
- docker-compose.yml
- prometheus.yml

---

# Start the Application

Run

```bash
docker compose up -d
```

Docker will

- Build the Flask application
- Download Prometheus
- Download Grafana
- Create a Docker network
- Start all services

The first run may take a few minutes because Docker downloads the required images.

---

# Verify Running Containers

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

# Verify the Application

Open your browser.

### Flask Application

```
http://localhost:5000
```

---

### Prometheus

```
http://localhost:9090
```

---

### Grafana

```
http://localhost:3000
```

Default login

```
Username

admin

Password

admin
```

---

# Verify Metrics Endpoint

Open

```
http://localhost:5000/metrics
```

You should see text similar to

```
process_cpu_seconds_total

python_gc_objects_collected_total

process_resident_memory_bytes
```

This confirms that the application is exposing Prometheus-compatible metrics.

---

# Common Docker Commands

View running containers

```bash
docker ps
```

View images

```bash
docker images
```

View logs

```bash
docker compose logs
```

Stop application

```bash
docker compose stop
```

Restart application

```bash
docker compose restart
```

Remove containers

```bash
docker compose down
```

---

# Troubleshooting

## Docker Command Not Found

Docker is not installed or not added to PATH.

Verify

```bash
docker version
```

---

## Docker Engine Not Running

Start Docker Desktop.

Wait until Docker shows

```
Engine Running
```

---

## Port Already in Use

If

```
5000

9090

3000
```

are already being used,

stop the conflicting applications or containers.

Find running containers

```bash
docker ps
```

---

## Images Download Slowly

Docker is downloading images from Docker Hub.

This is expected during the first run.

Subsequent runs will be much faster.

---

## Build Failed

Try rebuilding

```bash
docker compose build --no-cache
```

Then

```bash
docker compose up -d
```

---

# Verify Everything

You are ready for the next labs if the following URLs work:

| URL | Expected |
|------|----------|
| http://localhost:5000 | Flask application |
| http://localhost:5000/metrics | Prometheus metrics |
| http://localhost:9090 | Prometheus UI |
| http://localhost:3000 | Grafana Login |

---

# Learning Path

Follow the labs in order:

```
00-setup.md
        │
        ▼
01-docker-basics.md
        │
        ▼
02-docker-compose.md
        │
        ▼
03-monitoring-with-prometheus-grafana.md
        │
        ▼
04-promql-basics.md
        │
        ▼
05-grafana-dashboards.md
        │
        ▼
06-observability-fundamentals.md
```

---

# Need Help?

If you encounter any issues during setup:

- Ensure Docker Desktop is running.
- Verify all required ports (5000, 9090, 3000) are available.
- Check the container logs using:

```bash
docker compose logs
```

---

# Congratulations!

🎉 Your development environment is now ready.

In the next lab, you'll learn the fundamentals of Docker, including images, containers, volumes, networking, and essential Docker commands that form the foundation of modern DevOps workflows.
