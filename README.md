# Cold Storage Manager

A tool to scan your Linux drives for unused files and move them to a cold storage drive to reduce wear and optimize space.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Features


- Scans for unused files based on last access time
- Moves files to cold storage with mirrored directory structure
- Configurable with a YAML file
- CLI interface (`coldstore`)
- Cron-compatible for scheduled runs
- Built for Ubuntu Linux servers

## Getting Started

```bash
# Clone the repository
git clone https://github.com/your-username/Cold-Storage-Manager.git
cd Cold-Storage-Manager

# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install the project and dependencies
pip install -e .

# Optionally install dev tools (like pylint)
pip install pylint

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](./LICENSE) file for details.
