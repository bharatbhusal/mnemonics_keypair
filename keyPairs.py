from mnemonic import Mnemonic
from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes

class WalletGenerator:
    def __init__(self, mnemonic: str = None):
        """Initializes the Wallet Generator with a mnemonic."""
        self.mnemonic = mnemonic or Mnemonic("english").generate(strength=256)
        self.seed_bytes = Bip39SeedGenerator(self.mnemonic).Generate()

    def get_mnemonic(self):
        """Returns the mnemonic."""
        return self.mnemonic
    
    def get_seed_bytes(self):
        """Returns the seed bytes."""
        return self.seed_bytes


    def get_evm_wallet(self):
        bip44_eth = Bip44.FromSeed(self.seed_bytes, Bip44Coins.ETHEREUM)
        acct = bip44_eth.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
        return {
            "chain": "Ethereum",
            "public_key": acct.PublicKey().ToAddress(),
            "private_key": acct.PrivateKey().Raw().ToHex()
        }
    
    def get_polygon_wallet(self):
        bip44_polygon = Bip44.FromSeed(self.seed_bytes, Bip44Coins.POLYGON)
        acct = bip44_polygon.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
        return {
            "chain": "Polygon",
            "public_key": acct.PublicKey().ToAddress(),
            "private_key": acct.PrivateKey().Raw().ToHex()
        }

    def get_solana_wallet(self):
        bip44_solana = Bip44.FromSeed(self.seed_bytes, Bip44Coins.SOLANA)
        acct = bip44_solana.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
        return {
            "chain": "Solana",
            "public_key": acct.PublicKey().ToAddress(),
            "private_key": acct.PrivateKey().Raw().ToHex()
        }

    def get_tron_wallet(self):
        bip44_tron = Bip44.FromSeed(self.seed_bytes, Bip44Coins.TRON)
        acct = bip44_tron.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
        return {
            "chain": "Tron",
            "public_key": acct.PublicKey().ToAddress(),
            "private_key": acct.PrivateKey().Raw().ToHex()
        }
    
    def get_bsc_wallet(self):
        bip44_bsc = Bip44.FromSeed(self.seed_bytes, Bip44Coins.BINANCE_SMART_CHAIN)
        acct = bip44_bsc.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
        return {
            "chain": "BSC",
            "public_key": acct.PublicKey().ToAddress(),
            "private_key": acct.PrivateKey().Raw().ToHex()
        }
    
    def get_all_wallets(self):
        """Returns all wallets (EVM, Solana) along with mnemonic and seed."""
        return {
            "mnemonic": self.get_mnemonic(),
            "wallets": [
                self.get_evm_wallet(),
                self.get_solana_wallet(),
                self.get_bsc_wallet(),
                self.get_tron_wallet(),
                self.get_polygon_wallet(),

            ]
        }
