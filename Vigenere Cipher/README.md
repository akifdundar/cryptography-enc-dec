# Confidential Single-Price Auction for Tokens with Sealed Bids

## Overview

This project implements a Confidential Single-Price Auction system using Zama's Fully Homomorphic Encryption Virtual Machine (fhEVM). The auction allows for sealed, encrypted bids while maintaining privacy and fairness in the token sale process.

## 🏆 Zama fhEVM Bounty Submission

### Challenge Requirements

This implementation addresses the Zama fhEVM Bounty challenge by creating a single-price auction with the following key features:
- Encrypted bid submissions
- Confidential bidding process
- Fair price determination
- Flexible auction mechanics

## 🔐 Key Features

### Confidentiality
- Bids are encrypted using fhEVM, ensuring bidder privacy
- Sealed bid mechanism prevents bid manipulation
- Encrypted state variables protect sensitive auction information

### Auction Mechanics
- Single-price settlement (lowest price to clear all tokens)
- Supports both ETH and ERC20 token auctions
- Flexible auction configuration

## 📋 Detailed Specification

### Auction Initialization
- Auction creator can specify:
  - Total token quantity
  - Auction duration
  - Payment token (ETH or ERC20)
  - Minimum bid requirements

### Bidding Process
- Participants submit encrypted bids
- Bids include:
  - Number of tokens requested
  - Price per token
- Encrypted bid validation
- Prevention of duplicate or invalid bids

### Settlement Mechanism
- Tokens allocated based on bid prices
- Settlement price determined by the lowest bid that clears all tokens
- Partial allocations supported
- Unsold tokens handled through configurable mechanisms

## 🛠 Technical Implementation

### Smart Contracts
- Developed in Solidity
- Compatible with Zama's fhEVM on Sepolia testnet
- Utilizes Zama's encryption libraries

### Encrypted State Variables
- Bid amounts
- Token allocations
- Participant identities

### Edge Case Handling
- Multiple bid submissions
- Bid modification before auction end
- Insufficient funds prevention
- Equal lowest bid resolution

## 🧪 Testing

### Hardhat Test Suite
- Comprehensive unit tests
- Integration tests
- Edge case scenario testing

### Test Coverage
- Bid submission
- Auction settlement
- Error handling
- Encryption mechanisms

## 🚀 Deployment

### Supported Networks
- Sepolia Testnet
- Zama fhEVM Coprocessor

### Deployment Scripts
- Hardhat deployment configuration
- Network-specific deployment support

## 🔍 Additional Features

### Optional Enhancements
- Auction factory model
- React frontend integration
- Customizable asset auction

## 📦 Installation

### Prerequisites
- Node.js (v18+)
- Hardhat
- Zama fhEVM SDK

### Setup
```bash
git clone https://github.com/your-username/confidential-auction.git
cd confidential-auction
npm install
```

### Deployment
```bash
npx hardhat deploy --network sepolia
```

## 🤝 Contributing

Contributions are welcome! Please read our contributing guidelines and code of conduct.

## 📄 License

[Specify your license here]

## 💬 Contact

For questions or support, please open an issue or contact [your contact information]

## 🏅 Zama Bounty Submission

Submitted for the Zama fhEVM Confidential Auction Bounty
- Submission Date: February 9, 2025
- Challenge Requirements: Fully Addressed
- Privacy and Confidentiality: Maximized through fhEVM

---

**Disclaimer**: This implementation is a submission for the Zama fhEVM Bounty and should be considered a prototype. Extensive security audits are recommended before production use.
