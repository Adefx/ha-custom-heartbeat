import logging
from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.event import async_track_time_interval
from homeassistant.helpers.aiohttp_client import async_get_clientsession

DOMAIN = "heartbeat_push"
_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.data.setdefault(DOMAIN, {})

    url = entry.data.get("url_heartbeat")
    interval = entry.data.get("interval", 5)

    session = async_get_clientsession(hass)

    async def send_heartbeat(now=None):
        try:
            async with session.get(url, ssl=False) as response:
                if response.status >= 400:
                    _LOGGER.warning("Heartbeat Push: error %s on %s", response.status, url)
                else:
                    _LOGGER.debug("Heartbeat Push: sent succesfully to %s", url)
        except Exception as e:
            _LOGGER.error("Heartbeat Push: connection timeout on %s (%s)", url, e)

    hass.async_create_task(send_heartbeat())

    remove_listener = async_track_time_interval(
        hass, send_heartbeat, timedelta(minutes=interval)
    )

    hass.data[DOMAIN][entry.entry_id] = remove_listener

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    remove_listener = hass.data[DOMAIN].pop(entry.entry_id)
    remove_listener()
    return True