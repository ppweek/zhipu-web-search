# 🚀 Zhipu Web Search Skill v1.0.0 正式发布

> 为 OpenClaw 打造的智谱 AI 联网搜索技能，让 AI 助手实时获取最新信息

---

## ✨ 核心特性

### 🔍 智能联网搜索
- 自动判断何时需要联网获取最新信息
- 支持复杂查询，返回结构化结果
- 中文搜索场景深度优化

### ⚡ 极速响应
- 基于 `glm-4-flash` 模型，响应速度极快
- 性价比超高，适合高频调用场景
- 支持多模型切换（flash/4/plus）

### 🛠️ 极简配置
```bash
# 一行命令安装依赖
pip install zhipuai

# 配置 API Key
export ZHIPU_API_KEY="your-api-key"

# 立即使用
python3 scripts/search.py "最新科技新闻"
```

### 📦 OpenClaw 原生支持
- 完美集成 OpenClaw 框架
- 支持 Skill 市场一键安装
- 配置文件与环境变量双模式

---

## 🎯 适用场景

| 场景 | 示例查询 |
|-----|---------|
| **实时资讯** | "2025年3月最新科技新闻" |
| **市场动态** | "比特币今日价格走势" |
| **产品调研** | "iPhone 16 用户评价" |
| **学术搜索** | "量子计算最新进展" |
| **生活助手** | "今天北京天气怎么样" |

---

## 🚀 快速开始

### 1. 安装

```bash
git clone https://github.com/ppweek/zhipu-web-search.git
cd zhipu-web-search
pip install -r requirements.txt
```

### 2. 配置

获取 API Key：[智谱 AI 开放平台](https://open.bigmodel.cn/)

```bash
export ZHIPU_API_KEY="sk-xxxxxxxx"
```

### 3. 使用

```bash
# 基础搜索
python3 scripts/search.py "人工智能最新进展"

# 指定模型
python3 scripts/search.py --model glm-4 "深度分析量子计算"

# JSON 输出
python3 scripts/search.py --raw "比特币价格"
```

---

## 📊 性能对比

| 特性 | Zhipu Web Search | Kimi Web Search |
|-----|-----------------|-----------------|
| **响应速度** | ⚡ 极快 | 中等 |
| **成本** | 💰 更低 | 略高 |
| **搜索触发** | 智能判断 | 强制搜索 |
| **中文支持** | 🇨🇳 优秀 | 优秀 |
| **模型选择** | 多档可选 | 有限 |

---

## 🏗️ 项目亮点

- ✅ **完整测试覆盖** - 单元测试 + CI/CD
- ✅ **开源规范** - MIT 许可证，欢迎贡献
- ✅ **详细文档** - API 文档、贡献指南齐全
- ✅ **持续维护** - 活跃开发，快速响应 Issue

---

## 🙋‍♂️ 谁应该使用？

- **OpenClaw 用户** - 扩展 AI 助手的联网能力
- **开发者** - 需要集成搜索功能的应用
- **数据分析师** - 快速获取实时市场信息
- **内容创作者** - 追踪热点话题和趋势

---

## 🔗 相关链接

- 📦 **GitHub 仓库**: https://github.com/ppweek/zhipu-web-search
- 📖 **使用文档**: [README.md](https://github.com/ppweek/zhipu-web-search#readme)
- 🐛 **问题反馈**: [Issues](https://github.com/ppweek/zhipu-web-search/issues)
- 💬 **讨论交流**: [Discussions](https://github.com/ppweek/zhipu-web-search/discussions)

---

## 🙏 致谢

感谢 [智谱 AI](https://www.zhipuai.cn/) 提供强大的大模型 API

感谢 [OpenClaw](https://github.com/openclaw/openclaw) 社区的支持

---

## 📜 许可证

本项目采用 [MIT](LICENSE) 许可证开源

---

<p align="center">
  <b>🌟 如果这个项目对你有帮助，请给我们一个 Star！</b>
</p>

<p align="center">
  <a href="https://github.com/ppweek/zhipu-web-search">⭐ Star on GitHub</a>
</p>
