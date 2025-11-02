
from labjack import ljm
from enum import Enum
from typing import Union
from pydantic import BaseModel, Field

class Loop(BaseModel):
    
    port: str = Field(
        title="Port",
        description="The port for this loop",
        default="AIN0"
        )
    resistance: float = Field(
        title="resistance",
        description="The total resistance value for this loop in ohms",
        default=250
        )
    voltage_upper_bound: float = Field(
        title="Curent Upper Bound",
        description="The upper bound for the current input in mA",
        default=10
        )
    voltage_lower_bound: float = Field(
        title="Curent Lower Bound",
        description="The lower bound for the current input in mA",
        default=0.25
        )
class LabJackConnectionType(str, Enum):
   WIFI =  "WIFI"  # short codes for common LS design tags
   USB = "USB"
   TCP = "TCP"
   ETHERNET = "ETHERNET"
   ANY = "ANY"

class LabJackVersion(str, Enum):
   T7 =  "T7"  # short codes for common LS design tags
   T8 = "T8"
   T4 = "T4"
   ANY = "ANY"

        

class LabJack:

    def __init__(self, loops: dict[str, Loop], version: LabJackVersion, connection_type: LabJackConnectionType, device_id: str = "ANY"):
        self.handle = ljm.openS(version.value, connection_type.value, device_id)
        self.loops = loops
   
    def close_handle(self):         # Close connection
        ljm.close(self.handle)
        
    def read_voltage(self, loop_name: str):
        voltage = ljm.eReadName(self.handle, self.loops[loop_name].port)
        return voltage
    
    def read_percentage(self, loop_name: str):
        target_loop = self.loops[loop_name]

        voltage = ljm.eReadName(self.handle, target_loop.port)
        
        percentage = 100 * (voltage - target_loop.voltage_lower_bound) / (target_loop.voltage_upper_bound - target_loop.voltage_lower_bound)
        return percentage
    


    