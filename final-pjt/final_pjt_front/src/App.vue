<template>
  <NavBar />
  <div class="modal fade" id="exchangeModal" tabindex="-1" aria-labelledby="exchangeModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <ExchangeCalc/>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
        </div>
      </div>
    </div>
  </div>
  <RouterView />
  <!-- <Footer /> -->
</template>

<script setup>
import { RouterView } from 'vue-router';
import { useMemberStore } from './stores/member';
import ExchangeCalc from './components/ExchangeCalc.vue';
import NavBar from './components/NavBar.vue';
import Footer from './components/Footer.vue';
import { onMounted } from 'vue';
const store = useMemberStore()

// 페이지 껐다키면 로컬 삭제하려고 했는데 새로고침해도 삭제됨
// onMounted(() => {
//   const token = localStorage.getItem('token')
//   if (!token) {
//     localStorage.clear()
//   }
// })




</script>

<style scoped>

</style>