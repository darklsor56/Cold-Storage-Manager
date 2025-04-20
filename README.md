# Cold Storage Manager

A tool to scan your Linux drives for unused files and move them to a cold storage drive to reduce wear and optimize space.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Features

- Scans a drive for unused files based on last access time
- Moves files to cold storage in a mirrored folder structure
- Supports scheduled operation via cron
- Designed for use on Ubuntu Linux servers

## Getting Started

1. Clone the repo
2. Edit `config/settings.yaml` with your drive paths and thresholds
3. Run `main.py` manually or schedule with `cron`

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](./LICENSE) file for details.
