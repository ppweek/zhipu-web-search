# 贡献指南

感谢你对 Zhipu Web Search Skill 的兴趣！以下是参与贡献的指南。

## 开发环境设置

```bash
# 克隆仓库
git clone https://github.com/yourusername/zhipu-web-search.git
cd zhipu-web-search

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
pip install -r requirements-dev.txt

# 运行测试
pytest tests/
```

## 代码规范

- 遵循 PEP 8 规范
- 使用类型注解
- 编写 docstring
- 保持测试覆盖率 > 80%

## 提交规范

```
<type>(<scope>): <subject>

<body>

<footer>
```

类型：
- `feat`: 新功能
- `fix`: 修复
- `docs`: 文档
- `style`: 格式
- `refactor`: 重构
- `test`: 测试
- `chore`: 构建/工具

## Pull Request 流程

1. Fork 仓库
2. 创建分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'feat: add amazing feature'`)
4. 推送分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

## 报告问题

请使用 Issue 模板，包含：
- 问题描述
- 复现步骤
- 期望行为
- 环境信息
