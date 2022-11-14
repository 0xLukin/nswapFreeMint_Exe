import json
import time

import requests
from web3 import Web3
from eth_account import  Account

# bsc_url = "https://bsc.getblock.io/mainnet/?api_key=259ca811-276f-4f8e-937d-e0e8a65d4d22"
#bsc_url = "https://bsc-dataseed1.defibit.io/"
bsc_url = "https://rpc.ankr.com/bsc"
# BscTest_url = "https://data-seed-prebsc-1-s1.binance.org:8545/"
BscTest_url = 'https://data-seed-prebsc-1-s1.binance.org:8545/'
request_url = 'https://ad.magdao.tech'
# request_url = 'https://wgsj.moguldesign.shop'

web3 = Web3(Web3.HTTPProvider(bsc_url))  # 建立连接


Main_address = input("Gas消耗地址：")
Main_key = input("私钥：")

Mint_address = input("Mint合约地址：")
Mint_abi= json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"ApprovalCallerNotOwnerNorApproved","type":"error"},{"inputs":[],"name":"ApprovalQueryForNonexistentToken","type":"error"},{"inputs":[],"name":"BalanceQueryForZeroAddress","type":"error"},{"inputs":[],"name":"MintERC2309QuantityExceedsLimit","type":"error"},{"inputs":[],"name":"MintToZeroAddress","type":"error"},{"inputs":[],"name":"MintZeroQuantity","type":"error"},{"inputs":[],"name":"OwnerQueryForNonexistentToken","type":"error"},{"inputs":[],"name":"OwnershipNotInitializedForExtraData","type":"error"},{"inputs":[],"name":"TransferCallerNotOwnerNorApproved","type":"error"},{"inputs":[],"name":"TransferFromIncorrectOwner","type":"error"},{"inputs":[],"name":"TransferToNonERC721ReceiverImplementer","type":"error"},{"inputs":[],"name":"TransferToZeroAddress","type":"error"},{"inputs":[],"name":"URIQueryForNonexistentToken","type":"error"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"fromTokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"toTokenId","type":"uint256"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"ConsecutiveTransfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"","type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"Received","type":"event"},{"anonymous":false,"inputs":[{"components":[{"internalType":"uint64","name":"stageNum","type":"uint64"},{"internalType":"uint64","name":"maxPerStage","type":"uint64"},{"internalType":"uint64","name":"maxPerAddress","type":"uint64"},{"internalType":"bool","name":"isWhiteListMintActive","type":"bool"},{"internalType":"bool","name":"isPublicMintActive","type":"bool"},{"internalType":"uint64","name":"beginTime","type":"uint64"},{"internalType":"uint64","name":"endTime","type":"uint64"}],"indexed":false,"internalType":"struct LeggiNFT.StageMintConfig","name":"config","type":"tuple"}],"name":"StageMintConfigChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"MAX_SUPPLY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"address","name":"","type":"address"}],"name":"addressMinted","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"metaURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint64","name":"quantity","type":"uint64"}],"name":"publicMint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"salePrice","type":"uint256"}],"name":"royaltyInfo","outputs":[{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint256","name":"royaltyAmount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"uint64","name":"stageNum","type":"uint64"},{"internalType":"uint64","name":"maxPerStage","type":"uint64"},{"internalType":"uint64","name":"maxPerAddress","type":"uint64"},{"internalType":"bool","name":"isWhiteListMintActive","type":"bool"},{"internalType":"bool","name":"isPublicMintActive","type":"bool"},{"internalType":"uint64","name":"beginTime","type":"uint64"},{"internalType":"uint64","name":"endTime","type":"uint64"}],"internalType":"struct LeggiNFT.StageMintConfig","name":"config_","type":"tuple"}],"name":"setStageMintConfig","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"tokenURI_","type":"string"}],"name":"setTokenURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"stageMintConfig","outputs":[{"internalType":"uint64","name":"stageNum","type":"uint64"},{"internalType":"uint64","name":"maxPerStage","type":"uint64"},{"internalType":"uint64","name":"maxPerAddress","type":"uint64"},{"internalType":"bool","name":"isWhiteListMintActive","type":"bool"},{"internalType":"bool","name":"isPublicMintActive","type":"bool"},{"internalType":"uint64","name":"beginTime","type":"uint64"},{"internalType":"uint64","name":"endTime","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalMinted","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"token","type":"address"}],"name":"withdrawTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]')

