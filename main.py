from keyPairs import WalletGenerator
import json

if __name__ == "__main__":
    # Instantiate the wallet generator
    generator = WalletGenerator()
    
    # Retrieve all wallets (EVM, Solana) and print them
    result = generator.get_all_wallets()
    print(json.dumps(result, indent=2))