# Gaia Mobile Runtime Guide

This guide describes the minimal mobile-first runtime plan for Gaia.

## 1) Required components
- Gaia runtime (Python module or local service)
- Local model loader (llama.cpp / ggml branch)
- Policy enforcer
- Vector store and adapters
- Offline export/import tools

## 2) Recommended mobile stack
- CPU-friendly model in quantized form
- Use 1.3B as minimum viable model for entry-level smartphones
- Use 3B for mid/high-range devices and laptops
- Prefer local text first; add vision and voice later as optional modules

## 3) Runtime flow
1. Start Gaia on device
2. Load local memory and profile
3. Receive user text or voice input
4. Check policy
5. Run model locally if available
6. Produce response and save summary into memory
7. Offer export or sync only when authorized

## 4) Offline-safe defaults
- default offline mode: true
- online mode: opt-in only
- memory: local JSON + export/import patch
- no secret or model weights committed to repo

## 5) Suggested path
1. 1.3B minimum viable model
2. 3B upgrade path
3. async local memory + patch migration
4. optional multimodal modules later
