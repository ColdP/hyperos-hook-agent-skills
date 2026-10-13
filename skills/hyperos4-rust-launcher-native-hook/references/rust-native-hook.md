# Rust Native Hook engineering guide

This reference separates portable Rust/Android engineering from facts that must be recovered from the target Launcher. A template below is intentionally incomplete until the target function contract is verified.

## ABI and build contract

Record the device ABI (`arm64-v8a`, `armeabi-v7a`, or another supported ABI), API level, page size, NDK version, linker mode, Rust target triple, and whether the framework loads a `.so` through a C ABI entry point. Build every shipped ABI deliberately; a successful host build is not evidence that the device can load it.

For an Android native library, keep the entry boundary C-compatible and stable:

```rust
#[repr(C)]
pub struct HookApi {
    pub version: u32,
    // Exact fields are supplied by the hook framework contract.
}

#[no_mangle]
pub unsafe extern "C" fn native_init(api: *const HookApi) -> *const core::ffi::c_void {
    if api.is_null() {
        return core::ptr::null();
    }
    // Do not dereference, spawn threads, or patch code until the framework ABI
    // and process stage have been verified for this runtime.
    core::ptr::null()
}
```

The example is a safety boundary template, not a usable HyperOS hook. Confirm symbol visibility, calling convention, struct packing, pointer validity, and callback lifetime from the framework headers or a tested ABI contract. Rust's default `extern "Rust"` ABI and layout of ordinary structs are not suitable for an unknown foreign caller.

## Function signature and original-call path

Derive the target signature from the actual disassembly, exported type information, a matching debug build, or a controlled runtime probe. Confirm argument registers, floating-point versus integer registers, hidden return or receiver arguments, return register, stack alignment, and whether the function is a C ABI, C++ ABI, Rust ABI, or an AOT-generated internal convention. Do not cast a function pointer merely because the number of visible arguments appears to match.

When an inline hook needs an original trampoline, preserve whole instructions and relocate PC-relative branches/literals according to the architecture. A call-site redirect can be safer when it avoids relocating a prologue. Keep the original pointer immutable after installation and make rollback restore only bytes that still match the expected patched state.

## `unsafe`, memory, and object lifetime

- Keep each `unsafe` block small and state its invariant beside it.
- Treat a target pointer as borrowed only for the documented call duration. Do not retain a Rust reference to a Launcher object unless ownership and destruction are proven.
- Do not free executable islands, trampolines, or callback state while another thread could execute them.
- Respect page permissions, instruction-cache invalidation, atomic instruction writes, and architecture alignment. A multiword patch is not automatically atomic.
- Avoid reading or writing fields by guessed offsets. Rust layout, pointer tagging, and allocator ownership must come from the target binary or a compatible public contract.

## Threading, re-entry, and failure

Assume the hook may run concurrently on render, UI, worker, and binder threads. Use atomics or a lock with a defined ordering; avoid taking a lock that the original function may take. Add a re-entry guard around callbacks that can indirectly invoke the target. Initialization must tolerate the image not being mapped yet and must not create unsafe activity in a pre-fork or loader process.

Fail closed on an unknown image, ambiguous signature, invalid pointer, or failed page permission change. Log a concise reason and keep the original path. Do not catch a memory fault by treating arbitrary bytes as a valid object. A panic crossing a C ABI is undefined behavior; configure a suitable panic strategy and return an explicit failure where the contract permits.

## Build and artifact validation

Record the exact commands and tool versions, then inspect the output rather than trusting Gradle/Cargo success:

```text
cargo build --release --target <verified-android-target>
readelf -h -d -Ws <output>.so
llvm-readelf --notes <output>.so
sha256sum <output>.so
```

Use the project's actual Android build system when one exists. Verify ABI directory placement, `DT_NEEDED`, exported entry symbols, RELRO/segment permissions, 16 KB page alignment requirements where applicable, and that the packaged file is the one installed or loaded. Keep debug symbols outside a public release unless licensing permits them.

## Three validation states

1. **Compiled:** the compiler and packager produced an artifact for the intended ABI. This says nothing about loading or behavior.
2. **Loaded:** framework logs, `/proc/<pid>/maps`, or an equivalent runtime trace show the exact library and entry point in the intended Launcher process. This does not prove the target function was reached.
3. **Functionally effective:** a controlled before/after reproduction on the matching device/build shows the intended change and no regression, with logs tying the call to the observed behavior.

Only the third state supports a claim that the feature works. If the target contract is not confirmed, keep the implementation as a guarded template and list the missing evidence.

## Portable sources versus target facts

Rust FFI, `repr(C)`, Android ABI selection, ELF inspection, and instruction-cache rules are general engineering guidance. The public references consulted for these portions are the [Rustonomicon FFI chapter](https://doc.rust-lang.org/nomicon/ffi.html), [Android NDK guides](https://developer.android.com/ndk/guides), and the [ELF specification](https://refspecs.linuxfoundation.org/elf/). Function names, offsets, Rust object layouts, capability flags, hook framework callback timing, and required device properties are target facts and must be marked `STATICALLY_VERIFIED`, `DEVICE_VERIFIED`, `INFERRED`, or `UNKNOWN` in the project record.