Rec_address = input("归集nft的地址：")
Num = int(input("要mint的数量："))

#创建eth地址
def createAddress():
    acct = Account.create('KEYSMASH FJAFJKLDSKF7JKFDJ 1530')
    return acct.address,Web3.toHex(acct.key)
# add,key = createAddress()
# print(add,key)

def mint(address,key):
    contract_address = Web3.toChecksumAddress(Mint_address)
    # BatchContract ABI

    main_add = Web3.toChecksumAddress(address)

    contract = web3.eth.contract(address=contract_address, abi=Mint_abi)
    # print(contract.all_functions())
    nonce = web3.eth.getTransactionCount(main_add)
    # print("nonce:"+str(nonce))
    gas_price = web3.eth.gasPrice

    txn = contract.functions.publicMint(1).buildTransaction({
        'nonce': nonce,
        'value': web3.toWei(0, 'ether'),
        'gas': 120000,
        'gasPrice': gas_price,
    })

    signed_tx = web3.eth.account.signTransaction(txn, key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    hash = web3.toHex(tx_hash)
    print(hash)
    res = web3.eth.wait_for_transaction_receipt(hash)
    return hash

def getId(hash):
    contract_address = Web3.toChecksumAddress(Mint_address)
    contract = web3.eth.contract(address=contract_address, abi=Mint_abi)

    tx_receipt = web3.eth.get_transaction_receipt(hash)
    rich_logs = contract.events.Transfer().processReceipt(tx_receipt)
    id = rich_logs[0]['args']['tokenId']
    print(id)
    return id

def transferNFT(address,key,id):
    to_address = Rec_address
    to_address = Web3.toChecksumAddress(to_address)
    contract_address = Web3.toChecksumAddress(Mint_address)
    main_add = Web3.toChecksumAddress(address)
    contract = web3.eth.contract(address=contract_address, abi=Mint_abi)

    nonce = web3.eth.getTransactionCount(main_add)
    # print("nonce:" + str(nonce))
    gas_price = web3.eth.gasPrice

    txn = contract.functions.transferFrom(main_add,to_address,int(id)).buildTransaction({
        'nonce': 1,
        'value': web3.toWei(0, 'ether'),
        'gas': 120000,
        'gasPrice': gas_price,
    })

    signed_tx = web3.eth.account.signTransaction(txn, key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    hash = web3.toHex(tx_hash)
    print(hash)
    res = web3.eth.wait_for_transaction_receipt(hash)
    return hash

# 发送BNB
def sendBNB(address):
    to_address = Web3.toChecksumAddress(address)

    gas = web3.eth.estimate_gas(
        {'to': to_address, 'value': web3.toWei(0.0012, 'ether')})
    # print(gas)
    gas_price = web3.eth.gasPrice
    tx = dict(
        nonce=web3.eth.get_transaction_count(Main_address),

        gas=gas,
        gasPrice=gas_price,
        to=to_address,
        value=web3.toWei(0.0012, 'ether'),
        chainId=56,
        )

    signed_txn = web3.eth.account.sign_transaction(tx,Main_key)

    hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    hash = Web3.toHex(hash)
    print(hash)
    res = web3.eth.wait_for_transaction_receipt(hash)
    return hash

def oneMint(address,key):
    hash = mint(address,key)
    id = getId(hash)
    transferNFT(address,key,id)

def one():
    address, key = createAddress()
    print(address, key)
    sendBNB(address)
    # print("发送BNB成功！")
    oneMint(address, key)


for i in range(Num):
    try:
        one()
        print("第" + str(Num) + "个Mint成功！")
    except Exception as e:
        print(e)

res = input("任务结束！")

