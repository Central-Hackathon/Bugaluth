App = {
  web3Provider: null,
  contracts: {},
  users: null,

  init: function() {

    return App.initWeb3();
  },

  initWeb3: function() {
    // Is there an injected web3 instance?
    if (typeof web3 !== 'undefined') {
      App.web3Provider = web3.currentProvider;
    } else {
      // If no injected web3 instance is detected, fall back to Ganache
      App.web3Provider = new Web3.providers.HttpProvider('http://localhost:7545');
    }
    web3 = new Web3(App.web3Provider);

    return App.initContract();
  },

  initContract: function() {
    $.getJSON('EcoChainTokenDemo.json', function(data) {
      // Get the necessary contract artifact file and instantiate it with truffle-contract
      var EcoChainTokenArtifact = data;
      App.contracts.EcoChainToken = TruffleContract(EcoChainTokenArtifact);

      // Set the provider for our contract
      App.contracts.EcoChainToken.setProvider(App.web3Provider);

      // get data from contract
      return App.getContractData();
    });
  },

  getContractData: function() {
    var tokenInstance;

    App.contracts.EcoChainToken.deployed().then(function(instance) {
      tokenInstance = instance;

      return tokenInstance.getUsers.call();
    }).then(function(users) {
      if (users !== undefined) {

        App.users = users;
        console.log(App.users);
        for (i = 0; i < App.users.length; i++) {
          tokenInstance.getBalanceOf.call(App.users[i]).then(function(data) {
            App.addUser(data[1], data[0]);
          });

        }
      }
    }).catch(function(err) {
      console.log(err.message);
    });

    // return App.showTokens();
  },

  addUser: function(user, tokens) {
    var ul = document.getElementById("user-list");

    var li = document.createElement("li");
    li.setAttribute("id", user);
    li.setAttribute("class", "list-group-item");
    li.appendChild(document.createTextNode(user));
    // li.appendChild(document.createTextNode(user + " has " + tokens + " tokens."));

    var badge = document.createElement("span");
    badge.setAttribute("class", "badge")
    badge.appendChild(document.createTextNode(tokens));

    li.appendChild(badge);
    ul.appendChild(li);
  },

};

$(function() {
  $(window).load(function() {
    App.init();
  });
});
