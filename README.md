# 🔐 Confidential Single-Price Auction System

## 🌟 Project Overview

This project implements a cutting-edge Confidential Single-Price Auction system leveraging Zama's Fully Homomorphic Encryption Virtual Machine (fhEVM), providing unprecedented privacy and fairness in token auctions.

## 🚀 Key Features

- **End-to-End Encryption**: Sealed bids with complete confidentiality
- **Fair Price Discovery**: Lowest price mechanism for token allocation
- **Flexible Auction Mechanics**: Support for various token types and auction parameters
- **Privacy-Preserving**: Encrypted bid submissions and settlements

## 🛠 Technical Architecture

### Components
- **AuctionFactory.sol**: Dynamic auction creation contract
- **Auction.sol**: Core auction mechanics and bid management
- **MockERC20.sol**: Test token implementation

### Privacy Layers
- Homomorphic encryption of bid amounts
- Zero-knowledge proof validation
- Secure multiparty computation

## 📦 Installation & Setup

### Prerequisites
- Node.js (v20+)
- Hardhat
- Zama fhEVM SDK

### Install Dependencies
```bash
npm install
```

### Environment Configuration
1. Copy `.env.example` to `.env`
2. Fill in required environment variables

## 🧪 Testing

### Run Tests
```bash
# Run on Hardhat network
npx hardhat test

# Run on local fhEVM node
npx hardhat test:fhevm
```

## 🚀 Deployment

### Deploy to Sepolia Testnet
```bash
npx hardhat deploy --network sepolia
```

## 🎯 Auction Workflow

1. **Auction Creation**: Seller defines auction parameters
2. **Bid Submission**: Participants submit encrypted bids
3. **Bid Validation**: Cryptographic verification of bids
4. **Settlement**: Lowest price determines token allocation

## 🔍 Limitations & Considerations

- **Encryption Scope**: 
  - Bid amounts fully encrypted
  - Auction metadata partially visible
- **Performance**: Homomorphic encryption introduces computational overhead

## 🌐 Supported Networks
- Sepolia Testnet
- Zama fhEVM Coprocessor
- Local Hardhat Network

## 🛡️ Security Considerations

- Comprehensive encryption of sensitive auction data
- Zero-knowledge proof mechanisms
- Secure bid submission and settlement

## 🚧 Development Roadmap

1. Enhanced multi-token support
2. Cross-chain compatibility
3. Additional privacy features
4. Performance optimizations

## 📋 CLI Interactions (Planned)

```bash
# Create new auction
npx hardhat auction:create --title "Rare Digital Art" --supply 100 --duration 7200

# Submit encrypted bid
npx hardhat auction:bid --auction-id <ID> --amount <ENCRYPTED_AMOUNT>

# Finalize auction
npx hardhat auction:finalize --auction-id <ID>
```

## 🤝 Contributing

### Guidelines
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push and create a Pull Request

### Bug Reports
- Use GitHub Issues
- Provide detailed description
- Include reproduction steps

## 📜 License

[Specify your license here]

## 🙏 Acknowledgements

- **Zama Team**: For the incredible fhEVM technology
- **Ethereum Community**: Continuous innovation inspiration
- **Privacy Advocates**: Driving decentralized solutions

## 💬 Contact

- **Email**: [your-project-email]
- **Discord**: [Invite Link]
- **Twitter**: [@YourProjectHandle]

---

**Disclaimer**: This is a research prototype. Extensive security review recommended for production use.

<div align="center">
  <img src="https://img.shields.io/badge/Built%20with-%E2%9D%A4%EF%B8%8F-red?style=for-the-badge" alt="Built with Love"/>
</div>
