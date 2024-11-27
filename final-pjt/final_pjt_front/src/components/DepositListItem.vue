<template>
  <div class="table-responsive">
    <table class="table table-bordered table-hover mb-0">
      <tbody>
        <tr data-bs-toggle="modal" :data-bs-target="`#depositModal-${deposit.id}`" class="cursor-pointer">
          <td style="width: 8%" class="text-center">
            <span class="rank-badge" :class="{'top-three': rank <= 3}">
              {{ rank }}
            </span>
          </td>
          <td style="width: 15%" class="text-center bank-name">{{ deposit.kor_co_nm }}</td>
          <td style="width: 32%" class="product-name text-center">{{ deposit.fin_prdt_nm }}</td>
          <td style="width: 15%" class="text-center">
            <span class="badge-intr">{{ deposit.intr_rate }}%</span>
          </td>
          <td style="width: 15%" class="text-center">
            <span class="badge-intr">{{ deposit.intr_rate2 }}%</span>
          </td>
          <td style="width: 15%" class="text-center">
            <span class="badge-nm">{{ deposit.intr_rate_type_nm }}</span>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- 모달만 남기고 backdrop 제거 -->
    <div 
      class="modal fade" 
      :id="`depositModal-${deposit.id}`" 
      tabindex="-1" 
      aria-labelledby="depositModalLabel" 
      aria-hidden="true"
       data-bs-backdrop="false"
    >
      <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
          <DepositDetail :product="deposit" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import DepositDetail from './DepositDetail.vue';

const props = defineProps({
  deposit: Object,
  rank: Number
})

const isModalVisible = ref(false);

const openModal = () => {
  isModalVisible.value = true;
}

const updateModalVisibility = (newValue) => {
  isModalVisible.value = newValue;
}
</script>

<style scoped>
.table {
  margin-bottom: 0;
}

.bank-name{
  color: #0d6efd;
}

.table td {
  vertical-align: middle;
  padding: 1rem 0.5rem;
}

.rank-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  font-weight: bold;
  
}

.table {
  border-collapse: separate;
  border-spacing:0;
}
.table td {
  vertical-align: middle;
  padding: 1rem 0.5rem;
  border-left: none;  /* 왼쪽 세로선 제거 */
  border-right: none; /* 오른쪽 세로선 제거 */
  border-bottom: none;

}


.product-name {
  
  font-weight: 500;
}

.cursor-pointer:hover {
  background-color: #f8f9fa;
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

.badge {
  font-size: 0.9rem;
  padding: 0.5em 1em;
}

.modal-content {
  height: 750px;
  border: none;
}

.badge-intr{
  
  color: #d8205f;
}

.badge-nm{
  color: black;
}
</style>