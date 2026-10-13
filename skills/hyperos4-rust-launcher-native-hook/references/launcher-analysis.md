# Launcher analysis procedure

This procedure is for one named Launcher artifact and one named version. Preserve the artifact hash and tool versions with every result. The presence of Rust does not imply that a useful Rust symbol table or DEX exists.

## 1. Confirm the analysis object

Record the package, installed APK path, split APK set, version name, `versionCode`, ABI, and SHA-256. Compare the installed package with the local file before using any offset. Extract into a versioned working directory such as `launcher-<versionName>-<versionCode>`; never publish proprietary APKs or decompiled source in a public Skill.

`aapt2 dump badging`, `apkanalyzer manifest`, and package-manager output can establish package metadata. `unzip -l` identifies `classes*.dex`, `lib/<abi>/*.so`, assets, and native loader metadata. The result is evidence about that artifact only.

## 2. Identify DEX and ELF coverage

- If DEX is present, use a version-pinned decompiler only as a navigation aid. Confirm behavior with bytecode, resources, and runtime observations; decompiler names are not authoritative.
- If DEX is absent or the feature is in a Rust/native library, inspect every ABI-matching ELF. Record `readelf -h -S -d`, `readelf -Ws`/`nm -D`, `strings`, and dependency results. A stripped dynamic table, an AOT image, or a Rust symbol mangling scheme can make ordinary Java-oriented searches uninformative.
- Inspect `DT_NEEDED`, `SONAME`, GNU build ID, RELRO/execute permissions, and page alignment. Check whether a library is actually mapped in the target process before designing a hook.
- Use `objdump -d` or LLVM tools for focused disassembly. Ghidra/radare2/IDA may help with cross-references, but retain the exact input hash, architecture, and analysis settings.

## 3. Locate symbols and behavior

Search in this order:

1. Exported and dynamic symbols, including Rust demangled names where available.
2. Stable strings, format strings, panic text, class/field names, and nearby references.
3. Relocation and call targets, function prologues, literal pools, and repeated instruction signatures.
4. Callers and callees of a candidate, with enough surrounding instructions to distinguish similar functions.
5. Runtime evidence: loaded library maps, linker callbacks, logs, and a controlled feature change.

Do not assume an address found in a decompiler is a process address. Record it as an image-relative RVA only after establishing the ELF load bias and file identity. For a signature, document the bytes, wildcard mask, minimum context, uniqueness count, and rejection conditions. A signature that matches twice is not a safe automatic target.

## 4. Assess Hook feasibility

For each candidate, record:

| Item | Required evidence |
| --- | --- |
| Image | Exact ELF/APK hash, ABI, build ID, and mapped path |
| Location | RVA or symbol plus the method used to derive it |
| Contract | Parameter registers/stack, return register, ownership, alignment, and error conventions |
| Reachability | How the function is reached and when its image is loaded |
| Patch surface | Inline entry, call-site redirect, exported symbol, or supported framework hook |
| Safety | Instruction relocation needs, page permissions, atomicity, re-entry, thread safety, rollback |
| Version gate | What causes the hook to refuse an unknown or ambiguous image |

Choose no hook when the contract or image identity is `UNKNOWN` and a wrong call could corrupt the Launcher. Prefer a narrow, version-gated call-site or exported-symbol hook over a global device-mode substitution. Treat a Rust closure, trait object, or async state machine as an opaque object until its ABI and lifetime are confirmed.

## 5. Capture analysis evidence

Use a record like this for each target:

```text
Artifact hash / build ID:
ABI and load bias:
Candidate name (observed or descriptive):
RVA / file offset:
Discovery method:
Signature and mask:
Unique match count:
Caller path:
Expected input / output contract:
Hook insertion point:
Static status: STATICALLY_VERIFIED / INFERRED / UNKNOWN
Runtime status: DEVICE_VERIFIED / INFERRED / UNKNOWN
Rejected alternatives and reason:
```

## 6. Revalidate after an update

Never carry an RVA across a Launcher update by arithmetic alone. Recompute the hash, build ID, load bias, signature match count, surrounding control flow, and call contract. Compare an old and new disassembly only to generate hypotheses; require the new artifact to pass its own checks. A version table should list supported builds and explicit rejection behavior for all others.

## Sources and scope

The command families above follow the public Android APK/NDK tooling model and ELF inspection conventions. The public references consulted for this method are [Android developer tools](https://developer.android.com/tools), [Android NDK guides](https://developer.android.com/ndk/guides), and the [ELF specification](https://refspecs.linuxfoundation.org/elf/). They do not establish any particular HyperOS 4 internal function. HyperOS-specific names, offsets, Rust layouts, and capability bits remain `STATICALLY_VERIFIED` only when the supplied target artifact demonstrates them, and `DEVICE_VERIFIED` only after a matching runtime test.
