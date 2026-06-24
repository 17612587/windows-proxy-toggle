# Proxy On-Off

Windows 桌面快捷方式，一键切换系统代理开关。

## 文件说明

| 文件 | 说明 |
|------|------|
| `toggle_proxy.py` | 核心切换脚本，通过修改注册表控制 Windows 系统代理 |
| `toggle_proxy.vbs` | 无窗口调用器，双击快捷方式时不会弹出黑框 |
| `Proxy On-Off.lnk` | 桌面快捷方式，双击即可切换代理 |

---

## 一、下载项目到本地

### 方法一：下载 ZIP（推荐小白使用）

1. 打开项目页面：https://github.com/17612587/windows-proxy-toggle
2. 点击绿色的 **Code** 按钮
3. 点击 **Download ZIP**
4. 下载完成后，解压 ZIP 文件到任意文件夹（例如桌面）

### 方法二：使用 Git 克隆（适合有 Git 环境的用户）

```bash
git clone https://github.com/17612587/windows-proxy-toggle.git
```

---

## 二、修改代理地址

用记事本打开 `toggle_proxy.py`，找到这一行：

```python
# 这里是代理地址，格式：host:port（例如 127.0.0.1:7890）
PROXY_SERVER = '****'
```

将 `****` 替换为你的代理地址，例如：

```python
PROXY_SERVER = '127.0.0.1:7890'
```

> 如果你不知道代理地址，可以问你的网络管理员，或者在代理软件（如 Clash、v2rayN 等）的设置里查看。

保存并关闭文件。

---

## 三、创建桌面快捷方式

1. 进入解压后的文件夹
2. 找到 `toggle_proxy.vbs` 文件
3. 右键点击 `toggle_proxy.vbs` → **创建快捷方式**
4. 将生成的快捷方式（`toggle_proxy.lnk`）**剪切**并**粘贴到桌面**
5. （可选）重命名快捷方式为 `Proxy On-Off`

---

## 四、使用方式

双击桌面上的 `Proxy On-Off` 快捷方式：

- **当前代理是关闭状态** → 自动打开代理，弹出提示：`代理已打开\n地址：你的代理地址`
- **当前代理是打开状态** → 自动关闭代理，弹出提示：`代理已关闭\n地址：你的代理地址`

---

## 五、迁移到其他电脑

将整个文件夹复制到新电脑，然后重复 **第三步（创建桌面快捷方式）** 即可。

---

## 注意事项

- 修改的是当前用户的系统代理设置（`HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings`）。
- 脚本会自动刷新 WinINet 设置，浏览器等应用会立即生效。
- 需要安装 Python 环境（下载地址：https://www.python.org/downloads/），安装时请勾选 **Add Python to PATH**。

## 免责声明

本工具仅用于方便切换个人系统代理，请确保你使用的代理服务符合当地法律法规。
