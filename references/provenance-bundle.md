# Provenance Bundle Contract

A provenance bundle is a small machine-readable index for a final or decision-bearing result. It complements, rather than replaces, the Run Ledger and run manifest.

Recommended bundle fields:

- bundle schema/version and creation time;
- selected `run-manifest.json` path + SHA-256;
- optional Run Ledger path + SHA-256;
- optional competition-rule profile path + SHA-256;
- optional Claim-Evidence Map path + SHA-256;
- declared final/confirmatory status;
- notes and known unresolved warnings.

The bundle must not contain secret environment variables, API keys, tokens, personal credentials or a full machine snapshot. File hashes establish identity, not scientific correctness.
