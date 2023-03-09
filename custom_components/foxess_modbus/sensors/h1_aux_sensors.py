"""Inverter sensor"""
import logging
from datetime import time

from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.components.sensor import SensorStateClass

from ..const import MODBUS
from .modbus_sensor import ModbusSensor
from .sensor_desc import SensorDescription

_LOGGER: logging.Logger = logging.getLogger(__package__)

SENSORS: dict[str, SensorDescription] = {
    "pv1_voltage": SensorDescription(
        key="pv1_voltage",
        address=11000,
        name="PV1 Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        scale=0.1,
    ),
    "pv1_current": SensorDescription(
        key="pv1_current",
        address=11001,
        name="PV1 Current",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        scale=0.1,
    ),
    "pv1_power": SensorDescription(
        key="pv1_power",
        address=11002,
        name="PV1 Power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
    ),
    "pv2_voltage": SensorDescription(
        key="pv2_voltage",
        address=11003,
        name="PV2 Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        scale=0.1,
    ),
    "pv2_current": SensorDescription(
        key="pv2_current",
        address=11004,
        name="PV2 Current",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        scale=0.1,
    ),
    "pv2_power": SensorDescription(
        key="pv2_power",
        address=11005,
        name="PV2 Power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
    ),
    "battery_soc": SensorDescription(
        key="battery_soc",
        address=11036,
        name="Battery SoC",
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="%",
    ),
    "battery_discharge": SensorDescription(
        key="battery_discharge",
        address=11008,
        name="Battery Discharge",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        post_process=lambda v: v if v > 0 else 0,
    ),
    "battery_charge": SensorDescription(
        key="battery_charge",
        address=11008,
        name="Battery Charge",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        post_process=lambda v: abs(v) if v < 0 else 0,
    ),
    "feed_in": SensorDescription(
        key="feed_in",
        address=11021,
        name="Feed In",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        post_process=lambda v: v if v > 0 else 0,
    ),
    "grid_consumption": SensorDescription(
        key="grid_consumption",
        address=11021,
        name="Grid Consumption",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        post_process=lambda v: abs(v) if v < 0 else 0,
    ),
    "battery_temp": SensorDescription(
        key="battery_temp",
        address=11038,
        name="Battery Temp",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        scale=0.1,
    ),
    "invtemp": SensorDescription(
        key="invtemp",
        address=11025,
        name="Inverter Temp",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        scale=0.1,
    ),
    "ambtemp": SensorDescription(
        key="ambtemp",
        address=11024,
        name="Ambient Temp",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        scale=0.1,
    ),
    "load_power": SensorDescription(
        key="load_power",
        address=11023,
        name="Load Power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
    ),
    "invbatvolt": SensorDescription(
        key="invbatvolt",
        address=11006,
        name="Inverter Battery Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        scale=0.1,
    ),
    "invbatpower": SensorDescription(
        key="invbatpower",
        address=11007,
        name="Inverter Battery Power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.01,
    ),
    "grid_ct": SensorDescription(
        key="grid_ct",
        address=11021,
        name="Grid CT",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
    ),
    "batvolt": SensorDescription(
        key="batvolt",
        address=11034,
        name="Battery Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        scale=0.1,
    ),
    "bat_current": SensorDescription(
        key="bat_current",
        address=11035,
        name="Battery Current",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        scale=0.1,
    ),
    "rvolt": SensorDescription(
        key="rvolt",
        address=11009,
        name="Grid Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        scale=0.1,
    ),
    "rcurrent": SensorDescription(
        key="rcurrent",
        address=11010,
        name="Grid Current",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        scale=0.1,
    ),
    "rfreq": SensorDescription(
        key="rfreq",
        address=11014,
        name="Grid Frequency",
        device_class=SensorDeviceClass.FREQUENCY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="Hz",
        scale=0.01,
    ),
    "eps_rvolt": SensorDescription(
        key="eps_rvolt",
        address=11015,
        name="EPS Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        scale=0.1,
    ),
    "ct2_meter": SensorDescription(
        key="ct2_meter",
        address=11022,
        name="CT2 Meter",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
    ),
    "bms_watthours_total": SensorDescription(
        key="bms_watthours_total",
        address=11049,
        name="BMS Watthours Total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kWh",
        scale=0.1,
    ),
    "min_soc": SensorDescription(
        key="min_soc",
        address=41009,
        name="Min SoC",
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="%",
    ),
    "min_soc_on_grid": SensorDescription(
        key="min_soc_on_grid",
        address=41011,
        name="Min SoC (On Grid)",
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="%",
    ),
    "max_soc": SensorDescription(
        key="max_soc",
        address=41010,
        name="Max SoC",
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="%",
    ),
    "time_period_1_start": SensorDescription(
        key="time_period_1_start",
        address=41002,
        name="Period 1 - Start",
        post_process=lambda v: time(hour=(v // 256), minute=v - ((v // 256) * 256)),
    ),
    "time_period_1_end": SensorDescription(
        key="time_period_1_end",
        address=41003,
        name="Period 1 - End",
        post_process=lambda v: time(hour=(v // 256), minute=v - ((v // 256) * 256)),
    ),
    "time_period_2_start": SensorDescription(
        key="time_period_2_start",
        address=41005,
        name="Period 2 - Start",
        post_process=lambda v: time(hour=(v // 256), minute=v - ((v // 256) * 256)),
    ),
    "time_period_2_end": SensorDescription(
        key="time_period_2_end",
        address=41006,
        name="Period 2 - End",
        post_process=lambda v: time(hour=(v // 256), minute=v - ((v // 256) * 256)),
    ),
    "bms_cell_mv_high": SensorDescription(
        key="bms_cell_mv_high",
        address=11045,
        name="BMS Cell mV High",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="mV",
    ),
    "bms_cell_mv_low": SensorDescription(
        key="bms_cell_mv_low",
        address=11046,
        name="BMS Cell mV Low",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="mV",
    ),
    "bms_charge_rate": SensorDescription(
        key="bms_charge_rate",
        address=11041,
        name="BMS Charge Rate",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        scale=0.1,
    ),
    "bms_discharge_rate": SensorDescription(
        key="bms_discharge_rate",
        address=11042,
        name="BMS Discharge Rate",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        scale=0.1,
    ),
    "bms_cell_temp_high": SensorDescription(
        key="bms_cell_temp_high",
        address=11043,
        name="BMS Cell Temp High",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        scale=0.1,
    ),
    "bms_cell_temp_low": SensorDescription(
        key="bms_cell_temp_low",
        address=11044,
        name="BMS Cell Temp Low",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        scale=0.1,
    ),
    "bms_kwh_remaining": SensorDescription(
        key="bms_kwh_remaining",
        address=11037,
        name="BMS kW Remaining",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kWh",
        scale=0.01,
    ),
    "bms_cycle_count": SensorDescription(
        key="bms_cycle_count",
        address=11048,
        name="BMS Cycle Count",
        state_class=SensorStateClass.MEASUREMENT,
    ),
}


def sensors(controllers, entry, friendly_name) -> list:
    """Setup sensor platform."""
    entities = []

    for sensor in SENSORS:
        sen = ModbusSensor(controllers[MODBUS], SENSORS[sensor], entry, friendly_name)
        entities.append(sen)

    return entities
