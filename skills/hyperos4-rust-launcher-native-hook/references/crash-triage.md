# Crash and no-effect triage

Use the same loop for every incident: **symptom → collect evidence → state hypotheses → test one hypothesis → make the smallest fix → repeat the regression test**. Preserve the original artifact and disable the hook if the Launcher becomes unstable. Do not assume every crash has the same cause.

## Launcher immediately crashes after enabling the hook

**Symptom:** the process dies during startup or on the first affected screen.

**Collect evidence:** exact Launcher build and ABI; hook framework log; process maps; crash timestamp; `logcat` around the PID; tombstone/backtrace if available; whether the crash occurs with the library loaded but the target patch disabled. Capture registers and the PC, and map the PC to the exact ELF/build ID.

**Hypotheses:** wrong native entry ABI; patch applied before the image was complete; relocated PC-relative instruction is wrong; target signature matched a different function; parameter/return convention is wrong; retained object or callback lifetime ended; data race or re-entry occurred.

**Verify:** first run the library with initialization and logging only; then enable image identity checks; then install the patch without changing behavior; finally enable the replacement path. Compare the crashing PC and registers with the candidate's expected contract.

**Fix and regression:** restore the original bytes or disable the scope, narrow the signature/version gate, correct the trampoline or FFI type, and repeat cold start plus the original reproduction. Record the recovery action and the build that was tested.

## Hook is loaded but the feature does not change

**Symptom:** the library appears in maps or logs, but the UI/system behavior is unchanged.

**Collect evidence:** exact loaded path and hash, PID, entry log, target image map, runtime patch bytes, config values, function-call counter, and a before/after reproduction. Confirm that the tested feature actually uses the targeted code path.

**Hypotheses:** wrong process or scope; image loaded after initialization; target code is a different ABI/split; version gate selected no candidate; patch is in a never-used branch; configuration was not read; the UI caches the result.

**Verify:** log process name/PID and image load callback; rescan when the target ELF maps; compare live bytes against expected original and replacement; use a minimal call counter or safe trace; manually reload only when the task permits it.

**Fix and regression:** correct timing or process selection, replace guessed RVA with a unique signature, repair configuration publication, or target the actual caller. Test both enabled and disabled paths and report if no functional reproduction is available.

## Parameters, return values, or ABI appear wrong

**Symptom:** corrupted UI state, invalid values, a crash on return, or behavior that changes with optimization.

**Collect evidence:** disassembly at the call and return, register/stack snapshots where permitted, data widths and floating-point registers, receiver/hidden arguments, alignment, and a matching non-hooked trace.

**Hypotheses:** C versus Rust/C++ ABI mismatch; hidden receiver or sret argument omitted; integer/floating register confusion; wrong ownership or lifetime; structure layout guessed from a decompiler.

**Verify:** compare multiple call sites and return uses; use a no-op wrapper that forwards every argument unchanged; validate only documented fields; compile with the exact target ABI and inspect the generated call sequence.

**Fix and regression:** model the verified contract explicitly, keep unknown fields opaque, and add an ABI/version guard. Re-test startup, repeated entry, concurrent calls, and disable/restore behavior.

## Initialization, lifetime, thread, or re-entry issue

**Symptom:** intermittent crashes, only cold-start failures, deadlocks, duplicate installation, or failures after a Launcher reload.

**Collect evidence:** event order for process start, library load, image mapping, config read, patch install, and first call; thread IDs; install count; lock ownership; callback and object destruction events.

**Hypotheses:** work ran in a pre-fork loader; initialization raced image mapping; a callback was retained past destruction; a hook called itself; two generations of the same image were patched.

**Verify:** add bounded, non-invasive state logs and an atomic once/state machine; delay only the target scan until the image is present; test repeated process creation and a manual reload. Avoid adding arbitrary sleeps as a fix.

**Fix and regression:** make initialization idempotent, retain executable state for the process lifetime, guard re-entry, and synchronize configuration publication. Test multiple launches and both feature states.

## System or Launcher update breaks an existing hook

**Symptom:** the previous build worked, while the new build rejects the target, crashes, or silently has no effect.

**Collect evidence:** old/new hashes, build IDs, `versionCode`, ABI, disassembly diff around the old target, signature match counts, changed exports/dependencies, and new runtime logs.

**Hypotheses:** code moved or was rebuilt; the call contract changed; a capability gate moved; the framework changed load timing; the feature was removed or replaced.

**Verify:** analyze the new artifact independently. Recompute signatures and callers, then run with the hook disabled and a diagnostic-only build. Never derive a new RVA by adding the old delta without a matching control-flow and contract check.

**Fix and regression:** add a separate version-gated implementation only when independently verified; otherwise reject the build safely. Test old and new supported versions plus an unknown version to ensure fail-closed behavior.

## Restoring normal operation

Disable the module or Launcher scope through the installed hook framework, restore the original artifact/configuration, and capture logs before clearing them. Follow the user's authorization for any package change, process stop, or reboot. A recovery report should state whether the Launcher returned to normal and which hook state was active. Never claim recovery from a log-only observation.
