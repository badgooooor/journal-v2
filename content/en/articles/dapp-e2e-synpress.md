---
title: Make dApp testing automated with Synpress
description: "Make dApp testing more consistent, less painful"
published: 2025/01/15
slug: "dapp-e2e-synpress"
ogImage: https://images.yuttakhanb.dev/synpress-banner.webp
tags:
  - frontend
  - end-to-end testing
  - d-app
  - synpress
  - playwright
  - short-note
---

**tl:dr;**

In this read, you will get insights on:

- Problem on end-to-end testing in dApp, especially on implementing interaction with extensions
- Key points on using synpress in order to interact with wallet extension in browser e.g. wallet setup and interaction
- Result from end-to-end testing and some tips I found during implementing tests which should make life better

---

Testing is a process that is essential to ensure that software works as expected. In the state of web3 tooling, testing tools are well provided in both smart contracts (e.g., Hardhat and Foundry) and backend, which is even more straightforward.

For frontend application? This goes a bit different due to these reasons

- Implementing end-to-end testing is burdensome since you need to interact with wallet extension e.g. sending transaction, switch network. Even worse for some interaction e.g. setup wallet which requires to do in every test, results a really long flow for testing and debugging if it breaks
- Integration tests in the components requires to mock many parts. In this case, you need to mock not only components that is not interested in the test case but also mock interaction with chains e.g. changes on transaction submitted or failed.
  This results less confidence on tests that mocks components.

I did bit research on end-to-end testing during Q3 in 2024 since I hopped back to web3 career and found that there’s still some hope for this. So let’s introduce 🥁….

## Synpress

Synpress has been around for a while, but it got a major update in November that made it even better. It now works perfectly with Playwright (a testing tool), and I'd like to share what I learned while using it for testing.

### 1. Wallet setup

Setting up wallets for testing used to be a big challenge. With the latest version of Synpress, you can set up a wallet by writing the configuration in a single file. The best part is that these wallet settings are saved (cached) automatically, so you don't need to set them up again for each test. This makes testing much faster since all the setup work is done just once at the beginning.

Here is some sample code for wallet setup:

```typescript
import { defineWalletSetup } from "@synthetixio/synpress";
import { MetaMask } from "@synthetixio/synpress/playwright";
import "dotenv/config";

const SEED_PHRASE =
  "test test test test test test test test test test test junk";
const PASSWORD = "SynpressIsAwesomeNow!!!";

const TEST_NETWORK_RPC_URL = `${
  process.env.E2E_TEST_NETWORK_RPC_URL ?? ""
}:8545`;
const TEST_NETWORK_CHAIN_ID = process.env.E2E_TEST_NETWORK_CHAIN_ID;

const TEST_WALLET_PRIVATE_KEY = process.env.E2E_TEST_ACCOUNT_PRIVATE_KEY;
export const TEST_WALLET_ADDRESS = process.env.E2E_TEST_ACCOUNT_ADDRESS;

export default defineWalletSetup(PASSWORD, async (context, walletPage) => {
  // Initialize metamask and unlock wallet
  const metamask = new MetaMask(context, walletPage, PASSWORD);

  // Add wallet with seed phrase
  // NOTE: In metamask it is needed to add seed phrase wallet first
  await metamask.importWallet(SEED_PHRASE);

  // Importing wallets
  await metamask.importWalletFromPrivateKey(TEST_WALLET_PRIVATE_KEY);

  // Add networks
  await metamask.addNetwork({
    name: "OP Mainnet",
    rpcUrl: "https://1rpc.io/op",
    chainId: Number(10),
    symbol: "ETH",
  });

  await metamask.addNetwork({
    name: "Test network",
    rpcUrl: TEST_NETWORK_RPC_URL,
    chainId: Number(TEST_NETWORK_CHAIN_ID),
    symbol: "ETH",
  });
});
```

In order to invoke setup script, you can use command npx synpress <directory where setup file in> to start it.

![Setup wallet with synpress](https://images.yuttakhanb.dev/synpress-setup.png)

### 2. Wallet interaction

In order to interact with wallet in the test, it requires to create test fixture for using in the test with `mergeTests`. Here is some simple test.

```typescript
import { testWithSynpress } from "@synthetixio/synpress";
import { MetaMask, metaMaskFixtures } from "@synthetixio/synpress/playwright";
import { mergeTests } from "@playwright/test";
import { test as testWithSerenity } from "@serenity-js/playwright-test";
import basicSetup, { TEST_WALLET_ADDRESS } from "./wallet-setup/basic.setup";

const test = mergeTests(
  testWithSynpress(metaMaskFixtures(basicSetup)),
  testWithSerenity
);

const { describe } = test;

test("should able to connect wallet", async ({
    context,
    page,
    metamaskPage,
    extensionId,
  }) => {
    const metamask = new MetaMask(
      context,
      metamaskPage,
      basicSetup.walletPassword,
      extensionId
    );

		metamask.switchNetwork("Test network");

    await page.goto("/");

    await page.getByTestId("connect-wallet-dropdown-trigger").click();
    await page.getByTestId("connect-wallet-dropdown-metaMaskSDK").click();

    await metamask.connectToDapp();
    // other interactions in the test bla bla blah ...
  };
```

![Test cases in action so that you can be chill.](https://images.yuttakhanb.dev/synpress-run.png)

![As you can see in the timeline, Metamask tab will be opened and interact directly.](https://images.yuttakhanb.dev/synpress-metamask-interaction.webp)

Synpress provide 2 types of fixture for interactions, the Metamask wallet and EthereumWalletMock which simulates interaction of wallet without using blockchain. I think Metamask adapter could work for most test cases. Even it’s flaky at few times, that makes me spending less time on retesting when codebase changes.

## Perspective on implementing full end-to-end testing with these stuff

I think it is already stated since the beginning that mocking modules for tests is tedious tasks. With updated Synpress which improves quality-of-life on implementing and running tests, it is a perfect solution. With this, I only need to mock API response for some cases that is really needed.

For latest application on product that is in my current workplace, is tested with all of these mentioned libraries (Playwright and synpress) and also applied screenplay testing using serenity-js. I wish I could showcase real implementation but for now, you can read more on screenplay testing here.

[Screenplay Pattern Testing with Serenity.js](https://yuttakhanb.dev/posts/screenplay-serenity/)

I believe that with good test strategies and consistent automated tests, these can ensure that the application will work correctly and shipped to the user with less defects. Also testing landscape is even more evolved than before that end-to-end testing can even easier to implement (and have less cost).

And that’s all about what’ve tried during last month. I hope this blog has covered everything you need to know about Synpress. You can have a visit at official documentation and examples in Github repository. If you have any sharing thoughts, please comment or contact on my social networks.
