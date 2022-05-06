async function authenticate() {
    try {
        user = await Moralis.authenticate({ provider });
        web3 = await Moralis.enableWeb3({ provider });
    } catch (error) {
        console.log('authenticate failed', error);
    }
    renderApp();
}