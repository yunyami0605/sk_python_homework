
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

# 1. 지역별 총인구수 top5
population_of_area = data.loc[data["행정기관"] != "전국", ["행정기관", "총인구수"]].sort_values(by="총인구수", ascending=False)
top5 = population_of_area.head(5)
print(top5)
# print(population_of_area)


# 1-1. 지역별 총인구수 plot
figure, (axes) = plt.subplots(nrows=1, ncols=1, figsize=(15, 6))
sns.barplot(data=population_of_area, x='행정기관', y="총인구수", ax=axes,  hue='행정기관')

plt.xticks(rotation=45)
plt.title('지역별 총인구수')
plt.tight_layout()
plt.show()
