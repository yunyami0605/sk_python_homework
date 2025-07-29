# 4-1 인구현황 데이터 분석

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

# macOS에서는 'AppleGothic' 사용
matplotlib.rc('font', family='AppleGothic')

# 마이너스 깨짐 방지
matplotlib.rcParams['axes.unicode_minus'] = False

data = pd.read_csv('./data/인구현황.csv')
# print(data)

# 2. 세대당 인구수 높은 지역 Top5
house_of_area = data.loc[data["행정기관"] != "전국", ["행정기관", "세대당 인구"]].sort_values(by="세대당 인구", ascending=False)
top5 = house_of_area.head(5)
print(top5)
# print(population_of_area)


# 2-1. 지역별 세대당 인구수 plot
figure, (axes) = plt.subplots(nrows=1, ncols=1, figsize=(15, 6))
sns.barplot(data=house_of_area, x='행정기관', y="세대당 인구", ax=axes,  hue='행정기관')

plt.xticks(rotation=45)
plt.title('지역별 세대당 인구')
plt.tight_layout()
plt.show()

