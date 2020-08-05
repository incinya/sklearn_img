import base64
import execjs


def parse_gs(js_code):
    f = r"""
    target_js_code
    
    function ss(){
        return g_s
    }

    """
    f = f.replace('target_js_code', js_code)
    aa = execjs.compile(f)
    b = aa.call('ss')
    pp = base64.b64decode(b).decode("utf8")
    return pp
