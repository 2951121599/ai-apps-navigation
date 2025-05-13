# 如何将您的 AI 应用导航网站部署到 GitHub Pages

GitHub Pages 是一个很棒的免费托管静态网站的服务。以下是如何将您收到的 `index.html` 和 `style.css` 文件部署上去的步骤：

**前提条件：**

*   您需要一个 GitHub 账户。如果您还没有，可以在 [github.com](https://github.com) 免费创建一个。
*   您需要安装 Git。如果您还没有安装，可以从 [git-scm.com](https://git-scm.com/downloads) 下载并安装。

**部署步骤：**

1.  **创建新的 GitHub 仓库 (Repository)：**
    *   登录您的 GitHub 账户。
    *   点击右上角的 "+" 图标，然后选择 "New repository"。
    *   给您的仓库命名。一个常见的命名方式是 `your-username.github.io` (将 `your-username` 替换为您的 GitHub 用户名)。如果您使用这个命名格式，您的网站将可以直接通过 `https://your-username.github.io` 访问。
        *   或者，您可以选择任何其他仓库名称，例如 `ai-apps-navigation`。这种情况下，您的网站将通过 `https://your-username.github.io/repository-name` 访问。
    *   确保仓库是 **Public** (公开的)，因为 GitHub Pages 只为公共仓库提供免费服务（对于私有仓库，您可能需要 GitHub Pro）。
    *   您可以勾选 "Add a README file" (可选，但推荐)。
    *   点击 "Create repository"。

2.  **将您的网站文件上传到仓库：**
    *   **方法一：通过网页上传 (适合少量文件)**
        *   在您新创建的仓库页面，点击 "Add file"按钮，然后选择 "Upload files"。
        *   将您本地的 `index.html` 和 `style.css` 文件拖拽到上传区域，或者点击 "choose your files" 选择它们。
        *   在下方的 "Commit changes" 部分，输入一个提交信息 (例如 "Initial commit of website files")。
        *   点击 "Commit changes"。

    *   **方法二：通过 Git 命令行 (推荐，更灵活)**
        *   在您的电脑上，打开一个文件夹，将 `index.html` 和 `style.css` 文件放入其中。
        *   打开 Git Bash (Windows) 或终端 (macOS/Linux)。
        *   导航到包含您网站文件的文件夹。例如：
            ```bash
            cd path/to/your/website-files
            ```
        *   初始化一个新的 Git 仓库：
            ```bash
            git init
            ```
        *   将您的 GitHub 仓库添加为远程仓库 (将 `your-username` 和 `repository-name` 替换为您的实际信息)：
            ```bash
            git remote add origin https://github.com/your-username/repository-name.git
            ```
        *   将所有文件添加到暂存区：
            ```bash
            git add .
            ```
        *   提交更改：
            ```bash
            git commit -m "Initial commit of website files"
            ```
        *   将更改推送到 GitHub (通常主分支是 `main` 或 `master`，请根据您的仓库情况调整)：
            ```bash
            git branch -M main  # 如果您的默认分支不是 main，可以重命名为 main
            git push -u origin main
            ```

3.  **启用 GitHub Pages：**
    *   在您的 GitHub 仓库页面，点击顶部的 "Settings" 标签。
    *   在左侧导航栏中，找到并点击 "Pages" (在 "Code and automation" 部分下)。
    *   在 "Build and deployment" 部分下的 "Source"，选择 "Deploy from a branch"。
    *   在 "Branch" 部分，选择您上传文件的分支 (通常是 `main` 或 `master`)，并将文件夹选择为 `/(root)`。
    *   点击 "Save"。

4.  **访问您的网站：**
    *   GitHub Pages 可能需要几分钟来构建和部署您的网站。
    *   部署完成后，您会在 GitHub Pages 设置页面顶部看到一个绿色的提示框，显示 "Your site is live at [your-site-url]"。
    *   点击该链接即可访问您的 AI 应用导航网站！
        *   如果您的仓库名为 `your-username.github.io`，网址将是 `https://your-username.github.io`。
        *   如果您的仓库名为其他名称 (例如 `ai-apps-navigation`)，网址将是 `https://your-username.github.io/ai-apps-navigation`。

**更新您的网站：**

如果您将来需要更新网站内容 (例如，修改 `index.html` 或 `style.css`)：

*   **通过网页上传：** 在仓库中找到相应的文件，点击它，然后点击铅笔图标进行编辑，或者删除旧文件并重新上传新版本。
*   **通过 Git 命令行：** 在本地修改文件后，重复以下命令：
    ```bash
    git add .
    git commit -m "Update website content"  # 替换为您的提交信息
    git push origin main
    ```
    GitHub Pages 会自动检测到更改并重新部署您的网站。

如果您在部署过程中遇到任何问题，可以随时向我提问。

