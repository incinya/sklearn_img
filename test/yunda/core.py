from re_test import data_processing
from yun import parse_gs
from yunda import get_g_s

js_code = get_g_s()
res = parse_gs(js_code)
out = data_processing(res)
print(out)
