# Gaia on Mobile — Architecture (PT/EN)

## Objective
Gaia is designed to run first on mobile devices, especially mid-low range phones, as an offline-first local assistant with local memory, transparent governance, and strong protection for vulnerable people and contexts.

## Target hardware
- Primary: Android ARM64 and mid-range smartphones
- Secondary: low-end Android / budget phones
- Tertiary: laptops and edge devices when available

## Recommended runtime
- llama.cpp / ggml for local text inference
- ONNX / TFLite for lightweight vision & accessibility modules
- whisper.cpp for local voice-to-text when needed
- local TTS modules for accessibility

## Recommended model tiers
### Tier 1: Minimum viable mode (inclusion)
- 1.3B or smaller quantized model
- Ideal for low-end phones and battery-conscious use
- Use for: summary, Q&A, local memory, translation, guardrails, policy checks

### Tier 2: Quality mode (upgrade path)
- 3B quantized model
- Runs on modern devices and laptops
- Use for: more human-like responses, contextual reasoning, richer summaries, better support

## Migration strategy
- The same Gaia runtime should work with both tiers
- Memory is preserved by vector export/import + adapter patches
- Upgrades should not discard user memory or personal context

## Mobile-first logic
1. User opens Gaia locally
2. Gaia reads the local memory and preference profile
3. It processes prompt text or voice locally
4. It checks local policy (safe_reply / policy_enforcer)
5. If allowed, it responds with summary/context/resolution
6. Only if the user authorizes, it can further share a report or adapter patch

## Why this is important
- It reduces dependency on large cloud platforms
- It keeps the system accessible to everyone
- It minimizes censorship by opaque external systems
- It respects the user's context and local control
- It supports upgrades without destroying the user's previous context

## Minimal design principle
"Start with the smallest model that works, preserve memory, prove the system is useful, then upgrade when the device allows it."
