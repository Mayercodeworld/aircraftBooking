import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
 
header = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'cookie': 'MKT_CKID=1730292097710.vfe09.t0j5; GUID=09031067118870597256; _RF1=58.20.33.185; _RSG=4oa3uKRszKEoheoV0XxD9A; _RDG=288a7d6c60cccb26a132310ea7062d44d5; _RGUID=e53dd9b5-380e-4c84-a24d-ee101fca8af2; _bfaStatusPVSend=1; _bfa=1.1730292107919.48jemx.1.1730511239226.1730511263081.4.2.101021; _ubtstatus=%7B%22vid%22%3A%221730292107919.48jemx%22%2C%22sid%22%3A4%2C%22pvid%22%3A2%2C%22pid%22%3A101021%7D; _jzqco=%7C%7C%7C%7C1730459716543%7C1.1303622818.1730292097712.1730511238884.1730511263120.1730511238884.1730511263120.0.0.0.53.53; _bfi=p1%3D101021%26p2%3D101021%26v1%3D2%26v2%3D1; _bfaStatus=success',
    'origin': 'https://flights.ctrip.com',
    'priority': 'u=1, i',
    'referer': 'https://flights.ctrip.com/schedule/csx.bjs.html?pageno=2',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}
url1 = 'https://flights.ctrip.com/schedule/'
# req = requests.get(url=url1,headers=header).text
# soup = BeautifulSoup(req,'html.parser')
# print(soup)
city = {'阿尔山': 'yie', '安阳': 'ayn', '阿勒泰': 'aat', '阿拉尔': 'acf',
         '阿拉善右旗': 'rht', '安康': 'aka', '阿克苏': 'aku', '鞍山': 'aog', 
         '安庆': 'aqg', '安顺': 'ava', '阿拉善左旗': 'axf', '毕节': 'bfj', 
         '北海': 'bhy', '博乐': 'bpl', '保山': 'bsd', '巴中': 'bzx', '布尔津': 'kji', 
         '白山': 'nbs', '北京': 'bjs', '百色': 'aeb', '巴彦淖尔': 'rlk', '包头': 'bav', 
         '成都': 'ctu', '常德': 'cgd', '长春': 'cgq', '朝阳': 'chg', '赤峰': 'cif', 
         '长治': 'cih', '重庆': 'ckg', '长沙': 'csx', '嘉义': 'cyi', '常州': 'czx', 
         '承德': 'cde', '郴州': 'hcz', '池州': 'juh', '大同': 'dat', '稻城': 'dcy', 
         '东莞': 'xho', '丹东': 'ddg', '迪庆': 'dig', '大连': 'dlc', '大理': 'dlu', 
         '敦煌': 'dnh', '东营': 'doy', '大庆': 'dqa', '达州': 'dzh', '东阳': 'dyc', 
         '德令哈': 'hxd', '鄂州': 'ehu', '额济纳旗': 'ejn', '恩施': 'enh', '二连浩特': 'erl', 
         '福州': 'foc', '阜阳': 'fug', '佛山': 'fuo', '抚远': 'fyj', '富蕴': 'fyn', 
         '广州': 'can', '果洛': 'gmq', '格尔木': 'goq', '广元': 'gys', '固原': 'gyu', 
         '甘孜': 'gzg', '赣州': 'kow', '贵阳': 'kwe', '桂林': 'kwl', '黄山': 'txn', 
         '湖州': 'hzc', '合肥': 'hfe', '呼伦贝尔': 'xrq', '海口': 'hak', '河池': 'hcj', 
         '邯郸': 'hdg', '黑河': 'hek', '呼和浩特': 'het', '杭州': 'hgh', '淮安': 'hia', 
         '和静': 'hjb', '怀化': 'hjj', '香港': 'hkg', '海拉尔': 'hld', '哈密': 'hmi', 
         '呼玛': 'hmx', '衡阳': 'hny', '哈尔滨': 'hrb', '和田': 'htn', '花莲': 'hun', 
         '惠州': 'huz', '菏泽': 'hza', '汉中': 'hzg', '荆州': 'shs', '揭阳': 'swa', 
         '济南': 'tna', '江门': 'zbd', '景德镇': 'jdz', '加格达奇': 'jgd', '嘉峪关': 'jgn', 
         '井冈山': 'jgs', '金昌': 'jic', '九江': 'jiu', '嘉兴': 'jxs', '佳木 斯': 'jmu', 
         '济宁': 'jng', '锦州': 'jnz', '鸡西': 'jxa', '九寨沟': 'jzh', '库车': 'kca', 
         '康定': 'kgt', '高雄': 'khh', '喀什': 'khg', '凯里': 'kjh', '昆明': 'kmg', 
         '金门': 'knh', '库尔勒': 'krl', '克拉玛依': 'kry', '昆山': 'kvn', '黎平': 'hzh', 
         '龙岩': 'lcx', '临汾': 'lfq', '兰州': 'lhw', '梁平': 'lia', '丽江': 'ljg', 
         '荔波': 'llb', '吕 梁': 'llv', '临沧': 'lnj', '六盘水': 'lpf', '拉萨': 'lxa', 
         '洛阳': 'lya', '连云港': 'lyg', '临沂': 'lyi', '阆中': 'lzg', '柳州': 'lzh', 
         '泸州': 'lzo', '澳门': 'mfm', '牡丹江': 'mdg', '马祖': 'mfk', '绵阳': 'mig', 
         '梅州': 'mxz', '马公': 'mzg', '满洲里': 'nzh', '漠河': 'ohe', '南昌': 'khn', 
         '南竿': 'lzn', '林芝': 'lzy', '南充': 'nao', '宁 波': 'ngb', '阿里': 'ngq', 
         '嫩江': 'njj', '南京': 'nkg', '宁蒗': 'nlh', '南宁': 'nng', '南阳': 'nny', 
         '南通': 'ntg', '鄂尔多斯': 'dsn', '鄂托克旗': 'oto', '普洱': 'sym', '攀枝花': 'pzi', 
         '普兰': 'apj', '昌都': 'bpx', '青岛': 'tao', '祁连': 'hbq', '且末': 'iqm', 
         '庆阳': 'iqn', '奇台': 'jbk', '黔江': 'jiq', '泉州': 'jjn', '衢州': 'juz', 
         ' 齐齐哈尔': 'ndg', '琼海': 'bar', '上海': 'sha', '石河子': 'shf', '沈阳': 'she', 
         '石家庄': 'sjw', '上饶': 'sqd', '三亚': 'syx', '苏州': 'szv', '朔州': 'szh', 
         '深圳': 'szx', '日喀则': 'rkz', '三沙': 'xyi', '神农架': 'hpg', '绥芬河': 'hsf', 
         '山南': 'lgz', '塔城': 'tcg', '腾冲': 'tcz', '铜仁': 'ten', '通辽': 'tgo', 
         '天水': 'thq', '吐鲁番': 'tlq', '通化': 'tnh', '台南': 'tnn', '台北': 'tpe', 
         '天津': 'tsn', '台东': 'ttt', '唐山': 'tvs', '图木舒克': 'twc', '太原': 'tyn', 
         '塔什库尔干': 'hql', '台州': 'hyn', '台中': 'rmq', '乌鲁木齐': 'urc', 
         '乌尔禾': 'wrh', '乌兰浩特': 'hlh', '武隆': 'cqw', '文昌': 'wec', '潍坊': 'wef', 
         '威海': 'weh', '芜湖': 'whu', '武汉': 'wuh', '文山': 'wnh', '温州': 'wnz', 
         '巫山': 'wsk', '乌海': 'wua', '武夷山': 'wus', '无锡': 'wux', '梧州': 'wuz', 
         '万州': 'wxn', '湘 西土家族苗族自治州': 'dxj', '忻州': 'wut', '信阳': 'xai', 
         '襄阳': 'xfn', '西昌': 'xic', '锡林浩特': 'xil', '西安': 'sia', '厦门': 'xmn', 
         '西宁': 'xnn', '邢台': 'xnt', '徐州': 'xuz', '夏河': 'gxh', '西双版纳': 'jhg', 
         '新源': 'nlt', '兴义': 'acx', '榆林': 'uyn', '延安': 'eny', '宜宾': 'ybp', 
         '运城': 'ycu', '宜春': 'yic', '宜昌': 'yih', '伊宁': 'yin', '义乌': 'yiw', 
         '玉林': 'ylx', '延吉': 'ynj', '烟台': 'ynt', '盐城': 'ynz', '扬州': 'yty', 
         '玉树': 'yus', '银川': 'inc', '伊春': 'lds', '永州': 'llf', '郑州': 'cgo', 
         '张家界': 'dyg', '舟山': 'hsn', '张掖': 'yzy', ' 昭通': 'zat', '昭苏': 'zfl', 
         '中山': 'zgn', '湛江': 'zha', '中卫': 'zhy', '珠海': 'zuh', '张家口': 'zqz', 
         '遵义': 'zyi', '扎兰屯': 'nzl'}
ac = []

def getFlights(ks, js):
    ks, js = city[ks], city[js]
    curl = 'https://flights.ctrip.com/schedule/getScheduleByCityPair'
    data = {"departureCityCode": f'{str(ks).upper()}', "arriveCityCode": f'{str(js).upper()}', "pageNo": 1}
    req = requests.post(url=curl,headers=header,json=data).json()
    # print(req)
    max_page = req['totalPage']
    ac.extend(req['scheduleVOList'])
    for i in range(2,max_page+1):
        ac.extend(req['scheduleVOList'])
    # print(ac)
    return ac

if __name__ == '__main__':
    ks,js = city['北京'], city['三亚']
    print(getFlights(ks,js))
    
# df = pd.DataFrame(ac)
# acc = pd.DataFrame(df.pop('currentWeekSchedule').tolist())
# ps = pd.concat([df,acc],axis=1)
# ps.to_csv('飞机票数据.csv',index=False)