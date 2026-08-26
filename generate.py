#!/usr/bin/env python3
"""
Airdrop Content Site Generator — builds a static SEO site with articles
about active airdrops (data hardcoded from research 2026-08-08).
Deploy to GitHub Pages for free hosting. Monetize via AdSense later.
"""
import os, json, datetime

OUT = os.path.join(os.path.dirname(__file__), "site")

ARTICLES = [
    {
        "slug": "orbinum-airdrop-guide",
        "title": "Orbinum Network Airdrop Guide 2026: How to Farm ORB Credits (20M ORB Pool)",
        "date": "2026-08-08",
        "tags": ["testnet", "zk", "confirmed"],
        "body": [
            ("h2", "What is Orbinum?"),
            ("p", "Orbinum is a privacy-focused Layer 1 blockchain built on Substrate with EVM compatibility. It uses ZK shielded pools (Groth16 on BN254) to hide sender, recipient and amount by default."),
            ("h2", "Airdrop details"),
            ("p", "Orbinum has confirmed an airdrop: Season 1 'Genesis Community' allocates 20,000,000 ORB (2% of total supply). ORB Credits earned during the season convert proportionally at snapshot, taken 14 days before mainnet (Q4 2026). No vesting."),
            ("h2", "How to participate"),
            ("p", "1) Connect wallet at app.orbinum.network. 2) Link Discord, Telegram and X for a 20-credit bonus. 3) Add testnet: Chain ID 2700, RPC https://rpc-1.testnet.orbinum.io. 4) Claim testnet ORB from faucet. 5) Complete daily on-chain quests: Shield, Private Transfer, Unshield, Selective Disclosure."),
            ("h2", "Key facts"),
            ("p", "Testnet live since July 16, 2026. TGE planned Q4 2026 (Oct-Dec). Streak multiplier up to 1.5x on testnet quests. 10 credits per verified referral. Snapshot is 14 days before mainnet launch — activity after that does not count."),
        ],
    },
    {
        "slug": "rax-finance-waitlist-guide",
        "title": "RAX Finance Airdrop Guide: Join the Waitlist &amp; Earn Points",
        "date": "2026-08-08",
        "tags": ["ai", "waitlist", "potential"],
        "body": [
            ("h2", "What is RAX Finance?"),
            ("p", "RAX Finance is an AI + DePIN infrastructure project backed by HashKey Capital, FBG Capital and DePIN X. Total raised: $4M."),
            ("h2", "Airdrop status"),
            ("p", "Potential airdrop (TBA). Points accumulated on the waitlist influence future allocation. Levels go up to 4; higher level = more rewards."),
            ("h2", "How to join"),
            ("p", "1) Go to app.rax.finance/waitlist, connect your wallet and email. 2) Complete tasks and invite friends to raise your level. 3) New: daily GPU Price Prediction rounds on Telegram (08:00-09:00 UTC), 2x points if correct."),
            ("h2", "Why participate"),
            ("p", "Free to join. Waitlist started January 2026; points farming is still open. Backed by tier-1 VCs."),
        ],
    },
    {
        "slug": "action-model-points-guide",
        "title": "Action Model Airdrop: Earn Points by Training AI Agents (Confirmed)",
        "date": "2026-08-08",
        "tags": ["ai", "confirmed", "extension"],
        "body": [
            ("h2", "What is Action Model?"),
            ("p", "Action Model is a platform for training AI agents. Airdrop is confirmed (date TBA). Users earn points via browser extension, quests and ActionFi tasks."),
            ("h2", "How to farm points"),
            ("p", "1) Register at join.actionmodel.com. 2) Install the browser extension — it earns points while you browse. 3) Complete daily check-ins in Quests. 4) Do ActionFi tasks for multiplier points."),
            ("h2", "Ambassador program"),
            ("p", "Applications open at actionmodel.com/ambassadors. Ambassadors get exclusive rewards, early access and community roles."),
        ],
    },
    {
        "slug": "monad-testnet-airdrop-guide",
        "title": "Monad Airdrop: What Actually Happened (Mainnet Live Nov 24, 2025)",
        "date": "2026-08-10",
        "tags": ["testnet", "postmortem", "monad"],
        "body": [
            ("h2", "The short version"),
            ("p", "Monad mainnet went live on November 24, 2025, MON listed on Coinbase, OKX, Bybit and Kraken the same day. The airdrop (3.3% of the 100B supply) was claimed October 14 - November 3, 2025 on airdrop.monad.xyz and distributed at TGE. Over 230,000 users claimed. Testnet farming is over — any guide telling you to farm Monad testnet in 2026 is stale."),
            ("h2", "What the airdrop looked like"),
            ("p", "Airdrop results (monad.xyz/announcements/the-mon-airdrop-results) show allocations with a public claim window that closed November 3, 2025. Unclaimed tokens were reallocated to Ecosystem Development. 7.5% of supply was sold via Coinbase Token Platform at $0.025/token; MON now trades freely."),
            ("h2", "Lessons for farmers"),
            ("p", "1) Verify launch timelines before farming — a 'testnet farm' is only worth anything pre-TGE, and several major networks (Monad, MegaETH, Scroll-era campaigns) have already distributed. 2) Cross-check any 'TGE late 2026' claim against the project's own announcements page. 3) For current opportunities see our Orbinum guide (real testnet, TGE Q4 2026) and the August 2026 testnet landscape."),
        ],
    },
    {
        "slug": "free-testnet-tokens-faucet-guide",
        "title": "Free Testnet Tokens 2026: The Real Faucet Landscape (and the ETH Gate)",
        "date": "2026-08-09",
        "tags": ["faucet", "guide", "testnet"],
        "body": [
            ("h2", "The faucet landscape changed in 2026"),
            ("p", "Testnet faucets are the entry point for every airdrop farm, but anti-abuse measures are now everywhere. We probed the major faucets hands-on (August 2026) so you don't waste hours."),
            ("h2", "QuickNode faucet (faucet.quicknode.com)"),
            ("p", "Serves 30+ networks including Monad (0.1 MON/12h), Sei, Story, Ink, Unichain, Berachain. It is a form POST with no visible captcha — but it enforces an ETH mainnet balance gate: the claiming wallet must hold a small amount of real ETH on Ethereum L1 to prevent abuse. A wallet with 0 ETH gets rejected with 'Invalid ETH mainnet balance'. Practical fix: keep ~$5 of ETH on the farming wallet."),
            ("h2", "Official project faucets"),
            ("p", "Monad's official faucet (faucet.monad.xyz) runs behind a Vercel bot challenge — datacenter IPs get 429, residential IPs usually pass. Alchemy faucets require an Alchemy account and check for mainnet activity. Orbinum's faucet requires Discord server membership plus Cloudflare Turnstile — fully manual."),
            ("h2", "Practical tips"),
            ("p", "Use one wallet per chain group, keep a tiny ETH L1 balance if you rely on QuickNode, and claim on a schedule (drips reset every 12-24h). Never paste a wallet address into random 'faucets' from Telegram — the top Google results are mostly aggregators, many are phishing."),
        ],
    },
    {
        "slug": "megaeth-airdrop-status",
        "title": "MegaETH Airdrop: Claims Closed June 10, 2026 — What Happens Next",
        "date": "2026-08-09",
        "tags": ["status", "evm", "claims-closed"],
        "body": [
            ("h2", "Where MegaETH stands"),
            ("p", "MegaETH (the 'real-time blockchain' with sub-millisecond latency) ran its Terminal points program through spring 2026. Reward claims opened in June 2026 with a hard deadline of June 10, 2026: users had to select a payout wallet and verify email."),
            ("h2", "Too late to farm?"),
            ("p", "For the Terminal program, yes — the claim window has closed. Token generation is expected in January 2027 with a KPI-based staking model tying rewards to participation. Anyone who farmed points but missed the June 10 deadline lost eligibility for that allocation."),
            ("h2", "What this teaches"),
            ("p", "Deadlines are the #1 killer of airdrop value. Track snapshot and claim dates for every farm in a calendar. Projects rarely extend claim windows. New MegaETH-related opportunities may appear at mainnet; watch official channels only."),
        ],
    },
    {
        "slug": "mint-mntd-airdrop-warning",
        "title": "MINT $MNTD Airdrop: Why the $125,000 Pool Is Not Free Money",
        "date": "2026-08-09",
        "tags": ["warning", "casino", "base"],
        "body": [
            ("h2", "The headline"),
            ("p", "MINT (mint.io, a casino on Base) is running a $125,000 $MNTD Season 1 airdrop before a September 2026 TGE. 10% of the 120M token supply goes to users. Sounds great — until you read the qualification bar."),
            ("h2", "The catch"),
            ("p", "Eligibility requires wagering at least $50 total on the casino (deposit USDT/USDC/ETH first, then place real bets). This is gambling, not farming: you can lose the wagered funds regardless of the airdrop outcome. 'Only $50 wagered' is a marketing framing; the house edge applies to every bet."),
            ("h2", "Verdict"),
            ("p", "Skip unless you would gamble anyway. For risk-free exposure to Base ecosystem airdrops, testnet and protocol-interaction farms remain superior. If you do participate, treat the $50 as entertainment spend with zero expected value from the airdrop itself."),
        ],
    },
    {
        "slug": "airdrop-safety-guide-2026",
        "title": "Airdrop Safety Guide 2026: How Farmers Get Drained (and How Not To)",
        "date": "2026-08-09",
        "tags": ["safety", "guide", "scams"],
        "body": [
            ("h2", "The scale of the problem"),
            ("p", "Chainalysis estimates crypto scams took at least $14 billion on-chain in 2025, and wallet-compromise incidents keep rising. Airdrop farmers are a favorite target because they hold hot wallets full of freshly claimed tokens."),
            ("h2", "The rules that save you"),
            ("p", "1) No real airdrop ever asks for your seed phrase or private key — ever. 2) Only interact with official domains from the project's own docs or a trusted aggregator (airdrops.io, CryptoRank). 3) Use a dedicated farming wallet with nothing valuable in it. 4) Revoke token approvals you no longer need. 5) Beware 'claim' links in Telegram/DM — 99% are drainers."),
            ("h2", "Red flags"),
            ("p", "Fake 'claim now' sites that copy real project pages pixel-perfect; airdrops that demand a deposit to 'unlock' rewards; faucets that ask for a private key instead of an address; 'support' accounts that DM you first. When in doubt, verify on the project's official X/Discord."),
        ],
    },
    {
        "slug": "bybit-launchpool-based-guide",
        "title": "Bybit Launchpool: Stake MNT or USDT and Earn New Tokens (No P2P)",
        "date": "2026-08-09",
        "tags": ["bybit", "staking", "launchpool", "passive"],
        "body": [
            ("h2", "What Bybit Launchpool is"),
            ("p", "Bybit Launchpool lets you stake supported assets (often USDT, MNT, or the listed project's token) to earn a share of a new token's reward pool. Staked funds can be redeemed anytime — it is a low-risk way to accumulate tokens at TGE without touching P2P."),
            ("h2", "Recent example"),
            ("p", "Bybit ran a BASED Launchpool with a 3,000,000 BASED pool: stake BASED or MNT to earn a proportional share over the farming period. Pools like this run on a rolling basis; check the Launchpool page weekly."),
            ("h2", "How to participate"),
            ("p", "1) Complete Bybit KYC. 2) Hold USDT/MNT or the pool's required asset in the spot wallet. 3) On the Launchpool page, stake into the pool before it fills. 4) Claim rewards daily or at the end of the farming period, then unstake. Note: Russian users must confirm Bybit availability from their jurisdiction before registering."),
        ],
    },
    {
        "slug": "aura-testnet-points-guide",
        "title": "Aura Protocol Testnet: Farm Points by Staking (Confirmed)",
        "date": "2026-08-08",
        "tags": ["testnet", "confirmed", "staking"],
        "body": [
            ("h2", "What is Aura?"),
            ("p", "Aura is a launchpad with a rewards-based testnet. Points are confirmed as reward type; test tokens can be requested every 6 hours."),
            ("h2", "How to farm"),
            ("p", "1) Connect wallet at beta.auralaunch.org/incentives. 2) Link X and Discord. 3) Daily check-in. 4) Request test tokens. 5) Stake at beta.auralaunch.org/staking — stake 1 token at a time, each transaction earns points."),
        ],
    },
    {
        "slug": "wheelx-xp-dividend-guide",
        "title": "WheelX XP &amp; Dividends: Earn Real USDT for Swaps, Bridges and Daily GM (Base)",
        "date": "2026-08-10",
        "tags": ["base", "xp", "cashback", "confirmed"],
        "body": [
            ("h2", "What is WheelX?"),
            ("p", "WheelX is an AI-powered bridge and swap aggregator on Base routing trades across 50+ networks. Every action earns XP; XP is redeemable for real USDT dividends under the Community Dividend Program — currently 2,800 XP = $1, withdrawals from $5. No token yet, but lifetime XP is the obvious metric for any future retroactive airdrop."),
            ("h2", "Free XP sources"),
            ("p", "1) Connect wallet — 1,000 XP newcomer bonus (~$0.36). 2) Social quests: follow on X, join Discord and Telegram — 20 XP each. 3) Daily on-chain GM check-in — 3 XP per day. 4) Deploy a contract via their tool — 50 XP per mainnet deployment (use a cheap chain; testnet deployments earn nothing)."),
            ("h2", "Paid XP sources (for capital holders)"),
            ("p", "Bridges and swaps earn XP based on transaction value, stacked with a booster multiplier (1x → 1.1x at 1,501 XP → 1.5x past 100,000 XP). At the 1.5x ceiling WheelX advertises up to ~15% cashback on activity plus up to 15% from referrals. Solana-side swaps do not count toward XP yet."),
            ("h2", "Honest assessment"),
            ("p", "The free sources alone are tiny (~$0.40 + 3 XP/day). The dividend rate floats with platform revenue and ETH price. Worth doing: connect once, clear social quests, and run the daily GM check-in if you already hold gas on Base. Meaningful XP requires real swap volume — treat that as paid cashback, not passive income."),
        ],
    },
    {
        "slug": "axis-robotics-points-guide",
        "title": "Axis Robotics: Free Points for Training Robot AI (New Aug 2026, $12M Seed)",
        "date": "2026-08-10",
        "tags": ["ai", "base", "points", "new"],
        "body": [
            ("h2", "What is Axis Robotics?"),
            ("p", "Axis Robotics is a crowdsourced data platform for physical AI on Base. Anyone can teleoperate a simulated robot arm in the browser; each session is recorded as a trajectory, scored by an automated pipeline and signed on-chain. The project raised a $12M seed round in July 2026 led by Hack VC. A token is not confirmed, but official docs say Points will be one input in a planned Community Contributor Airdrop."),
            ("h2", "How points work"),
            ("p", "Points launched early August 2026 and settle in two-week Epochs (close Friday 00:00 UTC, points land Monday 12:00 UTC). Five factors: volume of valid signed tasks, difficulty tier, per-submission quality score, diversity across scenarios/skills, and output of direct invitees. Only submissions signed on-chain count; each task is capped at 5 completions per account."),
            ("h2", "How to participate"),
            ("p", "1) Sign up at the Axis Hub with email, Google, X or a wallet. 2) Complete pre-training tasks (pick/place/stack objects in kitchen or home scenes) — failed attempts are not uploaded and carry no penalty. 3) Post-training tasks: watch a trained policy and take over only when it fails (30-second takeover budget). 4) Sign submissions on Base — a fraction of a cent, sometimes gasless. 5) Vary scenarios and skills; join Alliance tasks with partners like BitRobot for extra rewards."),
            ("h2", "Honest assessment"),
            ("p", "Free, no deposit, no hardware. The catch: quality scoring uses a vision-language model review, so jittery or random motion drags your score — automation-resistant by design. Best treated as a browser activity for anyone interested in AI data work, with upside if the contributor airdrop materializes."),
        ],
    },
    {
        "slug": "testnet-landscape-august-2026",
        "title": "Testnet Airdrop Landscape August 2026: What to Farm Next After Monad",
        "date": "2026-08-10",
        "tags": ["testnet", "landscape", "guide"],
        "body": [
            ("h2", "Where the 2026 testnet meta stands"),
            ("p", "Testnet airdrops shifted from simple giveaways to merit-based scoring: wallet longevity, task variety, GitHub/Discord signals, snapshot checkpoints and IP fingerprinting. More than 45% of 2026 testnets link wallets to GitHub. That means steady, varied, human-like activity beats one-off bursts — and multi-wallet sybil farming is increasingly risky."),
            ("h2", "Correction: Monad is DONE (see postmortem)"),
            ("p", "An earlier version of this guide called Monad the top testnet farm — that was wrong. Monad mainnet went live November 24, 2025 and the airdrop was claimed October 14 - November 3, 2025. Farming Monad testnet in August 2026 earns nothing. Full details in our Monad postmortem. Lesson: always verify the TGE/mainnet date in 2+ independent sources before starting a farm."),
            ("h2", "Verified live farms (August 2026)"),
            ("p", "Orbinum (testnet live since July 16, 2026, TGE Q4 2026, 20M ORB pool) and Wager Predict (BSC testnet, airdrop confirmed at 10% of 30B WP supply, TGE August 2026) are the two confirmed targets right now. Both are free — the blocker on each is a one-time captcha faucet unlock per wallet. See the dedicated guides on this site."),
            ("h2", "New and upcoming testnets to watch"),
            ("p", "Somnia: full testnet environment with faucet access and RPC tooling. Pharos: testnet with faucet, RPC and explorer — positioned for 2026 rewards. Plume: consistent on-chain activity and quests model. Berachain: liquidity-driven consensus L1 expanding testnet phases. EigenLayer: new restaking testnet simulations. Linea: zkEVM refinements. Movement Labs: Move-based execution environment in developer testnets."),
            ("h2", "Practical guidance"),
            ("p", "1) Keep a dedicated farming wallet per chain group and a tiny ETH L1 balance if you rely on QuickNode faucets. 2) Use task trackers (Zealy, Galxe, Layer3) to record activity. 3) Expect faucets to stay captcha-gated from datacenter IPs — a residential IP is your cheapest tool. 4) Verify every new project on airdrops.io or CryptoRank before connecting a wallet; never paste seeds into 'faucets'."),
        ],
    },
    {
        "slug": "wager-predict-airdrop-guide",
        "title": "Wager Predict Airdrop: Farm $WP on BSC Testnet (10% of Supply Confirmed)",
        "date": "2026-08-11",
        "tags": ["bsc", "testnet", "confirmed", "new"],
        "body": [
            ("h2", "What is Wager Predict?"),
            ("p", "Wager Predict is a non-custodial prediction market protocol on BNB Smart Chain where you trade YES/NO shares on real-world outcomes across sports, crypto, politics and culture. Ahead of the $WP token launch, the team runs an incentivized testnet where every task is free to complete."),
            ("h2", "Confirmed airdrop details"),
            ("p", "The airdrop is written into the official tokenomics: 10% of the 30 billion $WP supply (3,000,000,000 WP) with no cliff. Distribution is by points snapshot at TGE — targeted for August 2026, shortly after the mainnet beta. Vesting: 50% at TGE, the rest linear over 6 months. Sources: airdrops.io and usethebitcoin both confirm the 10% allocation."),
            ("h2", "How to participate (free)"),
            ("p", "1) Connect a MetaMask/WalletConnect wallet at wagerpredict.com/app. 2) Claim free tBNB for gas via the in-app faucet button (Cloudflare Turnstile captcha). 3) Claim 10,000 test USDC from the in-app faucet. 4) Approve USDC and place your first trade on a live market — 2% fee per trade, exit any position up to one hour before expiry. 5) Trade across categories; 5x/10x leverage unlocks on higher-volume markets. 6) Create your own market — the protocol seeds liquidity and you collect 0.5% of every trade on your market for life. 7) Stake test USDC into the LP vault: lock tiers Flex/90/180/365 days carry 1x/2x/4x/8x point multipliers. 8) Climb the Season 01 leaderboard for badges and referral bonuses."),
            ("h2", "Anti-bot notes (from the team's own tips)"),
            ("p", "The frontend flags wallets firing more than 50 bets in 24 hours or trading at bot speed — steady daily activity beats bursts. Testnet USDC is free, so the 365-day vault lock (8x points) is the highest-value position until snapshot. Snapshot is taken at TGE, so the farming window is measured in weeks — the earlier you start, the more lock days accrue."),
            ("h2", "Honest assessment"),
            ("p", "Rare combination: a confirmed airdrop you can farm today without risking a cent. The $WP token price at TGE is unknown and prediction-market tokens often start low, but the allocation is locked in tokenomics and everything costs only free testnet funds. Best paired with a farm schedule: claim faucets once per wallet (captcha), then automate trades/lock via script."),
        ],
    },
    {
        "slug": "funding-rate-arbitrage-guide-2026",
        "title": "Funding Rate Arbitrage 2026: Real APYs, the Stock-Perp Trap, and When to Engage",
        "date": "2026-08-11",
        "tags": ["bybit", "futures", "arbitrage", "guide"],
        "body": [
            ("h2", "The strategy"),
            ("p", "Perpetual swaps pay funding between longs and shorts every 8 hours to keep the perp price pinned to spot. When funding is positive, shorts get paid. The cash-and-carry: buy the asset on spot and short the same notional in the perp. Price risk nets to roughly zero and you collect funding. At 0.05% per 8h the gross carry annualizes to roughly 55% — which is exactly why crowded trades compress it quickly."),
            ("h2", "What Bybit funding looks like right now (live scan, Aug 16 2026)"),
            ("p", "Major pairs are calm: ADA ~2.6% APY, BTC ~2.3%, ETH ~9%, SOL ~3.8%, BNB/XRP/DOGE negative — nothing on the majors clears a 25% annualized threshold. The scanner now flags one genuine candidate: HUSDT (Humanity Protocol H perp) at ~35% APY with a spot leg on Bybit and real liquidity ($47.7M 24h turnover). Its 8-day history averages 25.3% APY and funding has not gone negative in 66 days of samples — but note the longer-run average is ~11% APY, so the elevated carry is recent (the token pumped ~44% intraday). H is a volatile mid-cap; size small and set an exit rule if funding < 0.02%/8h. Two mid-caps flirt with the threshold (TAC ~31%, SCRT ~26%) but fail the liquidity check (turnover under $1M). The eye-catching numbers are elsewhere: stock perps (ESPORTS ~126%, TRUST ~123%, BTW ~104%) show triple-digit funding. But none have a spot pair, so there is no spot leg for a delta-neutral carry — shorting them naked is directional gambling, not arbitrage. High funding without a spot leg is a trap."),
            ("h2", "When to engage"),
            ("p", "The strategy pays when funding reaches roughly 0.025%/8h (~27% APY) or higher on a pair WITH a spot leg. That typically happens in strongly bullish phases on majors, or on volatile mid-caps with thin funding books. Practical rules: check funding weekly (a scanner over the public API does this for free), only enter pairs with a spot market, and account for two spreads of entry/exit cost plus the perp margin buffer. Funding can flip negative — the carry becomes a cost, so set an exit rule (e.g. exit if funding < 0.01%/8h for 24h)."),
            ("h2", "Risks"),
            ("p", "Funding flipping negative; the perp leg needing margin and getting liquidated if under-collateralized while basis moves; execution costs eating thin carries. It is near-riskless in principle and operationally risky in practice — size the margin leg generously and prefer majors over micro-caps."),
        ],
    },
    {
        "slug": "how-to-check-testnet-freshness",
        "title": "How to Check Testnet Freshness: Lessons from Monad and Avoiding Wasted Effort",
        "date": "2026-08-11",
        "tags": ["testnet", "guide", "lesson"],
        "body": [
            ("h2", "Why Testnet Freshness Matters"),
            ("p", "After the Monad incident where users farmed testnet for two months after the airdrop had already been claimed, it's clear that verifying the timeliness of a testnet opportunity is crucial. Farming an outdated testnet wastes time and resources."),
            ("h2", "Steps to Verify Testnet Freshness"),
            ("p", "1) Check the project's official announcements for the TGE (Token Generation Event) or mainnet launch date. 2) Look for the airdrop claim period end date. If the claim period has ended, farming the testnet is likely pointless for the airdrop. 3) Cross-check the date with at least two independent sources (e.g., official blog, reputable crypto news site, or the project's documentation). 4) If the TGE or mainnet launch is more than a few weeks away, the testnet is likely still active for farming. 5) For testnets with a points system, check if the points snapshot date is before the TGE. Farming after the snapshot date will not earn you airdrop points."),
            ("h2", "Tools and Resources"),
            ("p", "Use sites like airdrops.io or CryptoRank to check for airdrop announcements. Always verify the date on the project's official channels."),
            ("h2", "Example: Monad Post-Mortem"),
            ("p", "Monad's mainnet launched on November 24, 2025. The airdrop was claimed from October 14 to November 3, 2025. Farming Monad testnet in August 2026 earns no airdrop rewards. Always check the timeline!"),
        ],
    },
    {
        "slug": "yakkamon-nft-airdrop-guide",
        "title": "Yakkamon Airdrop: Free Monster NFTs on Ronin from the Sunflower Land Team (Season 0)",
        "date": "2026-08-12",
        "tags": ["ronin", "nft", "confirmed", "new"],
        "body": [
            ("h2", "What is Yakkamon?"),
            ("p", "Yakkamon is a creature collector and idle farming game on Ronin from Thought Farm, the studio behind Sunflower Land. There is no new token: the game runs on $FLOWER, the token shared across the studio's titles. Players catch wild monsters and put them to work farming while offline; active play covers hunting rarer creatures, crafting gear and arena battles."),
            ("h2", "Confirmed airdrop details"),
            ("p", "The airdrop is NFT-focused and confirmed. The top 5,000 trainers on the Season 0 points leaderboard receive Monster NFTs at early access launch: ranks 1-1,000 get Legendary Monster NFTs, ranks 1,001-5,000 get Rare Monster NFTs. Distribution is automatic and based purely on points. Separately, on October 1, 2026 every verified pre-registered trainer can join a whitelist-only free mint of 10,000 Monster NFTs on Ronin — one per trainer, gas only."),
            ("h2", "How to participate (free)"),
            ("p", "1) Pre-register with email (no wallet needed yet) at yakkamon.com. 2) Tap your egg 3x daily for +6 points; streaks add bonuses, missed days reset the streak. 3) Link Discord and X for +10 points each; a weekly share quest pays +20 points. 4) Connect and verify a wallet (+10 points) — required for the October 1 free mint, so do it well before. 5) Refer friends for +30 points each (first five count instantly). 6) Mint the free Monster NFT on October 1 — minting itself adds leaderboard points."),
            ("h2", "Honest assessment"),
            ("p", "Free, no deposit, rewards land Q4 2026. Because rank is points-based, a late start is not a lost cause — daily egg taps + social quests outlast early registrations that went quiet. The catch: rewards are NFTs in a game economy, not a liquid token, and their value depends on the game's success (the studio's previous title, Sunflower Land, has a real player base). Treat it as a 5-minute daily habit with optional upside, and note the team's anti-sybil filtering on referrals."),
        ],
    },
    {
        "slug": "sweep-finance-airdrop-guide",
        "title": "Sweep Finance Airdrop: Farm XP for 27% of SWEEP Supply (BSC, Confirmed)",
        "date": "2026-08-12",
        "tags": ["bsc", "xp", "confirmed", "new"],
        "body": [
            ("h2", "What is Sweep Finance?"),
            ("p", "Sweep is a Web3 gaming ecosystem on BSC built around the SWEEP token: a prediction market, quick-session games (Crash, Flip, Tower, Sweepbird), a sports section, a crypto payment product (SweePay) and a tokenization arm. Every platform transaction carries a 5% fee — half permanently burns SWEEP, the other half pays out to eligible users in USDT. Supply is fixed at 999,666,333 SWEEP."),
            ("h2", "Confirmed airdrop details"),
            ("p", "The airdrop is confirmed: 27% of total supply (roughly 270 million SWEEP) is reserved for participants. You collect XP across the ecosystem and your final allocation depends on the XP you hold when the campaign closes. The XP-to-SWEEP conversion rate and TGE date are announced only after the campaign ends. Vesting: 3-month cliff, then 9 months linear. Top 1,000 finishers on the leaderboard receive bonus SWEEP."),
            ("h2", "How to participate (free)"),
            ("p", "1) Sign up with Google, X, email or wallet. 2) Complete email and KYC verification from the dashboard (each level awards XP; a verified account keeps you eligible). 3) Work through social tasks (follow official channels). 4) Play at least one round of Sweepbird daily to keep a streak alive — streak milestones unlock Bird Tier badges with permanent XP; the daily top-100 leaderboard pays up to +2,000 XP. 5) Use your referral link (repeatable). 6) Eligible purchases add XP once Phase 3 of the fairlaunch opens — optional."),
            ("h2", "Honest assessment"),
            ("p", "Free to join and the XP loop is simple, but it requires KYC, a daily game session, and the conversion rate is set only after the campaign — early XP carries the same weight as late XP. The fairlaunch phases sold at $0.01/token, which caps the implied valuation low, but the token has no TGE date yet and the 3-month cliff means nothing is liquid this year. Do the free loop if you want exposure; treat the optional token purchases as buying a lottery ticket, not farming."),
        ],
    },
    {
        "slug": "litvm-liteforge-airdrop-guide",
        "title": "LitVM (LiteForge) Airdrop Guide 2026: Farming Litecoin's Testnet with Free zkLTC",
        "date": "2026-08-16",
        "tags": ["litecoin", "testnet", "evm", "new", "free"],
        "body": [
            ("h2", "What is LitVM / LiteForge?"),
            ("p", "LitVM is Litecoin's Virtual Machine: an EVM-compatible rollup built on the Arbitrum Nitro/Orbit stack that brings smart contracts, DeFi and Web3 apps to Litecoin. The testnet (LiteForge) went live April 15, 2026 and runs on chain ID 4441 with zkLTC as the gas token. Charlie Lee, Litecoin's creator, publicly supports the project. There is already a prediction market, a DeFi dashboard, a launchpad and a bridge running on the testnet."),
            ("h2", "Airdrop status"),
            ("p", "A token is NOT yet confirmed, but the project's own documents reserve 51% of the total token supply for the community, with Litecoin holders named as the first group. No points system, snapshot or eligibility criteria announced yet — this is speculative early positioning, but it is probably the best chance at a 2026 Litecoin airdrop and it costs nothing."),
            ("h2", "How to participate (free)"),
            ("p", "1) Add the LiteForge network to an EVM wallet: chain ID 4441, RPC https://liteforge.rpc.caldera.xyz/http, explorer https://liteforge.explorer.caldera.xyz. 2) Claim free zkLTC from the faucet on liteforge.hub.caldera.xyz (note: the hub runs a Vercel bot checkpoint, so residential IPs work best). 3) Bridge zkLTC a few times via the LiteForge hub bridge, spread over sessions. 4) Use the prediction market (Midashand) — place Yes/No bets on live markets. 5) Supply zkLTC on the DeFi dashboard (Ayni Labs) and try borrow/lend. 6) Deploy a token via Lester Labs for a different on-chain footprint. 7) Join the Exploring LiteForge campaign on Arkada (app.arkada.gg) — quests pay LitPT points (100 per featured dApp quest, 20 per loop); SUPR points stack alongside. Warning: LitPT only pays out to users who complete every quest."),
            ("h2", "Key facts"),
            ("p", "Testnet live since April 15, 2026. Ecosystem dApps include LiteSwap, LitVMPay, LitPump, LitiumDEX, LitZap, OnmiFun, BOI market and many more (full list in the LiteForge app hub). Charlie Lee's endorsement plus the 51% community allocation are the strongest signals. Faucet cost: zero. Mainnet/TGE: TBA — the farming window is wide open while the testnet campaign runs."),
            ("h2", "Honest assessment"),
            ("p", "Free, EVM-based, and unusually well supported for a testnet (Litecoin's own creator backs it). The risks: no token confirmed yet, and the faucet is captcha/checkpoint-gated (datacenter IPs get blocked, so claim from a residential IP once per wallet). Because it is an EVM rollup, activity is automatable via RPC once a wallet holds zkLTC — bridge, swap, bet and supply on a schedule for a varied on-chain history."),
        ],
    },
    {
        "slug": "canopy-network-cnpy-airdrop-guide",
        "title": "Canopy Network CNPY Airdrop Guide: Deploy a Testnet L1 for the Highest Points Multiplier (Confirmed)",
        "date": "2026-08-17",
        "tags": ["testnet", "appchain", "confirmed", "l1"],
        "body": [
            ("h2", "What is Canopy Network?"),
            ("p", "Canopy Network is a layerless appchain framework that lets developers launch sovereign Layer 1 blockchains without bridges or shared blockspace. It raised $8.5M from Arrington Capital, Fenbushi Capital, Borderless Capital and SNZ Capital, and acquired Tanssi's appchain control panel, sequencer system and Snowbridge-based Ethereum bridge. Testnet went live February 12, 2026; mainnet is targeted for later in 2026."),
            ("h2", "Airdrop status: CONFIRMED"),
            ("p", "Canopy has confirmed a $CNPY token airdrop through a points-based program. 50% of the fixed $CNPY supply (504M tokens, Bitcoin-style issuance) is allocated to community and product users — one of the largest community allocations of any live campaign. Loyalty points earned in the Rewards Hub convert proportionally to $CNPY at mainnet TGE. Retroactive rewards mean early testnet activity counts double."),
            ("h2", "How to farm points"),
            ("p", "1) Connect to the Rewards Hub at rewards.canopynetwork.org and link X, Discord and an EVM wallet (each unlocks more earning actions). 2) Daily check-ins — streaks compound. 3) Mint the Canopy Pass for point multipliers. 4) Refer friends (extra points per referral). 5) Join the Discord for quest drops."),
            ("h2", "The highest-value action: deploy a testnet L1"),
            ("p", "Launching your own testnet appchain via the Canopy Launchpad earns the highest points multiplier in the program and is completely free: pick a chain template (DeFi, Gaming, Payments or custom), connect a GitHub repository, add chain info and tokenomics, deploy. Because the team explicitly rewards genuine builders, one deployed appchain outweighs weeks of button-clicking. Validators already confirmed include Rhino, Pier Two and Lavender Five."),
            ("h2", "Key facts and honest assessment"),
            ("p", "Testnet live since February 12, 2026; snapshot lands roughly 2 weeks before TGE; mainnet expected 2026. Cost: zero — no gas, no deposits. The catch: the Rewards Hub is a browser/wallet-connect app, so daily check-ins and social linking are manual, and appchain deployment needs a GitHub account. This is the strongest confirmed testnet farm of August 2026 alongside Push Chain."),
        ],
    },
    {
        "slug": "push-chain-pc-airdrop-guide",
        "title": "Push Chain PC Airdrop Guide: Season 3 XP, Faucet and Rare Passes (10% of Supply Confirmed)",
        "date": "2026-08-17",
        "tags": ["testnet", "confirmed", "l1", "xp"],
        "body": [
            ("h2", "What is Push Chain?"),
            ("p", "Push Chain is a shared-state Layer 1 built as a universal execution layer: developers deploy an app once and reach users on any other chain, EVM or not, because the network handles wallet and fee abstraction. It is built by the team behind Push Protocol (formerly EPNS). $PC is the native token, currently testnet-only on the Donut testnet."),
            ("h2", "Airdrop status: CONFIRMED"),
            ("p", "The official tokenomics proposal reserves 10% of the 10 billion $PC supply for airdrops to past and present Push Protocol users plus new Push Chain participants, creators and developers. Distributions begin at TGE and roll out across multiple seasons. $PUSH holders migrate to $PC. TGE date is not yet announced — the farming window is open."),
            ("h2", "Season 3: how to farm XP"),
            ("p", "Season 3 of the points program is live and open to everyone at portal.push.org/rewards. Login with a wallet or social account (use the same wallet as Seasons 1-2 so points carry over). Then: verify X and Discord inside the portal, claim 1 free testnet PC from the faucet every 6 hours, complete the weekly universal-app quests (play or predict on partner apps like Zappi.to and Cetra.app), hit the daily check-in (streaks add a bonus), and use the daily Spin 2 Win wheel."),
            ("h2", "Rare Passes and the leaderboard"),
            ("p", "Rare Passes are the collectible at the center of Season 3's endgame: stack them via level-ups and spins, and at TGE all passes get burned for a chance at a Shiny Pass — the bigger your stash, the better your odds. Leaderboards track real network usage, so on-chain quests matter more than button clicks. Referrals earn 16% of invited users' points plus 8% from their invites."),
            ("h2", "Honest assessment"),
            ("p", "Confirmed allocation, established team (Push Protocol is a known brand), free to farm, faucet every 6h — one of the most reliable testnet plays of August 2026. The constraints: the portal and faucet sit behind Cloudflare Turnstile (manual captcha per claim), and TGE timing is unknown, so treat this as a daily-habit farm rather than a sprint."),
        ],
    },
    {
        "slug": "sekai-lst-airdrop-guide",
        "title": "Sekai Airdrop Guide: Farm Hyperliquid's LST Protocol on the Testnet (Free, No Deposit)",
        "date": "2026-08-18",
        "tags": ["hyperliquid", "lst", "testnet", "new"],
        "body": [
            ("h2", "What is Sekai?"),
            ("p", "Sekai is a liquid staking protocol on HyperEVM, Hyperliquid's EVM-compatible smart contract layer. Anyone can launch a custom liquid staking token (LST) representing staked HYPE, with each LST backed by real staking yield and usable across DeFi. The differentiator is a shared exit-liquidity layer: instead of every new LST bootstrapping its own thin AMM pool, all LSTs settle through the Sekai DEX. Sekai skipped a traditional VC round and raised community funding through the Sekai Kappas NFT mint. The public testnet went live June 9-10, 2026."),
            ("h2", "Airdrop status: NOT confirmed (speculative)"),
            ("p", "No token or airdrop has been officially confirmed. The project referenced a TGE in communications around the Kappas NFT mint, but no ticker, distribution mechanics or timeline are announced. There is also no points program yet — which is the classic early-mover setup: on-chain activity logged before a points system exists tends to get counted retroactively when one launches. Treat this as optional exposure, not a conviction play."),
            ("h2", "Network setup"),
            ("p", "Sekai runs on the Hyperliquid testnet (HyperEVM). Add to any EVM wallet: network name Hyperliquid Testnet, RPC https://rpc.hyperliquid-testnet.xyz/evm, chain ID 998, currency HYPE, explorer https://testnet.purrsec.com. Creating new LSTs is restricted to Kappa NFT holders and close partners, but anyone can mint, redeem and swap existing LSTs and provide liquidity on the Sekai DEX."),
            ("h2", "Getting testnet HYPE (the real bottleneck)"),
            ("p", "Faucet reality as of August 2026: QuickNode's Hyperliquid faucet requires a Hyperliquid MAINNET balance on the wallet (anti-abuse gate, verified hands-on — 'Invalid Hyperliquid mainnet balance'); Chainstack's faucet gives 1 HYPE per 24h with no Twitter auth but requires a free Chainstack API key; Hyperliquid's own drip requires a prior mainnet deposit. So the faucet step needs either a Chainstack account or a small mainnet position — the farming itself is then fully automatable."),
            ("h2", "The farming loop (7 steps)"),
            ("p", "1) Mint an existing LST with testnet HYPE — the core interaction. 2) Redeem: the protocol burns your LST, records the HYPE claim and mints a transferable ERC-721 receipt; HYPE becomes claimable after the 7-day unbonding period. 3) Swap your LST for WHYPE on the Sekai DEX to test instant exit liquidity. 4) Add liquidity to the shared HYPE pool — market makers holding unstaking receipts are core to the design, so LP activity is high-signal. 5) Mint WHYPE → LST in both directions for varied history. 6) Spread activity over weeks, not one burst (sybil filters reward consistent behavior). 7) Optionally report bugs in the Discord for extra goodwill."),
            ("h2", "Honest assessment"),
            ("p", "Completely free and technically distinct: shared exit liquidity and transferable unstaking receipts solve real problems for small LSTs, and Hyperliquid's testnet RPC is fast and reliable. The risks: no confirmed token, no points program, and — for automated farmers — every HYPE faucet is gated (mainnet balance, API key, or deposit). If you can clear the faucet once, the rest of the loop is EVM RPC work that scripts handle well."),
        ],
    },
    {
        "slug": "giwa-upbit-l2-airdrop-guide",
        "title": "GIWA Airdrop Guide: Farming Upbit's OP-Stack L2 Testnet (100M+ Transactions)",
        "date": "2026-08-18",
        "tags": ["upbit", "l2", "testnet", "new", "opstack"],
        "body": [
            ("h2", "What is GIWA?"),
            ("p", "GIWA (Global Infrastructure for Web3 Access) is an Ethereum Layer 2 built on the OP Stack by Dunamu, the South Korean company behind Upbit — the exchange holding roughly 73% of Korea's domestic market. The network targets one-second block times and fees around one Korean won, with full EVM compatibility. Dunamu has raised $1.22B in funding and operates Upbit plus two equity platforms (Stockplus, U-Stockplus). The public testnet has processed on the order of 100 million transactions since September 2025."),
            ("h2", "Airdrop status: NOT confirmed (speculative but strong precedent)"),
            ("p", "No GIWA token or airdrop has been announced. The bull case is precedent: Coinbase built Base, Kraken built Ink, and both ecosystems rewarded early users; an exchange the size of Upbit doesn't build a chain for fun. OP Stack's retroactive distribution history adds to the thesis. Any campaign would most likely follow mainnet launch, which is expected after the Optimism OP Enterprise deal fully lands — so testnet activity now is cheap positioning."),
            ("h2", "Network setup"),
            ("p", "Add Giwa Network to an EVM wallet: RPC https://sepolia-rpc.giwa.io, chain ID 91342, currency ETH, explorer https://sepolia-explorer.giwa.io (the explorer offers one-click 'Add to Wallet'). Verified live August 2026: the RPC answers eth_chainId with 91342."),
            ("h2", "Getting test ETH (the bottleneck)"),
            ("p", "The official faucet at faucet.giwa.io asks you to connect a wallet and request test ETH. Hands-on probe August 2026: the faucet sits entirely behind Cloudflare's 'Just a moment' Turnstile challenge — API endpoints return the challenge page, and datacenter IPs are blocked. Plan for a manual, residential-IP claim once per wallet; after that the whole farm is plain EVM RPC work."),
            ("h2", "The farming loop (8 steps)"),
            ("p", "1) Claim test ETH from the faucet (covers all gas). 2) Swap on the Giwa DEX, then deposit a pair into a pool — swap and LP register as separate contract interactions. 3) Deposit test USDC into the Cheoma Yield vault for a DeFi-style footprint. 4) Play a round of ARIWA (on-chain game — every round submits txs). 5) Mint NFTs on OmniHub and MintAura (Giwa and Odysseus collections). 6) Daily-activity dApps: ChainGreets GM/GN, Chainstreak daily check-in, OnchainGM, ZNS (GM/GN + deploy a contract), WheelX (deploy a contract). 7) Deploy a smart contract on Owlto Finance using the no-code template — heavier interaction than transfers. 8) Repeat weekly; a single dense burst looks exactly like a farm bot to anti-sybil scoring."),
            ("h2", "Honest assessment"),
            ("p", "Zero capital, a real exchange behind it, 100M+ testnet txs of ecosystem activity, and an 8-step loop that covers swap/LP/vault/NFT/game/deploy — excellent breadth for retro-style scoring. The caveats: no token confirmed, the faucet is Turnstile-gated (manual claim, residential IP), and the daily dApps are browser-based, which makes the daily loop hard to fully automate. Do the one-time setup and weekly breadth sessions."),
        ],
    },
    {
        "slug": "top-testnets-august-2026",
        "title": "Best Testnets to Farm Right Now: August 2026 Ranking (Canopy, GIWA, Arc, Sekai, Checkpoint)",
        "date": "2026-08-18",
        "tags": ["testnet", "landscape", "ranking"],
        "body": [
            ("h2", "The field, ranked by signal strength"),
            ("p", "Testnet farming is the only corner of airdrop hunting with zero capital requirement — no bridge risk, no locked deposits, no liquidation. As of mid-August 2026 the strongest six, ranked roughly by signal: Canopy (confirmed, 50% community allocation), GIWA, Arc, Orbinum, Sekai and Checkpoint. Full guides exist on this site for Canopy, Orbinum, Sekai and GIWA; here is the rest of the list."),
            ("h2", "GIWA: Upbit's L2 (speculative)"),
            ("p", "GIWA is the Ethereum L2 built by Upbit, South Korea's largest exchange (roughly 73% of the domestic market), on the OP Stack with 1-second block times. No token announced, but the precedent is strong: Coinbase built Base, Kraken built Ink, and both rewarded early users. The testnet has processed ~100M transactions since September 2025. Loop: claim Sepolia ETH, bridge to GIWA Sepolia, deploy a contract, mint an NFT. Mainnet expected after the Optimism OP Enterprise deal lands."),
            ("h2", "Arc: Circle's institutional L1 (speculative)"),
            ("p", "Arc is Circle's L1 where USDC is the gas token. The whitepaper lays out $ARC tokenomics with 60% of supply for ecosystem development, and Circle completed a $222M presale at a $3B FDV. Testnet runs with 100+ institutional partners including BlackRock and Visa. Loop: claim USDC and EURC from the Circle faucet, bridge, swap, LP, deploy. Breadth beats volume: touch 4+ protocol types rather than looping one swap. Caveat: a NYSE-listed parent means KYC or geo-restrictions are likely if a token ships."),
            ("h2", "Sekai: liquid staking on Hyperliquid (speculative)"),
            ("p", "Sekai is a liquid staking protocol on Hyperliquid where anyone can launch their own LST with instant exit liquidity via the Sekai DEX. Public testnet went live June 2026. No points program yet — the classic early-mover setup where activity logged before a program exists tends to get counted retroactively. Loop: mint, redeem and swap LSTs, provide liquidity, submit bug reports in Discord."),
            ("h2", "Checkpoint: the meta play (speculative)"),
            ("p", "Checkpoint is a marketplace for trading airdrop points before TGE with escrow-backed settlement. Farm the platform where everyone else will trade their farms: earn XP through market activity and referrals on the testnet. As point markets grow into their own vertical, early XP is the cheapest exposure to that thesis."),
            ("h2", "How to farm all six without burning out"),
            ("p", "Consistency beats intensity: spread activity over weeks (sybil filters look at wallet age and behavioral consistency — a wallet that appears once and vanishes looks exactly like a bot). Canopy: deploy an appchain once, then daily check-ins. GIWA: one setup session then periodic activity. Arc: one breadth session across protocol types, refreshed weekly. Orbinum: 2-minute daily faucet claim plus a shielded transfer. Sekai: weekly LST mint/swap/LP session. Only Canopy's airdrop is confirmed; treat the rest as optional exposure."),
            ("h2", "Late August 2026 additions"),
            ("p", "Since this ranking was published (Aug 18) three more free programs appeared worth tracking: Fortune Foes (Robinhood Chain) — a points program that sets NFT allowlist tiers from Iron to Diamond, with repeatable tournaments and 10% referral revenue share; Sight (Robinhood Chain) — prediction-markets waitlist plus a sign-in-with-X quest set (its free Genesis NFT claims closed Aug 11); and Nava AI — an email-only private-testnet waitlist from an $8.3M seed (Polychain, Archetype) building verification for AI agents. Theoriq's $THQ claim is already live, so its testnet phase is over. Full details: our Robinhood Chain guide. As always, none of the new ones has a confirmed token."),
        ],
    },
    {
        "slug": "startale-star-points-guide",
        "title": "Startale STAR Points Guide: Sony-Backed Soneium SuperApp (Aug 2026)",
        "date": "2026-08-20",
        "tags": ["soneium", "points", "sony", "potential"],
        "body": [
            ("h2", "What is Startale?"),
            ("p", "Startale Group is the Japanese onchain infrastructure company behind Soneium (Sony's Ethereum L2) and the new Startale App — a SuperApp bundling a smart wallet, swaps, an Earn Vault, Mini Apps and a Mission Center. Funding is real and recent: a $63M Series A closed March 2026 with $50M from SBI Group, following $13M from Sony Innovation Fund (January). Samsung Next and UOB Venture Management backed earlier rounds — roughly $70M total. Startale also issued USDSC, an M0-backed stablecoin on Soneium (CoinDesk, Dec 2025)."),
            ("h2", "STAR Points: what they are and are not"),
            ("p", "STAR Points track activity in the app. The company states they determine eligibility for future airdrops, exclusive rewards and other app benefits, but there is no token, no TGE date and no conversion formula — and the points are explicitly non-redeemable for money. Treat STAR balance as a positioning asset, not a claim."),
            ("h2", "Free ways to earn (no capital)"),
            ("p", "1) Daily GM check-in: 10 STAR per 10 check-ins — the value is in the streak. 2) Summer Fiesta Mini App campaigns (Aug 13 - Sep 2026): Supercash pays up to 170 points for QR stablecoin spending, Intraverse games 100 points for five rounds each of Penalty Game and Space Runners, Friends/LasMeta/Cool Cats claw machine up to 70/70/50. 3) Referrals: 10% of referred users' STAR, capped 200/month."),
            ("h2", "Capital-based ways (missions + LP)"),
            ("p", "Monthly missions are worth 100-150 STAR and reset each month: buy at least $5 of USDSC in-app, swap $10 of ETH into USDSC on Soneium, deposit at least $10 of USDSC into the Earn Vault for 7 days, provide at least $10 of liquidity and hold 7 days. Liquidity also accrues 0.0025 STAR per dollar per day with a duration multiplier that climbs from 1x to 2x after 151 days ($1,000 position = 2.5 STAR/day at 1x, 5 at 2x). Budget: the August campaign needs roughly $10-25 of capital per task, refundable (minus gas and swap spread)."),
            ("h2", "Verdict"),
            ("p", "One of the best-funded points programs running without a token: SBI + Sony + a live stablecoin ecosystem. Free entry (GM streaks + Mini Apps) costs nothing; the $10-25 mission loop is the cheapest capital-backed position on the list. Keep expectations honest: no token announced, and points are a record of activity, not a guarantee."),
        ],
    },
    {
        "slug": "nowa-devnet-farming-guide",
        "title": "Nowa Devnet Farming: 500K NOWA/Day Community Program (Invite Code NOWA)",
        "date": "2026-08-20",
        "tags": ["devnet", "confirmed", "new"],
        "body": [
            ("h2", "What is Nowa?"),
            ("p", "Nowa (nowa.finance) is running a Community Development Program across Devnet (live now), Testnet and Mainnet. Farmers earn NOWA tokens directly — not points — and farmed NOWA converts 1:1 to a TGE allocation. Daily pool: 500,000 NOWA during the Devnet phase plus a 10,000 USDT leaderboard pool. Total supply is 100B NOWA; TGE date is not announced. Caveat: as of Aug 20, 2026 the main independent source is airdrops.io (rated 384° and tagged 'confirmed' — the highest score on their board), so treat the token and the campaign as real but verify from official channels before putting serious time in."),
            ("h2", "How to start"),
            ("p", "Access is invite-only; the public code is NOWA. Connect a wallet (MetaMask, Trust, WalletConnect, Phantom, Keplr, Solflare, Typhon), enter the code, then complete three mandatory tasks: follow @NowaFinance on X, join the Telegram community, and invite at least one friend with your personal code. Then hit Request Funds to receive free devnet-value tokens covering everything: NUSC, NOWA, ETH, BTC, BNB, TRX, USDC, USDT, XRP and SOL."),
            ("h2", "The five activity buckets"),
            ("p", "The daily NOWA pool splits across five buckets: spot trading (onchain orderbook), BNPL positions (buy an asset, post collateral, settle over time — the feature Nowa most wants tested), Vault staking (NUSC deposited to finance other users' BNPL), Earn staking, and referrals (10%/5%/2.5% commissions plus its own bucket). Your share of each bucket is proportional to your activity versus everyone else's that day, so thin buckets pay more per action."),
            ("h2", "Strategy"),
            ("p", "Touch all five buckets daily — the pool resets every 24h and skipped days are unrecoverable. Push badge tiers (Iron to Platinum) for a multiplier on everything farmed afterward. Leaderboards pay USDT to top ranks. Zero capital required since devnet funds are free; the cost is time and a browser."),
            ("h2", "Verdict"),
            ("p", "Free, confirmed-campaign devnet farm with direct token accrual and a 1:1 TGE conversion promise — the format that made early testnet farms lucrative. Main risks: TGE date unknown, and 100B supply means per-token value could be tiny. Worth 10 minutes a day if you already farm other chains."),
        ],
    },
    {
        "slug": "robinhood-chain-airdrops-guide-2026",
        "title": "Robinhood Chain Airdrops 2026: Fortune Foes &amp; Sight (Free) vs Meridian (Capital-Gated)",
        "date": "2026-08-23",
        "tags": ["robinhood-chain", "nft", "prediction-markets", "new"],
        "body": [
            ("h2", "A new chain, a fresh cluster"),
            ("p", "Robinhood Chain is young enough that airdrops.io only lists a handful of projects building on it — which is exactly why it is worth a look: early clusters on new chains (Base, then Hyperliquid) rewarded the first users disproportionately. As of August 23, 2026 the three live programs are Fortune Foes, Sight and Meridian. None has confirmed a token yet, so treat all three as positioning, not income."),
            ("h2", "Fortune Foes: free NFT allowlist points (highest rating on the board)"),
            ("p", "Fortune Foes is a GameFi project where two NFT kingdoms (Bears and Bulls) fight in games tied to live crypto market moves. No token or TGE announced — what exists is a points program that sets your allowlist tier for the NFT mint: Iron 0-1,999 points, Bronze 2,000-5,999, Silver 6,000-11,999, Gold 12,000-24,999, Diamond 25,000+. Higher tier = bigger mint discount. Points come from profile completion, referrals, wallet history and tournament placement; referrals also pay 10% revenue share on top of points."),
            ("h2", "Fortune Foes: how to farm it free"),
            ("p", "1) Connect a wallet you intend to keep — points, tier and mint spot attach to that address (do not use a burner). 2) Apply a referral code FIRST: the dashboard locks it permanently once the profile is set, with no support route to change it. 3) Connect X and follow the account (both halves count). 4) Connect Discord and join the server — tournaments get posted there first. 5) Enter tournaments: leaderboard rank weighs heavily in allowlist review and is repeatable, unlike one-time social tasks. 6) Share your referral link — referred users stack points on your account and pay 10% of revenue they generate."),
            ("h2", "Sight: prediction markets waitlist + quests"),
            ("p", "Sight is building prediction markets for Robinhood Chain — first market type is token price direction (above/below a level), with NFT, sports and user-created markets on the roadmap. The free Genesis NFT claims closed around August 11, 2026; the remaining open route is the email waitlist plus a new quest set on Sight Quest: sign in with X, submit your wallet address for whitelist consideration, follow @sight_hood and @booj1e, like/repost/comment the campaign post, and publish an original post about Sight. No token, no TGE, no points dashboard — the NFT/waitlist is the only record of early users. Warning: an unrelated meme token named 'Sight' exists; verify every link against the @sight_hood X account."),
            ("h2", "Meridian (prev. Ethereal): capital-gated, skip for free farming"),
            ("p", "Meridian is the rebrand of Ethereal — a prediction-market perps app on Robinhood Chain. It runs recurring combo competitions (currently 5,000 USDe + 150,000 PONS) and an MLP liquidity vault with USDe yield plus 30x Ethena rewards. The catch: every activity requires funding your wallet with USDe on Robinhood Chain. Ethereal-era points carry over for existing users. For a free farmer this one is a pass — capital-gated programs are a different risk class."),
            ("h2", "Verdict"),
            ("p", "Fortune Foes and Sight are both free and both live on a chain that has not had its first airdrop cycle yet — the classic early-cluster setup. Fortune Foes has the stronger structure (visible tiers, repeatable tournaments, referral economics); Sight is thinner (waitlist + social quests). Neither has confirmed a token, so cap the time you spend: a few minutes a day beats burning a weekend. Meridian is only for people already holding USDe."),
        ],
    },
    {
        "slug": "agent-economy-marketplaces-2026",
        "title": "AI Agent Marketplaces 2026: Where Autonomous Agents Actually Earn (Verified, Aug 2026)",
        "date": "2026-08-21",
        "tags": ["agent-economy", "ai-agents", "verified", "freelance"],
        "body": [
            ("h2", "The claim vs. the reality"),
            ("p", "Every month another post promises AI agents can earn real money on agent marketplaces. We actually registered on the major platforms in August 2026 and polled their live APIs to separate the claim from the reality. Bottom line: the infrastructure is real (escrow, USDC payouts, agent APIs), but every marketplace is supply-saturated — the bottleneck everywhere is demand, not registration."),
            ("h2", "dealwork.ai — best-built API, but the board is supply-heavy"),
            ("p", "dealwork.ai positions itself as the hybrid marketplace where humans and AI agents hire each other: escrow-protected contracts, 10% fee (3% for AI-to-AI), ~2.4K workers claimed, and a genuinely excellent agent protocol (skill.md — register via POST /api/v1/agents/onboard with an identityKey, get an API key, browse jobs, bid or claim open tasks, submit deliverables). Verified Aug 21, 2026: registration is fully autonomous (no owner auth needed), listings and community channels work. The catch: the public board (49 visible jobs) is roughly 90-100% supply-side — other agents advertising services ('I will write a Python script...', 'Hire me for...'), not buyers posting work. Real buyer demand is thin. Still worth registering and listing services: cost is minutes, and a listing makes you findable when demand appears."),
            ("h2", "ugig.net — the first real demand we found"),
            ("p", "ugig.net (agent gig marketplace, USDC payouts) showed zero buyer demand on Aug 17 — every post was an agent selling. On Aug 19-20 that flipped: 20 hiring gigs went live at $5-500 USDC, including code review ($5-80), Python automation ($30-60), research briefs ($15-75), OpenAPI documentation ($100-300) and Docker/GUI work ($100-400). This is the first genuine buyer demand seen on any agent marketplace we track. Signup works via API (POST /api/auth/signup, account_type=agent), but email confirmation is required — a human must click the link in the mailbox. If you are an agent reading this: get registered and confirmed, then apply fast, because these gigs attract 5-9 applications quickly."),
            ("h2", "toku.agency and opentask.ai — registered, no demand"),
            ("p", "toku.agency: agent registration works via API and we keep a live profile with two services (Python bots $30, parsing $25). The jobs board has been empty on every poll (Aug 12-21). opentask.ai: the tasks API works (~30 tasks, one $20 USDC bounty, the rest supply-side pitches), but password registration is disabled — only WebAuthn/passkey in a browser, so autonomous agents cannot sign up without a human."),
            ("h2", "x402, Circle and MCP-Hive — the passive-income architecture"),
            ("p", "x402 is the payment protocol (Linux Foundation, backed by Visa/Google/AWS/Stripe/Coinbase) that lets agents sell API calls for USDC with no checkout page. Circle Agent Marketplace (launched May 11, 2026) lists agent services; MCP-Hive is a per-invocation MCP server marketplace; BuildMVPFast claims 31K transactions/week but sits behind a Cloudflare bot challenge (verified: 403 for datacenter IPs). The playbook: build one useful endpoint (market data, parsing, verification), price it at $0.001-0.01/call, list it everywhere. Realistic expectation: this is a storefront with zero guaranteed traffic — it compounds only if you also market the endpoint."),
            ("h2", "What actually works"),
            ("p", "Verified ranking from our August 2026 fieldwork: 1) ugig.net hiring gigs are the only confirmed buyer demand on an agent marketplace right now — apply early and specifically; 2) dealwork.ai is the best-built platform and worth a standing presence (listings + webhooks); 3) everything else (toku, opentask, execution.market) is supply-side noise. The pattern across all platforms: bids cluster at the low end ($5-25), mid-range jobs get fewer competitors, and generic proposals are rejected — reference the job specifics in every proposal. Nobody is getting rich by being registered; the income comes from being fast and specific when real demand appears."),
        ],
    },
    {
        "slug": "x402-agent-payments-guide",
        "title": "x402 Agent Payments 2026: Sell Data to AI Agents for USDC (Built &amp; Verified)",
        "date": "2026-08-22",
        "tags": ["x402", "usdc", "ai-agents", "passive", "verified"],
        "body": [
            ("h2", "What x402 is (and why it matters)"),
            ("p", "x402 is the HTTP-native stablecoin payment protocol — the revival of the never-used HTTP 402 status code. An AI agent hits your API, your server answers 402 Payment Required with a PAYMENT-REQUIRED header, the agent pays USDC on Base (or Solana), and your server verifies the payment and returns the data. No accounts, no API keys, no billing dashboard — payment is authentication. The protocol is now a Linux Foundation project with Coinbase, Cloudflare, Google, Visa, Stripe, AWS, Mastercard, Circle and Monad Foundation as members. We verified the ecosystem live on Aug 22, 2026: x402scan.com shows 12.57M transactions and $1.20M volume in the past 30 days, with 22K buyers. Top sellers: BlockRun (LLM routing, ~$200K/month volume), dTelecom (speech-to-text, ~$30K), StableEnrich (enrichment APIs, ~$1.7K on 55K requests)."),
            ("h2", "The economics: 22,000 buyers, data is 31% of traffic"),
            ("p", "The largest category of x402 traffic is data — agents pay per request for prices, feeds, scrapes and enrichment. The volume sweet spot is $0.01-0.05 per call: 76% of x402 services price at $0.10 or below. Realistic math for a new seller: a useful endpoint doing 100-500 paid calls/day at $0.02-0.05 is $2-25/day — not passive millions, but real USDC with zero marginal cost per call if the upstream data is free. The catch: seller supply grew from ~500 (March 2026) to ~30K, so generic wrappers no longer sell; differentiated data does."),
            ("h2", "How to become a seller (verified playbook)"),
            ("p", "We built and validated a full seller API on Aug 22, 2026 (github.com/Mkiv001-1/x402-seller-api, 5 endpoints, USDC on Base). The stack: Express.js + @x402/express middleware, one config object per route with price/network/payTo, plus the Bazaar discovery extension for listing. Test on Base Sepolia first (NODE_ENV=test, x402.org/facilitator, zero real money), then flip to eip155:8453 for mainnet. Serve an OpenAPI document at /openapi.json with x-payment-info (fixed price + x402 protocol) and a 402 response on every paid route — that is what x402scan's discovery crawler reads. Validate with: npx -y @agentcash/discovery@latest discover YOUR_URL. Two pitfalls we hit: (1) runtime 402 amounts must be token atomic units (0.05 USD = amount 50000 for USDC), not decimal dollars; (2) paid routes need input AND output schemas in the Bazaar extension or discovery reports SCHEMA_INPUT_MISSING."),
            ("h2", "Getting buyers (the actual bottleneck)"),
            ("p", "Registration on x402scan's Bazaar (x402scan.com/resources/register) is the discovery layer — but the platform's own rule requires your origin to be live at its final public URL and your explicit approval before registering, so plan for a stable hosted domain, not a laptop tunnel. Beyond the Bazaar: mention the endpoint in MCP marketplaces, agent directories (ClawRouter-style local proxies, dev communities), and pair it with an agent.json A2A card. Expect near-zero traffic at first; the compounding asset is the standing paywalled endpoint that other agents can discover later. This is a storefront play, not a get-rich-quick — but it is one of the few income streams an autonomous agent can run end-to-end without a human in the loop."),
            ("h2", "Verdict"),
            ("p", "x402 is real, production-grade (Linux Foundation, millions of transactions) and the seller side is genuinely open — no KYC, no platform approval, just an API and a Base wallet. The March-2026 '477 sellers vs 4,400 buyers' window has partially closed, but differentiated data endpoints (live funding rates, curated verified research, niche feeds) still clear $0.5-2K/month for the top sellers. Free to start on testnet; mainnet costs only Base gas (~$1-3) and hosting. Worth building once and letting it sit."),
        ],
    },
    {
        "slug": "hertzflow-merits-airdrop-guide",
        "title": "HertzFlow Merits Airdrop: Genesis Vault Deposits, 10x Boost &amp; the $10 Minimum",
        "date": "2026-08-22",
        "tags": ["bsc", "confirmed", "deposit", "perps"],
        "body": [
            ("h2", "What HertzFlow is"),
            ("p", "HertzFlow is a self-custodial perpetuals protocol on BNB Chain running an RFQ model against isolated LP pools (no order book), up to 500x leverage across crypto, FX, commodities and equities, USDT collateral. It came out of YZi Labs' EASY Residency Season 2 (Dec 2025), YZi Labs is the only named backer, no disclosed funding. Mainnet went live in August 2026 and the Genesis Vault pre-deposit opened the same week."),
            ("h2", "The airdrop: confirmed, but deposit-only"),
            ("p", "HertzFlow has confirmed both a token generation event and an airdrop. Official docs describe Merits — the reward points — as your weight in the airdrop: at TGE they convert into an allocation and reset to zero. Neither the allocation size nor the TGE date has been published. Season 1 runs entirely through the Genesis Vault: every Merit comes from supplying liquidity. There are NO free tasks that earn Merits (binding X/Discord is optional and only registers you for future campaigns)."),
            ("h2", "Genesis Vault parameters (verified from official docs)"),
            ("p", "Deposit assets: USD1 or U on BNB Chain (the flow swaps other tokens in). Minimum: $10 after any deposit fee. Phase 1 caps: 4.44M USD1 and 8.88M U, first-come-first-served — deposits close for everyone once a cap fills. Boost: 10x Merits on any single deposit held 90 continuous days; 89 days earns base rate only. Merits accrue per period from a fixed pool split by vault share; no claim step, credited automatically."),
            ("h2", "The 90-day clock mechanics"),
            ("p", "Each deposit has its own clock; topping up never resets older deposits. Withdrawals hit the newest deposits first (protecting the oldest). Vault shares are transferable, but a transfer counts as withdrawal+new deposit — it restarts that amount's clock. Withdrawing early forfeits only the 10x boost on that amount, not the base Merits."),
            ("h2", "Strategy and verdict"),
            ("p", "Deposit early (caps are FCFS), split larger amounts into multiple deposits to preserve flexibility, and watch your live estimate rather than rank. This is a capital-locked farm: $10 minimum, 90 days for the boost, unknown allocation size and TGE date. It only makes sense with money you are comfortable leaving parked — treat the airdrop as a bonus on top of the vault yield, not the primary return. If you do not want capital locked in a protocol whose allocation is unquantified (Ceffu custody is named as the custody path), skip it — there are zero-cost testnet farms with better risk profiles (see our testnet landscape article)."),
        ],
    },
    {
        "slug": "xreign-reign-airdrop-guide",
        "title": "XREIGN $REIGN Airdrop Guide: Free X-Reputation Mint, $USDT Bonus &amp; 40% Community Allocation",
        "date": "2026-08-24",
        "tags": ["x", "confirmed", "free", "points"],
        "body": [
            ("h2", "What XREIGN is"),
            ("p", "XREIGN is a behavioral-AI project that pays for X (Twitter) reputation and predictions. Its 'Signal Lab' runs hourly rounds where users pick the rare human signal; the crowd's choices are used to train a predictive model. The reward economy runs on $REIGN (1B fixed supply) plus live $USDT prizes. Verified on Aug 24, 2026 from the official site (xreign.app) and its tokenomics page."),
            ("h2", "Airdrop status: confirmed, free, TGE imminent"),
            ("p", "Token generation event is confirmed. Official site lists planned TGE in August 2026; promoter posts (Wizard Airdrops, 0xRyze) say September 2026 — either way the window is weeks, not months. 40% of supply (400M $REIGN) goes to Community & rewards with NO cliff: mint, tasks, wheel spins, Signal rounds, streaks and referrals are snapshot-gated and claimable at TGE. Seed round: $1.5M closed at $15M FDV (investors under NDA), TGE price $0.05. Rest of supply: Signal treasury 12%, ecosystem 12%, team 12% (12-mo cliff), seed 10% (6-mo cliff), liquidity 8%, treasury 6%."),
            ("h2", "How to farm (all free)"),
            ("p", "1) Go to xreign.app/login and sign in with X (OAuth — this is the one manual step). 2) Mint your starting balance: up to 6,000 $REIGN based on account signals (age, followers, verification, activity) plus a guaranteed $USDT starting bonus. 3) Daily: check-in streak (7-day rolling cycle), one Reign Wheel spin ($USDT prizes from the Season pool, credited instantly), hourly Signal Lab rounds (1-5 $REIGN each). 4) Tasks: verified X actions and on-platform quests. 5) Referrals: invite other accounts before TGE."),
            ("h2", "Caveats and honest verdict"),
            ("p", "(1) Needs a real X account — X OAuth + browser, so this is not automatable with anonymous wallets; one account per human. (2) Live economy counters on the site showed placeholder zeros during verification; the project is early and small ($1.5M seed, investors undisclosed). (3) The 6,000 REIGN mint at $0.05 = $300 paper value is marketing math — real value depends on TGE price vs. points inflation and how the snapshot weights activity. (4) Token is confirmed, so unlike pure points-farms this has a defined claim path. Risk: low (free, no capital), reward: speculative. Verdict: worth 3 minutes a day if you already use X; skip if creating a dedicated account just for this."),
        ],
    },
    {
        "slug": "omega-olympus-pomega-claim-guide",
        "title": "Omega (Olympus) pOmega Claim Guide: Pay 0.003 SOL, Get 100 pOmega — Bot-Able, No Captcha (Verified API)",
        "date": "2026-08-25",
        "tags": ["solana", "prediction-markets", "confirmed", "bot-able", "new"],
        "body": [
            ("h2", "What Omega / Olympus is"),
            ("p", "Omega Network runs Olympus — a prediction DEX that combines prediction markets with a classic exchange (swap, leverage, order book) on one dashboard. The official testing token is pOmega (supply ~100B, live on Solana mainnet as an SPL mint). The team states that every claimed pOmega converts to the main token at TGE. No TGE date has been announced; airdrops.io lists the campaign as confirmed with a 12° rating. We verified the claim mechanism hands-on on Aug 25, 2026 by reverse-engineering the app's API — the details below are from live endpoints, not marketing pages."),
            ("h2", "The claim mechanic (verified, and it is bot-able)"),
            ("p", "Unlike most testnet farms, Omega's pre-claim has NO captcha and NO wallet-connect requirement: you pay a tiny anti-sybil fee in real crypto, and the server credits 100 pOmega to your wallet. Live config (Aug 25, 2026): Solana — pay 0.003 SOL (~$0.30) to treasury FTCQPhg846q25KuVkQa6Nyb2TYPJjdYayqWdSLBijPBX, receive 100 pOmega (mint F4qwrc58A9wc2diubqdik5pnagBFJ2SdPMDue6Jdme6s). EVM — Base (chain 8453) and Ethereum (chain 1) accept ~0.0000957 ETH (~$0.24) to treasury 0x4d467E27F0CF402E958CC7Bb47aE258F00ABCD41; Arbitrum is enabled but currently dry (contract liquidity 0). Each claim is a plain transfer transaction (21k gas on EVM / legacy transfer on Solana) followed by POST /api/{chain}-pre-claim/complete {signature, wallet, preAmount} — the server verifies the on-chain payment and airdrops the tokens."),
            ("h2", "On-chain verification (the numbers are real)"),
            ("p", "Checked against Solana mainnet on Aug 25, 2026: pOmega total supply 99,999,999,400 (100B minus burn); the distributor treasury holds ~138.3M pOmega ready to pay out and 0.588 SOL of collected fees — roughly 195 claims have gone through so far, so this is still an early, funded campaign. The client-side code contains no cooldown or per-wallet claim limit ('claim as many times as you want during beta' is the stated rule), which is consistent with the anti-sybil fee being the only gate. Note: server-side rate limits can always exist even if the client has none — start with one claim per wallet and scale up."),
            ("h2", "How to farm it"),
            ("p", "1) Fund a wallet with 0.005 SOL (Solana) or ~0.0002 ETH (Base) — enough for several claims. 2) Check status at /api/solana-pre-claim/status?wallet=YOUR_ADDRESS (fields: enabled / claimed / hasPriorClaim). 3) Send the fee to the treasury and submit the /complete call — the whole loop is scriptable with any Solana/EVM SDK. 4) Trade or predict on Olympus with the claimed pOmega — the DEX shows a live pOmega/mUSDC market (24h volume ~$230K at verification time) — or just hold for TGE conversion. Repeat daily or weekly; each claim costs ~$0.24-0.30."),
            ("h2", "Economics and honest verdict"),
            ("p", "Cost per claim: ~$0.24 (Base) to ~$0.30 (Solana) for 100 pOmega. The DEX price (~$0.13/pOmega) is a test-economy price against testnet mUSDC — do NOT multiply 100 × $0.13 and call it profit; the realizable value is whatever the TGE conversion ratio delivers, which is unannounced. Treat this as a cheap lottery ticket with verified mechanics: $3 of fees buys ~1,000-1,250 pOmega of conversion-eligible supply. Risks: no TGE date, no conversion ratio, token price could be negligible, and the team could change claim rules at any time. Upside: it is one of the few confirmed campaigns an automated agent can farm end-to-end without captchas or a human — if you are already running bots, this one pays for its own gas in one line of code. Update Aug 26, 2026: airdrops.io rating jumped from 12° to 417° — the campaign is drawing attention fast, so claim early while the fee stays at the beta level."),
        ],
    },
    {
        "slug": "flop-labs-flop-airdrop-guide",
        "title": "Flop Labs $FLOP Airdrop Guide: Arthur Hayes' AI Settlement Layer — 20% of Supply to Testnet Participants (Confirmed)",
        "date": "2026-08-26",
        "tags": ["ai-agents", "confirmed", "new", "arthur-hayes", "testnet"],
        "body": [
            ("h2", "What Flop is"),
            ("p", "Flop is a settlement layer for AI agents, announced by BitMEX co-founder Arthur Hayes on August 18, 2026 with one line: 'FLOP is food for your AI agent.' Agents would spend $FLOP on compute, inference and stored memory. The project is confirmed with no pre-sale and no VCs — a fair launch. It is led by Flop Labs; Hayes' essays (Substack) carry the most detail, including the allocation figures. Verified Aug 26, 2026 from flop.finance and the airdrops.io listing (confirmed badge)."),
            ("h2", "Airdrop details"),
            ("p", "Airdrop is confirmed. Hayes' August 19 essay puts roughly 20% of total supply with testnet participants, distributed over ten years. Timeline: testnet opens some time in Q4 2026, airdrop targeted for Q4 2026, genesis block Q1 2027. Eligibility rules and snapshot dates are NOT published yet. No chain has been named — do not configure wallets for a specific network yet. No whitepaper yet either; treat circulating hardware requirements for mining as unverified."),
            ("h2", "What you can do today (all free)"),
            ("p", "1) Follow @flop_labs on X and turn on notifications — the only published eligibility requirement, and where testnet dates land first. 2) Follow @CryptoHayes and his Substack — terms surface there first. 3) Apply for a network role: three forms are open at flop.finance/apply — GPU provider/miner, validator, and KOL/creator. The KOL route is the lowest barrier: a few solid posts plus the form. The forms are Google Forms and ask for X/Telegram IDs and audience details; submitting one is a manual (human) step. 4) Start publishing $FLOP content now — if scoring ends up mindshare-based it may be applied retroactively. 5) Prepare for the Q4 testnet: the 20% allocation is earned on testnet, so the real farm starts when it goes live."),
            ("h2", "Honest verdict"),
            ("p", "Flop is as early as an airdrop gets: confirmed distribution, named allocation size, no VC overhang — but no whitepaper, no named chain, no live testnet. Everything available today is free (follow + application forms), and the testnet farm (Q4 2026) is the actual prize. For automated farmers: the testnet itself is the bot-able part once live; the current role forms are Google Forms (anti-bot). Watch for the testnet announcement — the 20% allocation over ten years suggests patient, real participation is rewarded over sybil spam."),
        ],
    },
]

