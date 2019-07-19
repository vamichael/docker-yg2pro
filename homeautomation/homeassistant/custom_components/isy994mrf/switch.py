"""Support for isy994mrf switches."""
import logging
from typing import Callable

from homeassistant.components.switch import DOMAIN, SwitchDevice
from homeassistant.helpers.typing import ConfigType

from . import isy994mrf_NODES, isy994mrf_PROGRAMS, ISYDevice

_LOGGER = logging.getLogger(__name__)


def setup_platform(hass, config: ConfigType,
                   add_entities: Callable[[list], None], discovery_info=None):
    """Set up the isy994mrf switch platform."""
    devices = []
    for node in hass.data[isy994mrf_NODES][DOMAIN]:
        if not node.dimmable:
            devices.append(ISYSwitchDevice(node))

    for name, status, actions in hass.data[isy994mrf_PROGRAMS][DOMAIN]:
        devices.append(ISYSwitchProgram(name, status, actions))

    add_entities(devices)


class ISYSwitchDevice(ISYDevice, SwitchDevice):
    """Representation of an isy994mrf switch device."""

    @property
    def is_on(self) -> bool:
        """Get whether the isy994mrf device is in the on state."""
        return bool(self.value)

    def turn_off(self, **kwargs) -> None:
        """Send the turn on command to the isy994mrf switch."""
        if not self._node.off():
            _LOGGER.debug('Unable to turn on switch.')

    def turn_on(self, **kwargs) -> None:
        """Send the turn off command to the isy994mrf switch."""
        if not self._node.on():
            _LOGGER.debug('Unable to turn on switch.')


class ISYSwitchProgram(ISYSwitchDevice):
    """A representation of an isy994mrf program switch."""

    def __init__(self, name: str, node, actions) -> None:
        """Initialize the isy994mrf switch program."""
        super().__init__(node)
        self._name = name
        self._actions = actions

    @property
    def is_on(self) -> bool:
        """Get whether the isy994mrf switch program is on."""
        return bool(self.value)

    def turn_on(self, **kwargs) -> None:
        """Send the turn on command to the isy994mrf switch program."""
        if not self._actions.runThen():
            _LOGGER.error('Unable to turn on switch')

    def turn_off(self, **kwargs) -> None:
        """Send the turn off command to the isy994mrf switch program."""
        if not self._actions.runElse():
            _LOGGER.error('Unable to turn off switch')
