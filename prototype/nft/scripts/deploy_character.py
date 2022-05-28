from scripts.helpful_scripts import get_account, get_contract
from brownie import RandomCharacter, network, config

def deploy():
    account = get_account()
    print(f"On network {network.show_active()}")
    fee = 0.1 * 10**18
    contract = RandomCharacter.deploy(
        config["networks"][network.show_active()]["vrf_coordinator"],
        config["networks"][network.show_active()]["link_token"],
        config["networks"][network.show_active()]["keyhash"],
        fee,
        {"from": account},
        publish_source=True
    )

def main():
    deploy()