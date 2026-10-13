# hyperos-hook-agent-skills

Reusable Agent Skills for evidence-based HyperOS system analysis, native Hook development, debugging, and Launcher version adaptation.

## Skills

| Skill | Scope | Path |
| --- | --- | --- |
| `hyperos4-rust-launcher-native-hook` | HyperOS 4 Rust/native Launcher analysis, ABI-aware Hook design, load/function verification, crash triage, and version gating | [`skills/hyperos4-rust-launcher-native-hook/`](skills/hyperos4-rust-launcher-native-hook/) |

Use the Skill by loading [`skills/hyperos4-rust-launcher-native-hook/SKILL.md`](skills/hyperos4-rust-launcher-native-hook/SKILL.md) or invoking `$hyperos4-rust-launcher-native-hook` in an Agent environment that supports repository Skills. Its detailed procedures are in the linked `references/` files, and behavioral evaluation prompts are in [`skills/hyperos4-rust-launcher-native-hook/evals/test-cases.md`](skills/hyperos4-rust-launcher-native-hook/evals/test-cases.md).

## Evidence status

The Skill uses four labels consistently:

- `DEVICE_VERIFIED`: reproduced on a named device and build with traceable runtime evidence.
- `STATICALLY_VERIFIED`: confirmed in a named APK/ELF or other supplied artifact.
- `INFERRED`: a hypothesis supported by evidence but not yet confirmed.
- `UNKNOWN`: the required artifact or observation is missing.

The Skill itself provides reusable analysis methods and contains no proprietary APKs, decompiled sources, private keys, device logs, or device-specific offsets. Any HyperOS function name, RVA, ABI, Rust object layout, or capability gate must be re-established for the target artifact. A compilation result, a loaded library, and a functionally effective Hook are reported as separate outcomes.

## Current validation boundary

The repository currently contains the first Skill and its templates; it does not claim that a particular HyperOS 4 Launcher version has been functionally hooked. Device-specific claims require the user or Agent to supply the matching artifact and runtime evidence, then label the result using the status terms above.

## Specification basis

The Skill layout and frontmatter follow the public [Agent Skills specification](https://agentskills.io/specification), checked on 2026-10-13. Its Android and ELF workflow is deliberately framed as a method: public Android/NDK and ELF inspection tools support the command families described in the references, while HyperOS Launcher symbols, offsets, object layouts, and runtime behavior must be re-established from each supplied artifact and device. No private reverse-engineering result is asserted by this repository.
