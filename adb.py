from adb_shell.adb_device import AdbDeviceTcp
from adb_shell.auth.keygen import keygen
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
from adb_shell.exceptions import AdbTimeoutError, AdbConnectionError
import os


class ADB:
    def __init__(self, host='127.0.0.1'):
        self.host = host
        self.device = None
        self.adbkey_path = 'adbkey'
        self._setup_keys()

    def _setup_keys(self):
        if not os.path.exists(self.adbkey_path):
            keygen(self.adbkey_path)
        with open(self.adbkey_path, 'r') as f:
            priv = f.read()
        with open(self.adbkey_path + '.pub', 'r') as f:
            pub = f.read()
        self.signer = PythonRSASigner(pub, priv)

    def connect(self, port):
        try:
            self.device = AdbDeviceTcp(self.host, int(
                port), default_transport_timeout_s=9.)
            self.device.connect(rsa_keys=[self.signer], auth_timeout_s=0.1)
            return self.device.available, '连接成功'
        except (AdbTimeoutError, AdbConnectionError, ConnectionRefusedError) as e:
            return False, str(e)

    def take_screenshot(self, filename='screenshot.png'):
        if not self.device or not self.device.available:
            return False, "设备未连接"

        try:
            # 在设备上保存截图
            self.device.shell('screencap -p /sdcard/screenshot.png')

            # 从设备拉取截图到本地
            self.device.pull('/sdcard/screenshot.png', filename)
            return True, filename
        except Exception as e:
            return False, str(e)
