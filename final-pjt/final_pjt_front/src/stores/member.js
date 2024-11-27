import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useMemberStore = defineStore('member', () => {
  const BASE_URL = 'http://127.0.0.1:8000'
  const currentUserId = ref(null)
  const currentUsername = ref('')
  const userEmail = ref('')
  const nickname = ref('')
  const userAge = ref('')
  const userAssets = ref('')
  const userSalary = ref('')
  const userGender = ref('')
  const userJob = ref('')
  const token = ref(null)
  const router = useRouter()
  const isLogin = computed(()=>{
    if(token.value === null){
      return false
    } else {
      return true
    }
  })
  const currentPassword = ref('')


  const signUp = function(payload) {
    const { username, password1, password2, email, nickname, age, gender, assets, salary, job } = payload;
    console.log(payload)
    // Promise 반환
    return axios({
      method: 'post',
      url: `${BASE_URL}/accounts/signup/`,
      data: {
        username, password1, password2, email, nickname, age, gender, assets, salary, job,
      },
    })
      .then((res) => {
        // 회원가입 성공 시
        const password = password1;
        logIn({ username, password }); // 로그인을 비동기로 처리
        return res.data; // 성공 결과 반환
      })
      .catch((error) => {
        // 회원가입 실패 시 에러 반환
        throw error; // 에러를 Vue 컴포넌트로 전달
      });
  };

  const logIn = function(payload){
    const username = payload.username
    const password = payload.password

    return axios({
      method:'post',
      url: `${BASE_URL}/accounts/login/`,
      data:{
        username,password
      }
    })
    .then(res => {
      console.log('로그인이 완료되었습니다.')
      console.log(res.data)
      token.value = res.data.key
      router.push({name:'HomeView'})
      return res
    })
    .catch((err) => {
      throw err
    })
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${BASE_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        sessionStorage.clear()
        router.push({ name: 'HomeView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const findCurrentUser = function(){
    axios({
      method: 'get',
      url: `${BASE_URL}/accounts/current-user/`,
      headers : {Authorization : `Token ${token.value}`}
    })
      .then((res) => {
        console.log(res.data.user_id);
        currentUserId.value = res.data.user_id
        currentUsername.value = res.data.username
        userEmail.value = res.data.userEmail
        nickname.value = res.data.nickname
        userAge.value = res.data.userAge
        userAssets.value = res.data.userAssets
        userSalary.value = res.data.userSalary
        userGender.value = res.data.userGender
        userJob.value = res.data.userJob
        currentPassword.value = res.data.password
      })
      .catch((err) => {
        console.log(err)
      })
    }

  const changePassword = function(payload) {
    const new_password1 = payload.new_password1
    const new_password2 = payload.new_password2
    return axios({
      method: 'post',
      url: `${BASE_URL}/accounts/password/change/`,
      headers: {Authorization : `Token ${token.value}`},
      data: { new_password1, new_password2 }
    })
    .then(() => {
      alert("비밀번호가 성공적으로 변경되었습니다.");
      logOut()
    })
    .catch((err) => {
      // 서버로부터 받은 에러 데이터를 반환
      if (err.response && err.response.data) {
        console.error('비밀번호 변경 실패:', err.response.data);
        console.log(Promise.reject(err.response.data))
        return Promise.reject(err.response.data) // 에러 데이터를 반환
      } else {
        console.error('예기치 않은 오류 발생');
        return Promise.reject({ non_field_errors: ['예기치 않은 오류가 발생했습니다.'] }); // 일반 에러 반환
      }
    });
  }

    const signOut = function () {
      axios({
        method: 'delete',
        url: `${BASE_URL}/accounts/delete/`,
        headers: {Authorization : `Token ${token.value}`},
      })
      .then(() => {
        alert('회원 탈퇴가 정상적으로 완료되었습니다.')
        logOut()
        router.push({name:'HomeView'})
      })
      .catch((err)=> {
        console.log(err)
        alert('회원 탈퇴에 실패했습니다.')
      })
    }
    return {signUp, logIn, token,currentUsername, isLogin,
      logOut, findCurrentUser,currentUserId,userEmail,nickname,userAge ,userAssets,userSalary,userGender,userJob, changePassword, signOut}}
      ,{persist:true}
)
