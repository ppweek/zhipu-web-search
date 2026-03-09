#!/usr/bin/env python3
"""
智谱 AI Web Search Tool
使用智谱 AI API 的 web_search 工具进行联网搜索

Usage:
    python3 search.py "搜索关键词"
    python3 search.py "快手 2025年3月 最新财报"

Environment:
    ZHIPU_API_KEY: 智谱 AI API Key
"""

import os
import sys
import json
from typing import Dict, Any, Optional

try:
    from zhipuai import ZhipuAI
except ImportError:
    print("Error: zhipuai package not installed. Run: pip install zhipuai")
    sys.exit(1)


def get_api_key() -> str:
    """获取智谱 AI API Key"""
    api_key = os.environ.get("ZHIPU_API_KEY")
    if not api_key:
        # 尝试从配置文件读取
        config_paths = [
            os.path.expanduser("~/.config/zhipuai/api_key"),
            os.path.expanduser("~/.openclaw/credentials/zhipuai-api-key"),
        ]
        for path in config_paths:
            if os.path.exists(path):
                with open(path, "r") as f:
                    api_key = f.read().strip()
                    if api_key:
                        break
    
    if not api_key:
        print("Error: ZHIPU_API_KEY not found. Please set it as environment variable or in config file.")
        print("You can get API key from: https://open.bigmodel.cn/")
        sys.exit(1)
    
    return api_key


def search(
    query: str, 
    model: str = "glm-4-flash",
    enable_search: bool = True,
    search_query: Optional[str] = None
) -> Dict[str, Any]:
    """
    使用智谱 AI web_search 进行联网搜索
    
    Args:
        query: 用户查询问题
        model: 模型名称，默认使用 glm-4-flash（性价比高）
        enable_search: 是否启用联网搜索
        search_query: 可选，自定义搜索关键词（不设置则使用 query）
    
    Returns:
        包含搜索结果的字典
    """
    client = ZhipuAI(api_key=get_api_key())
    
    # 构建工具配置
    tools = []
    if enable_search:
        tools.append({
            "type": "web_search",
            "web_search": {
                "enable": True,
                # 可选：指定搜索关键词
                # "search_query": search_query or query
            }
        })
    
    # 发送请求
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "你是智谱 AI 助手，擅长使用联网搜索获取最新信息，并提供准确、详细的回答。请尽可能引用搜索结果中的信息。"},
            {"role": "user", "content": query}
        ],
        tools=tools,
        temperature=0.7,
        max_tokens=4096,
    )
    
    # 解析响应
    result = {
        "content": response.choices[0].message.content,
        "model": model,
        "usage": {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens,
        }
    }
    
    # 提取引用信息（如果有）
    message = response.choices[0].message
    if hasattr(message, 'tool_calls') and message.tool_calls:
        result["tool_calls"] = []
        for tc in message.tool_calls:
            result["tool_calls"].append({
                "id": tc.id,
                "type": tc.type,
                "function": {
                    "name": tc.function.name,
                    "arguments": tc.function.arguments
                }
            })
    
    return result


def format_output(result: Dict[str, Any]) -> str:
    """格式化输出搜索结果"""
    output = []
    
    # 主要内容
    output.append("=" * 60)
    output.append("搜索结果")
    output.append("=" * 60)
    output.append("")
    output.append(result["content"])
    output.append("")
    
    # 元信息
    output.append("-" * 60)
    output.append(f"模型: {result['model']}")
    output.append(f"Token 消耗: {result['usage']['total_tokens']} "
                  f"(输入: {result['usage']['prompt_tokens']}, "
                  f"输出: {result['usage']['completion_tokens']})")
    
    return "\n".join(output)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 search.py <query>")
        print('Example: python3 search.py "快手 2025年3月 最新财报"')
        print("")
        print("Environment Variables:")
        print("  ZHIPU_API_KEY    智谱 AI API Key")
        print("")
        print("Options:")
        print("  --model MODEL    指定模型 (default: glm-4-flash)")
        print("  --raw            输出原始 JSON")
        sys.exit(1)
    
    # 解析参数
    args = sys.argv[1:]
    query = None
    model = "glm-4-flash"
    raw_output = False
    
    i = 0
    while i < len(args):
        if args[i] == "--model" and i + 1 < len(args):
            model = args[i + 1]
            i += 2
        elif args[i] == "--raw":
            raw_output = True
            i += 1
        elif query is None:
            query = args[i]
            i += 1
        else:
            query += " " + args[i]
            i += 1
    
    if not query:
        print("Error: No query provided")
        sys.exit(1)
    
    print(f"Searching: {query}", file=sys.stderr)
    print(f"Model: {model}", file=sys.stderr)
    print("", file=sys.stderr)
    
    try:
        result = search(query, model=model)
        
        if raw_output:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(format_output(result))
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
