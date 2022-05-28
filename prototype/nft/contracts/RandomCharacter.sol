// contracts/MyNFT.sol
// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract RandomCharacter is ERC721, VRFConsumerBase {

    //Should be internal
    bytes32 public keyHash;
    address public vrfCoordinator;
    uint256 internal fee;
    uint256 public randomResult;
    string[] hairColors = ["Brown", "Black", "Blonde"];
    string[] avatarStyles = ["Default", "Circle", "Square"];
    string[] skinColors = ["Black", "Tan", "White"];

    struct Character {
        string hairColor;
        string avatarStyle;
        string skinColor;
        string name;
    }

    Character[] public characters;

    mapping(bytes32 => string) requestToCharacterName;
    mapping(bytes32 => address) requestToSender;
    mapping(bytes32 => uint256) requesttoTokenId;

    constructor(address _VRFCoordinator, address _LinkToken, bytes32 _keyHash, uint256 _fee)
        VRFConsumerBase(_VRFCoordinator, _LinkToken) 
        ERC721("RandomCharacter", "RNFT") {
            vrfCoordinator = _VRFCoordinator;
            keyHash = _keyHash;
            fee = _fee;
    }

    function requestNewRandomCharacter(uint256 userProvidedSeed, string memory name) public returns (bytes32) {
        bytes32 requestId = requestRandomness(keyHash, fee);
        requestToCharacterName[requestId] = name;
        requestToSender[requestId] = msg.sender;
        return requestId;
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomNumber) internal override {
        uint256 newId = characters.length;
        string memory hairColor = hairColors[randomNumber % 3];
        string memory avatarStyle = avatarStyles[randomNumber % 3];
        string memory skinColor = skinColors[randomNumber % 3];

        characters.push(
            Character(
                hairColor,
                avatarStyle,
                skinColor,
                requestToCharacterName[requestId]
            )
        );
        _safeMint(requestToSender[requestId], newId);
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "ERC721: transfer caller is not owner nor approved"
        );
        setTokenURI(tokenId, _tokenURI);
    }

}