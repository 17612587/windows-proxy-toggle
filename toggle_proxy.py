import winreg
import ctypes
import sys

KEY_PATH = r'Software\Microsoft\Windows\CurrentVersion\Internet Settings'
# 这里是代理地址，格式：host:port（例如 127.0.0.1:7890）
PROXY_SERVER = '****'

def show_message(message):
    """Show a simple Windows message box."""
    ctypes.windll.user32.MessageBoxW(0, message, 'Proxy On-Off', 0x40 | 0x00)

def main():
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, KEY_PATH) as key:
            try:
                enabled, _ = winreg.QueryValueEx(key, 'ProxyEnable')
            except FileNotFoundError:
                enabled = 0
            try:
                current_server, _ = winreg.QueryValueEx(key, 'ProxyServer')
            except FileNotFoundError:
                current_server = ''

        new_state = 1 if enabled == 0 else 0

        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, KEY_PATH, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, 'ProxyEnable', 0, winreg.REG_DWORD, new_state)
            if new_state == 1:
                winreg.SetValueEx(key, 'ProxyServer', 0, winreg.REG_SZ, PROXY_SERVER)

        # Refresh WinINet settings so apps pick up the change immediately
        INTERNET_OPTION_SETTINGS_CHANGED = 39
        INTERNET_OPTION_REFRESH = 37
        ctypes.windll.wininet.InternetSetOptionW(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)
        ctypes.windll.wininet.InternetSetOptionW(0, INTERNET_OPTION_REFRESH, 0, 0)

        server_to_show = PROXY_SERVER if new_state == 1 else current_server
        if new_state == 1:
            message = f'代理已打开\n地址：{server_to_show}'
        else:
            message = f'代理已关闭\n地址：{server_to_show}'
        show_message(message)
    except Exception as e:
        show_message(f'切换失败：{e}')
        sys.exit(1)

if __name__ == '__main__':
    main()
