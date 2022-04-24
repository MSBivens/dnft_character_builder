This write up serves to provide additional direction and clarity during the initial development process. 

Here is the link to the wireframe: https://miro.com/app/board/uXjVO64iY1k=/?share_link_id=495672257442 

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

## Chainlink Integration
- VRF https://chain.link/chainlink-vrf 
    Using this, characters can randomize character options


## Helpful Links 
What Is a Dynamic NFT? https://blog.chain.link/what-is-a-dynamic-nft/ 
How to Build Dynamic NFTs on Polygon https://blog.chain.link/how-to-build-dynamic-nfts-on-polygon/ 

## Basic Components
Here are some of the basic components for the project
- Wallet Sign In / Registration
- Statistics mechanism
- dNFTs
- Smart Contracts
    - Mint basic dNFT
    - Update dNFT (this changes the traits and appearance)


## Expansions
This section lists out the ideas for additional features. This is ONLY for if we have enough time, and all of these are up for debate. Anything we want but don't have time for can be added to the roadmap and implemented after the hackathon by us or others.
- Additional traits to customize character
- Additional options for already implemented traits
- Special Items: these would be items not available by default
    - This is in consideration because it would replicate how earned items are unlocked for use by a character in a game
    - These would be their own NFTs that if a wallet has access to, can be applied to a character
- Special Item Inventory (reliant on previous expansion)
    - Inventory displaying the special items you have and who each one is attached to
- Statistics Page; a page where it shows the rarest characters, and rarest pieces by category
    - These examples focus on a single character and not a page showing rarest pieces but they help to get an idea
    - EX1: https://app.traitsniper.com/the-plague?view=754 
    - EX2: https://raritysniper.com/nyokies/942 
    - EX3: https://rarity.tools/chillbearclub-genesis/view/1?filters=%24Mouth%240%3Atrue 