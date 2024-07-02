import time
import requests


def is_ts_accessible(url):
    try:
        response = requests.get(url, timeout=0.5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        pass
    return None


def get_otv_py(timestamps, txts, channels, mls):
    py = None
    j = 0
    while j < 6:
        stream = f'http://{txts}-txt.otvstream.otvcloud.com/otv/skcc/live/channel{channels}/{mls}/'
        time_ymd = time.strftime('%Y%m%d', time.localtime(timestamps * 6))
        time_his = time.strftime('%H%M%S', time.localtime(timestamps * 6))
        time_his = str(int(time_his) + j)
        if len(time_his) < 6:
            time_his = f'0{time_his}'
        ts_name = f'{time_ymd}T{time_his}.ts'
        current = f'{stream}{time_ymd}/{ts_name}'
        ts_accessible = is_ts_accessible(current)
        if ts_accessible:
            py = j
            break
        else:
            j += 1
        time.sleep(0.2)
    return py


def otv():
    ids = ["CCTV1/4403/1/2300", "CCTV2/4403/2/2300", "CCTV3/4403/3/2300", "CCTV4/4403/4/2300", "CCTV5/4403/5/2300",
           "CCTV5+/4403/13/2300", "CCTV6/4403/6/2300", "CCTV7/4403/7/2300", "CCTV8/4403/8/2300", "CCTV9/4403/9/2300",
           "CCTV10/4403/10/2300", "CCTV11/4403/41/2300", "CCTV12/4403/11/2300", "CCTV13/4403/39/2300",
           "CCTV14/4403/12/2300", "CCTV15/4403/40/2300", "CCTV17/4403/90/2300", "CGTN/4403/15/2300",
           "CGTN纪录/4403/14/2300", "CETV1/4403/33/2300", "CETV4/4403/38/1300", "北京卫视/4403/24/2300",
           "东方卫视/4403/26/2300", "天津卫视/4403/28/2300", "吉林卫视/4403/20/2300", "辽宁卫视/4403/32/2300",
           "陕西卫视/4403/55/2300", "安徽卫视/4403/23/2300", "湖北卫视/4403/21/2300", "湖南卫视/4403/25/2300",
           "江西卫视/4403/22/2300", "江苏卫视/4403/18/2300", "浙江卫视/4403/19/2300", "东南卫视/4403/80/2300",
           "广东卫视/4403/16/2300", "深圳卫视/4403/17/2300", "大湾区卫视/4403/58/1300", "云南卫视/4403/61/2300",
           "四川卫视/4403/31/2300", "新疆卫视/4403/64/2300", "兵团卫视/4403/67/2300", "西藏卫视/4403/66/2300",
           "广东珠江/4403/65/1300", "广东民生/4403/45/1300", "广东体育/4403/34/2300", "广东少儿/4403/63/1300",
           "深圳都市/4403/46/1300", "深圳电视剧/4403/47/1300", "深圳财经生活/4403/48/1300", "深圳娱乐/4403/49/1300",
           "深圳体育健康/4403/50/1300", "深圳少儿/4403/51/1300", "深圳公共/4403/52/1300", "蛇口电视台/4403/37/1300"]
    otvtxt = "OTV亦非云,#genre#\n"
    timestamp = int(time.time() / 6) - 6
    for id_x in ids:
        id_x = id_x.split("/")
        py = get_otv_py(timestamp, id_x[1], id_x[2], id_x[3])
        if py is not None:
            otvtxt += f'{id_x[0]},txt={id_x[1]}&channel={id_x[2]}&ml={id_x[3]}&py={py}\n'
    return otvtxt


if __name__ == "__main__":
    with (open('otv.txt', 'w', encoding='utf-8') as x_file):
        x_file.write(otv())
