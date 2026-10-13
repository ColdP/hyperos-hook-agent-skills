# hyperos-hook-agent-skills

面向能够读取仓库文件、分析代码并执行开发工具的 AI 编程 Agent，持续积累 HyperOS 系统 Hook 分析、Native 开发、调试和版本适配经验的 Agent Skills 集合。

## Skill 列表

| Skill | 适用范围 | 路径 |
| --- | --- | --- |
| `hyperos4-rust-launcher-native-hook` | HyperOS 4 Rust/Native 桌面分析、ABI 安全的 Hook 设计、加载与功能验证、闪退排查和版本门控 | [`skills/hyperos4-rust-launcher-native-hook/`](skills/hyperos4-rust-launcher-native-hook/) |

使用时读取 [`SKILL.md`](skills/hyperos4-rust-launcher-native-hook/SKILL.md)，或在支持 Skill 的 Agent 中显式调用 `$hyperos4-rust-launcher-native-hook`。详细流程位于 Skill 的 `references/` 目录，评估提示位于 [`evals/test-cases.md`](skills/hyperos4-rust-launcher-native-hook/evals/test-cases.md)。安装方式见 [INSTALL.md](INSTALL.md) 或 [INSTALL_zh.md](INSTALL_zh.md)。

## 证据状态

Skill 统一使用以下标签：

- `DEVICE_VERIFIED`：在指定设备和系统版本上复现，并有可追溯的运行时证据。
- `STATICALLY_VERIFIED`：由指定 APK、ELF 或其他实际提供的文件静态确认。
- `INFERRED`：有证据支持但尚未完全确认的推断。
- `UNKNOWN`：缺少必要文件或观察结果，无法确认。

Skill 本身只提供可复用的方法，不包含专有 APK、反编译源码、私钥、设备日志或设备专属偏移。任何 HyperOS 函数名、RVA、ABI、Rust 对象布局或能力开关，都必须针对目标文件重新确认。编译成功、库已加载和功能真正生效会分别报告。

## 当前验证边界

当前仓库包含第一个 Skill、安装指南、贡献指南和自动校验配置；没有宣称任何具体 HyperOS 4 桌面版本已经完成真机 Hook 验证。设备相关结论必须提供匹配的目标文件和运行时证据，并使用上述标签标记。

## 许可证

本仓库及其中的 Skill 采用 [Apache License 2.0](LICENSE)。
