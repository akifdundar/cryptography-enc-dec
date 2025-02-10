# Confidential Single-Price Auction

## About
The Confidential Single-Price Auction package is an implementation of a privacy-preserving auction mechanism using Fully Homomorphic Encryption (FHE) across the auction platform. The TFHE library is deployed on auction contracts to encrypt bid amounts and related data.

It is a single Hardhat project with an integrated CLI (via the hardhat task system) that allows users to deploy and interact with fully encrypted auctions on a local Zama node.

## Encryption Scope
- Bid amounts: Fully encrypted
- Token allocations: Encrypted
- Auction metadata: Partially visible

## Limitations
- Few modules have been fully converted to FHE
- Test suite complexity limits full node testing
- Large test suites may cause runtime memory constraints
- Some CLI interactions are still under development

## Development Roadmap
Improve the hardhat-fhevm hardhat plug-in to:
- Support multiple nodes
- Enhance CLI for auction creation and management
- Add more comprehensive encryption features
- Test on various networks:
  - Zama's dev node
  - Anvil
  - Hardhat node
- Implement additional auction types
- Expand encryption coverage
- Optimize performance and reduce computational overhead

## Install & Test
### Install
```bash
npm install
```

### Test on hardhat network
```bash
npm run test
```

### Test on local fhevm node (very slow)
```bash
npm run test:fhevm
```

### Local FHEVM Node Management
```bash
# starts a new local node (if not already running)
npm run start

# stops the running local node
npm run stop

# restart a running local node
npm run restart
```

## How to Use the Confidential Auction
### Setup an Auction (slow)
The new auction address is displayed at the end of the deployment process.

```bash
npx hardhat --network fhevm auction setup --mint 1000 --unpause
# --mint option to distribute tokens to all participants
# --unpause option to activate the auction
# --help to list all available commands
```

### Inspect the Latest Deployed Auction
```bash
npx hardhat --network fhevm auction show
```

### Wallet and Auction Aliases
Instead of using addresses, you can execute CLI commands using wallet aliases. 
Auction address is optional. If not provided, the CLI will use the latest valid deployed auction.

```bash
# Use auction address
npx hardhat --network fhevm auction bid \
  --auction 0x3Aa5ebB10DC797CAC828524e59A333d0A371443c \
  --user alice \
  --amount 10n

# Resolve auction address automatically
npx hardhat --network fhevm auction bid \
  --user alice \
  --amount 10n
```

## Test Wallets and Roles
| Name | Wallet Index | Wallet Aliases | Role | Note |
|------|--------------|----------------|------|------|
| 🚀 Admin | 0 | admin | Auction Creator | Owner of AuctionFactory |
| 👨‍🚀 Seller | 1 | seller | Auction Seller | Creates and manages auctions |
| 👩 Bidder 1 | 5 | alice | Auction Participant | Can submit encrypted bids |
| 👱🏼‍♂️ Bidder 2 | 6 | bob | Auction Participant | Can submit encrypted bids |
| 👱🏼‍♂️ Bidder 3 | 7 | charlie | Auction Participant | Can submit encrypted bids |

## The 🚧 hardhat-fhevm 🚧 npm package
Uses the hardhat-fhevm hardhat plugin to develop Solidity contracts on Zama's FHEVM. 
Supports both mock and local node modes. Currently in alpha testing.

- NPM: https://www.npmjs.com/package/hardhat-fhevm
- Git: https://github.com/0xalexbel/hardhat-fhevm

## Detailed Limitations
- For debugging, events emit encrypted handles
- Some CLI commands are incomplete
- Performance overhead due to homomorphic encryption
- Not all auction modules fully converted to FHE

## License
[Specify your license]

## Disclaimer
This is a research prototype. Extensive security review recommended before production use.

---

Built with ❤️ using Zama's FHEVM
