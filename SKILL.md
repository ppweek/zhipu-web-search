---
name: zhipu-web-search
description: 使用智谱 AI API 的 web_search 工具进行联网搜索。当需要搜索最新信息、新闻、实时数据时使用此技能。支持中文搜索，返回带引用的搜索结果。
---

# 智谱 AI 联网搜索技能

本技能使用智谱 AI API 的 `web_search` 工具实现联网搜索功能。

## 工作原理

智谱 AI 的联网搜索通过 Tools 机制实现：
1. 在请求中声明 `web_search` 工具
2. 模型自动判断是否需要搜索
3. 执行搜索并返回带引用的结果

## 使用方法

### 方式一：使用脚本（推荐）

```bash
python3 ~/.openclaw/skills/zhipu-web-search/scripts/search.py "搜索关键词"
```

### 方式二：直接调用智谱 AI API

```python
from zhipuai import ZhipuAI

client = ZhipuAI(api_key="your-api-key")

response = client.chat.completions.create(
    model="glm-4-flash",
    messages=[
        {"role": "user", "content": "搜索最新科技新闻"}
    ],
    tools=[{
        "type": "web_search",
        "web_search": {"enable": True}
    }]
)

print(response.choices[0].message.content)
```

## 环境变量

- `ZHIPU_API_KEY`：智谱 AI API Key（必需）
  - 获取地址：https://open.bigmodel.cn/

## 支持的模型

| 模型 | 说明 | 推荐度 |
|-----|------|-------|
| `glm-4-flash` | 轻量级，速度快，成本低 | ⭐⭐⭐⭐⭐ |
| `glm-4` | 标准版，综合能力好 | ⭐⭐⭐⭐ |
| `glm-4-plus` | 增强版，能力更强 | ⭐⭐⭐⭐ |

## 示例

搜索最新新闻：
```bash
python3 scripts/search.py "快手 2025年3月 最新财报"
```

使用特定模型：
```bash
python3 scripts/search.py --model glm-4 "人工智能最新进展"
```

输出原始 JSON：
```bash
python3 scripts/search.py --raw "比特币价格"
```

## 与 Kimi 搜索的对比

| 特性 | 智谱 AI | Kimi |
|-----|---------|------|
| 搜索触发 | 模型自动判断 | 强制搜索（通过 tool_calls） |
| 结果引用 | 支持引用标注 | 支持 |
| 价格 | 按 token 计费 | 搜索额外 ¥0.03/次 |
| 速度 | 快 | 中等 |
| 中文支持 | 优秀 | 优秀 |

## 注意事项

1. **模型选择**：推荐使用 `glm-4-flash`，性价比高
2. **搜索触发**：智谱 AI 会智能判断是否需要搜索，不是所有查询都会触发
3. **Token 消耗**：搜索结果会计入 prompt_tokens
4. **引用格式**：结果中可能包含 `[^index^]` 格式的引用标记

## 依赖安装

```bash
pip install zhipuai
```
