---
name: hyperos4-rust-launcher-native-hook
description: Analyze and develop evidence-based HyperOS 4 Rust Launcher native hooks, including ELF and native symbol analysis, ABI-safe Rust hook design, hook loading verification, crash triage, and version compatibility work.
---

# HyperOS 4 Rust Launcher Native Hook Analysis & Development

Use this skill for a HyperOS 4 system Launcher (`com.miui.home` or an explicitly identified replacement) implemented mainly as Rust/native code, when the task involves locating native symbols, designing a native hook, diagnosing a hook that does not load or does not change behavior, or adapting a hook to a new Launcher build. It is not a general Android or Rust development guide.

## Evidence gate

Label every important claim with one of these states:

- `DEVICE_VERIFIED`: reproduced on a named device and build, with a timestamped command or log excerpt.
- `STATICALLY_VERIFIED`: confirmed in the supplied APK/ELF or another named artifact by a repeatable analysis step.
- `INFERRED`: a working hypothesis derived from evidence but not yet confirmed.
- `UNKNOWN`: the required artifact or observation is missing.

Never turn an RVA, function name, signature, ABI, or test result from one Launcher build into a universal fact. A successful compile proves only that the artifact compiled. A loaded library proves only that the injection path ran. Report functional success separately and require a real reproduction for it.

## Workflow

1. **Collect the environment before touching code.** Fill in [references/environment-checklist.md](references/environment-checklist.md). Record the exact device build, Launcher package and `versionCode`, target file hashes, ABI, hook framework, Rust toolchain, and NDK. If a required field is unavailable, mark it `UNKNOWN` and explain how it limits the analysis.
2. **Identify the actual implementation.** Follow [references/launcher-analysis.md](references/launcher-analysis.md) to inventory APK contents, DEX when present, ELF files, symbols, strings, dependencies, and call relationships. Treat Rust/AOT snapshots and stripped ELF files as possibilities to be tested, not assumptions.
3. **Make a feasibility decision.** State which target is supported by evidence, which address is an RVA relative to which image, which bytes or symbol signature identify it, and what remains unknown. Stop short of a hook when the function contract, image identity, or load timing cannot be established safely.
4. **Design the native hook.** Read [references/rust-native-hook.md](references/rust-native-hook.md). Confirm the target ABI and calling convention from the binary and runtime context; define the original-call path, object lifetime, thread and re-entry behavior, failure handling, and rollback before writing `unsafe` code. Use a guarded template when the contract is not proven.
5. **Build and validate in layers.** Record the exact build command and artifact hash. Then verify, in order: (a) the library is packaged for the device ABI, (b) the hook framework loads it in the intended process, and (c) the feature changes the intended behavior without a crash. Do not report (a) or (b) as functional success.
6. **Diagnose failures from evidence.** For a crash, a loaded-but-inert hook, or a version upgrade, use [references/crash-triage.md](references/crash-triage.md). Capture the symptom, logs, reproduction steps, and image version before changing a hypothesis. Prefer a version-gated signature match and a reversible patch over a global device-mode or framework change.
7. **Deliver a reproducible result.** Include changed files, artifact hashes, supported versions, evidence labels, test commands and outcomes, known limitations, rollback steps, and the next missing artifact. Do not package proprietary APKs, decompiled source, secrets, or unverified offsets in a public Skill.

## Reference routing

- Use the environment template before analysis: [references/environment-checklist.md](references/environment-checklist.md).
- Use the static and dynamic analysis procedure for Launcher work: [references/launcher-analysis.md](references/launcher-analysis.md).
- Use the Rust/FFI and build guidance while implementing native code: [references/rust-native-hook.md](references/rust-native-hook.md).
- Use the symptom-driven recovery procedure after a failed load, crash, or upgrade: [references/crash-triage.md](references/crash-triage.md).

Evaluate this Skill with the prompts and observable criteria in [evals/test-cases.md](evals/test-cases.md).
