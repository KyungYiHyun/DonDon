<template>
  <div class="container py-5">
    <div class="row">
      <!-- 프로필 섹션 -->
     

    <div class="profile-card mx-auto">
      <div class="profile-header">
        <div class="profile-avatar">
          <span class="avatar-text">{{ store.currentUsername[0] }}</span>
        </div>
        <h4 class="mt-3 mb-0">{{ store.currentUsername }}</h4>
      </div>
      
      <div class="profile-body">
        <div v-if="!isEditing">
          <div class="info-group">
            <div class="info-item">
              <span class="info-label">회원번호</span>
              <span class="info-value">{{ store.currentUserId }}</span>
            </div>
            <div class="info-item">
              <span class="info-label">아이디</span>
              <span class="info-value">{{ store.currentUsername }}</span>
            </div>
            <div class="info-item">
              <span class="info-label">Email</span>
              <span class="info-value">{{ store.userEmail }}</span>
            </div>
            <div class="info-item">
              <span class="info-label">닉네임</span>
              <span class="info-value">{{ store.nickname }}</span>
            </div>
            <div class="info-item">
              <span class="info-label">성별</span>
              <span class="info-value">{{ store.userGender }}</span>
            </div>
            <div class="info-item">
              <span class="info-label">나이</span>
              <span class="info-value">{{ store.userAge }}</span>
            </div>
            <div class="info-item">
              <span class="info-label">직업군</span>
              <span class="info-value">{{ store.userJob }}</span>
            </div>
            <div class="info-item">
              <span class="info-label">자산</span>
              <span class="info-value">{{ store.userAssets.toLocaleString() }} 원</span>
            </div>
            <div class="info-item">
              <span class="info-label">연봉</span>
              <span class="info-value">{{ store.userSalary.toLocaleString() }} 원</span>
            </div>
          </div>
          <div class="text-center mt-4">
            <button class="btn-custom edit" @click="startEdit">
              <i class="fas fa-user-edit me-2"></i>프로필 수정
            </button>
            <div class="mt-3">
              <RouterLink :to="{name: 'PasswordChangeView'}" class="btn-custom password me-2">
                <i class="fas fa-key me-2"></i>비밀번호 변경
              </RouterLink>
              <button class="btn-custom delete" @click="signOut">
                <i class="fas fa-user-times me-2"></i>회원탈퇴
              </button>
            </div>
          </div>
        </div>

        <div v-else class="edit-form">
          <div class="mb-4">
            <label class="form-label">Email</label>
            <input type="email" class="form-control custom-input" v-model="editedEmail">
          </div>
          <div class="mb-4">
            <label class="form-label">닉네임</label>
            <input type="text" class="form-control custom-input" v-model="editedNickname">
          </div>
          <div class="mb-4">
            <label class="form-label d-block">성별</label>
            <div class="gender-group">
              <label class="gender-option">
                <input type="radio" v-model="editedGender" value="남">
                <span class="gender-text">남성</span>
              </label>
              <label class="gender-option">
                <input type="radio" v-model="editedGender" value="여">
                <span class="gender-text">여성</span>
              </label>
            </div>
          </div>
          <div class="mb-4">
            <label class="form-label">나이</label>
            <input type="number" class="form-control custom-input" v-model="editedAge">
          </div>
          <div class="mb-4">
            <label class="form-label">직업군</label>
            <select id="job" class="form-control custom-input" v-model="editedJob">
              <option disabled value="">직업 선택</option>
              <option v-for="job in jobs" :key="job">
                {{ job }}
              </option>
            </select>
            <!-- <input type="text" class="form-control custom-input" v-model="editedJob"> -->
          </div>
          <div class="mb-4">
            <label class="form-label">자산</label>
            <input type="number" class="form-control custom-input" v-model="editedAssets">
          </div>
          <div class="mb-4">
            <label class="form-label">연봉</label>
            <input type="number" class="form-control custom-input" v-model="editedSalary">
          </div>
          <div class="button-group">
            <button class="btn-custom save" @click="updateProfile">
              <i class="fas fa-check me-2"></i>저장
            </button>
            <button class="btn-custom cancel" @click="cancelEdit">
              <i class="fas fa-times me-2"></i>취소
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="col-lg-6">
 
        <div class="charts-container">
          <h1 class="text-center pb-3 portfolio" >포트폴리오</h1>
          <div class="chart-wrapper mb-4">
            <canvas id="intrChart"></canvas>
          </div>
          <div class="chart-wrapper">
            <canvas id="typeChart"></canvas>
          </div>
        </div>
      </div>
  </div>
    </div>
 
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { RouterLink } from 'vue-router'
import { useMemberStore } from '@/stores/member'
import { useCartStore } from '@/stores/cart';



