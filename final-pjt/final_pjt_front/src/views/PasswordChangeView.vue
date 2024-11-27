<template>
  <div class="container py-5">
    <div class="profile-card mx-auto">
      <!-- 헤더 -->
      <div class="profile-header">
        <h2>비밀번호 변경</h2>
        <p class="mb-0">변경할 비밀번호와 확인 비밀번호를 입력해주세요.</p>
      </div>

      <!-- 비밀번호 변경 폼 -->
      <div class="profile-body">
        <form @submit.prevent="changePassword" class="edit-form">
          <!-- 새 비밀번호 입력 -->
          <div class="mb-3">
            <div class="input-wrapper">
              <i class="fa-solid fa-lock input-icon"></i>
              <input
                type="password"
                id="new_password1"
                v-model.trim="new_password1"
                placeholder="새 비밀번호"
                :class="{'custom-input': true, 'error-input': errors.new_password1}"
                @input="clearError('new_password1')"
              />
            </div>
            <span v-if="errors.new_password1" class="error">{{ errors.new_password1[0] }}</span>
          </div>

          <!-- 새 비밀번호 확인 -->
          <div class="mb-3">
            <div class="input-wrapper">
              <i class="fa-solid fa-lock input-icon"></i>
              <input
                type="password"
                id="new_password2"
                v-model.trim="new_password2"
                placeholder="새 비밀번호 확인"
                :class="{'custom-input': true, 'error-input': errors.new_password2}"
                @input="clearError('new_password2')"
              />
            </div>
            <span v-if="errors.new_password2" class="error">{{ errors.new_password2[0] }}</span>
          </div>

          <!-- 버튼 -->
          <div class="button-group">
            <button type="submit" class="btn-custom save">
              <i class="fas fa-key me-2"></i>비밀번호 변경
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
const new_password1 = ref("");
const new_password2 = ref("");
const errors = ref({})


const changePassword = function () {
  const payload = {
    new_password1: new_password1.value,
    new_password2: new_password2.value,
  }
  store.changePassword(payload)
    .then(() => {
      new_password1.value = ""
      new_password2.value = ""
      errors.value = {}
    })
    .catch((err) => {
      errors.value = err
      console.log(err);
    });
}

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
  height: 1.2rem; /* 일정 높이 유지 */
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

.mb-3 {
  display: flex;
  flex-direction: column; /* 수직 정렬 */
  align-items: center; /* 중앙 정렬 유지 */
  position: relative;
}


</style>
