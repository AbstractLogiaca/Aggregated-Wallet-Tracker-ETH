import requests
from web3 import Web3

# Initialize Web3 connection to the L2 provider
# Replace with your L2 provider URL
rpc = 'YOUR_ETH_PROVIDER_URL'
web3 = Web3(Web3.HTTPProvider(rpc))

# Define the ERC-20 token contract address and ABI
token_contract = 'ERC20_CONTRACT_ADDRESS'
erc20_abi = '''
[
    {
        "constant": true,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "name": "balance",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
]
'''

# Convert contract address to checksum address
token_contract = web3.to_checksum_address(token_contract)

# Initialize the contract
contract = web3.eth.contract(address=token_contract, abi=erc20_abi)

# Verify contract initialization
print(f"Contract initialized: {contract}")

# Define the array of addresses (fill this with as many addresses as needed)
addresses = [
    # '0xYourAddress1',
    # '0xYourAddress2',
    # Add more addresses here
]

def get_balance(address):
    """
    Fetch the balance of the specified address from the ERC-20 contract.
    """
    try:
        balance = contract.functions.balanceOf(web3.to_checksum_address(address)).call()
        return balance
    except Exception as e:
        print(f"Error fetching balance for address {address}: {e}")
        return None

def get_combined_balance():
    """
    Get the combined balance of all specified addresses.
    """
    total_balance = 0
    for address in addresses:
        balance = get_balance(address)
        if balance:
            total_balance += balance
    return total_balance

def get_token_price_from_uniswap(token_address):
    """
    Fetch the current price of the token from Uniswap using The Graph API.
    """
    query = '''
    {
      token(id: "%s") {
        derivedETH
      }
      bundle(id: "1") {
        ethPrice
      }
    }
    ''' % token_address.lower()
    
    url = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
    response = requests.post(url, json={'query': query})
    data = response.json()
    
    eth_price_in_usd = float(data['data']['bundle']['ethPrice'])
    token_price_in_eth = float(data['data']['token']['derivedETH'])
    token_price_in_usd = token_price_in_eth * eth_price_in_usd
    
    return token_price_in_usd

def format_significant_figures(value, significant_figures):
    """
    Format a number to the specified significant figures.
    """
    format_string = f"{{:.{significant_figures}g}}"
    return format_string.format(value)

def fetch_balances():
    """
    Fetch the combined balance of all addresses, the current token price,
    and calculate the combined balance in USD.
    """
    total_balance = get_combined_balance()
    token_price = get_token_price_from_uniswap(token_contract)
    combined_balance_ether = float(Web3.from_wei(total_balance, "ether"))
    combined_balance_usd = combined_balance_ether * token_price
    return combined_balance_ether, token_price, combined_balance_usd

def main():
    """
    Main function to fetch and display balances.
    """
    combined_balance_ether, token_price, combined_balance_usd = fetch_balances()
    formatted_token_price = format_significant_figures(token_price, 4)
    
    print(f'Combined token balance: {combined_balance_ether:.8f} tokens')
    print(f'Current price of the token: ${formatted_token_price} USD')
    print(f'Combined balance in USD: ${combined_balance_usd:.2f} USD')

if __name__ == '__main__':
    main()