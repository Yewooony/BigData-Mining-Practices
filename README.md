# Big Data Collection and Mining (Capstone Design) Course Labs.

This collection contains practical Python code exercises focusing on the full Big Data lifecycle: acquisition (Web Crawling/APIs), processing (NumPy, Pandas), analysis, and visualization (Matplotlib). The curriculum follows the concepts from the textbook, **'모두의 데이터 분석 with 파이썬'**. Projects utilize public domain datasets (e.g., weather, public transit, demographic data) to develop real-world Capstone Design skills in data-driven problem-solving.

본 저장소는 빅데이터의 전체 라이프사이클에 중점을 둔 실무적인 파이썬 코드 실습을 담고 있습니다: 수집 (웹 크롤링/API), 처리 (NumPy, Pandas), 분석 및 시각화 (Matplotlib). 교재 **'모두의 데이터 분석 with 파이썬'**의 개념을 따릅니다. 공공 데이터셋 (예: 기상, 대중교통, 인구 구조 데이터)을 활용하여 데이터 기반 문제 해결에 필요한 실제 캡스톤 디자인 역량을 개발합니다.

---

## 🛠 Tech Stack

* **Language**: Python 3.x
* **Libraries**: `csv`, `numpy`, `pandas`, `matplotlib`, `math`
* **Datasets**: `subwaytime.csv`, `subwayfee.csv`, `age.csv`, `age2.csv`, `gender.csv`

---

## 📂 Project Structure by Dataset

제공된 데이터셋별 폴더 구조에 따른 분석 내용입니다.

### 1. Tmoney_지하철시간대별이용현황

지하철 시간대별 이용객 데이터를 분석하여 특정 시각의 혼잡도 및 승하차 추이를 파악합니다.

* **시간대별 피크 탐색**: 사용자로부터 입력받은 특정 시각의 최대 승차역을 찾거나, 24시간 전체 시간대별 최대 승차역을 도출하여 막대그래프로 시각화합니다.
* **승하차 추이 분석**: 전체 지하철역의 시간대별 승하차 인원 흐름을 선 그래프로 비교 분석합니다.
* **출근 시간대 집중 분석**: 아침 7시~9시 사이의 승차 인원 분포를 추출하여 이용 패턴을 분석합니다.
* **데이터 리스트 출력**: 각 시간대별 최대 승차역과 인원 데이터를 텍스트 형태로 상세 출력합니다.

### 2. Tmoney_지하철유무임별이용현황

유임 및 무임 승하차 데이터를 비교하여 역별 이용객 특성을 분석합니다.

* **이용객 유형별 최대역**: 유임/무임 승하차 각 카테고리에서 이용객이 가장 많은 역을 식별합니다.
* **유임 승차 비율 분석**: 유동 인구(10만 명 이상)를 고려하여 유임 승차 비율이 가장 높은 역을 계산합니다.
* **비율 시각화**: 역별 유무임 승하차 비율을 파이 차트로 나타내고 시각화 결과물을 이미지 파일로 자동 저장합니다.

### 3. wikipedia_올림픽메달획득결과

외부 웹 데이터를 수집하고 Pandas를 활용한 심화 데이터 처리를 수행합니다.

* **웹 크롤링**: `pandas.read_html()`을 사용하여 위키피디아의 테이블 데이터를 데이터프레임으로 수집합니다.
* **고급 데이터 분석**: Pandas를 활용해 인구 비율 차이의 제곱 합이 가장 작은 유사 지역들을 탐색하고 시각화합니다.

### 4. 행정안전부_인구공공데이터

공공 인구 데이터를 기반으로 지역별 인구 구조를 다각도로 시각화하고 유사도를 계산합니다.

* **인구 구조 시각화**: 연령별 남녀 인구 분포를 선 그래프, 막대그래프, 또는 좌우 대칭형 피라미드로 구현합니다.
* **성별 상관관계**: 산점도와 버블 차트를 활용하여 남녀 인구수의 상관관계와 연령별 밀집도를 분석합니다.
* **NumPy 기반 유사도 매칭**: NumPy 배열 연산을 활용하여 특정 지역과 가장 유사한 인구 비율을 가진 지역을 탐색하는 알고리즘을 구현합니다.

---

## 📊 Visualization Examples
<img width="450" height="320" alt="image (13)" src="https://github.com/user-attachments/assets/84ca9170-eae7-4772-819e-f12ed31aabf6" />
<img width="450" height="320" alt="image (14)" src="https://github.com/user-attachments/assets/1863abd2-acad-40d3-a806-6870f128d11a" />
<img width="450" height="320" alt="image (15)" src="https://github.com/user-attachments/assets/fe57a103-c843-4128-99b0-193d803c6ef5" />
<img width="450" height="320" alt="동묘앞 " src="https://github.com/user-attachments/assets/748ffdb4-bd32-48ee-beee-bfe237dd80e3" />


---

## 🏃 How to Run

1. 각 폴더의 Python 파일과 동일한 위치에 해당 CSV 데이터 파일이 있는지 확인합니다.
2. 차트의 한글 깨짐 방지를 위해 `Malgun Gothic` 폰트 환경에서 실행하는 것을 권장합니다.
3. 필요 라이브러리 설치:
```bash
pip install numpy pandas matplotlib

```
