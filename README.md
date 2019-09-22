# EthereumSmartContractCrawler
This is a crawler using Python 3 to crawl the source code of the Ethereum smart contract.(From etherscan verified contracts ). 
This crawler is based on the following Python third-party libraries:
1. requests
2. re
3. BeautifulSoup

Because of the use of requests and re libraries, the crawler speed is slow. In my use, it takes about __ten seconds__ to crawl the source code of a contract. So when you start running it, you can go to dinner.

# Quantity and limitation
The crawler can crawl the source code of up to 500 smart contracts at a time.
But the crawler won't crawl contracts in multi-file format.

# Usage
```
python main.py
```

# Attention
When you use it, the crawler asks you to set two paths.
1. The first is the path through which the source code files of smart contracts are stored. All contracts can be named __addressOfContract.sol__
2. The second is the path to the file that stores the URLs of 500 contracts.

The two paths can be the same, but the correct path must be given.

# License
All codes of this program are released under the MIT License.


