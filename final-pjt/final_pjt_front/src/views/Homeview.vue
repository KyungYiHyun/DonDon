<template>
  <div class="">
    <div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <div class="carousel-content">
            <div class="text-content">
              <h1 class="main-title">스마트한 금융 생활의 첫걸음<br>모든 은행 상품 비교를 한눈에</h1>
              <RouterLink :to="{name: 'DepositView'}" class="compare-btn">
                상품 비교하기
              </RouterLink>
            </div>
            <div class="image-content">
              <img class="img1" src="@/assets/compare2.png" alt="compare">
            </div>
          </div>
        </div>
        <div class="carousel-item">
  <div class="carousel-content">
    <div class="text-content">
      <h1 class="main-title">아까운 점심시간<br>10분 안에 끝내는 은행 업무</h1>
      <RouterLink :to="{name: 'MapView'}" class="compare-btn">
        가까운 은행 찾기
      </RouterLink>
    </div>
    <div class="image-content">
      <img class="img2" src="@/assets/map.png" alt="map">
    </div>
  </div>
</div>
<div class="carousel-item">
  <div class="carousel-content">
    <div class="text-content">
      <h1 class="main-title">2만명의 선택<br>나만을 위한 맞춤 상품 추천</h1>
      <RouterLink :to="{name: 'RecommendDepositView'}" class="compare-btn">
        상품 추천받기
      </RouterLink>
    </div>
    <div class="image-content">
      <img class="img3" src="@/assets/recommendation.png" alt="laptop">
    </div>
  </div>
</div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { roundToNearestHours } from 'date-fns';
import { RouterLink } from 'vue-router';
</script>

<style scoped>
.carousel-item {
  height: 100vh;
  background: linear-gradient(135deg, #e8f5e9 0%, #a5d6a7 100%); /* 더 연한 초록색 그라데이션 */
}


.carousel-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100%;
  padding: 0 10%;
}

.carousel-control-prev,
.carousel-control-next {
  width: 5%;
  opacity: 0.8;
}

.carousel-control-prev-icon,
.carousel-control-next-icon {
  background-color: rgba(0, 0, 0, 0.3);
  padding: 20px;
  border-radius: 50%;
  background-size: 50%;
}

.carousel-control-prev-icon:hover,
.carousel-control-next-icon:hover {
  background-color: rgba(0, 0, 0, 0.5);
}

.text-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-bottom: 100px; /* 텍스트 위로 이동 */
}
.main-title {
  color: #333;
  font-size: 3rem;
  font-weight: bold;
  line-height: 1.4;
  margin-bottom: 2rem; /* 버튼과의 간격 */
}

.image-content {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.compare-btn {
  display: inline-block;
  padding: 1rem 2rem;
  background-color: #4CAF50;
  color: white;
  text-decoration: none;
  border-radius: 30px;
  font-size: 1.2rem;
  font-weight: 600;
  transition: all 0.3s ease;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}


.compare-btn:hover {
  background-color: #45a049;
  transform: translateY(-2px);
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
}
.img2 {
  height: 600px;
  object-fit: contain;
  animation: float 3s ease-in-out infinite;
  /* position: 50vh; */
}
.img3 {
  height: 600px;
  object-fit: contain;
  animation: float 3s ease-in-out infinite;
  /* position: 50vh; */
}
.carousel-item:nth-child(2) {
  background: linear-gradient(135deg, #e0f2f1 0%, #80cbc4 100%); /* 부드러운 민트색 그라데이션 */
}
.carousel-item:nth-child(2) .img1 {
  height: 350px; /* 지도 이미지 크기 조정 */
  border-radius: 20px; /* 모서리 둥글게 */
/* 그림자 효과 */
}

.carousel-item:nth-child(2) .compare-btn {
  background-color: #00bfa5; /* 민트/터콰이즈 계열 */
}

.carousel-item:nth-child(2) .compare-btn:hover {
  background-color: #00a08c;
}

/* 세번째 캐러셀 배경 - 부드러운 라벤더/보라색 계열 */
.carousel-item:nth-child(3) {
  background: linear-gradient(135deg, #f3e5f5 0%, #b39ddb 100%);
}

/* 세번째 캐러셀 이미지 */
.carousel-item:nth-child(3) .img1 {
  height: 450px;
  border-radius: 15px;
  
}

/* 세번째 캐러셀 버튼 */
.carousel-item:nth-child(3) .compare-btn {
  background-color: #7e57c2;
}

.carousel-item:nth-child(3) .compare-btn:hover {
  background-color: #673ab7;
}


</style>