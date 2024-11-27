<template>
  <div class="container text-center">
    
    <div class="filter-group justify-content-center">
      <RouterLink 
        :to="{name: 'DepositView'}" 
        class="btn btn-outline-success"
        :class="{ active: $route.name === 'DepositView' }"
      >
      <i class="fas fa-coins me-2"></i>정기예금
      </RouterLink>
      <RouterLink 
        :to="{name: 'SavingView'}" 
        class="btn btn-outline-success"
        :class="{ active: $route.name === 'SavingView' }"
      >
        <i class="fas fa-piggy-bank me-2"></i>정기적금
      </RouterLink>
    </div>
    <SavingList />
  </div>
</template>

<script setup> 
import SavingList from '@/components/SavingList.vue';
import { RouterLink } from 'vue-router';
</script>

<style scoped>
.filter-group {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  margin-top: 30px;
  justify-content: center;
  padding: 10px 20px;
}
.btn {
  padding: 8px 16px;
  border: none;
  background: none;
  color: #666;
  transition: all 0.3s ease;
  min-width: 120px;
  position: relative;
  text-decoration: none; /* RouterLink 밑줄 제거 */
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

.btn:hover {
  color: #000;
  background: none;
  transform: none;
}

.btn.active {
  color: #000;
  transform: none;
  background: none;
}

.btn.active::after {
  width: 80%;
}

.btn:hover::after {
  width: 40%;
}

.btn-outline-success {
  border: none;
}

.btn-outline-success:hover,
.btn-outline-success.active {
  background: none;
  color: #000;
  transform: none;
}
/* 반응형 조정 */
@media (max-width: 768px) {
  .btn {
    min-width: auto;
    width: 45%;
  }
}
</style>