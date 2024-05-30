
# Treasury Wallet Tracker

This repository contains two scripts for tracking the balances of multiple Ethereum addresses holding a specific ERC-20 token. The scripts can either output the balance information locally or send it to a Telegram bot.

## Scripts

1. **treasury_wallet_tracker_local.py**: Outputs balance information to the local console.
2. **treasury_wallet_tracker_telegram.py**: Sends balance information to a Telegram bot.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.6 or higher
- Git

## Setting Up Your Environment

### For Windows

1. **Install Python**:
   - Download the installer from the [Python website](https://www.python.org/downloads/).
   - Run the installer and follow the instructions. Make sure to check the option to add Python to your PATH.

2. **Install Git**:
   - Download the installer from the [Git website](https://git-scm.com/download/win).
   - Run the installer and follow the instructions.

### For macOS

1. **Install Python**:
   - Open Terminal.
   - Install Homebrew if you don't have it already:

     ```sh
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```

   - Install Python using Homebrew:

     ```sh
     brew install python
     ```

2. **Install Git**:
   - Git is usually pre-installed on macOS. To verify, open Terminal and type:

     ```sh
     git --version
     ```

   - If not installed, install it using Homebrew:

     ```sh
     brew install git
     ```

### For Linux

1. **Install Python**:
   - Open Terminal.
   - Use your package manager to install Python. For example, on Debian-based systems:

     ```sh
     sudo apt update
     sudo apt install python3 python3-pip
     ```

2. **Install Git**:
   - Use your package manager to install Git. For example, on Debian-based systems:

     ```sh
     sudo apt install git
     ```

## Cloning the Repository

1. **Clone the repository**:
   - Open your terminal or command prompt.
   - Run the following command to clone the repository:

     ```sh
     git clone https://github.com/AbstractLogiaca/Aggregated-Wallet-Tracker-ETH.git
     ```

   - Navigate into the cloned directory:

     ```sh
     cd Aggregated-Wallet-Tracker-ETH
     ```

## Installing Dependencies

1. **Create a virtual environment** (optional but recommended):

   ```sh
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - On Windows:

     ```sh
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```sh
     source venv/bin/activate
     ```

3. **Install required Python packages**:

   ```sh
   pip install -r requirements.txt
   ```

## Configuring the Scripts

### treasury_wallet_tracker_local.py

1. **Open the script** in a text editor.
2. **Replace placeholders**:
   - `YOUR_ETH_RPC_URL`: Replace with your RPC provider URL.
   - `ERC20_CONTRACT_ADDRESS`: Replace with the ERC-20 token contract address.
   - Populate the `addresses` array with the Ethereum addresses you want to track.

### treasury_wallet_tracker_telegram.py

1. **Open the script** in a text editor.
2. **Replace placeholders**:
   - `YOUR_ETH_RPC_URL`: Replace with your RPC provider URL.
   - `ERC20_CONTRACT_ADDRESS`: Replace with the ERC-20 token contract address.
   - `YOUR_TELEGRAM_BOT_TOKEN`: Replace with the token you received from `BotFather`.
   - Populate the `addresses` array with the Ethereum addresses you want to track.

## Running the Scripts

### Running treasury_wallet_tracker_local.py

1. **Navigate to the project directory** if not already there:

   ```sh
   cd Aggregated-Wallet-Tracker-ETH
   ```

2. **Run the script**:

   ```sh
   python treasury_wallet_tracker_local.py
   ```

### Running treasury_wallet_tracker_telegram.py

1. **Navigate to the project directory** if not already there:

   ```sh
   cd Aggregated-Wallet-Tracker-ETH
   ```

2. **Run the script**:

   ```sh
   python treasury_wallet_tracker_telegram.py
   ```

3. **Interact with the bot**:
   - Open Telegram and search for your bot.
   - Start a chat with the bot and press the "Update Balance" button to fetch and display the balance information.

## Scripts Overview

### treasury_wallet_tracker_local.py

This script:
- Connects to an Ethereum or ETH Layer 2 provider.
- Fetches balances of specified Ethereum addresses for a given ERC-20 token.
- Retrieves the current token price from Uniswap.
- Calculates the combined token balance and its value in USD.
- Outputs the balance information to the local console.

### treasury_wallet_tracker_telegram.py

This script:
- Connects to an Ethereum or ETH Layer 2 provider.
- Fetches balances of specified Ethereum addresses for a given ERC-20 token.
- Retrieves the current token price from Uniswap.
- Calculates the combined token balance and its value in USD.
- Sends the balance information to a Telegram bot and allows users to update the balance information by pressing a button.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements.

## License

This project is licensed under the MIT License.
