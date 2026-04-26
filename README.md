# 💓 Custom Heartbeat for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)
[![Maintainer](https://img.shields.io/badge/Maintained_by-You-blue?style=for-the-badge)](#)

A lightweight, 100% UI-based integration for **Home Assistant** to send a regular life signal (Heartbeat / Ping) to external monitoring services like **Uptime Kuma**, **Healthchecks.io**, or **UptimeRobot**.

Stop messing with complex automations or YAML files: configure your pings directly from the graphical interface!

## ✨ Features

- 🖥️ **100% UI Configuration (Config Flow)**: No YAML coding required.
- ⏱️ **Customizable Interval**: Choose the exact time (in minutes) between each request.
- 🏷️ **Customizable Name**: Useful if you have multiple instances (e.g., "Kuma Living Room", "Healthchecks NAS").
- 🪶 **Ultra Lightweight**: Uses Home Assistant's native async HTTP client (`aiohttp`) for near-zero resource consumption.
- 🌐 **GET Method**: Perfectly suited for Uptime Kuma ("Push" monitors).

---

## 📥 Installation

### Step 1: Download via HACS (Recommended)

This integration can be easily added via [HACS](https://hacs.xyz/). 

1. Open Home Assistant and navigate to **HACS** > **Integrations**.
2. Click the 3 dots in the top right corner and choose **Custom repositories**.
3. Add the URL of this GitHub repository and choose the category **Integration**.
4. Click **Add**, then search for "Custom Heartbeat" and download it.
5. **Restart Home Assistant** (Mandatory).
6. **Clear your browser cache** (`Ctrl` + `F5` or `Cmd` + `Shift` + `R`).

### Step 2: Add to Home Assistant

Once downloaded and your Home Assistant restarted, you can click the button below to add the integration directly, or do it manually via *Settings > Devices & Services > Add Integration*.

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=heartbeat_push)

*(Note: The integration is named "Custom Heartbeat" in the list).*

---

## ⚙️ Configuration

When adding the integration, you will be prompted for 3 fields:

1. **Instance Name**: The display name in your interface (e.g., `Ping Uptime Kuma`).
2. **Heartbeat Push Url**: The full URL provided by your monitoring service (must start with `http://` or `https://`).
   - *Example Uptime Kuma: `https://uptime.yourdomain.com/api/push/yoursecretcode?status=up&msg=OK&ping=`*
3. **Heartbeat Interval (in min.)**: The wait time between each request (e.g., `5` for 5 minutes).

---

## 🗑️ Uninstallation

To remove a Heartbeat, simply go to **Settings > Devices & Services**, find your "Custom Heartbeat" integration, click the 3 little dots, and select **Delete**. The background task will stop immediately and cleanly.

---
*Created with ❤️ for the Home Assistant community.*
