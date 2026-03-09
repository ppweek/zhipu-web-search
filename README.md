# Zhipu AI Web Search Skill

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw Skill](https://img.shields.io/badge/OpenClaw-Skill-green.svg)](https://github.com/openclaw/openclaw)

使用智谱 AI (Zhipu AI) API 的 `web_search` 工具进行联网搜索的 OpenClaw Skill。

## ✨ 特性

- 🔍 **智能搜索** - 自动判断是否需要联网获取最新信息
- ⚡ **快速响应** - 使用 `glm-4-flash` 模型，性价比高
- 📝 **结果引用** - 支持搜索结果引用标注
- 🌐 **中文优化** - 针对中文搜索场景优化
- 🔧 **易于配置** - 支持环境变量或配置文件

## 📦 安装

### 1. 克隆仓库

```bash
git clone https://github.com/yourusername/zhipu-web-search.git
cd zhipu-web-search
```

### 2. 安装依赖

```bash
pip install zhipuai
```

### 3. 配置 API Key

**方式一：环境变量（推荐）**

```bash
export ZHIPU_API_KEY="your-api-key"
```

**方式二：配置文件**

```bash
# 创建配置文件目录
mkdir -p ~/.openclaw/credentials

# 写入 API Key
echo "your-api-key" > ~/.openclaw/credentials/zhipuai-api-key
```

获取 API Key：[智谱 AI 开放平台](https://open.bigmodel.cn/)

## 🚀 使用

### 命令行

```bash
# 基础搜索
python3 scripts/search.py "今天天气怎么样"

# 指定模型
python3 scripts/search.py --model glm-4 "人工智能最新进展"

# 输出原始 JSON
python3 scripts/search.py --raw "比特币价格"
```

### 作为 Python 模块

```python
from scripts.search import search

result = search("最新科技新闻", model="glm-4-flash")
print(result["content"])
```

### 在 OpenClaw 中使用

```yaml
# 在 OpenClaw 配置中引用
skills:
  - name: zhipu-web-search
    path: /path/to/zhipu-web-search
```

## 📋 支持的模型

| 模型 | 说明 | 推荐度 |
|-----|------|-------|
| `glm-4-flash` | 轻量级，速度快，成本低 | ⭐⭐⭐⭐⭐ |
| `glm-4` | 标准版，综合能力好 | ⭐⭐⭐⭐ |
| `glm-4-plus` | 增强版，能力更强 | ⭐⭐⭐⭐ |

## 🏗️ 项目结构

```
zhipu-web-search/
├── scripts/
│   └── search.py          # 主搜索脚本
├── tests/
│   └── test_search.py     # 单元测试
├── docs/
│   └── API.md             # API 文档
├── .github/
│   └── workflows/
│       └── ci.yml         # CI/CD 配置
├── LICENSE                # MIT 许可证
├── README.md              # 本文件
├── requirements.txt       # Python 依赖
└── SKILL.md               # OpenClaw Skill 规范
```

## 🔧 配置选项

### 环境变量

| 变量名 | 说明 | 必需 |
|-------|------|------|
| `ZHIPU_API_KEY` | 智谱 AI API Key | ✅ |
| `ZHIPU_MODEL` | 默认模型（可选） | ❌ |

### 配置文件路径

- `~/.openclaw/credentials/zhipuai-api-key`
- `~/.config/zhipuai/api_key`

## 📝 示例输出

```
============================================================
搜索结果
============================================================

2025年3月，以下是一些最新的科技新闻：

1. **量子计算取得重大突破**：中国科学技术大学联合国内多家科研机构...

2. **天问二号探测器任务**：中国成功发射天问二号探测器...

...

------------------------------------------------------------
模型: glm-4-flash
Token 消耗: 5447 (输入: 5019, 输出: 428)
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 📄 许可证

本项目采用 [MIT](LICENSE) 许可证开源。

## 🙏 致谢

- [智谱 AI](https://www.zhipuai.cn/) - 提供大模型 API
- [OpenClaw](https://github.com/openclaw/openclaw) - AI 助手框架

## 📮 联系方式

- 项目主页：https://github.com/yourusername/zhipu-web-search
- 问题反馈：https://github.com/yourusername/zhipu-web-search/issues

---

<p align="center">Made with ❤️ for OpenClaw Community</p>