const BASE_URL = 'http://127.0.0.1:8000'
const store = useMemberStore()
const cartStore = useCartStore()
const isEditing = ref(false)

// 수정할 정보를 저장할 변수들
const editedEmail = ref('')
const editedNickname = ref('')
const editedAge = ref('')
const editedAssets = ref('')
const editedSalary = ref('')
const editedGender = ref('')
const editedJob = ref('')

const job = ref("")
const jobs = [
    "경영·사무",
    "금융·보험",
    "교육",
    "자연·사회과학",
    "법률·경찰·소방·교도·국방",
    "보건·의료",
    "사회복지·종교", 
    "문화·예술·디자인·방송",
    "운전·운송",
    "영업·판매",
    "경비·청소",
    "미용·숙박·여행·오락·스포츠", 
    "음식서비스",
    "건설", 
    "기계", 
    "재료", 
    "화학", 
    "섬유·의복",
    "전기·전자",
    "정보통신", 
    "식품가공", 
    "인쇄·목재·가구·공예",
    "환경·에너지·안전",
    "농림어업",
    "학생", 
    "무직", 
]
// 수정 모드 시작
const startEdit = () => {
  isEditing.value = true
  // 현재 값으로 초기화
  editedEmail.value = store.userEmail
  editedNickname.value = store.nickname
  editedAge.value = store.userAge
  editedAssets.value = store.userAssets
  editedSalary.value = store.userSalary
  editedGender.value = store.userGender
  editedJob.value = store.userJob
}

const signOut = function() {
  const answer = window.confirm('정말 탈퇴하시겠습니까?')
  if (answer === false) {
    return false
  } else {
    store.signOut()
  }
}

// 수정 취소
const cancelEdit = () => {
  isEditing.value = false
  // 입력 필드 초기화
  editedEmail.value = ''
  editedNickname.value = ''
  editedAge.value = ''
  editedAssets.value = ''
  editedSalary.value = ''
  editedGender.value = ''
  editedJob.value = ''
}

// 프로필 업데이트
const updateProfile = async () => {
  try {
    await axios({
      method: 'patch',
      url: `${BASE_URL}/accounts/update/`,
      headers: {
        Authorization: `Token ${store.token}`
      },
      data: {
        email: editedEmail.value,
        nickname: editedNickname.value,
        gender : editedGender.value,
        age: editedAge.value,
        assets: editedAssets.value,
        salary: editedSalary.value,
        job: editedJob.value
      }
    })
    // 수정 완료 후 처리
    isEditing.value = false
    // 프로필 정보 새로고침
    await store.findCurrentUser()
  } catch (error) {
    console.error('프로필 수정 실패:', error)
  }
}

onMounted(async () => {
  // 데이터 로딩 대기
  await Promise.all([
    store.findCurrentUser(),
    cartStore.getLikesDepositProducts(),
    cartStore.getLikesSavingProducts()
  ])
  
})


setTimeout(()=>{
  if (cartStore.depositProducts.length > 0) {
  const typeCt = document.getElementById('typeChart')
  if (typeCt) {
    new Chart(typeCt, {
      type: 'doughnut',
      data: {
        labels: ['정기예금', '정기적금'],
        datasets: [{
          data: [cartStore.likesDepositProductsCount, cartStore.likesSavingProductsCount],
          backgroundColor: [
            'rgba(46, 204, 113, 0.5)',
            'rgba(52, 152, 219, 0.5)'
          ]
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'top',
          },
          title: {
            display: true,
            text: '상품 유형별 분포'
          }
        }
      }
    })
  }
  
}
const intrCt = document.getElementById('intrChart')
if (intrCt) {
  new Chart(intrCt, {
    type: 'bar',
    data: {
      labels: [...cartStore.depositProducts.map(product => product.fin_prdt_nm),
               ...cartStore.savingProducts.map(product => product.fin_prdt_nm)],
      datasets: 
      [{
        label: '예금 기본금리',
        data: [...cartStore.depositProducts.map(product => product.intr_rate),
               ...Array(cartStore.savingProducts.length).fill(null)],
        backgroundColor: 'rgba(46, 204, 113, 0.5)',
        borderColor: 'rgb(46, 204, 113)',
        borderWidth: 2
      },
      {
        label: '적금 기본금리',
        data: [...Array(cartStore.depositProducts.length).fill(null),
               ...cartStore.savingProducts.map(product => product.intr_rate)],
        backgroundColor: 'rgba(52, 152, 219, 0.5)',
        borderColor: 'rgb(52, 152, 219)',
        borderWidth: 2
      }],
  
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales :{
        x :{
          offset:true,
          grid: {
            display:false
          }
        },
        y :{
          grid:{
            display:false
          }
        }
      },
      
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: '예금/적금 상품별 금리 비교'
        }
      }
    }
  })
}
  }
  ,50)



