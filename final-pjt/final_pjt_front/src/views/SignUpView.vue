<template>
  <div class="container py-5">
    <div class="profile-card mx-auto">
      <!-- 헤더 -->
      <div class="profile-header">
        <h2>회원가입</h2>
        <p class="mb-0">필수 정보들을 입력해주세요.</p>
      </div>
      <!-- 회원가입 폼 -->
      <div class="profile-body">
        <form @submit.prevent="signUp" class="edit-form">
          <!-- 아이디 입력 -->
          <div class="mb-3">
            <div class="input-wrapper">
              <i class="fa-solid fa-user input-icon"></i>
              <input
                type="text"
                id="username"
                v-model.trim="username"
                placeholder="아이디"
                :class="{'custom-input': true, 'error-input': errors.username}"
              />
            </div>
            <span v-if="errors.username" class="error">{{ errors.username }}</span>
          </div>

          <!-- 비밀번호 입력 -->
          <div class="mb-3">
            <div class="input-wrapper">
              <i class="fa-solid fa-lock input-icon"></i>
              <input
                type="password"
                id="password1"
                v-model.trim="password1"
                placeholder="비밀번호"
                :class="{'custom-input': true, 'error-input': errors.password1}"
              />
            </div>
            <span v-if="errors.password1" class="error">{{ errors.password1 }}</span>
          </div>

          <!-- 비밀번호 확인 -->
          <div class="mb-3">
            <div class="input-wrapper">
              <i class="fa-solid fa-lock input-icon"></i>
              <input
                type="password"
                id="password2"
                v-model.trim="password2"
                placeholder="비밀번호 확인"
                :class="{'custom-input': true, 'error-input': errors.password2}"
              />
            </div>
            <span v-if="errors.password2" class="error">{{ errors.password2 }}</span>
          </div>

          <!-- 이메일 입력 -->
          <div class="mb-3">
            <div class="input-wrapper">
              <i class="fa-solid fa-envelope input-icon"></i>
              <input
                type="email"
                id="email"
                v-model.trim="email"
                placeholder="이메일"
                :class="{'custom-input': true, 'error-input': errors.email}"
              />
            </div>
            <span v-if="errors.email" class="error">{{ errors.email }}</span>
          </div>

          <!-- 닉네임 입력 -->
          <div class="mb-3">
            <div class="input-wrapper">
              <i class="fa-solid fa-user-tag input-icon"></i>
              <input
                type="text"
                id="nickname"
                v-model.trim="nickname"
                placeholder="닉네임"
                :class="{'custom-input': true, 'error-input': errors.nickname}"
              />
            </div>
            <span v-if="errors.nickname" class="error">{{ errors.nickname }}</span>
          </div>

          <!-- 나이 입력 -->
          <div class="mb-3">
            <div class="input-wrapper">
              <i class="fa-solid fa-calendar input-icon"></i>
              <input
                type="text"
                id="age"
                v-model.trim="age"
                placeholder="나이"
                :class="{'custom-input': true, 'error-input': errors.age}"
              />
            </div>
            <span v-if="errors.age" class="error">{{ errors.age }}</span>
          </div>

          <div class="mb-3">
            <div class="gender-group">
              <label class="gender-option">
                <input
                  type="radio"
                  id="gender-male"
                  name="gender"
                  value="남"
                  v-model="gender"
                />
                <span class="gender-text">남성</span>
              </label>
              <label class="gender-option">
                <input
                  type="radio"
                  id="gender-female"
                  name="gender"
                  value="여"
                  v-model="gender"
                />
                <span class="gender-text">여성</span>
              </label>
            </div>
            <span v-if="errors.gender" class="error">{{ errors.gender }}</span>
          </div>
          <!-- 직업 -->
          <div class="mb-3">
            <div class="job">
              <select
              id="job"
              v-model="job"
              class="form-control"
            >
              <option disabled value="">직업 선택</option>
              <option v-for="job in jobs" :key="job">
                {{ job }}
              </option>
              </select>
            </div>
            <span v-if="errors.job" class="error">{{ errors.job }}</span>
          </div>

          <!-- 자산 입력 -->
          <div class="mb-3">
            <div class="input-wrapper">
              <i class="fa-solid fa-wallet input-icon"></i>
              <input
                type="text"
                id="assets"
                v-model.trim="assets"
                placeholder="자산"
                :class="{'custom-input': true, 'error-input': errors.assets}"
              />
            </div>
            <span v-if="errors.assets" class="error">{{ errors.assets }}</span>
          </div>

          <!-- 연봉 입력 -->
          <div class="mb-3">
            <div class="input-wrapper">
              <i class="fa-solid fa-money-bill input-icon"></i>
              <input
                type="text"
                id="salary"
                v-model.trim="salary"
                placeholder="연봉"
                :class="{'custom-input': true, 'error-input': errors.salary}"
              />
            </div>
            <span v-if="errors.salary" class="error">{{ errors.salary }}</span>
          </div>

          <!-- 버튼 -->
          <div class="button-group">
            <button type="submit" class="btn-custom save">
              <i class="fas fa-user-plus me-2"></i>회원가입
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref } from "vue";
import { useMemberStore } from "@/stores/member";

const store = useMemberStore()
const username = ref("")
const password1 = ref("")
const password2 = ref("")
const email = ref("")
const nickname = ref("")
const age = ref("")
const gender = ref("")
const assets = ref("")
const salary = ref("")
const errors = ref({})
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
console.log(job.value)
const signUp = () => {
  errors.value = {}
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    email: email.value,
    nickname: nickname.value,
    age: age.value,
    gender: gender.value,
    assets: assets.value,
    salary: salary.value,
    job: job.value,
  };
  console.log(payload)

  store
    .signUp(payload)
    .then(() => {
      errors.value = {};
    })
    .catch((error) => {
      if (error.response && error.response.data) {
        const serverErrors = error.response.data;
        for (const [field, messages] of Object.entries(serverErrors)) {
          errors.value[field] = messages[0];
        }
      } else {
        alert("예기치 않은 오류가 발생했습니다. 다시 시도해주세요.");
      }
    });
};
</script>

<style scoped>
/* 기존 디자인 구조 스타일 재사용 */
.profile-card {
  max-width: 600px;
  background: white;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.profile-header {
  background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
  color: white;
  padding: 1rem;
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  text-align: center;
}

.profile-body {
  padding: 2rem;
}

.custom-input {
  padding-left: 35px; /* 아이콘 공간 확보 */
  border: 2px solid #e9ecef;
  border-radius: 10px;
  width: 100%;
  height: 40px;
  transition: all 0.3s;
}

.custom-input:focus {
  border-color: #2ecc71 !important;
  outline: none;
}

.error-input {
  border-color: #e74c3c;
}

.error {
  color: #e74c3c;
  font-size: 0.9rem;
  margin-top: 0.5rem;
  display: block;
  box-shadow: none;
}

.button-group {
  display: flex;
  justify-content: center;
  margin-top: 2rem;
}

.btn-custom {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 10px;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  background: #2ecc71;
  color: white;
  transition: all 0.3s;
}

.btn-custom:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(46, 204, 113, 0.2);
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

.input-group {
  position: relative;
  margin-bottom: 1rem;
}

/* 입력 필드와 아이콘 컨테이너 */
.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
  margin-bottom: 0.5rem;
}

/* 아이콘 스타일 */
.input-icon {
  position: absolute;
  left: 10px; /* 아이콘 위치 */
  top: 50%;
  font-size: 16px;
  transform: translateY(-50%);
  color: #999;
  pointer-events: none; /* 클릭 불가능 */
}

</style>
