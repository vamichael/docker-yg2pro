"""Support for isy994mrf lights."""
import logging
from typing import Callable

from homeassistant.components.light import DOMAIN, SUPPORT_BRIGHTNESS, Light
from homeassistant.helpers.typing import ConfigType

from . import isy994mrf_NODES, ISYDevice

_LOGGER = logging.getLogger(__name__)


def setup_platform(hass, config: ConfigType,
                   add_entities: Callable[[list], None], discovery_info=None):
    """Set up the isy994mrf light platform."""
    devices = []
    for node in hass.data[isy994mrf_NODES][DOMAIN]:
        devices.append(ISYLightDevice(node))

    add_entities(devices)


class ISYLightDevice(ISYDevice, Light):
    """Representation of an isy994mrf light device."""

    @property
    def is_on(self) -> bool:
        """Get whether the isy994mrf light is on."""
        if self.is_unknown():
            return False
        return self.value != 0

    @property
    def brightness(self) -> float:
        """Get the brightness of the isy994mrf light."""
        return None if self.is_unknown() else self.value

    def turn_off(self, **kwargs) -> None:
        """Send the turn off command to the isy994mrf light device."""
        if not self._node.off():
            _LOGGER.debug("Unable to turn off light")

    # pylint: disable=arguments-differ
    def turn_on(self, brightness=None, **kwargs) -> None:
        """Send the turn on command to the isy994mrf light device."""
        if not self._node.on(val=brightness):
            _LOGGER.debug("Unable to turn on light")

    @property
    def supported_features(self):
        """Flag supported features."""
        return SUPPORT_BRIGHTNESS
