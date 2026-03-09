#!/usr/bin/env python3
"""
智谱 AI Web Search Skill 单元测试
"""

import os
import sys
import unittest
from unittest.mock import Mock, patch, MagicMock

# 添加脚本路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from search import get_api_key, search, format_output


class TestGetApiKey(unittest.TestCase):
    """测试 API Key 获取"""
    
    def setUp(self):
        # 保存原始环境变量
        self.original_env = os.environ.get('ZHIPU_API_KEY')
    
    def tearDown(self):
        # 恢复环境变量
        if self.original_env:
            os.environ['ZHIPU_API_KEY'] = self.original_env
        elif 'ZHIPU_API_KEY' in os.environ:
            del os.environ['ZHIPU_API_KEY']
    
    @patch.dict(os.environ, {'ZHIPU_API_KEY': 'test-key-from-env'})
    def test_get_api_key_from_env(self):
        """测试从环境变量获取 API Key"""
        key = get_api_key()
        self.assertEqual(key, 'test-key-from-env')
    
    @patch('os.path.exists')
    @patch('builtins.open', unittest.mock.mock_open(read_data='test-key-from-file'))
    def test_get_api_key_from_file(self):
        """测试从配置文件获取 API Key"""
        # 清除环境变量
        if 'ZHIPU_API_KEY' in os.environ:
            del os.environ['ZHIPU_API_KEY']
        
        with patch('os.path.exists', return_value=True):
            key = get_api_key()
            self.assertEqual(key, 'test-key-from-file')


class TestFormatOutput(unittest.TestCase):
    """测试输出格式化"""
    
    def test_format_output(self):
        """测试格式化输出"""
        result = {
            "content": "测试内容",
            "model": "glm-4-flash",
            "usage": {
                "prompt_tokens": 100,
                "completion_tokens": 50,
                "total_tokens": 150
            }
        }
        
        output = format_output(result)
        
        self.assertIn("测试结果", output)
        self.assertIn("glm-4-flash", output)
        self.assertIn("150", output)
        self.assertIn("测试内容", output)


class TestSearch(unittest.TestCase):
    """测试搜索功能"""
    
    @patch('search.ZhipuAI')
    def test_search_success(self, mock_zhipuai):
        """测试搜索成功"""
        # 模拟 API 响应
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "搜索结果"
        mock_response.usage.prompt_tokens = 100
        mock_response.usage.completion_tokens = 50
        mock_response.usage.total_tokens = 150
        
        mock_client.chat.completions.create.return_value = mock_response
        mock_zhipuai.return_value = mock_client
        
        with patch.dict(os.environ, {'ZHIPU_API_KEY': 'test-key'}):
            result = search("测试查询")
            
            self.assertEqual(result["content"], "搜索结果")
            self.assertEqual(result["model"], "glm-4-flash")
            self.assertEqual(result["usage"]["total_tokens"], 150)


if __name__ == '__main__':
    unittest.main()
