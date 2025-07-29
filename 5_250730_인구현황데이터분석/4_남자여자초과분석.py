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

# 4. 남자초과 / 여자초과 분석
gender_of_area = data.loc[data["행정기관"] != "전국", ["행정기관", "남여 비율"]]

gender_of_area["남초여초"] = gender_of_area["남여 비율"].map(
    lambda x: "동일" if x == 1.00 else ("여초" if x > 1.00 else "남초")
)

print(gender_of_area)


