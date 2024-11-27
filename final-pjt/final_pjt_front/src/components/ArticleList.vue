<template>
  <div class="container">
    <!-- 페이지 제목 -->
    <div class="text-center pb-0">
      <div class="title-section text-center">
      <h2 class="main-title animate-typing">DonDon TalkTalk</h2>
      <p class="sub-title animate-fade">금융 꿀팁부터 똑똑한 금융 생활까지, 지금 돈돈하세요!</p>
    </div>
    </div>

    <!-- 글 작성 버튼 -->
    <div class="d-flex justify-content-center mt-4 ">
      <button @click="createArticle" class="btn">
        <i class="fa-solid fa-pencil p-1"></i>
        작성하기</button>
    </div>

    <!-- 테이블 -->
    <div class="table-responsive my-5 mt-1">
      <table class="table table-hover">
        <thead class="table">
          <tr>
            <th scope="col" class="col-1">번호</th>
            <th scope="col" class="col-7 ">제목</th>
            <th scope="col" class="col-2 text-end">작성자</th>
            <th scope="col" class="col-2 text-end">작성일</th>
          </tr>
        </thead>
        <tbody>
          <!-- 게시글 리스트 -->
          <tr
            v-for="article in paginatedArticles"
            :key="article.id"
            class="table-row-hover">

            <td>{{ article.id }}</td>
            <td class="text-start" @click="detailView(article.id)">
                {{ article.title }}
            </td>
            <td class="text-end">{{ article.user_nickname }}</td>
            <td class="text-end">{{ formatDate(article.created_at) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- 페이지네이션 -->
    <nav class="fixed-pagination">
      <ul class="pagination justify-content-center">
        <li class="page-item" :class="{ disabled: currentPage === 1 }">
          <button class="page-link aria-hidden" @click="updatePagination(currentPage - 1)">
            <
          </button>
        </li>
        <li
          class="page-item"
          v-for="page in totalPages"
          :key="page"
          :class="{ active: currentPage === page }"
        >
          <button class="page-link" @click="updatePagination(page)">
            {{ page }}
          </button>
        </li>
        <li class="page-item" :class="{ disabled: currentPage === totalPages }">
          <button class="page-link aria-hidden" @click="updatePagination(currentPage + 1)">
            >
          </button>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from "vue"
import { useArticleStore } from "@/stores/article"
import { useRouter } from "vue-router"
import { format, parseISO } from "date-fns"

const router = useRouter()
const store = useArticleStore()
const currentPage = ref(1)
const itemsPerPage = 10
const items = ref([])

const createArticle = function () {
  router.push({ name: "CreateArticleView" })
}

onMounted(() => {
  store.getArticle()
})


watch(
  () => store.articles,
  (newArticles) => {
    items.value = newArticles
  }
)

const sortedArticles = computed(() => {
  return [...store.articles].sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
})

const paginatedArticles = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage
  return sortedArticles.value.slice(start, end)
})

const totalPages = computed(() => {
  return Math.ceil(sortedArticles.value.length / itemsPerPage)
})

const updatePagination = (page) => {
  currentPage.value = page
}

const detailView = function (articleId) {
  router.push({ name: "ArticleDetailView", params: { articleId: articleId } })
}

const formatDate = (date) => {
  if (!date) return '' // undefined 또는 null 방지
  try {
    return format(parseISO(date), 'yyyy-MM-dd') // ISO 8601 형식 지원
  } catch (error) {
    console.error('Invalid date format:', date, error)
    return '' // 기본값 반환
  }
}
</script>

<style scoped>
.btn {
  padding: 0;
  border: none;
  background: none;
  color: #666;
  transition: all 0.3s ease;
  min-width: 140px;
  position: relative;
  font-weight: 500;
  text-decoration: none;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
}

.btn::after {
  content: '';
  position: absolute;
  width: 0;
  height: 2px;
  bottom: 0;
  left: 50%;
  background-color: #2ecc71;
  transition: all 0.3s ease;
  transform: translateX(-50%);
}

.btn-outline-success {
  color: #2ecc71;
  border-color: #2ecc71;
}

.btn:hover {
  color: #000;
}

.btn.active {
  color: #000;
}

.btn.active::after {
  width: 80%;
}

.btn:hover::after {
  width: 51%;
}
.fas {
  color:black;
  margin-right: 8px;
}

.btn-outline-success:hover,
.btn-outline-success.active {
  background-color: #2ecc71;
  color: white;
  transform: scale(1.05);
}
.container {
  margin-top: 40px;
}
.table-row-hover:hover {
  background-color: #f8f9fa;
  cursor: pointer;
}
.pagination .page-link:focus {
  outline: none; /* 기본 포커스 제거 */
  box-shadow: none; /* 테두리 그림자 제거 */
}
.page-item {
  border-color: white;
}
.page-link {
    position: relative;
    display: inline-block;
    color: black;
    border-radius: 25px;
    text-decoration: none;
    font-size: 1.2rem;
    font-weight: bold;
    padding: 8px 16px 10px;
    margin-left:10px;
    margin-right:10px;
    border-color: white;
}
.page-item.active .page-link {
  z-index: 3;
  background-color: rgba(141, 141, 141, 0.26);
  border-color: none;
}
.page-link.disabled {
  border-color: white;
}
.page-link.aria-hidden {
  border-radius: 25px;
  border-color: white;
}
.disabled {
  background-color: none;
}
.main-title {
  color: #2ecc71;
  font-weight: 600;
  margin-bottom: 15px;
  font-size: 2rem;
  opacity: 0;
  animation: typing 1s ease-in-out forwards;
}

.sub-title {
  color: #666;
  font-size: 1.1rem;
  margin-bottom: 30px;
  opacity: 0;
  animation: fadeIn 1s ease-in-out 1s forwards;
}


@keyframes typing {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

</style>
