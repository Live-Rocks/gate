import json
from collections import defaultdict
from datetime import datetime

# 从文件中读取交易所数据
with open('exchange_data.json', 'r') as f:
    exchange_data = json.load(f)

# 初始化统计数据结构
yearly_new_exchanges = defaultdict(lambda: {'count': 0, 'names': []})

for exchange in exchange_data:
    created_date = exchange.get('created_date')
    name = exchange.get('name', 'N/A')

    if created_date:
        try:
            created_year = datetime.strptime(created_date, '%Y-%m-%dT%H:%M:%S.%fZ').year
            yearly_new_exchanges[created_year]['count'] += 1
            yearly_new_exchanges[created_year]['names'].append(name)
        except ValueError:
            print(f"Error parsing date: {created_date}")

# 计算总交易所数量
total_exchanges = sum(year_data['count'] for year_data in yearly_new_exchanges.values())

# 打印每年的新增交易所数量和名称
current_year = datetime.now().year
for year in range(2011, current_year + 1):
    count = yearly_new_exchanges[year]['count']
    names = ', '.join(yearly_new_exchanges[year]['names'])
    print(f"Year: {year}, New Exchanges: {count}, Names: {names}")

# 打印总交易所数量
print(f"Total Exchanges: {total_exchanges}")
