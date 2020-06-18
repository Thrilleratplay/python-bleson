from bleson.core.types import Advertisement, BDAddress
from bleson.interfaces.adapter import Adapter
import threading

class BluetoothAdapter(Adapter):

    def __init__(self, device_id=0):
        self.on_advertising_data = None

    def open(self):
        pass

    def on(self):
        pass

    def off(self):
        pass

    def start_scanning(self):
        threading.Timer(0.5, self._send_dummy_advertising).start()

    def stop_scanning(self):
        pass

    def start_advertising(self, advertisement, scan_response=None):
        pass

    def stop_advertising(self):
        pass

    def _on_advertising_data(self, data):
        pass

    def _send_dummy_advertising(self):
        advertisement = Advertisement()
        advertisement.flags = 0
        advertisement.rssi = 123
        advertisement.address = BDAddress('b1:eb:1e:b1:eb:1e')
        advertisement.name = 'Stub'
        advertisement.tx_pwr_lvl = 1
        if self.on_advertising_data:
            self.on_advertising_data(advertisement)