<template>
  <div class="container text-center">
    <div class="title-section">
      <h2 class="main-title animate-typing">나와 비슷한 사람들의 스마트한 선택</h2>
      <p class="sub-title animate-fade">연령, 성별, 직군, 소득수준이 비슷한 사용자들이 선택한 금융상품을 추천해드립니다</p>
    </div>
    <div class="filter-group justify-content-center">
      <RouterLink 
        :to="{name: 'RecommendDepositView'}" 
        class="btn"
        :class="{ active: $route.name === 'RecommendDepositView' }"
      >
      <i class="fas fa-coins me-2"></i>예금 추천받기
      </RouterLink>
      <RouterLink 
        :to="{name: 'RecommendSavingView'}" 
        class="btn"
        :class="{ active: $route.name === 'RecommendSavingView' }"
      >
        <i class="fas fa-piggy-bank me-2"></i>적금 추천받기
      </RouterLink>
    </div>
    <div class="mt-4">
      <RecommendSavingList/>
    </div>
  </div>
</template>

<script setup>
import RecommendSavingList from '@/components/RecommendSavingList.vue';
import { RouterLink, RouterView } from 'vue-router';

</script>

<style scoped>
.filter-group {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-bottom: 20px;
  margin-top: 5px;
}

.title-section {
  margin-left: 0px;
  margin-right: 0px;
  margin-top: 40px;
  padding: 20px;
}

.main-title {
  color: #2ecc71;
  font-weight: 600;
  margin-bottom: 15px;
  font-size: 2rem;
  opacity: 0;
  animation: typing 1s ease-in-out forwards;
}

.sub-title {
  color: #666;
  font-size: 1.1rem;
  margin-bottom: 30px;
  opacity: 0;
  animation: fadeIn 1s ease-in-out 1s forwards;
}

@keyframes typing {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.btn {
  padding: 8px 16px;
  border: none;
  background: none;
  color: #666;
  transition: all 0.3s ease;
  min-width: 140px;
  position: relative;
  font-weight: 500;
  text-decoration: none;
  display: flex;
  align-items: center;
  justify-content: center;
}

.btn::after {
  content: '';
  position: absolute;
  width: 0;
  height: 2px;
  bottom: 0;
  left: 50%;
  background-color: #2ecc71;
  transition: all 0.3s ease;
  transform: translateX(-50%);
}

.btn-outline-success {
  color: #2ecc71;
  border-color: #2ecc71;
}

.btn:hover {
  color: #000;
}

.btn.active {
  color: #000;
}

.btn.active::after {
  width: 80%;
}

.btn:hover::after {
  width: 40%;
}
.fas {
  color:black;
  margin-right: 8px;
}

.btn-outline-success:hover,
.btn-outline-success.active {
  background-color: #2ecc71;
  color: white;
  transform: scale(1.05);
}

/* 반응형 디자인 */
@media (max-width: 768px) {
  .btn {
    min-width: auto;
    width: 45%;
  }
}
</style>