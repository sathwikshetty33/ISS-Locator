# ISS-Locator

This Python project sends an email notification when the International Space Station (ISS) is directly above you during nighttime. It utilizes the ISS API to track the position of the ISS and the Sunrise-Sunset API to determine if it's dark outside.

## Features

- Monitors the position of the ISS in real-time.
- Checks local sunrise and sunset times to determine if it's nighttime.
- Sends an email alert when the ISS is directly overhead at night.

## Prerequisites

- Python 3.x
- An email account (e.g., Gmail) for sending notifications
- Required Python libraries:
  - `requests`
  - `smtplib` (built-in)
