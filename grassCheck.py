import requests
import json


# 从txt文件中读取钱包地址
def get_wallet_addresses(file_path):
    with open(file_path, 'r') as file:
        addresses = [line.strip() for line in file]
    return addresses


# 定义请求的函数
def get_airdrop_allocation(wallet_address):
    url = 'https://api.getgrass.io/airdropAllocations'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://www.grassfoundation.io',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.grassfoundation.io/',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'priority': 'u=1, i'
    }
    # 构建请求参数
    params = {
        'input': json.dumps({"walletAddress": wallet_address})
    }

    # 发送GET请求
    response = requests.get(url, headers=headers, params=params)

    # 检查响应状态并返回结果
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to retrieve data for wallet {wallet_address}. Status code: {response.status_code}"}


# 主函数
def main():
    file_path = 'wallet_addresses.txt'  # 存放钱包地址的文件
    wallet_addresses = get_wallet_addresses(file_path)

    # 遍历每个钱包地址并获取空投分配
    for wallet_address in wallet_addresses:
        result = get_airdrop_allocation(wallet_address)
        print(f"Results for {wallet_address}: {result}")


# 执行主函数
if __name__ == "__main__":
    main()
