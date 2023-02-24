import pandas as pd
import matplotlib.pyplot as plt
col = ['Type', 'Offset', 'Size', 'ResponseTime']
hm0df = pd.read_csv('./dp_hm_0.csv', names=col)
hm1df = pd.read_csv('./dp_hm_1.csv', names=col)
p0df = pd.read_csv('./dp_prn_0.csv', names=col)
p1df = pd.read_csv('./dp_prn_1.csv', names=col)
s0df = pd.read_csv('./dp_stg_0.csv', names=col)
s1df = pd.read_csv('./dp_stg_1.csv', names=col)
tsdf = pd.read_csv('./dp_ts_0.csv', names=col)
dflists = [hm0df, hm1df, p0df, p1df, s0df, s1df, tsdf]
titles = ['hm0', 'hm1', 'prn0', 'prn1', 'stg0', 'stg1', 'ts']
for dfs, title in zip(dflists, titles):
    ratio = dfs.Type.value_counts()
    labels = dfs.Type.value_counts().index
    plt.pie(ratio, labels=labels, autopct='%.2f%%', startangle=90, counterclock=False)
    plt.title(f'I/O Ratio of {title}')
    plt.show()
