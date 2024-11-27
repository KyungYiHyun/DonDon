import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useMemberStore } from './member'


export const useBankStore = defineStore('bank', () => {

    const BASE_URL = 'http://127.0.0.1:8000/'

    const deposits = ref([])
    const savings = ref([])
    const recommended_deposits = ref([])
    const recommended_savings = ref([])
    const store = useMemberStore()
    
    const getDeposit = function() {
      console.log(store.token)
      axios({
        method: 'get',
        url : BASE_URL + 'fin/send/deposit/',
        headers : {Authorization : `Token ${store.token}`}
      })
      .then(res=>deposits.value = res.data)
    }

    const getSaving = function() {
      axios({
        method: 'get',
        url : BASE_URL + 'fin/send/saving/',
        headers : {Authorization : `Token ${store.token}`}
      })
      .then(res=>savings.value = res.data)
    }

    const recommendDeposits = function() {
      axios({
        method:'get',
        url : BASE_URL + 'fin/recommend/deposit/',
        headers : {Authorization : `Token ${store.token}`}
      })
      .then(res => recommended_deposits.value = res.data)
    }

    
    const recommendSavings = function() {
      axios({
        method:'get',
        url : BASE_URL + 'fin/recommend/saving/',
        headers : {Authorization : `Token ${store.token}`}
      })
      .then(res => recommended_savings.value = res.data)
    }

  


  return {getDeposit, getSaving,recommendDeposits, recommendSavings,recommended_savings,recommended_deposits, deposits, savings}
})
