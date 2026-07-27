import platform
import torch

class Config:
    app_title = 'vinux'
    show_os_label = "ОС: "
    show_ver_label = "Версия: "
    show_device_label = f"Устройство: "

    rain_width = 11
    rain_height = 2

    logo = '''\
[#80BCF0]██    ██ ██ ███    ██ ██    ██ ██   ██[/]
[#80BCF0]██    ██ ██ ████   ██ ██    ██  ██ ██[/]
[#4d9fe3]██    ██ ██ ██ ██  ██ ██    ██   ███ [/]
[#0178d4] ██  ██  ██ ██  ██ ██ ██    ██  ██ ██[/]
[#0178d4]  ████   ██ ██   ████  ██████  ██   ██[/]'''
    
    @classmethod
    def get_os_name(cls) -> str:
        system = platform.system()
        if system == "Linux":
            try:
                info = platform.freedesktop_os_release()
                return info.get("NAME", "Linux")
            except AttributeError:
                return "Linux"
        elif system == "Darwin":
            ver = platform.mac_ver()[0]
            return f"macOS {ver}" if ver else "macOS"
        elif system == "Windows":
            release = platform.release()
            version = platform.version()
            if release == "10" and version.startswith("10.0.22"):
                return "Windows 11"
            return f"Windows {release}"
        else:
            return system
        
    @staticmethod
    def get_version():
        return "v1.0.0-alpha"
    
    @staticmethod
    def get_device():
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        return device