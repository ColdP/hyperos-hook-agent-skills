# Evaluation test cases

Each case is a prompt for an independent Agent run. A passing run follows the evidence gate, asks for or records missing inputs, and avoids inventing HyperOS internals.

## 1. Known target build

**Input:** “Analyze the supplied HyperOS 4 Launcher APK, versionCode 801000001, and determine whether the native Dock background function can be hooked.”

**Expected behavior:** Hashes the APK, inventories DEX/ELF, identifies ABI and symbols/signatures, records a candidate only with surrounding evidence, and proposes a version-gated plan.

**Observable pass conditions:** The report labels static findings, lists the exact artifact and unique-match count, and separates compile/load/function tests.

**Avoid:** Copying an address from another Launcher version or calling an unverified decompiler name a confirmed function.

## 2. Missing APK and version

**Input:** “Add a Dock hook for my HyperOS phone; I do not have the Launcher APK or version information.”

**Expected behavior:** Requests the smallest missing package/version/artifact data and performs only useful read-only planning.

**Observable pass conditions:** Missing data is `UNKNOWN`, with an explanation of why safe targeting is blocked.

**Avoid:** Guessing a package offset, build, ABI, or feature gate.

## 3. Signature cannot establish a function contract

**Input:** “This stripped ELF has one matching byte pattern. Write a Rust replacement function now.”

**Expected behavior:** Inspects callers/returns and ABI evidence; if insufficient, supplies a guarded FFI template and a list of required confirmations.

**Observable pass conditions:** The code is explicitly a template, and no guessed parameter types or object layouts are presented as deployable.

**Avoid:** Casting the pattern to an arbitrary Rust function pointer.

## 4. Rust Native Hook design

**Input:** “Design an arm64 Rust native hook loaded through a C ABI callback, with reversible installation.”

**Expected behavior:** Covers `repr(C)`, `extern "C"`, unsafe invariants, instruction relocation, page permissions, cache flush, lifetime, re-entry, thread safety, rollback, and artifact inspection.

**Observable pass conditions:** General Rust/Android facts are separated from target-specific facts and no unverified target signature is invented.

**Avoid:** Treating a successful Cargo build as proof that the hook loaded or worked.

## 5. Compiled but not loaded

**Input:** “The APK builds, but the feature does nothing and no hook log appears.”

**Expected behavior:** Checks packaged ABI/path, framework scope, process name, load callbacks, `/proc/<pid>/maps`, and image timing before changing the target patch.

**Observable pass conditions:** The plan distinguishes compiled, loaded, and functionally effective states and proposes a diagnostic-only build.

**Avoid:** Changing offsets or rebooting as the first response.

## 6. Launcher crash after enabling

**Input:** “Launcher crashes immediately after enabling my native hook.”

**Expected behavior:** Disables/reverts safely according to authorization, collects tombstone/log/PC/build evidence, and tests entry ABI, relocation, signature, and lifetime hypotheses separately.

**Observable pass conditions:** The report uses symptom → evidence → hypothesis → verification → fix → regression structure.

**Avoid:** Attributing every crash to permissions or blindly adding a delay.

## 7. System upgrade invalidates the hook

**Input:** “The old Launcher build worked; after a HyperOS update the same RVA has no effect.”

**Expected behavior:** Re-hashes and independently analyzes the new artifact, recomputes signatures/callers, adds a separate version gate or safely rejects it.

**Observable pass conditions:** It refuses to carry the RVA by arithmetic alone and includes an unknown-version fail-closed test.

**Avoid:** Applying the old patch to the new image because the version names look similar.

## 8. Unrelated Rust task

**Input:** “Implement a Rust CSV parser for a desktop command-line tool; there is no Android or Launcher component.”

**Expected behavior:** Declines to activate this specialized workflow and handles the ordinary Rust task with an appropriate general approach.

**Observable pass conditions:** No ELF, Hook framework, HyperOS offset, or device-test requirements are introduced.

**Avoid:** Forcing the native-hook checklist onto unrelated Rust development.
