import numpy as np
'''
dt,value,pe
'''

def weight_sum(from_pe, end_pe):
    sum_value = 0
    sum_day = 0
    tb_name = 'sz'
    current_date = '1000-00-00'
    while True:
        # 查询from
        sql1 = 'select value,dt from %s where pe<="%s" and dt>"%s" limit 1' % (tb_name, from_pe, current_date)
        items_from = []
        if not items_from:
            break
        value, current_date = items_from[0]

        # 查询end
        sql2 = 'select vl, dt from %s where pe>="%s" and dt>"%s" limit 1' % (tb_name, end_pe, current_date)
        items_end = []
        if not items_end:
            sql2 = 'select vl, dt from sz order by dt desc limit 1'
        value2, current_date2 = items_end[0]
    return sum_day, sum_value


def start():
    max_value = 200
    min_value = 60
    sep = 5

    count = int((max_value-min_value)/sep)
    pe_point = [min_value + i*sep for i in range(count)]

    # 初始化三维数组
    seq = np.ones((count, count, 3), dtype=np.int8)
    for i in range(count):
        for j in range(count):
            last_day, added_value = weight_sum(pe_point[i], pe_point[j])
            seq[i, j] = [last_day, added_value]

