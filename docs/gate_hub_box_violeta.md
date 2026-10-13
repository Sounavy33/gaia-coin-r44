# Gate Hub and Box Violeta — Public/Private Flow

This document proposes the practical flow between the user device, Gate Hub, and the Box Violeta package model.

## 1. Objective
The Gate Hub acts as the continuity layer between the personal device and the broader ecosystem. It stores signed bundles, allows restore, and provides a verified path for updates and auditability without forcing raw data exposure.

## 2. Data flow
1. User interacts with Gaia on the phone.
2. Gaia processes local data and creates a local memory bundle.
3. If authorized, Gaia prepares an encrypted package or signed metadata package.
4. The package is sent to Gate Hub for validation and storage.
5. Gate Hub verifies signature and checksum.
6. Gate Hub publishes metadata and hash references for auditability.
7. User can restore from Gate Hub using the private key or a local recovery bundle.

## 3. Security rules
- All package uploads must be signed.
- Raw health or voice data requires explicit consent.
- Stored content should be encrypted by default.
- Gate Hub never replaces the user’s local control of data.

## 4. Box Violeta package format
The Four layers of Violeta:
- manifest.json
- adapter patch files
- signed memory export bundle
- metadata for audit and versioning

## 5. Restore logic
- if the device is lost: user restores by reinstalling Gaia and importing the encrypted package from Gate Hub
- if device is replaced: user imports memory package and dictionary, preserving context and identity

## 6. Why this matters
It makes the system portable, recoverable, and upgradeable while keeping the personal layer in the user’s control.
