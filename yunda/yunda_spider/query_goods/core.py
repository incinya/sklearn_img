from yunda_spider.query_goods.re_map import data_processing
from yunda_spider.query_goods.yun import parse_gs
from yunda_spider.query_goods.yunda import get_g_s

order_number = "4602680000002"
js_code = get_g_s(order_number)
res = parse_gs(js_code)
out = data_processing(res)
print(out)
