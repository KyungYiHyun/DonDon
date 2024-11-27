<template>
  <div>
    <DepositCartList />
    <SavingCartList/>
  </div>

 
  
</template>

<script setup>
import DepositCartList from '@/components/DepositCartList.vue';
import SavingCartList from '@/components/SavingCartList.vue';
import { useCartStore } from '@/stores/cart';
import { RouterLink } from 'vue-router';


const store = useCartStore()


// const goDetail = (product) => 
// useCartStore
</script>

<style scoped>

</style>