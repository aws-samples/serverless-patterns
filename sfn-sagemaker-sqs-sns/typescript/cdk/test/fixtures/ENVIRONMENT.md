# Environment of the recorded responses

- Date: 2026-10-05
- Hardware: Apple M4, 16 GiB, macOS 26.7.1
- Device: `mps` (bfloat16). The container in this pattern runs the model on CPU; upstream documents that CPU serving casts the torso to float32 and is slower, and that answers on different devices agree only within numerical noise. Expect small differences on your endpoint.
- Packages: strands-decider 0.1.0, torch 2.7.1, transformers 5.17.0, peft 0.21.0, huggingface_hub 1.33.0 (Python 3.12)
- Adapter: `StrandsAgents/strands-decider-2B-hobson-v19` at commit `bb282d786bc251fd4e3068de3ada9ddbb38127cd` (Apache-2.0 on the model card)
- Base model: `Qwen/Qwen3.5-2B-Base` at commit `b1485b2fa6dfa1287294f269f5fb618e03d52d7c` (Apache-2.0 on the model card), the revision recorded in the adapter's `provenance.json`
- Latency: `latency_ms` in each fixture is the server-side time on this Mac. The first request after start took 32 s, later ones 1.2 to 3.8 s (7.7 s for the 7,240 character ticket). These are not AWS numbers.