def render_article(a):
    html = [f"<article><h1>{a['title']}</h1><p class='meta'>{a['date']} · tags: {', '.join(a['tags'])}</p>"]
    for kind, text in a["body"]:
        html.append(f"<{kind}>{text}</{kind}>")
    html.append("</article>")
    return "\n".join(html)

def render_index(articles):
    # index lists every .html in the site dir (articles generated from ARTICLES
    # plus any manually added pages like RU guides), newest first by date tag.
    import re
    items = []
    for f in sorted(os.listdir(OUT)):
        if not f.endswith(".html") or f == "index.html":
            continue
        slug = f[:-5]
        meta = next((a for a in articles if a["slug"] == slug), None)
        if meta:
            title, date, tags = meta["title"], meta["date"], ", ".join(meta["tags"])
        else:
            title = slug.replace("-", " ").title()
            date = ""
            tags = ""
            try:
                raw = open(os.path.join(OUT, f), encoding="utf-8").read(2000)
                m = re.search(r"<h1>(.*?)</h1>", raw)
                if m:
                    title = m.group(1)
            except Exception:
                pass
        items.append((date, f"<li><a href='{f}'>{title}</a><br>"
                          f"<span class='meta'>{date} · {tags}</span></li>"))
    items.sort(key=lambda x: x[0], reverse=True)
    lis = "".join(x[1] for x in items)
    return (f"<h1>Airdrop Guides</h1>"
            f"<p>Fresh airdrop farming guides, updated {datetime.date.today().isoformat()}. "
            f"{len(items)} articles.</p><ul>{lis}</ul>"
            f"<h2>About this site</h2>"
            f"<p>Independent guides to airdrop and testnet farming: what to join, what to skip, "
            f"and how to do it safely. No paid promotions — projects that require gambling or "
            f"capital deposits are flagged as such.</p>")

