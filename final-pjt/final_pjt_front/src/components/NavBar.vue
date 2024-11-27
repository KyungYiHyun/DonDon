<template>
  <nav class="navbar navbar-expand-lg sticky-top bg-white p-0">
    <div class="container-fluid">
      <RouterLink class="navbar-brand" :to="{ name: 'HomeView' }" style="font-family: sans-serif; ">
        <div class="logo">
        <span class="logo-top">Don</span>
        <span class="logo-bottom">Don</span>
    </div>


      </RouterLink>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse nav-font" id="navbarNav">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name: 'DepositView' }">예금/적금 비교하기</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name: 'RecommendDepositView' }">예금/적금 추천받기</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name: 'ArticleView' }">게시판</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name: 'MapView' }">은행검색</RouterLink>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#exchangeModal">환율계산기</a>
          </li>
        </ul>
        <ul class="navbar-nav">
          <template v-if="!store.isLogin">
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'LoginView' }">로그인</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'SignUpView' }">회원가입</RouterLink>
            </li>
          </template>
          <template v-else>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'ProfileView' }">프로필</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink  class="nav-link logout-link" c :to="{ name: 'HomeView' }" @click="logOut">로그아웃</RouterLink>
            </li>
          </template>
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name: 'CartView' }">예금/적금 장바구니</RouterLink>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { computed } from 'vue';
import { useMemberStore } from '@/stores/member';
import { RouterLink } from 'vue-router';

const store = useMemberStore()
const logOut = () => {
  store.logOut()
}

</script>

<style scoped>

 
.logout-link.router-link-active::after {
  width: 0 !important;  /* active 상태에서 밑줄 제거 */
}

.logout-link:hover::after {
  width: 30% !important; /* hover 시에는 밑줄 표시 */
}
.nav-link {
  padding: 8px 25px !important;  /* 상하 패딩 줄임 */
  position: relative;
}

.nav-link::after {
  content: '';
  position: absolute;
  width: 0;
  height: 2px;
  bottom: 5px;  /* 밑줄 위치 조정 */
  left: 50%;
  background-color: #2ecc71;
  transition: all 0.3s ease;
  transform: translateX(-50%);
}


.nav-link.router-link-active {
  color: #000;
}

.nav-link.router-link-active::after {
  width: 70%;  /* 밑줄 길이 조정 */
}

.nav-link:hover::after {
  width: 30%;
}

.nav-link:hover {
  color: #000;
}
.nav-font{
  font-weight: bold;
}

.navbar-expand {
  padding: 0;
}

.navbar-brand{
  color:#2ecc71;
}

.logo {
  font-family: 'Pretendard', sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-weight: bold;
  font-size: 1.2rem;
  
}

.logo-top {
  color: #2ecc71;
  margin-left: 0px; /* 첫 번째 Don을 약간 왼쪽으로 */
  font-weight: bold;
}

.logo-bottom {
  margin-right: -33px; /* 두 번째 Don을 약간 오른쪽으로 */
  transform: translateY(-5px);
  font-weight: bold;
  color: #27ae60;
}
</style>