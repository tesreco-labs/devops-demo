# 🐙 Docker Compose - Running Multi-Container Applications

> **Module 2 - TESRECO DevOps Labs**
>
> **Estimated Time:** 60 Minutes
>
> **Difficulty:** ⭐⭐ Beginner

---

# Learning Objectives

After completing this lab, you will be able to:

- Understand why Docker Compose is needed
- Read a docker-compose.yml file
- Start multiple containers together
- Understand services
- Build images automatically
- Mount configuration files
- Access multiple services
- Debug Docker Compose applications
- Stop and clean up the environment

---

# Why Docker Compose?

In the previous lab we learned how to run a single container.

Example:

```
docker run nginx
```

But real-world applications rarely consist of just one container.

A typical application may contain:

```
                Browser
                    │
                    ▼
              Reverse Proxy
                    │
      ┌─────────────┴─────────────┐
      ▼                           ▼
 Backend API                 Frontend
      │
      ▼
 Database

      ▼
 Cache (Redis)

      ▼
 Monitoring

      ▼
 Logging
```

Managing each container individually becomes difficult.

Docker Compose lets us manage an entire application using **one file**.

---

# What is Docker Compose?

Docker Compose is a tool that allows you to define an entire application using YAML.

Instead of typing:

```bash
docker run ...
docker run ...
docker run ...
docker run ...
```

You simply write

```
docker-compose.yml
```

and execute

```bash
docker compose up
```

Everything starts automatically.

---

# Our Demo Application

This repository contains **three services**:

```text
                 +--------------------+
                 |   Flask App        |
                 |     Port 5000      |
                 +---------+----------+
                           |
                           |
                Exposes Metrics
                           |
                           ▼
                 +--------------------+
                 |    Prometheus      |
                 |     Port 9090      |
                 +---------+----------+
                           |
                           |
                     Collect Metrics
                           |
                           ▼
                 +--------------------+
                 |      Grafana       |
                 |     Port 3000      |
                 +--------------------+
```

The application exposes Prometheus metrics.

Prometheus collects those metrics.

Grafana visualizes them.

This architecture is widely used in production.

---

# Understanding docker-compose.yml

Open

```
docker-compose.yml
```

You will see three services.

---

## Service 1

```yaml
app:
  build: .
```

Meaning

Instead of downloading an image,

Docker will build one using

```
Dockerfile
```

present in this repository.

---

### Exposed Port

```yaml
ports:
  - "5000:5000"
```

Meaning

```
Host Machine

localhost:5000

↓

Container

5000
```

Open

```
http://localhost:5000
```

You should see the application running.

---

## Service 2

```yaml
prometheus:
```

This downloads the official Prometheus image.

```yaml
image: prom/prometheus
```

---

### Configuration File

```yaml
volumes:
  - ./prometheus.yml:/etc/prometheus/prometheus.yml
```

This is called a **Bind Mount**.

It tells Docker

```
Local File

prometheus.yml

↓

Inside Container

/etc/prometheus/prometheus.yml
```

Any change made locally is immediately visible inside the container.

---

### Port Mapping

```yaml
9090:9090
```

Open

```
http://localhost:9090
```

Prometheus UI should appear.

---

## Service 3

```yaml
grafana:
```

Grafana uses

```yaml
image: grafana/grafana
```

Expose

```
3000
```

Open

```
http://localhost:3000
```

Grafana Login

Default

```
Username

admin

Password

admin
```

(Change it after first login.)

---

# Starting the Entire Application

From the project root

Run

```bash
docker compose up
```

Docker performs the following:

✔ Reads docker-compose.yml

↓

✔ Builds application image

↓

✔ Downloads Prometheus

↓

✔ Downloads Grafana

↓

✔ Creates network

↓

✔ Starts containers

---

Run in background

```bash
docker compose up -d
```

Recommended during development.

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

# Verify Images

```bash
docker images
```

You should see

- App Image
- Prometheus
- Grafana

---

# View Logs

All services

```bash
docker compose logs
```

Follow logs

```bash
docker compose logs -f
```

Only application logs

```bash
docker compose logs app
```

Only Prometheus

```bash
docker compose logs prometheus
```

Only Grafana

```bash
docker compose logs grafana
```

---

# Execute Commands Inside Containers

Application

```bash
docker compose exec app sh
```

Prometheus

```bash
docker compose exec prometheus sh
```

Grafana

```bash
docker compose exec grafana sh
```

---

# Build Application Again

Whenever Dockerfile changes

```bash
docker compose build
```

Or

```bash
docker compose up --build
```

---

# Restart Application

```bash
docker compose restart
```

Restart only application

```bash
docker compose restart app
```

---

# Stop Everything

```bash
docker compose stop
```

Containers remain available.

---

# Remove Everything

```bash
docker compose down
```

Removes

- Containers
- Networks

---

Remove volumes too

```bash
docker compose down -v
```

---

# Validate Compose File

Always validate before running

```bash
docker compose config
```

If YAML has syntax errors,

Docker will report them here.

---

# Check Container Health

```bash
docker compose ps
```

Detailed information

```bash
docker inspect <container-id>
```

---

# Exercise 1

Start the complete application

```bash
docker compose up -d
```

Verify

```
localhost:5000
localhost:9090
localhost:3000
```

---

# Exercise 2

Check running containers

```bash
docker compose ps
```

---

# Exercise 3

View application logs

```bash
docker compose logs app
```

Observe application startup.

---

# Exercise 4

Open Prometheus

Navigate to

```
Status

↓

Targets
```

Verify

Application target is UP.

---

# Exercise 5

Open Grafana

Login

Explore Dashboards

Understand the UI.

(Dashboard creation will be covered in later labs.)

---

# Common Problems

## Port Already Used

```
Bind for 5000 failed
```

Solution

```bash
docker ps
```

Stop conflicting container.

---

## Build Failed

Run

```bash
docker compose build --no-cache
```

---

## YAML Syntax Error

Run

```bash
docker compose config
```

---

## Service Exits Immediately

Check

```bash
docker compose logs app
```

---

## Prometheus Not Collecting Metrics

Check

```
localhost:9090/targets
```

Verify target state.

---

## Grafana Not Opening

Check

```bash
docker compose logs grafana
```

Wait for startup.

Grafana typically takes longer than the other services.

---

# Interview Questions

### Why do we use Docker Compose?

### Difference between

```
docker run

docker compose up
```

### What is a Service?

### What does

```
build: .
```

mean?

### Difference between

```
image:
```

and

```
build:
```

### What is a Bind Mount?

### Difference between

```
docker compose stop

docker compose down
```

### What happens when Docker Compose starts an application?

---

# Quick Command Cheat Sheet

```bash
docker compose up

docker compose up -d

docker compose ps

docker compose logs

docker compose logs -f

docker compose logs app

docker compose exec app sh

docker compose restart

docker compose build

docker compose up --build

docker compose config

docker compose stop

docker compose down

docker compose down -v
```

---

# Key Takeaways

✅ Docker Compose manages multiple containers using a single YAML file.

✅ Each application component is defined as a **service**.

✅ The **app** service is built locally using the repository's Dockerfile.

✅ **Prometheus** collects metrics exposed by the application.

✅ **Grafana** visualizes those metrics.

✅ Docker Compose automatically creates a shared network so the services can communicate.

---

# What's Next?

In the next lab (**03-Monitoring-with-Prometheus-and-Grafana.md**), you'll configure Prometheus to scrape application metrics and build your first Grafana dashboard using the services started in this Docker Compose environment.
