<!-- <template>
  <div class="container py-5">
    <div class="form-card mx-auto">
      
      <div class="form-header">
        <h2>글 작성하기</h2>
        <p class="mb-0">제목과 내용을 입력한 후 글쓰기를 눌러주세요.</p>
      </div>

      
      <div class="form-body">
        <form @submit.prevent="submitArticle" class="edit-form">
          
          <div class="mb-3">
            <div class="input-wrapper">
              <i class="fa-solid fa-heading input-icon"></i>
              <input
                type="text"
                v-model="title"
                placeholder="게시글의 제목을 입력해주세요."
                class="custom-input"
                required
              />
            </div>
          </div>

          
          <div class="mb-3">
            <div class="input-wrapper textarea-wrapper">
              <i class="fa-solid fa-align-left input-icon"></i>
              <textarea
                v-model="content"
                placeholder="작성하실 내용을 입력해주세요."
                class="custom-textarea"
                required
              ></textarea>
            </div>
          </div>

          
          <div class="button-group">
            <button type="submit" class="btn-custom save">
              <i class="fa-solid fa-paper-plane me-2"></i>글쓰기
            </button>
            <button type="submit" class="btn-custom cancel">
              <i class="fa-solid fa-xmark"></i>취소
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template> -->
<template>
  <div class="container py-5">
    <div class="form-card mx-auto">
      <!-- 헤더 -->
      <div class="form-header">
        <h2>글 작성하기</h2>
        <p class="mb-0">제목과 내용을 입력한 후 글쓰기를 눌러주세요.</p>
      </div>

      <!-- 글 작성 폼 -->
      <div class="form-body">
        <form @submit.prevent="submitArticle" class="edit-form">
          <!-- 제목 -->
          <div class="mb-3">
            <div class="input-wrapper">
              <i class="fa-solid fa-heading input-icon"></i>
              <input
                type="text"
                v-model="title"
                placeholder="게시글의 제목을 입력해주세요."
                class="custom-input"
                required
              />
            </div>
          </div>

          <!-- 내용 -->
          <div class="mb-3">
            <div class="input-wrapper textarea-wrapper">
              <i class="fa-solid fa-align-left input-icon"></i>
              <textarea
                v-model="content"
                placeholder="작성하실 내용을 입력해주세요."
                class="custom-textarea"
                required
              ></textarea>
            </div>
          </div>

          <!-- 버튼 -->
          <div class="button-group">
            <button type="submit" class="btn-custom save">
              <i class="fa-solid fa-paper-plane me-2"></i>글쓰기
            </button>
            <button type="button" class="btn-custom cancel" @click="cancelArticle">
              <i class="fa-solid fa-xmark me-2 "></i>취소
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
  import router from '@/router';
  import { useMemberStore } from '@/stores/member';
  import axios from 'axios';
  import { ref , onMounted} from 'vue';
  onMounted(()=>{
  store.findCurrentUser()
})
  
  const store = useMemberStore()
  const BASE_URL = 'http://127.0.0.1:8000/'
  const title = ref('')
  const content = ref('')

  const submitArticle = function() {
    axios({
      method: 'post',
      url: BASE_URL + 'article/',
      headers: {
        Authorization: `Token ${store.token}`
      },
      data: {
        user:store.currentUserId,
        title: title.value,
        content: content.value
      }
    })
    .then((res) => {
      console.log("글 생성 완료")
      // 글 작성 후 목록 페이지로 이동
      router.push({ name: 'ArticleView' })
    })
    .catch((err) => {
      console.log(err)
    })
  }
</script>

<style scoped>
/* 카드 스타일 */
.form-card {
  max-width: 800px;
  background: white;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  margin: 0 auto;
}

/* 헤더 스타일 */
.form-header {
  /* background: linear-gradient(135deg, #3498db 0%, #2980b9 100%); */
  background-color: #2ecc71;
  color: white;
  padding: 1rem;
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  text-align: center;
}

/* 폼 바디 스타일 */
.form-body {
  padding: 2rem;
}
.container {
  margin-top: 40px;
}
/* 입력 필드 스타일 */
.custom-input {
  width: 100%;
  padding-left: 40px; /* 아이콘 공간 */
  border: 2px solid #e9ecef;
  border-radius: 10px;
  height: 40px;
  transition: all 0.3s;
  font-size: 1rem;
}
.custom-input:focus {
  border-color: #3498db !important;
  outline: none;
}

/* 버튼 스타일 */
.button-group {
  display: flex;
  justify-content: center;
  margin-top: 1rem;
  gap: 1rem;
}
/* .btn-custom {
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
.btn-custom.save {
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
.btn-custom:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(52, 152, 219, 0.2);
}
.btn-custom.cancel {
  background: #e74c3c;
  color: white;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.75rem 1.5rem;
  border-radius: 10px;
  font-weight: 600;
  transition: all 0.3s;
} */
 /* 버튼 스타일 */
.button-group {
  display: flex;
  justify-content: center;
  margin-top: 1rem;
  gap: 1rem;
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

.btn-custom.save {
  background: #3498db;
  color: white;
}

.btn-custom.cancel {
  background: #e74c3c;
  color: white;
}

.btn-custom:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.btn-custom.save:hover {
  box-shadow: 0 5px 15px rgba(52, 152, 219, 0.2);
}

.btn-custom.cancel:hover {
  box-shadow: 0 5px 15px rgba(231, 76, 60, 0.2);
}
/* 아이콘 스타일 */
.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
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
/* 텍스트 영역 스타일 */
.custom-textarea {
  width: 100%;
  padding: 10px 40px; /* 아이콘 공간 */
  border: 2px solid #e9ecef;
  border-radius: 10px;
  height: 200px; /* 기본 높이 */
  font-size: 1rem;
  resize: vertical; /* 세로 크기 조정만 가능 */
  transition: all 0.3s;
}
.custom-textarea:focus {
  border-color: #3498db !important;
  outline: none;
}

/* 텍스트 영역 아이콘 */
.textarea-wrapper {
  position: relative;
}
</style>
