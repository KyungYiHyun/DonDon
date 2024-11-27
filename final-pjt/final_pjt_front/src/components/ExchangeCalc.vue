<template>
  <div class="container">
    <div class="mb-4">
      <label class="form-label">원화</label>
      <div class="input-group">
        <input 
          type="text" 
          class="form-control" 
          v-model="country1Amount"
          placeholder="금액을 입력하세요"
        >
        <span class="input-group-text">원</span>
      </div>
    </div>

    <div class="mb-4">
      <label class="form-label">국가 선택</label>
      <select class="form-select" v-model="selectedCountry">
        <option value="none">나라를 선택하세요</option>
        <option value="노르웨이">노르웨이</option>
        <option value="뉴질랜드">뉴질랜드</option>
        <option value="덴마아크">덴마크</option>
        <option value="말레이지아">말레이시아</option>
        <option value="미국">미국</option>
        <option value="바레인">바레인</option>
        <option value="사우디">사우디아라비아</option>
        <option value="스웨덴">스웨덴</option>
        <option value="스위스">스위스</option>
        <option value="싱가포르">싱가포르</option>
        <option value="아랍에미리트">아랍에미리트</option>
        <option value="영국">영국</option>
        <option value="위안화">중국</option>
        <option value="유로">유럽연합</option>
        <option value="인도네시아">인도네시아</option>
        <option value="일본">일본</option>
        <option value="캐나다">캐나다</option>
        <option value="쿠웨이트">쿠웨이트</option>
        <option value="태국">태국</option>
        <option value="호주">호주</option>
        <option value="홍콩">홍콩</option>
      </select>
    </div>

    <div class="mb-3">
      <label class="form-label">환전 금액</label>
      <div class="input-group">
        <input 
          type="text" 
          class="form-control" 
          v-model="country2Amount"
          placeholder="환전 금액이 표시됩니다"
        >
        <span class="input-group-text">{{unit}}</span>
      </div>
      
    </div>
    <span style="font-weight: 600;">나라를 선택하고 금액을 입력하세요</span> 
  </div>
  
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref, watch } from 'vue';
import { useMemberStore } from '../stores/member.js'

onMounted(()=>{
  exchange()
})
const BASE_URL = 'http://127.0.0.1:8000/'
const exchange_rate_info = ref([])
const selectedCountry = ref('none')
const countrydeal = ref(0)
const store = useMemberStore()

const country1Amount = ref('')
const country2Amount = ref('')

const unit = ref('')

const formatNumber = (value) => {
  if (!value) return ''
  return Number(value).toLocaleString('ko-KR', {
    maximumFractionDigits: 2,
    minimumFractionDigits: 2
  })
}

const exchange = function() {
  axios({
    method:'get',
    url : BASE_URL + 'fin/exchange/',
    headers : {Authorization : `Token ${store.token}`}
  })
  .then(res => {
    exchange_rate_info.value = res.data;
  
  })
}

const processExchangeData = (name) => {
  if (exchange_rate_info.value.length > 0) {
    exchange_rate_info.value.forEach(item => {
      const current_country = item.cur_nm.split(' ')
      
      
      
      if(current_country[0] == name){
        countrydeal.value = parseFloat(item.deal_bas_r.replace(/,/g, '')) || 0
        unit.value = current_country[1]
        if (name == '위안화'){unit.value = '元'}
        if (name == '유로'){unit.value = '€'}
        if (unit.value == '달러'){unit.value='$'}
        else if (unit.value == '옌'){unit.value='¥'}
        else if (unit.value == '크로네' || unit.value=='크로나'){unit.value='kr'}
        else if (unit.value == '링기트'){unit.value='MYR'}
        else if (unit.value == '디나르'){unit.value='BHD'}
        else if (unit.value == '리얄'){unit.value='﷼'}
        else if (unit.value == '프랑'){unit.value='Fr'}
        else if (unit.value == '디르함'){unit.value='Dhs'}
        else if (unit.value == '파운드'){unit.value='£'}
        else if (unit.value == '중국'){unit.value='元'}
        else if (unit.value == '루피아'){unit.value='Rp'}
        else if (unit.value == '바트'){unit.value='฿'}
      }
    })
  }
}

watch(selectedCountry, (newValue) => {
  processExchangeData(selectedCountry.value)
  country1Amount.value = ''
  country2Amount.value = ''
});

const isProcessing = ref(false)

const convertToKRW = (value) => {
  if (!value || isNaN(value) || countrydeal.value === 0) return ''
  return Math.floor(Number(value) * countrydeal.value)
}

const convertToForeign = (value) => {
  if (!value || isNaN(value) || countrydeal.value === 0) return ''
  return (Number(value) / countrydeal.value).toFixed(2)
}

watch(country1Amount, (newValue) => {
  if (isProcessing.value) return
  isProcessing.value = true
  
  if (isNaN(newValue)) {
    country2Amount.value = ''
  } else {
    const converted = convertToForeign(newValue)
    country2Amount.value = formatNumber(converted)
   
  }
  
  setTimeout(() => {
    isProcessing.value = false
  }, 40)
})
watch(country2Amount, (newValue) => {
  if (isProcessing.value) return
  isProcessing.value = true
  
  if (isNaN(newValue)) {
    country1Amount.value = ''
  } else {
    const converted = convertToKRW(newValue)
    country1Amount.value = formatNumber(converted)
  }
  
  setTimeout(() => {
    isProcessing.value = false
  }, 40)
})
</script>

<style scoped>
.container {
  padding: 20px;
}

.form-control:focus {
  border-color: #80bdff;
  box-shadow: 0 0 0 0.2rem rgba(0,123,255,.25);
}

.input-group-text {
  background-color: #f8f9fa;
}
</style>