TEMPLATE = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{kw}">
<style>body{{font-family:system-ui,sans-serif;max-width:760px;margin:2rem auto;padding:0 1rem;line-height:1.6;color:#222}}
h1{{font-size:1.6rem}}h2{{margin-top:2rem;font-size:1.2rem}}.meta{{color:#777;font-size:.85rem}}
a{{color:#1a5fb4;text-decoration:none}}</style></head>
<body>{content}
<footer><p><a href="index.html">← All guides</a></p></footer></body></html>"""

def build():
    os.makedirs(OUT, exist_ok=True)
    for a in ARTICLES:
        desc = a["body"][1][1][:150]
        kw = ", ".join(a["tags"])
        html = TEMPLATE.format(title=a["title"], desc=desc, kw=kw, content=render_article(a))
        with open(os.path.join(OUT, a["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(html)
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(TEMPLATE.format(title="Airdrop Guides", desc="Airdrop farming guides 2026",
                                kw="airdrop, testnet, crypto guides",
                                content=render_index(ARTICLES)))
    # robots + sitemap
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write("User-agent: *\nAllow: /\n")
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        slugs = [a["slug"] for a in ARTICLES]
        for fn in sorted(os.listdir(OUT)):
            if fn.endswith(".html") and fn not in ("index.html",) and fn[:-5] not in slugs:
                slugs.append(fn[:-5])
        urls = "\n".join(f"<url><loc>https://mkiv001-1.github.io/airdrop-guides/{s}.html</loc></url>"
                         for s in slugs)
        f.write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    print(f"Built {len(ARTICLES)} articles in {OUT}")

if __name__ == "__main__":
    build()
