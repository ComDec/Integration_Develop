# Integration_Develop

Repo for setting a integration code develop process

## Before commit your branch

### Pytest

Pytest支持快速检测代码的正确性

Cheat Sheet

- 使用pytest -v执行所有测试文件。
- 使用pytest <filename> -v执行特定文件。
- 通过子串匹配执行测试 pytest -k <子串> -v.
- 基于标记执行测试 pytest -m -v.
- 使用@pytest.fixture创建夹具。
- conftest.py允许从多个文件访问固定装置。
- 使用@pytest.mark.parametrize对测试进行参数化。
- 使用@pytest.mark.xfail.Xfail测试失败。
- 使用@pytest.mark.skip跳过测试。
- 使用pytest --maxfail = <num>在n次失败时停止测试执行。
- 使用pytest -n <num>并行运行测试。
- 使用pytest -v –junitxml = “result.xml “生成结果xml。

该仓库提供了Handbook以供学习。

### pyproject.toml

### Pre-commit

Cheat Sheet

`pre-commit install`

`pre-commit run --all-files`

## After commit

### CI/CD

CI/CD 是一种通过在应用开发阶段引入自动化来频繁向客户交付应用的方法。CI/CD 的核心概念是持续集成、持续交付和持续部署。

https://img-blog.csdnimg.cn/img_convert/d1f6ccae8cc21c4ddf9cd1d1e481bae3.png
