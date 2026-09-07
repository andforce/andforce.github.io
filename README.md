# App 隐私政策站点

用于托管各 App 的隐私政策、使用条款和技术支持页面。采用纯静态 HTML，无需安装前端依赖或执行构建。

## 现有页面

| 页面 | 路径 |
| --- | --- |
| 政策目录首页 | `/` |
| 掌上梁山隐私政策（中英文） | `/apps/liangshan/privacy.html` |
| 掌上梁山技术支持（中英文） | `/apps/liangshan/` |
| HumanBrain 隐私政策（中英文） | `/apps/humanbrain/privacy.html` |
| HumanBrain 技术支持（中英文） | `/apps/humanbrain/` |
| 通用隐私政策 | `/apps/app-privacy-policy.html` |
| 通用隐私政策（不收集数据） | `/apps/app-privacy-policy-no-data.html` |
| 既有中文隐私政策 | `/privacy.html` |
| 既有英文隐私政策 | `/privacy_app.html` |
| 既有中文使用条款 | `/terms_of_use.html` |
| 既有英文使用条款 | `/terms_of_use_app.html` |

上述既有页面的路径和正文均保留，避免影响 App 或商店页面中已经配置的链接。中英文页面分别维护，不应假定内容完全对应。

## 新增 App

1. 在 `apps/` 下创建使用小写字母和连字符命名的目录，例如 `apps/my-app/`。
2. 添加 `privacy.html`；如需技术支持或使用条款，可添加 `index.html`、`terms.html`。专属样式和图片放在同一目录。
3. 根据该 App 的实际情况填写政策内容、联系信息和生效日期。
4. 在根目录 `index.html` 添加该 App 的页面链接。

新页面的政策网址示例：`https://andforce.github.io/apps/my-app/privacy.html`。发布后保持路径稳定。

## 本地预览

需要 Python 3，在仓库根目录执行：

```bash
./run-dev.sh
```

打开 <http://127.0.0.1:8000>。可用 `PORT=8080 ./run-dev.sh` 更换端口，按 `Ctrl+C` 停止服务。

## 静态托管

仓库根目录可以直接作为 GitHub Pages 的发布目录，`.nojekyll` 用于跳过 Jekyll 处理。无需构建产物或后端服务。

旧博客文章、归档、主题资源以及与本站无关的脚本、代理和配置文件已移除，需要时可从 Git 历史查找。
