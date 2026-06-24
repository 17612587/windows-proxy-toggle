# Proxy On-Off

Windows 桌面快捷方式，一键切换系统代理开关。

## 文件说明

| 文件 | 说明 |
|------|------|
| `toggle_proxy.py` | 核心切换脚本，通过修改注册表控制 Windows 系统代理 |
| `toggle_proxy.vbs` | 无窗口调用器，双击快捷方式时不会弹出黑框 |
| `Proxy On-Off.lnk` | 桌面快捷方式，双击即可切换代理 |

## 使用方法

1. 克隆仓库到本地：
   ```bash
   git clone https://github.com/17612587/windows-proxy-toggle.git
   ```

2. 修改 `toggle_proxy.py` 中的代理地址：
   ```python
   # 这里是代理地址，格式：host:port（例如 127.0.0.1:7890）
   PROXY_SERVER = '****'
   ```
   将 `****` 替换为你的代理地址，例如 `127.0.0.1:7890`。

3. 双击 `Proxy On-Off.lnk`，即可在"打开代理"和"关闭代理"之间切换。

4. 切换成功后会弹出提示框：
   - 打开代理：`代理已打开\n地址：xxx.xxx.xxx:xxxx`
   - 关闭代理：`代理已关闭\n地址：xxx.xxx.xxx:xxxx`

## 首次使用或迁移到其他电脑

如果 `Proxy On-Off.lnk` 无法正常工作，可以重新创建快捷方式：

1. 右键 `toggle_proxy.vbs` → **创建快捷方式**。
2. 将生成的快捷方式拖到桌面。
3. 右键快捷方式 → **属性** → **图标** → 选择喜欢的图标。

## 手动运行脚本

也可以直接双击 `toggle_proxy.vbs` 运行，不会显示命令行窗口。

## 注意事项

- 修改的是当前用户的系统代理设置（`HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings`）。
- 脚本会自动刷新 WinINet 设置，浏览器等应用会立即生效。
- 需要安装 Python 环境，并确保 `pyw` 或 `pythonw` 在系统 PATH 中。

## 免责声明

本工具仅用于方便切换个人系统代理，请确保你使用的代理服务符合当地法律法规。
