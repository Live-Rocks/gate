Dune page: https://dune.com/aa5961311/exchange-2011-2024 
<br/>
<h4>每年新增交易所數量 (排除日交易量小於1百萬美元交易所)</h4>

1. fetch_exchanges.py 搜集資料，存成json檔
2. process_exchanges.py 整理篩選結果，存成resuit檔
3. 到Dune生成圖表


<h4>每年倒閉交易所數量 (排除日交易量小於1百萬美元交易所)</h4>
未完成
CoinGecko和CoinMarketCap的API似乎沒提供已關閉交易所的資訊
有從官方文檔找到不活躍交易所、未被追蹤項目的api，但裡面的交易量都是0
