var EcoChainToken = artifacts.require("EcoChainTokenDemo");

module.exports = function(deployer){
  deployer.deploy(EcoChainToken);
};
