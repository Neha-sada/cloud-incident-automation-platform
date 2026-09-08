# Cloud Incident Automation Platform

A cloud-native incident monitoring and auto-remediation platform built on AWS.

## Overview
This platform simulates production incident detection, automated alerting and 
remediation workflows. Built to demonstrate cloud-native architecture, 
infrastructure as code and end-to-end testing practices.

## Features
- **Incident Ingestion API** — REST API built with FastAPI to receive and process incidents
- **Severity Classification Engine** — Automatic classification (LOW/MEDIUM/HIGH/CRITICAL)
- **Automated Recovery Workflows** — Service restart, ECS scaling, queue clearing
- **Rule-Based Alerting** — Email notifications via AWS SES
- **Full Observability** — CloudWatch monitoring dashboards, structured logging, health checks
- **End-to-End Testing** — Playwright test suite

## Tech Stack
- **Backend:** Python (FastAPI)
- **Infrastructure:** AWS (EC2, ECS, SES, CloudWatch) — Free Tier
- **IaC:** Terraform
- **Containerisation:** Docker
- **CI/CD:** GitHub Actions
- **Testing:** Playwright (E2E), Pytest

## Architecture
FastAPI Backend → Docker Container → AWS EC2(t2.micro) → CloudWatch Monitoring → SES Alerting

## Note
Originally deployed on AWS Free Tier. Instance taken down after free tier 
limits to avoid ongoing costs. All infrastructure code available in /terraform.

## Project Structure
cloud-incident-automation-platform/
├── backend/          # FastAPI application
├── terraform/        # AWS infrastructure as code  
├── tests/            # Playwright E2E and Pytest unit tests
├── .github/workflows # CI/CD pipeline
└── README.md