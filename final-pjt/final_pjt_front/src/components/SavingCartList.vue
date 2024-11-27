<template>
  <div class="container py-2">
    <div class="cart-card mx-auto">
      <div class="cart-header">
        <div class="cart-icon">
          <i class="fas fa-piggy-bank" aria-hidden="true"></i>
        </div>
        <h4 class="mt-3 mb-0" style="font-weight: bold;">
          적금상품
          <span v-if="store.likesSavingProductsCount" class="count-badge">
            {{ store.likesSavingProductsCount }}
          </span>
        </h4>
      </div>
      
      <div class="cart-body">
        <div v-if="store.savingProducts.length > 0" class="scroll-box">
          <div class="scroll-content">
            <SavingCartListItem 
              v-for="product in store.savingProducts"
              :key="product.id"
              :product="product"
            />
          </div>
        </div>
        <div v-else class="empty-cart">
          <i class="fas fa-heart-broken mb-3" aria-hidden="true"></i>
          <p>관심있는 상품을 추가해주세요</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useCartStore } from '@/stores/cart';
import { onMounted } from 'vue';
import SavingCartListItem from './SavingCartListItem.vue';

const store = useCartStore()

onMounted(() => {
  store.getLikesSavingProducts()
})
</script>

<style scoped>
.cart-card {
  max-width: 1200px;
  background: white;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}
.cart-header {
  background: white; /* 배경을 흰색으로 변경 */
  color: #333; /* 텍스트 색상을 어두운 색으로 변경 */
  padding: 2rem;
  text-align: center;
  border-bottom: 2px solid #f0f0f0; /* 구분선 추가 */
}
.cart-icon {
  width: 80px;
  height: 80px;
  background: #2ecc71; /* 아이콘 배경만 초록색으로 */
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
  transition: transform 0.3s ease;
}

.cart-icon:hover {
  transform: scale(1.05);
}

.cart-icon i {
  font-size: 2rem;
  color: white;
}

.count-badge {
  display: inline-block;
  background: #2ecc71; /* 뱃지 배경을 초록색으로 */
  color: white; /* 뱃지 텍스트는 흰색으로 */
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.9rem;

  
}
.cart-body {
  padding: 2rem;
}

.scroll-box {
  width: 100%;
  overflow-x: auto;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 10px;
}

.scroll-content {
  display: flex;
  gap: 20px;
  align-items: flex-start;
  min-width: min-content;
}

.empty-cart {
  text-align: center;
  padding: 3rem;
  color: #666;
}

.empty-cart i {
  font-size: 3rem;
  color: #ddd;
  display: block;
}

/* 스크롤바 스타일링 */
.scroll-box::-webkit-scrollbar {
  height: 8px;
}

.scroll-box::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 4px;
}

.scroll-box::-webkit-scrollbar-thumb {
  background: #2ecc71;
  border-radius: 4px;
}

.scroll-box::-webkit-scrollbar-thumb:hover {
  background: #27ae60;
}

/* 반응형 디자인 */
@media (max-width: 768px) {
  .cart-card {
    margin: 0 1rem;
  }
  
  .cart-body {
    padding: 1rem;
  }
}
</style>