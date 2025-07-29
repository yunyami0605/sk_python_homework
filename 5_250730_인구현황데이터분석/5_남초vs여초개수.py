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

# 5세대당 인구 평균보다 높은 지역
population_of_area = data.loc[data["행정기관"] != "전국", ["행정기관", "세대당 인구"]].sort_values(by="세대당 인구", ascending=False)

print("5. 세대당 인구 평균보다 높은 지역")
print(f"전국 평균 세대당 인구수: {population_of_area["세대당 인구"].mean():.2f}")
print(population_of_area.head(7).reset_index(drop=True))

# 5-1 남초 vs 여초 개수 Plot
gender_of_area = data.loc[data["행정기관"] != "전국", ["행정기관", "남여 비율"]]

gender_of_area["남초여초"] = gender_of_area["남여 비율"].map(
    lambda x: "동일" if x == 1.00 else ("여초" if x > 1.00 else "남초")
)


figure, (axes1, axes2) = plt.subplots(nrows=2, ncols=1, figsize=(16, 8))

sns.countplot(data=gender_of_area, x='남초여초', ax=axes1,  hue='남초여초')
axes1.set_title("남초 vs 여초 지역 개수")


house_of_area = data.loc[data["행정기관"] != "전국", ["행정기관", "세대수"]].sort_values(by="세대수", ascending=False)

sns.barplot(data=house_of_area, x='행정기관', y='세대수', ax=axes2,  hue='행정기관')

axes2.set_title("지역별 세대수")

plt.tight_layout()
plt.show()