</script>
<style scoped>
.profile-card {
  max-width: 600px;
  background: white;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.profile-header {
  /* 초록색 그라데이션으로 변경 */
  background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
  color: white;
  padding: 2rem;
  text-align: center;
  margin-top: 30px;
  border-radius: 10px;

}

.profile-avatar {
  width: 80px;
  height: 80px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
}

.avatar-text {
  font-size: 2rem;
  font-weight: bold;
  color: white;
}

.profile-body {
  padding: 2rem;
}

.info-group {
  display: grid;
  gap: 1rem;
}

.info-item {
  display: flex;
  align-items: center;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 10px;
}

.info-label {
  font-weight: 600;
  color: #666;
  width: 100px;
}

.info-value {
  color: #333;
  flex: 1;
}

.custom-input {
  border: 2px solid #e9ecef;
  border-radius: 10px;
  padding: 0.75rem;
  transition: all 0.3s;
}

.custom-input:focus {
  /* 입력창 포커스 효과 */
  border-color: #2ecc71;
  box-shadow: 0 0 0 3px rgba(46, 204, 113, 0.1);
}


.gender-group {
  display: flex;
  gap: 1rem;
}

.gender-option {
  flex: 1;
  position: relative;
  cursor: pointer;
}

.gender-option input {
  display: none;
}

.gender-text {
  display: block;
  padding: 0.75rem;
  text-align: center;
  background: #f8f9fa;
  border-radius: 10px;
  transition: all 0.3s;
}

.gender-option input:checked + .gender-text {
  /* 선택된 성별 버튼 색상 */
  background: #2ecc71;
  color: white;
}

.button-group {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
}

.btn-custom {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 10px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.btn-custom.edit {
  /* 프로필 수정 버튼 */
  background: #2ecc71;
  color: white;
  width: 200px;
}

.btn-custom.save {
  /* 저장 버튼 */
  background: #2ecc71;
  color: white;
  flex: 1;
}
.btn-custom.cancel {
  /* 취소 버튼 */
  background: #e74c3c;
  color: white;
  flex: 1;
}

.btn-custom:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(46, 204, 113, 0.2);
}

.form-label {
  font-weight: 600;
  color: #666;
  margin-bottom: 0.5rem;
}

.edit-form {
  max-width: 500px;
  margin: 0 auto;
}

.btn-custom.cancel:hover {
  box-shadow: 0 5px 15px rgba(231, 76, 60, 0.2);
}

.btn-custom.password {
  background: #3498db;
  color: white;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.75rem 1.5rem;
  border-radius: 10px;
  font-weight: 600;
  transition: all 0.3s;
}

.btn-custom.delete {
  background: #e74c3c;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 10px;
  font-weight: 600;
  transition: all 0.3s;
}


.btn-custom.password:hover,
.btn-custom.delete:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.btn-custom.password:hover {
  background: #2980b9;
}


.btn-custom.delete:hover {
  background: #c0392b;
}

.container-fluid {
  max-width: 1400px;
  margin: 0 auto;
}

.charts-container {
  background: white;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  padding: 2rem;
  height: 100%;
}

.chart-wrapper {
  margin-bottom: 2rem;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 10px;
  height: 400px;
}

.chart-wrapper:last-child {
  margin-bottom: 0;
}

@media (max-width: 992px) {
  .profile-card {
    margin-bottom: 2rem;
  }
  
  .charts-container {
    height: auto;
  }
}

.portfolio{
  color: #2ecc71;
  font-weight: 600;
  
  font-size: 2rem;
}
  

</style>