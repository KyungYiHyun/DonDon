<template>
  <div class="saving-card cursor-pointer me-2"  data-bs-toggle="modal" 
            :data-bs-target="`#savingModal-${product.id}`" 
          
          >
    <div class="card">
      <div class="card-body d-flex flex-column justify-content-between">
        <div>
          <h5 class="card-title mb-3">{{ product.fin_prdt_nm }}</h5>
          <div class="bank-info mb-2">
            <span class="bank-name text-primary">{{ product.kor_co_nm }}</span>
          </div>
          <div class="rates">
            <div class="rate-item">
              <span class="badge-intr me-2">기본금리</span>
              <span class="rate">{{ product.intr_rate }}%</span>
            </div>
            <div class="rate-item">
              <span class="badge-intr me-2">우대금리</span>
              <span class="rate">{{ product.intr_rate2 }}%</span>
            </div>
          </div>
        </div>
        <div class="button-group mt-3">
          
          <button class="btn btn-outline-danger" @click="deleteFromSavingCart(product)">삭제</button>
        </div>
      </div>
    </div>
    </div>
  

  <!-- 모달 -->
  <div 
    class="modal fade custom-modal"
    :id="`savingModal-${product.id}`"
    tabindex="-1"
    aria-labelledby="savingModalLabel"
    aria-hidden="true"
    data-bs-backdrop="false"
  >
    <div class="modal-dialog modal-dialog-centered modal-lg">
      <div class="modal-content">
        <SavingDetail :product="product" />
      </div>
    </div>
  </div>
  
</template>

<script setup>
import { ref } from 'vue';
import { useCartStore } from '@/stores/cart';
import SavingDetail from './SavingDetail.vue';
defineProps({
  product: Object
})
const store = useCartStore()

const isModalVisible = ref(false)

const openModal = () => {
  isModalVisible.value = true;
}

const updateModalVisibility = (newValue) => {
  isModalVisible.value = newValue;
}

const deleteFromSavingCart = (product) => {
  store.deleteFromSavingCart(product)
}
</script>

<style scoped>
.saving-card {
  flex: 0 0 300px; /* flex-grow: 0, flex-shrink: 0, flex-basis: 300px */
  width: 300px;
  height: 250px; /* 고정된 높이 설정 */
}

/* 모달의 기본 설정 */
.modal {
  position: fixed !important; /* 고정 위치로 설정 */
  z-index: 1050; /* Bootstrap 기본 z-index */
}

.badge-intr{
  color: black;
  font-weight: bold;
}

.card {
  height: 100%;
  transition: transform 0.2s;
}
.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.bank-name {
  color: #666;
  font-size: 0.9rem;
}

.rates {
  margin-top: 15px;
}


.card-body {
  height: 100%;
  padding: 1rem;
}

.card-title{
  font-weight: bold;
}
.rate-item {
  margin-bottom: 8px;
  display: flex;
  align-items: center;
}

.rate {
  font-size: 1.1rem;
  font-weight: bold;
  color: #d8205f;
}

.button-group {
  display: flex;
  justify-content: flex-end;
}

.modal-content{
  border: none;
}
.modal-backdrop {
  position: fixed !important;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1040; /* 모달 뒤로 설정 */
}

/* 반응형 디자인 */
@media (max-width: 768px) {
  .saving-card {
    width: calc(50% - 20px);
  }
}

@media (max-width: 576px) {
  .saving-card {
    width: 100%;
    margin: 10px 0;
  }
}

:deep(.custom-modal) {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 1500 !important;
}

:deep(.modal-dialog) {
  z-index: 1510 !important;
}

:deep(.modal-backdrop) {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 1499 !important;
}
</style>