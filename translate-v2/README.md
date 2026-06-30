# translate-v2 Public Package

This is an original-preserved public edition of `translate-v2`. It keeps the
working skill structure and the dense v0.3.12 spec instead of replacing them
with a short rewritten summary.

## Files

- `SKILL.md`: public Codex-fork skill entry point.
- `NOTES.md`: public runtime guardrails and artifact contracts.
- `spec-v0.3.12.md`: original-preserved living spec; historical revision stream
  removed, living algorithm retained.
- `REFERENCES.md`: standards, research directions, and open-source projects
  reviewed while designing the workflow.

## Sanitization Boundary

Removed:

- local absolute paths and machine/account identifiers
- raw handover and sync metadata
- historical revision stream
- non-public incident evidence and local archive pointers
- generated platform junk

Preserved:

- relay aliases and channel topology
- Web Relay and CLI/API boundaries
- N-1 / N-2 relay context rules
- three-layer fourteen-dimension scoring
- artifact/report schemas and validation requirements
- Antique Game Within Game / 《古董局中局》 workflow boundary

Run the public package gate before publishing.

## References

The workflow was informed by translation quality frameworks such as MQM,
ISO 17100, ISO 18587, ASTM F2575, DQF-MQM, Chinese translation theory,
LLM-era evaluation methods, and several open-source translation projects.

See [`REFERENCES.md`](./REFERENCES.md) for the full reviewed list and license
boundary notes.
