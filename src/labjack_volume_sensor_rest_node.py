
from madsci.common.types.action_types import (
    ActionResult,
    ActionSucceeded,
    ActionFailed
)
from madsci.common.types.node_types import RestNodeConfig
from madsci.node_module.helpers import action
from madsci.node_module.rest_node_module import RestNode
from labjack_interface import Loop, LabJack, LabJackConnectionType, LabJackVersion
from pathlib import Path


class LabJackVolumeSensorConfig(RestNodeConfig):
    """Configuration for a LabJack volume sensor node"""
    loops: dict[Loop] = {"AIN0": Loop()}

    total_volume: float = 113.56
    """Total volume of the container in liters """

    volume_units: str = "liters"
    """Units used for the volume"""

    labjack_version: LabJackVersion = "T7"
    """Version of LabJack used"""

    labjack_connection_type: LabJackConnectionType = "ANY"
    """type of connection used by the LabJack"""

    device_id: str = "ANY"
    """ID of the LabJack device to connect to"""





    


class LabJackVolumeSensorNode(RestNode):
    """Node Module Implementation for the Big Kahuna Instruments"""

    config_model = LabJackVolumeSensorConfig
    def startup_handler(self):
        self.labjack = LabJack(self.config.loops, self.config.labjack_version, self.config.connection_type, self.config.device_id)
        
    def state_handler(self):
        volumes = {}
        for loop in self.config.loops.keys():
           
            percentage = self.labjack.read_percentage(loop)
            volumes[loop] = (percentage/100)*self.config.total_volume
        self.node_state = {"volumes": volumes, "units": self.config.volume_units}
        return super().state_handler()

   
if __name__ == "__main__":
    ljvs_node = LabJackVolumeSensorNode()
    ljvs_node.start_node()