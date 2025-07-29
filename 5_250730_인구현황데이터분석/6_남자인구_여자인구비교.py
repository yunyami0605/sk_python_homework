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
gender_of_area = data.loc[data["행정기관"] != "전국", ["행정기관", "남자 인구수", "여자 인구수"]]


df_melted = gender_of_area.melt(
    id_vars='행정기관',
    value_vars=["남자 인구수", "여자 인구수"],
    var_name="성별",
    value_name="인구수"
)

# 성별에 따른 색상 지정
palette = {
    "남자 인구수": "royalblue",
    "여자 인구수": "orange"
}

figure, (axes1) = plt.subplots(nrows=1, ncols=1, figsize=(16, 8))

sns.barplot(
    data=df_melted,
    x="행정기관",
    y="인구수",
    hue="성별",
    palette=palette
)

plt.title("남자 vs 여자 인구 비교")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


