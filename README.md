# VINK — AI/LLM Security Middleware

A security middleware layer built to prevent sensitive data leakage at the LLM trust boundary.

## What it does
- Detects and blocks Personally Identifiable Information (PII) before it reaches an LLM
- Hybrid detection engine combining rule-based pattern matching and NLP risk scoring
- Enforces ALLOW, MASK, and BLOCK policies on flagged data
- Real-time audit logging via Firebase (Firestore)
- Security dashboard to monitor enforcement events and anomalies

## Tech Stack
Python · NLP · Firebase · Firestore · Flutter

## Use Case
Addresses prompt injection and SSRF-style agent risks in AI-integrated applications — relevant to EU AI Act compliance and enterprise AI security requirements.
