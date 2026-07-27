# DevOps Demo

A hands-on DevOps learning repository for students.

This project is designed to help you learn the core building blocks of modern DevOps through a simple multi-container application. You will work with Docker, Docker Compose, Prometheus, Grafana, and basic observability concepts using a practical demo environment.

## What you will learn

- Docker fundamentals
- Running multi-container applications with Docker Compose
- Monitoring application metrics with Prometheus
- Visualizing metrics in Grafana
- Basic troubleshooting for containers and services

## Repository Overview

This repo contains a small application stack that includes:

- A sample application running in a container
- Prometheus for collecting metrics
- Grafana for visualizing metrics
- Documentation files inside the `docs/` folder for step-by-step learning

## Suggested Learning Path

1. Start with the setup guide
2. Learn Docker basics
3. Learn Docker Compose
4. Connect Prometheus and Grafana
5. Explore monitoring and dashboards

## Prerequisites

Before starting, install:

- Docker Desktop
- Docker Compose
- Git
- A code editor like VS Code

## Getting Started

Clone the repository:

```bash
git clone https://github.com/tesreco-labs/devops-demo.git
cd devops-demo
```
Start the application stack:

```docker compose up -d```

Check the running services:

```docker compose ps```

Open the application and tools in your browser:
```
Application: http://localhost:5000
Prometheus: http://localhost:9090
Grafana: http://localhost:3000
```
# 📚 Documentation
The detailed learning material is available in the docs/ folder.

- [00 - Environment Setup](docs/00-setup.md)
- [01 - Docker Basics](docs/01-docker-basics.md)
- [02 - Docker Compose](docs/02-docker-compose.md)
- [03 - Monitoring with Prometheus & Grafana](docs/03-monitoring-with-prometheus-grafana.md)

Goal of This Repo
The goal of this repository is to give students a practical DevOps starting point so they can understand how containers, monitoring, and dashboards work together in a real-world workflow.
