
<template>
  <br>
  <div class="container-fluid px-5">
    <!-- 필터링 섹션 중앙 정렬 -->
    
    <div class="filter-section">
  <div class="filter-group" data-label="은행 유형">
    <button 
      v-for="type in bankTypes" 
      :key="type.code"
      @click="filterByBankType(type.code)"
      :class="{ active: selectedBankType === type.code }"
      class="btn"
    >
      {{ type.name }}
    </button>
  </div>
  
  <div class="filter-group" data-label="금리 유형">
    <button 
      @click="filterByRateType(null)"
      :class="{ active: selectedRateType === null }"
      class="btn"
    >
      전체
    </button>
    <button 
      v-for="type in rateTypes" 
      :key="type"
      @click="filterByRateType(type)"
      :class="{ active: selectedRateType === type }"
      class="btn"
    >
      {{ type }}
    </button>
  </div>
  
  <div class="filter-group" data-label="가입 기간">
    <button 
      @click="filterByTerm(null)"
      :class="{ active: selectedTerm === null }"
      class="btn"
    >
      전체
    </button>
    <button 
      v-for="term in terms" 
      :key="term"
      @click="filterByTerm(term)"
      :class="{ active: selectedTerm === term }"
      class="btn"
    >
      {{ term }}개월
    </button>
  </div>
</div>
    <!-- 고정된 테이블 헤더 -->
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

    <!-- 스크롤 가능한 테이블 본문 -->
    <div class="table-content">
      <DepositListItem 
        v-for="(deposit, index) in displayedDeposits" 
        :key="deposit.id"
        :deposit="deposit"
        :rank="index + 1"
      />

      <!-- 로딩 스피너 -->
      <div v-if="isLoading" class="text-center my-3">
        <div class="spinner-border text-primary" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useBankStore } from '@/stores/bank';
import { onMounted, ref, computed, onUnmounted } from 'vue';
import DepositListItem from './DepositListItem.vue';

const store = useBankStore()
const terms = [6, 12, 24, 36]
const rateTypes = ['단리', '복리']
const selectedTerm = ref(null)
const selectedRateType = ref(null)
const page = ref(1)
const itemsPerPage = 15
const isLoading = ref(false)
const bankTypes = [
  { name: '전체', code: null },
  { name: '은행', code: '020000' },
  { name: '저축은행', code: '030300' }
]
const selectedBankType = ref(null)

// 필터링 및 정렬
const sortedAndFilteredDeposits = computed(() => {
  const filtered = store.deposits.filter(deposit => {
    const termMatch = selectedTerm.value === null || deposit.save_trm === selectedTerm.value
    const rateTypeMatch = selectedRateType.value === null || deposit.intr_rate_type_nm === selectedRateType.value
    const bankTypeMatch = selectedBankType.value === null || deposit.fin_grp_cd === selectedBankType.value
    return termMatch && rateTypeMatch && bankTypeMatch
  })
  return filtered.sort((a, b) => b.intr_rate - a.intr_rate)
})

// 화면에 표시될 데이터
const displayedDeposits = computed(() => {
  return sortedAndFilteredDeposits.value.slice(0, page.value * itemsPerPage)
})

// 무한 스크롤 처리
const handleScroll = () => {
  if (isLoading.value) return

  const scrollPosition = window.pageYOffset + window.innerHeight
  const documentHeight = document.documentElement.scrollHeight

  if (scrollPosition >= documentHeight - 100) {
    if (displayedDeposits.value.length < sortedAndFilteredDeposits.value.length) {
      loadMoreData()
    }
  }
}

const loadMoreData = async () => {
  isLoading.value = true
  await new Promise(resolve => setTimeout(resolve, 500))
  page.value++
  isLoading.value = false
}

const filterByTerm = (term) => {
  selectedTerm.value = term === selectedTerm.value ? null : term
  resetPagination()
}

const filterByRateType = (type) => {
  selectedRateType.value = type === selectedRateType.value ? null : type
  resetPagination()
}

const filterByBankType = (code) => {
  selectedBankType.value = code === selectedBankType.value ? null : code
  resetPagination()
}

const resetPagination = () => {
  page.value = 1
}

onMounted(() => {
  store.getDeposit()
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.container-fluid {
  max-width: 1400px; /* 전체 너비 증가 */
  margin: 0 auto;
}

.filter-section {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: 20px 0;
}

.table {
  border-collapse: separate;
  border-spacing:0;
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


.filter-group {
  border-bottom: 2px solid #eee;
  align-items: center;
}

.filter-group::before {
  content: attr(data-label);
  font-weight: 500;
  color: #666;
  margin-right: 15px;
  min-width: 80px;
  text-align: left;
}
.table-header-container {
 
  top: 80px;
  background-color: white;
  z-index: 90; /* 필터 섹션보다 더 낮은 z-index */
}

.table-body-container {
  overflow-y: auto;
  min-height: 400px; /* 최소 높이 설정 */
}
.table-content {
  position: relative;
  z-index: 1;
}


.filter-group {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  margin-bottom: 0;
  padding: 10px 20px;
  

}

.btn {
  padding: 8px 16px;
  border: none;
  background: none;
  color: #666;  /* 기본 텍스트 색상 */
  transition: all 0.3s ease;
  min-width: 100px;
  position: relative;
}


.btn::after {
  content: '';
  position: absolute;
  width: 0;
  height: 2px;
  bottom: 0;
  left: 50%;
  background-color: #2ecc71;  /* 밑줄 색상을 검은색으로 통일 */
  transition: all 0.3s ease;
  transform: translateX(-50%);
}

.btn.active {
  color: #000;  /* 활성화 상태 텍스트 색상 */
  transform: none;
  background: none;
}

.btn.active::after {
  width: 80%;  /* 활성화 시 밑줄 너비 */
}
.btn:hover {
  color: #000;
  background: none;
}



.btn-outline-info.active::after,
.btn-outline-secondary.active::after,
.btn-outline-primary.active::after {
  background-color: #000;
}
.btn-outline-info.active,
.btn-outline-secondary.active,
.btn-outline-primary.active {
  background: none;
  color: #000;
}

.table {
  margin-bottom: 0;
  background-color: white;
}

.table th, .table td {
  vertical-align: middle;
  padding: 1rem;

}


.btn-outline-primary.active {
  background: none;
  color: black;
}
.btn-outline-primary.active::after {
  background-color: black;
}
.btn:hover::after {
  width: 40%;
}

.rank-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background-color: #e9ecef;
  font-weight: bold;
  color: #495057;
}

.top-three {
  background-color: #ffd700;
  color: #000;
  font-size: 1.1em;
  width: 35px;
  height: 35px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.product-name {
  color: #0d6efd;
  font-weight: 500;
}

.cursor-pointer:hover {
  background-color: #f8f9fa;
}

.badge {
  font-size: 0.9rem;
  padding: 0.5em 1em;
}

/* 테이블 내부 여백 조정 */
.table td, .table th {
  padding: 1rem 0.5rem;
  
}

/* 반응형 조정 */
@media (max-width: 768px) {
  .container-fluid {
    padding: 10px;
  }
  
  .btn {
    min-width: auto;
  }
}





</style>