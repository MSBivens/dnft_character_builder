// contracts/MyNFT.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";


//Polygon (Matic) Mumbai Testnet
// const POLYGON_VRF_COORDINATOR = '0x7a1BaC17Ccc5b313516C5E16fb24f7659aA5ebed'
// const POLYGON_LINKTOKEN = '0x326C977E6efc84E512bB9C30f76E30c160eD06FB'
// //500 gwei keyhash
// const POLYGON_KEYHASH = '0x4b09e658ed251bcafeebbc69400383d49f344ace09b9576fe248bb02c003fe9f'

contract CustomCharacter is ERC721, VRFConsumerBase {

    bytes32 internal keyHash;
    uint256 internal fee;
    uint256 public randomResult;
    address public vrfCoordinator;

    //basic prototype object
    struct Character {
        string name;
        string background;
        string hair;
        string skin;
        string clothes;
        string item;
        string pet;
        string description;
    }

    //A list of characters created
    Character[] public characters;

    //mappings
    mapping(bytes32 => string) requestToCharacterName;
    mapping(bytes32 => address) requestToSender;
    mapping(bytes32 => uint256) requestToTokenId;

    /**
     * Constructor inherits VRFConsumerBase
     * 
     * Network: Polygon mumbai testnet
     * Chainlink VRF Coordinator address: 0x7a1BaC17Ccc5b313516C5E16fb24f7659aA5ebed
     * LINK token address:                0x326C977E6efc84E512bB9C30f76E30c160eD06FB
     * Key Hash: 0x4b09e658ed251bcafeebbc69400383d49f344ace09b9576fe248bb02c003fe9f

     */

    constructor(address _VRFCoordinator, address _LinkToken, bytes32 _keyHash) public
    VRFConsumerBase(_VRFCoordinator, _LinkToken)
    ERC721("CustomCharacter", "CustomCharacter") {
        vrfCoordinator = _VRFCoordinator;
        keyHash = _keyhash;
        fee = 0.1 * 10**18; // defaulting to 0.1 LINK
    }

    //This function below requests a random number from the VRF
    function requestNewRandomCharacter (uint256 userProvidedSeed, string memory name) public returns (bytes32) {
        bytes32 requestId = requestRandomness(keyHash, fee, userProvidedSeed);
        //The random number request is going to be associated with the character name given
        requestToCharacterName[requestId] = name;
        //the owneer of the NFT
        requestToSender[requestId] = msg.sender;
        return requestId;
    }

    function fulfillRandomness(bytes32, requestId, uint256 randomNumber) internal override {
        //defines NFT creation
        //utilize random number to generate randomness to the characters traits
        //maybe RGBA color or pulls a randomly from a list of clothing
        uint256 newId = character.length;


        characters.push(
            Character(
                //other traits go here
                requestToCharacterName[requestId]
            )
        );
        //From openzeppelin ERC721
        _safeMint(requestToSender[requestId], newId);
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "ERC721: transfer caller is not owner nor approved"
        );
        //This allows for image rendering
        _setTokenURI(tokenId, _tokenURI);
    }
}