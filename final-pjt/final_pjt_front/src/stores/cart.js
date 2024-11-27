import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useMemberStore } from "./member";

export const useCartStore = defineStore('cart', () => {
  const depositProducts = ref([])
  const savingProducts = ref([])
  const BASE_URL = 'http://127.0.0.1:8000/fin/'
  const store = useMemberStore()

  // 예금 관심 상품 조회
  const getLikesDepositProducts = function () {
    axios({
      method: 'get',
      url: BASE_URL + 'deposit/likes/',
      headers : {Authorization : `Token ${store.token}`}
    })
    .then(res => {
      depositProducts.value = res.data
    })
  }

  // 적금 관심 상품 조회
  const getLikesSavingProducts = function () {
    axios({
      method: 'get',
      url: BASE_URL + 'saving/likes/',
      headers : {Authorization : `Token ${store.token}`}
    })
    .then(res => {
      savingProducts.value = res.data
    })
  }

  // 예금 관심 상품 추가
  const addToDepositCart = (product) => {
    axios({
      method: 'post',
      url: BASE_URL + `deposit/${product.id}/likes/`,
      headers: {Authorization : `Token ${store.token}`}
    })
    .then(() => {
      const index = depositProducts.value.findIndex((element) => element.id === product.id)
      if (index === -1) {
        depositProducts.value.push(product);
      }
    })
    .catch(err => {
      console.log(err)
    })
  }
  // 예금 관심 상품 삭제
  const deleteFromDepositCart = (product) => {
    axios({
      method: 'post',
      url: BASE_URL + `deposit/${product.id}/likes/`,
      headers: {Authorization : `Token ${store.token}`}
    })
    .then(() => {
      const index = depositProducts.value.findIndex((elem) => elem.id===product.id)
      if (index !== -1) {
        depositProducts.value.splice(index, 1)
      }
    })
    .catch(err => {
      console.log(err)
    })
  }

  // 적금 관심 상품 추가
  const addToSavingCart = (product) => {
    axios({
      method: 'post',
      url: BASE_URL + `saving/${product.id}/likes/`,
      headers: {Authorization : `Token ${store.token}`}
    })
    .then(() => {
      const index = savingProducts.value.findIndex((element) => element.id === product.id)
      if (index === -1) {
        savingProducts.value.push(product);
      }
    })
    .catch(err => {
      console.log(err)
    })
  }
  // 예금 관심 상품 삭제
  const deleteFromSavingCart = (product) => {
    axios({
      method: 'post',
      url: BASE_URL + `deposit/${product.id}/likes/`,
      headers: {Authorization : `Token ${store.token}`}
    })
    .then(() => {
      const index = savingProducts.value.findIndex((elem) => elem.id===product.id)
      if (index !== -1) {
        savingProducts.value.splice(index, 1)
      }
    })
    .catch(err => {
      console.log(err)
    })
  }
 
  // 관심 상품 수
  const likesDepositProductsCount = computed(() => {
    return depositProducts.value.length
  })
  const likesSavingProductsCount = computed(() => {
    return savingProducts.value.length
  })
  
  
  return { depositProducts, savingProducts, getLikesDepositProducts, getLikesSavingProducts, addToDepositCart, deleteFromDepositCart, addToSavingCart, deleteFromSavingCart, likesDepositProductsCount, likesSavingProductsCount }
})