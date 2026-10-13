# Environment checklist

Complete this record before interpreting a Launcher hook result. Keep the original command output or a dated log beside the record. A blank required field is `UNKNOWN`; do not fill it with a value copied from another device or Launcher release.

## Required identity

| Field | Value | Evidence / command | Status |
| --- | --- | --- | --- |
| Device model and product |  | `adb shell getprop ro.product.model` and `ro.product.device` |  |
| Android and HyperOS build |  | `adb shell getprop ro.build.version.release`, `ro.build.version.incremental`, and relevant `ro.miui.*` properties |  |
| Launcher package and process |  | `adb shell dumpsys package <package>`; confirm the running process separately |  |
| Launcher version name |  | `dumpsys package` or `pm dump` output |  |
| Launcher `versionCode` |  | `dumpsys package` or package manager output |  |
| Target APK/ELF path |  | `adb shell pm path <package>` and the local copy path |  |
| Target SHA-256 |  | `sha256sum <file>` or `Get-FileHash -Algorithm SHA256 <file>` |  |
| Device CPU ABI |  | `adb shell getprop ro.product.cpu.abilist` |  |
| Hook framework and version |  | Installed module/app metadata and scope configuration |  |
| Hook entry mechanism |  | Native init, Zygisk/LSPosed, framework API, or other documented path |  |
| Rust toolchain |  | `rustc -Vv`, `cargo -V` |  |
| Android NDK and build tools |  | `sdkmanager --list`, Gradle/CMake configuration, or `ndk-build --version` |  |

## Optional but high-value evidence

- A matching local APK extracted from the same installed package, rather than an apparently similar download.
- Split APK names, install source, and ABI-specific native libraries.
- ELF build ID, section table, dynamic dependencies, symbol table state, and stripped/debug companion files.
- Reproduction steps, timestamps, process IDs, `logcat` filters, tombstone path, and whether the Launcher was manually reloaded.
- The hook library's packaged path, load address, `maps` excerpt, and framework load log.
- A known-good older build and a minimal diff of its relevant functions or instruction signatures.
- SELinux, linker namespace, ptrace restrictions, and whether root access changes read/write permissions.

## Handling missing information

1. Mark the field `UNKNOWN` and state the exact decision it blocks. For example, an unknown `versionCode` prevents safe version gating, while an unknown SHA-256 prevents associating an RVA with a specific artifact.
2. Continue read-only inventory that does not depend on the missing field.
3. Request the smallest missing artifact or command output. Do not invent an address, symbol, ABI, or test result to complete the table.
4. If implementation proceeds with a hypothesis, label it `INFERRED`, add a guard that fails closed when the expected image/signature is absent, and define the observation that would confirm or reject it.

## Session record

```text
Analysis date (UTC):
Analyst / agent:
Device model / product:
Android / HyperOS build:
Launcher package:
Launcher process and PID:
Version name:
VersionCode:
Target artifact and local path:
Target SHA-256:
ABI / page size:
Hook framework and version:
Native entry mechanism:
Rust toolchain:
NDK / CMake / linker:
Read-only commands and timestamps:
Reproduction steps:
Known-good comparison artifact:
Missing evidence:
Evidence labels used:
```

The commands above are examples of read-only collection. Installing packages, changing scopes, killing system processes, or rebooting must remain an explicit user-authorized action in the surrounding task.
