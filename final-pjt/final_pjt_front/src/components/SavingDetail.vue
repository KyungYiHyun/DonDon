<template>
  <div class="modal-content">
    <div class="modal-header bg-success text-white">
      <div class="d-flex align-items-center">
        <div class="product-icon me-3">
          <i class="fas fa-piggy-bank"></i>
        </div>
        <h5 class="modal-title">{{ product.fin_prdt_nm }}</h5>
      </div>
      <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
    </div>
    
    <div class="modal-body">
      <div class="container">
        <div class="row mb-4">
          <div class="col-md-6">
            <div class="info-card">
              <div class="card-body">
                <h6 class="card-subtitle mb-3">
                  <i class="fas fa-info-circle me-2"></i>기본 정보
                </h6>
                <div class="info-item">
                  <span class="info-label">은행명</span>
                  <span class="info-value">{{ product.kor_co_nm }}</span>
                </div>
                <div class="info-item">
                  <span class="info-label">금리</span>
                  <span class="info-value">{{ product.intr_rate }}%</span>
                </div>
                <div class="info-item">
                  <span class="info-label">최고우대금리</span>
                  <span class="info-value">{{ product.intr_rate2 }}%</span>
                </div>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="info-card">
              <div class="card-body">
                <h6 class="card-subtitle mb-3">
                  <i class="fas fa-user-plus me-2"></i>가입 정보
                </h6>
                <div class="info-item">
                  <span class="info-label">가입대상</span>
                  <span class="info-value">{{ product.join_member }}</span>
                </div>
                <div class="info-item">
                  <span class="info-label">가입방법</span>
                  <span class="info-value">{{ product.join_way }}</span>
                </div>
                <div class="info-item">
                  <span class="info-label">가입제한</span>
                  <span class="info-value">{{ product.join_deny }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="info-card mb-4">
          <div class="card-body">
            <h6 class="card-subtitle mb-3">
              <i class="fas fa-file-alt me-2"></i>상품 상세
            </h6>
            <div class="info-item">
              <span class="info-label">만기 후 이자율</span>
              <span class="info-value">{{ product.mtrt_int }}</span>
            </div>
            <div class="info-item">
              <span class="info-label">우대조건</span>
              <span class="info-value">{{ product.spcl_cnd }}</span>
            </div>
            <div class="info-item">
              <span class="info-label">기타 유의사항</span>
              <span class="info-value">{{ product.etc_note }}</span>
            </div>
            <div class="info-item">
  <span class="info-label">최고한도</span>
  <span class="info-value">{{ product.max_limit ? `${product.max_limit} 원` : '없음' }}</span>
</div>
          </div>
        </div>

        <div class="info-card">
          <div class="card-body">
            <h6 class="card-subtitle mb-3">
              <i class="fas fa-percentage me-2"></i>금리 정보
            </h6>
            <div class="info-item">
              <span class="info-label">저축금리유형</span>
              <span class="info-value">{{ product.intr_rate_type }}</span>
            </div>
            <div class="info-item">
              <span class="info-label">저축금리유형명</span>
              <span class="info-value">{{ product.intr_rate_type_nm }}</span>
            </div>
            <div class="info-item">
              <span class="info-label">저축기간</span>
              <span class="info-value">{{ product.save_trm }}개월</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="modal-footer">
      <button 
        class="btn-custom"
        :class="isInCart(product.id) ? 'delete' : 'add'"
        @click="isInCart(product.id) ? deleteFromSavingCart(product) : addToSavingCart(product)"
      >
        <i :class="isInCart(product.id) ? 'fas fa-trash-alt' : 'fas fa-plus'" class="me-2"></i>
        {{ isInCart(product.id) ? '삭제' : '담기' }}
      </button>
    </div>
  </div>
</template>

<script setup>

import { ref } from 'vue';
import {  defineEmits} from 'vue';
import { useCartStore } from '@/stores/cart';
const emit = defineEmits(['update:isModalVisible'])

defineProps({
  product : Object,
})

const store = useCartStore()

const addToSavingCart = (product) => {
  store.addToSavingCart(product)
}

const deleteFromSavingCart = (product) => {
  store.deleteFromSavingCart(product)
}

const isInCart = (productId) => {
  return store.savingProducts.some((item) => item.id === productId)
}

</script>

<style scoped>
.modal-content {
  height: 750px;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.modal-body {
  height: calc(750px - 130px); /* 헤더(70px)와 푸터(60px) 높이를 제외 */
  overflow-y: auto;
  padding: 1.5rem;
}
.product-icon {
  width: 40px;
  height: 40px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}


.info-item {
  display: flex;
  align-items: flex-start;
  margin-bottom: 1rem;
  padding: 0.75rem;
  background: #f8f9fa;
  border-radius: 8px;
}
.modal-footer {
  height: 60px;
  padding: 0.75rem 1.5rem;
  border-top: 1px solid #e9ecef;
  display: flex;
  justify-content: center;
  align-items: center;
  transform: translateY(-10px); /* 버튼을 10px 위로 이동 */
}
.product-icon i {
  font-size: 1.2rem;
  color: white;
}

.info-card {
  background: white;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  border: 1px solid #e9ecef;
}

.info-item {
  margin-bottom: 0.5rem;
}

.info-item:last-child {
  border-bottom: none;
}
.info-label {
  font-weight: 600;
  color: #666;
  width: 140px; /* 너비 증가 */
  flex-shrink: 0;
  padding-right: 1rem; /* 오른쪽 여백 추가 */
}

.info-value {
  color: #333;
  flex: 1;
}

.btn-custom {
  padding: 0.5rem 2rem; /* 상하 패딩 줄임 */
  border: none;
  border-radius: 10px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 120px; /* 최소 너비 설정 */
  height:40x; /* 높이 고정 */
}
.btn-custom.add {
  background: #2ecc71;
  color: white;
 
}

.btn-custom.delete {
  background: #e74c3c;
  color: white;
}
.btn-custom:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.card-subtitle {
  color: #2ecc71;
  font-weight: 600;
  display: flex;
  align-items: center;
  margin-bottom: 1.5rem; /* 제목 아래 여백 증가 */
}

@media (max-width: 768px) {
  .info-item {
    flex-direction: column;
    padding: 1rem;
  }
  
  .info-label {
    width: 100%;
    margin-bottom: 0.5rem;
    padding-right: 0;
  }
  .info-value {
    width: 100%;
  }
}

.modal-header {
  height: 70px;
  background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
  color: white;
  padding: 1rem 1.5rem;
}

.modal-body::-webkit-scrollbar-thumb:hover {
  background: #27ae60;
}

.card {
  margin-bottom: 1rem;
}

.card:last-child {
  margin-bottom: 0;
}

.card-body {
  padding: 1.5rem; /* 카드 내부 여백 증가 */
}

.info-value {
  color: #333;
  flex: 1;
  line-height: 1.5; /* 줄 간격 추가 */
}

</style>