# API 文档

## 智谱 AI Web Search API

### 基础信息

- **Base URL**: `https://open.bigmodel.cn/api/paas/v4/`
- **认证方式**: API Key（Header: `Authorization: Bearer {api_key}`）
- **文档**: https://open.bigmodel.cn/dev/api

### 搜索接口

#### 请求

```http
POST /chat/completions
Content-Type: application/json
Authorization: Bearer {api_key}
```

```json
{
  "model": "glm-4-flash",
  "messages": [
    {"role": "system", "content": "你是智谱 AI 助手..."},
    {"role": "user", "content": "搜索关键词"}
  ],
  "tools": [
    {
      "type": "web_search",
      "web_search": {
        "enable": true
      }
    }
  ],
  "temperature": 0.7,
  "max_tokens": 4096
}
```

#### 响应

```json
{
  "id": "chatcmpl-xxx",
  "object": "chat.completion",
  "created": 1234567890,
  "model": "glm-4-flash",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "搜索结果内容..."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 100,
    "completion_tokens": 200,
    "total_tokens": 300
  }
}
```

### 模型列表

| 模型 | 上下文长度 | 特点 |
|-----|-----------|------|
| glm-4-flash | 128K | 轻量级，速度快 |
| glm-4 | 128K | 标准版 |
| glm-4-plus | 128K | 增强版 |

### 错误码

| 错误码 | 说明 |
|-------|------|
| 401 | 认证失败，API Key 无效或过期 |
| 429 | 请求过于频繁 |
| 500 | 服务器内部错误 |

### 价格

- 按 Token 计费
- 输入/输出价格不同
- 具体价格请参考官方定价页
