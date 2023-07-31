# Pub-Sub System

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Pub-Sub system template using Python and Redis for communication between publishers and subscribers.

## Overview

The Pub-Sub System is a simple Python project that demonstrates the implementation of a publish-subscribe messaging pattern using Redis as the message broker. This system allows publishers to send messages to specific channels, and subscribers can receive messages from those channels.

## Features

- Publish messages to channels.
- Subscribe to channels and receive messages.
- Redis as the message broker for communication.

## Requirements

- Python 3.x
- Redis (should be installed and running)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/IbLahlou/pub-sub-system.git
   cd pub-sub-system
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure that Redis is installed and running on your system. If you don't have it installed, you can use the provided installation script (`install_redis.bat` for Windows or `install_redis.sh` for Linux/Unix) to install Redis via Chocolatey (Windows) or APT/YUM (Linux).

## Usage

1. Start the Redis server:

   ```bash
   # Windows (with Chocolatey)
   .\install_redis.bat

   # Linux/Unix (with APT)
   ./install_redis.sh
   ```

2. Run the main script to start the Pub-Sub system:

   ```bash
   python main.py
   ```

3. The system will start the Redis server, demonstrate message publishing, and show how subscribers receive messages.

4. Feel free to extend and use this template in your projects.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Acknowledgments

Special thanks to OpenAI for creating the GPT-3.5-based language model used to generate this README.md file 