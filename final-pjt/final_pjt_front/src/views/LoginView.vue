<!-- <template>
  <div class="container py-5">
    <h1>로그인</h1>
    <form @submit.prevent="logIn">
      <label for="username" class="form-label">아이디</label>
      <input type="text" id="username" v-model.trim="username" class="form-control">
      <br/>

      <label for="password" class="from-label">비밀번호</label>
      <input type="password" id="password" v-model.trim="password" class="form-control">
      
      <input type="submit" value="logIn">
    </form>
  </div>
</template>

<script setup>
import { useMemberStore } from '@/stores/member';
import { ref } from 'vue';

const store = useMemberStore()

const logIn = function(){
  const payload = {
    username : username.value,
    password : password.value
  }
  store.logIn(payload)
}

const username = ref(null)
const password = ref(null)

</script>

<style lang="scss" scoped>

</style> -->

<template>
  <div class="container py-5">
    <div class="profile-card mx-auto">
      <!-- 헤더 -->
      <div class="profile-header">
        <h2>로그인</h2>
        <p class="mb-0">아이디와 비밀번호를 입력해주세요.</p>
      </div>

      <!-- 로그인 폼 -->
      <div class="profile-body">
        <form @submit.prevent="logIn" class="edit-form">
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
                @input="clearError('username')"
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
                id="password"
                v-model.trim="password"
                placeholder="비밀번호"
                :class="{'custom-input': true, 'error-input': errors.password}"
                @input="clearError('password')"
              />
            </div>
            <span v-if="errors.password" class="error">{{ errors.password }}</span>
          </div>
          <span v-if="errors.non_field_errors" class="error">{{errors.non_field_errors}}</span>
          <!-- 버튼 -->
          <div class="button-group">
            <button type="submit" class="btn-custom save">
              <i class="fas fa-sign-in-alt me-2"></i>로그인
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

const store = useMemberStore();

const username = ref("");
const password = ref("");
const errors = ref({});

const logIn = () => {
  const payload = {
    username: username.value,
    password: password.value,
  };

  store
    .logIn(payload)
    .then(() => {
      console.log("로그인이 성공했습니다.");
      errors.value = {}; // 모든 에러 메시지 초기화
    })
    .catch((error) => {
      if (error.response && error.response.data) {
        const serverErrors = error.response.data;
        console.log(serverErrors)
        for (const [field, messages] of Object.entries(serverErrors)) {
          errors.value[field] = messages[0];
        }
      } else {
        console.error("로그인 중 오류가 발생했습니다.");
      }
    });
};

// 특정 필드의 에러를 제거
const clearError = (field) => {
  if (errors.value[field]) {
    delete errors.value[field];
  }
};
</script>

<style scoped>
/* 기존 스타일 재사용 */
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
  display: flex;
  justify-content: center;
}

.custom-input {
  padding-left: 35px; /* 아이콘 공간 확보 */
  border: 2px solid #e9ecef;
  border-radius: 10px;
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

.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
  margin-bottom: 0.5rem;
}

.input-icon {
  position: absolute;
  left: 10px;
  top: 50%;
  font-size: 16px;
  transform: translateY(-50%);
  color: #999;
  pointer-events: none;
}
</style>
