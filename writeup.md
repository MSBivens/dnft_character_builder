This write up serves to provide additional direction and clarity during the initial development process. 

Here is the link to the wireframe (draft!): [Link](https://miro.com/app/board/uXjVO64iY1k=/?share_link_id=495672257442) 

## Informal Description
The dNFT Character Generator allows users to freely mint a base dNFT character (via Polygon). They can customize and edit their character with the available options. Using Chainlink's VRF, users can randomize thier character's traits.

This project can be forked by any dev looking to implement the system in their own game, they would only have to edit it to work directly with it. We are building a working demo and template they can see to understand how and why dNFTs should be used in their game. 

## Version1 of the website will allow a user to:
- Log In / Register via an Ethereum Wallet, e.g. MetaMask
- Mint their base dNFT, 
    - NOTE: v1 will only have one base option
- Customize (and edit) their dNFT 
    - Name, 5 trait options, and description
- View Dashboard 
    - View their characters and their stats
- Read the about
    - Basic information about the project and us as the devs

NOTE: Filecoin can store everything for us including the website.

## Chainlink Integration
- [VRF](https://chain.link/chainlink-vrf) 
    - Using this, characters can randomize character options


## Helpful Links 
[Ultimate Guide: How to Build Ethereum dApps](https://moralis.io/ultimate-guide-how-to-build-ethereum-dapps/)
[Chainlink Spring Hackathon page](https://chain.link/hackathon)
[Chainlink Spring hackathon devpost](https://chainlinkspring2022.devpost.com/) 
[Chainlink Docs](https://docs.chain.link/docs/hackathon-rules-waiver-release-and-code-of-conduct/?utm_campaign=Spring%20%2722%20Hackathon&utm_medium=email&_hsmi=210744206&_hsenc=p2ANqtz-_rTTH_WT6W0TQAX2sIH1rtD9mo4VR9p_uZiTHTRO6xsaqls2PtZY_4zh6F0vy981EZQPuHaPkoJtsZMTl84nABCv7Ohw&utm_content=210744206&utm_source=hs_email) 
[What Is a Dynamic NFT?](https://blog.chain.link/what-is-a-dynamic-nft/) 
[How to Build Dynamic NFTs on Polygon](https://blog.chain.link/how-to-build-dynamic-nfts-on-polygon/) 
[Team Collaboration With GitHub](https://code.tutsplus.com/articles/team-collaboration-with-github--net-29876) 
[Difference b/t UI & UX](https://webflow.com/blog/ux-vs-ui-design?utm_source=google&utm_medium=search&utm_campaign=general-paid-workhorse&utm_term=keyword-targeting&utm_content=dynamic-search-ads-t1&gclid=Cj0KCQjw6pOTBhCTARIsAHF23fK8HxOiNnMRsGFXBGgZt0DGB0PCeAnN_uJ9eHWD-Cv0ll5FjNyO4gYaAhaREALw_wcB)


## Basic Components
Here are some of the basic components for the project
- Wallet Sign In / Registration
- Statistics mechanism
- dNFTs
- Smart Contracts
    - Mint basic dNFT
    - Update dNFT (this changes the traits and appearance)

## Roles
| Role | Person | Description |
| --- | --- | --- |
| Front End Basics | Jared | Create a clickable MVP front-end |
| User Interface | Jared | Advanced front-end work |
| User Experience | TBD | Drives overall experience of the dApp |
| Scanning Wallet | TBD | Scan wallet to find and pull dNFT information |
| Wallet Access | Mike | Account access to website |
| Minting & Updating dNFT | Eric | Smart contract for minting & updating dNFT |
| Deployer | Frank | Manages deploying dApp to Filecoin or IPFS |
| Trait Builder | Eric | Creates the customization options |
| Copywriting | TBD | Create the copy |
| Repo Manager | Mike | Manage push/pull requests |
| Customizer | Mike | Create the customizer (not the smart contract) |
| Art | Mike | Create the artwork for the customization |
<!-- | X | TBD | X | -->

## Guidelines for development
Commit to master often, e.g. after writing a working method, fixing typos, fixing indentation
Commit to a branch (you'll have to make one) if what you're committing would break the build or isn't done yet
Comment what each function/method does, where new sections begin (navigation/container/footer)

## Product Backlog
This section lists out the ideas for additional features. This is ONLY for if we have enough time, and all of these are up for debate. Anything we want but don't have time for can be added to the roadmap and implemented after the hackathon by us or others.
- Advanced user settings (TBD what these could be) e.g. light/dark mode
- Additional traits to customize character (e.g. frames?)
- Additional options for already implemented traits
- Special Items: these would be items not available by default
    - This is in consideration because it would replicate how earned items are unlocked for use by a character in a game
    - These would be their own NFTs that if a wallet has access to, can be applied to a character
    - If implemented, would need to create one for us (maybe special item only enough minted for each of us, like a founding team item or even a contributor item?)
- Special Item Inventory (reliant on previous backlog item)
    - Inventory displaying the special items you have and who each one is attached to
- Statistics Page; a page where it shows the rarest characters, and rarest pieces by category
    - These examples focus on a single character and not a page showing rarest pieces but they help to get an idea
    - [EX1](https://app.traitsniper.com/the-plague?view=754)
    - [EX2](https://raritysniper.com/nyokies/942)
    - [EX3](https://rarity.tools/chillbearclub-genesis/view/1?filters=%24Mouth%240%3Atrue)
