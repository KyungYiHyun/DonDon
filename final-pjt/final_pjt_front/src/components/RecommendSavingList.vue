<template>
  <div class="container">
    <!-- Top 3 Cards -->
    <div class="row mb-5">
      <div v-for="(product, index) in savingTopThree" :key="index" class="col-md-4 cursor-pointer" data-bs-toggle="modal" :data-bs-target="`#savingModal-${product.id}`">
        <div class="card h-100" >
          <div class="card-header text-center">
            <span class="badge-text">
              {{ index + 1 }}위
            </span>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" :class="{'gold-medal': index === 0, 'silver-medal': index === 1, 'bronze-medal': index === 2} "><path d="M14.9 17.276a8.256 8.256 0 0 1-2.9.524 8.256 8.256 0 0 1-4.5-1.332v4.73a.799.799 0 0 0 1.18.705L12 20.109l3.32 1.794a.803.803 0 0 0 .79-.017.799.799 0 0 0 .39-.687v-4.731a8.191 8.191 0 0 1-1.6.808Z" fill="currentColor"></path><path d="M12 2C7.864 2 4.5 5.365 4.5 9.5a7.495 7.495 0 0 0 3.8 6.52A7.432 7.432 0 0 0 12 17a7.453 7.453 0 0 0 4.5-1.504c1.82-1.37 3-3.548 3-5.996C19.5 5.365 16.136 2 12 2Zm2.924 10.629a.6.6 0 0 1-.855.727l-.28-.156-1.787-.993-1.787.993-.28.156a.6.6 0 0 1-.856-.727l.798-2.229-1.762-1.49a.6.6 0 0 1 .387-1.058h2.244l.693-1.889a.6.6 0 0 1 1.126 0l.693 1.889h2.244a.598.598 0 0 1 .387 1.058l-1.762 1.49.798 2.229h-.001Z" fill="currentColor"></path></svg>
          </div>
          <div class="card-body" @click="openModal(index)" style="cursor: pointer;">
            <h5 class="card-title prdt-name">{{ product.fin_prdt_nm }}</h5>
            <p class="card-text bank-name">{{ product.kor_co_nm }}</p>
            <div class="rates mt-3">
              <div class="d-flex justify-content-between mb-2">
                <span class="badge-text">기본금리</span>
                <span class="intr">{{ product.intr_rate }}%</span>
              </div>
              <div class="d-flex justify-content-between">
                <span class="badge-text">우대금리</span>
                <span class="intr">{{ product.intr_rate2 }}%</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Rest of the products table -->
    <!-- <div class="table-responsive">
      <h4 class="mb-3">기타 추천 상품</h4>
      <table class="table table-hover">
        <thead class="table-light">
          <tr>
            <th>순위</th>
            <th>은행</th>
            <th>상품명</th>
            <th>기본금리</th>
            <th>우대금리</th>
          </tr>
        </thead>
        <tbody>
          <RecommendSavingListItem 
            v-for="(saving,index) in store.recommended_savings.slice(3)" 
            :key="saving.id" 
            :saving="saving"
            :rank ="index + 1"
          />
        </tbody>
      </table>
    </div> -->
    <div class="table-header-container">
      <table class="table table-bordered">
        <thead>
          <tr class="table-light text-center">
            <th style="width: 8%">순위</th>
            <th style="width: 15%">은행</th>
            <th style="width: 32%">상품명</th>
            <th style="width: 15%">기본금리</th>
            <th style="width: 15%">우대금리</th>
            <th style="width: 15%">금리유형</th>
          </tr>
        </thead>
      </table>
    </div>
    <div class="table-content">
      <RecommendSavingListItem 
        v-for="(saving, index) in store.recommended_savings.slice(3)" 
        :key="saving.id"
        :saving="saving"
        :rank="index + 1"
      />

      <!-- 로딩 스피너 -->
      <div v-if="isLoading" class="text-center my-3">
        <div class="spinner-border text-primary" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      </div>
    </div>
    <!-- Modal -->
    <div v-for="product in savingTopThree" :key="product.id">
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
    </div>
  </div>
</template>

<script setup>
import RecommendSavingListItem from './RecommendSavingListItem.vue';
import { useBankStore } from '@/stores/bank';
import { onMounted } from 'vue';
import { ref, watch} from 'vue';
import SavingDetail from './SavingDetail.vue';

const store = useBankStore()
const savingTopThree = ref([])
const selectedProduct = ref(null)


onMounted(()=>{
  store.recommendSavings()
})
watch(
  () => store.recommended_savings,
  (newValue) => {
    savingTopThree.value = newValue.slice(0,3)
  
  }
)


const isModalVisible = ref(false);

const openModal = (index) => {
  selectedProduct.value = savingTopThree.value[index]
  isModalVisible.value = true
}

const updateModalVisibility = (newValue) => {
  isModalVisible.value = newValue;
}

</script>

<style scoped>
.table {
  border-collapse: separate;
  border-spacing:0;
}
.table-header-container {
 
 top: 80px;
 background-color: white;
 z-index: 90; /* 필터 섹션보다 더 낮은 z-index */
}

.table th {
  vertical-align: middle;
  padding: 1rem 0.5rem;
  border-left: none;  /* 왼쪽 세로선 제거 */
  border-right: none; /* 오른쪽 세로선 제거 */ 
  background-color: white;
  border-top: none;
  border-bottom: 1px solid #999999
}
.gold-medal {
  color: #FFDB51;
    
}
.silver-medal {
  color: #D7D7D7;;
    
}
.bronze-medal {
  color: #CD7F32;
    
}
.table th, .table td {
  vertical-align: middle;
  padding: 1rem;

}
.card {
  transition: transform 0.2s;
  border-width: 2px;
}
.table-content {
  position: relative;
  z-index: 1;
}
.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
 
}

.card-header{
  background-color: white;
}

.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1050;
}

.intr{
  color: #d8205f;
}

th {
  background: white;
}

.badge-text{
  font-weight: bold;
}

.modal-content{
  border: none;
}
 
.bank-name{
  color: #0073c9;
  font-weight: bold;
}

.prdt-name{
  font-weight: bold;
}
.table-bordered{
margin-bottom: 0px;
}

</style>