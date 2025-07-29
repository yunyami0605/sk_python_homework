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

# 3. 남녀 비율 분석
gender_of_area = data.loc[data["행정기관"] != "전국", ["행정기관", "남여 비율"]].sort_values(by="남여 비율", ascending=False)
print(gender_of_area)


# 3-1. 지역별 남녀 비율 plot
figure, (axes) = plt.subplots(nrows=1, ncols=1, figsize=(15, 6))
sns.barplot(data=gender_of_area, x='행정기관', y="남여 비율", ax=axes,  hue='행정기관')

axes.axhline(y=1.0, color='red', linestyle='--', linewidth=2, label='남녀 1:1 비율')

plt.xticks(rotation=45)
plt.title('지역별 남녀 비율')
plt.tight_layout()
plt.show()

