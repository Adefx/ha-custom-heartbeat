import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import HomeAssistant

DOMAIN = "heartbeat_push"

class HeartbeatConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        
        if user_input is not None:
            if not user_input["url_heartbeat"].startswith("http"):
                errors["base"] = "invalid_url"
            else:
                # On utilise maintenant le nom saisi par l'utilisateur pour le titre
                return self.async_create_entry(
                    title=user_input["name"], 
                    data=user_input
                )

        # Ajout du champ "name" dans le formulaire
        data_schema = vol.Schema({
            vol.Required("name", default="Heartbeat"): str,
            vol.Required("url_heartbeat", default="https://"): str,
            vol.Required("interval", default=5): int,
        })

        return self.async_show_form(
            step_id="user", data_schema=data_schema, errors=errors
        )