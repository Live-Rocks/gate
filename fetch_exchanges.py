import requests
import json
import time

# 设置API密钥
headers = {
    'X-CMC_PRO_API_KEY': '620ad0cb-58b3-43da-bfa3-bc8ee64a3f87',
}

# 获取交易所列表
response = requests.get('https://pro-api.coinmarketcap.com/v1/exchange/map', headers=headers)
if response.status_code == 200:
    exchanges = response.json().get('data', [])
    print("Fetched exchange list successfully.")
else:
    print("Error fetching exchange list:", response.status_code, response.json())
    exchanges = []

# 获取每个交易所的详细信息
exchange_data = []
request_count = 0

for exchange in exchanges:
    if request_count >= 30:  # 确保每分钟不超过30次请求
        print("Rate limit reached, sleeping for 60 seconds...")
        time.sleep(60)
        request_count = 0

    exchange_id = exchange.get('id')
    if not exchange_id:
        continue

    details_response = requests.get(f'https://pro-api.coinmarketcap.com/v1/exchange/info?id={exchange_id}', headers=headers)
    request_count += 1

    if details_response.status_code == 200:
        details = details_response.json().get('data', {}).get(str(exchange_id), {})
        
        # 打印详细信息以检查数据结构
        print(f"Details for exchange ID {exchange_id}: {details}")
        
        daily_volume_usd = details.get('spot_volume_usd', 0)
        if daily_volume_usd and daily_volume_usd >= 1_000_000:  # 排除日交易量小于100万美元的交易所
            exchange_info = {
                'name': details.get('name', 'N/A'),
                'created_date': details.get('date_launched', 'N/A'),
                'daily_volume_usd': daily_volume_usd
            }
            exchange_data.append(exchange_info)
            print(f"Added exchange: {exchange_info}")
        else:
            print(f"Exchange {details.get('name', 'N/A')} has insufficient daily volume: {daily_volume_usd}")
    else:
        print(f"Error fetching details for exchange ID {exchange_id}: {details_response.status_code}, {details_response.json()}")

# 检查是否收集到了数据
if not exchange_data:
    print("No exchange data collected.")
else:
    print(f"Collected data for {len(exchange_data)} exchanges.")

# 将数据保存到文件中
with open('exchange_data.json', 'w') as f:
    json.dump(exchange_data, f)

print("Exchange data fetched and saved to exchange_data.json successfully.")
