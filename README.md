# 🔐 Multi-Chain Wallet Generator in Python

This Python project allows you to generate deterministic wallets (public/private key pairs) for multiple blockchains using a **single mnemonic (seed phrase)**. It supports major blockchains including:

- Ethereum
- Binance Smart Chain (BSC)
- Polygon
- Solana
- Tron

## 🚀 Features

- Generates a secure **BIP-39** mnemonic phrase.
- Derives wallet addresses using **BIP-44** paths.
- Returns **public** and **private keys** for each supported chain.
- Supports adding more chains easily by modifying the class.

## 🛠️ Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

### Dependencies

- `bip_utils`
- `mnemonic`

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
```

## 📁 Project Structure

```
mnemonics_keypair/
├── keyPairs.py          # Core logic for generating wallets
├── main.py              # Entry point to run and print wallets
├── requirements.txt     # Python dependencies
└── README.md            # You're reading it!
```

## 📦 Usage

Run the project:

```bash
python main.py
```

Sample output:

```json
{
  "mnemonic": "spirit toast basket ...",
  "wallets": [
    {
      "chain": "Ethereum",
      "public_key": "0x...",
      "private_key": "..."
    },
    ...
  ]
}
```

## 📚 Extending Support

To add support for more chains (like Bitcoin, Cosmos, TON), update `keyPairs.py` using supported coins from the `bip_utils.Bip44Coins` enum.

## ⚠️ Security Warning

- Do not share your mnemonic or private keys.
- Use this code **only for educational or testing purposes**.
- For production, integrate with secure key management solutions like hardware wallets or HSMs.