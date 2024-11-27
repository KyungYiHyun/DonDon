<template>
  <div class="container">
    <!-- 게시글 상세 -->
    <div class="card mb-4">
      <div class="card-body">
        <h3 class="card-title">{{ store.articleDetail.title }}</h3>
        <p class="text-muted">
          작성자: {{ store.articleDetail.user_nickname }} | 
          {{ formatDate(store.articleDetail.created_at) }}
        </p>
        <div class="cart-text-container">
        <p class="card-text">{{ store.articleDetail.content }}</p>
      </div>
        <div class="d-flex justify-content-end">
          <button
            v-if="store.articleDetail.user == memberStore.currentUserId"
            class="btn btn-outline-primary me-2"
            @click="startEdit">
            <i class="fa-regular fa-pen-to-square"></i>
            수정
          </button>
          <button
            v-if="store.articleDetail.user == memberStore.currentUserId"
            class="btn btn-outline-danger"
            @click="store.deleteArticle(store.articleDetail.id)">
            <i class="fa-solid fa-trash-can"></i>
            삭제
          </button>
        </div>
      </div>
    </div>

    <!-- 게시글 수정 -->
    <div v-if="isEditing" class="card mb-4">
      <div class="card-body">
        <h5>게시글 수정</h5>
        <div class="mb-3">
          <label for="editTitle" class="form-label">제목</label>
          <input
            type="text"
            id="editTitle"
            v-model="editedTitle"
            class="form-control"
            :placeholder="store.articleDetail.title"/>
        </div>
        <div class="mb-3">
          <label for="editContent" class="form-label">내용</label>
          <textarea
            id="editContent"
            v-model="editedContent"
            class="form-control"
            :placeholder="store.articleDetail.content"
            rows="4">
          </textarea>
        </div>
        <div class="d-flex justify-content-end btn-wrap" >
          <button class="btn btn-outline-primary me-2" @click="updateAndRedirect">
            <i class="fa-regular fa-pen-to-square"></i>
            수정 완료
          </button>
          <button class="btn btn-outline-danger" @click="cancelEdit">
            <i class="fa-solid fa-xmark"></i>
            취소
          </button>
        </div>
      </div>
    </div>


    <div v-if="!isCommentEditing && !isEditing" class="card">
      <div class="card-body">
        <h5>댓글 쓰기</h5>
        <form @submit.prevent="createComment" class="comment-form">
          <textarea
            v-model="content"
            class="form-control mb-2"
            placeholder="댓글을 입력하세요."
            rows="3"
            required
          ></textarea>
          <button type="submit" class="btn btn-primary mt-0">
            <i class="fa-regular fa-comment p-1"></i>
            등록
          </button>
        </form>
      </div>
    </div>
    <!-- 댓글 목록 -->
    <div v-if="!isEditing && !isCommentEditing">
      <h5>댓글 {{ store.comment.length }}개</h5>
      <ul class="list-group mb-4">
        <li
          v-for="comment in store.comment"
          :key="comment.id"
          class="list-group-item d-flex justify-content-between align-items-center"
        >
          <div>
            <p class="mb-1"><strong>{{ comment.user_nickname }}</strong></p>
            <p class="mb-1">{{ comment.content }}</p>
            <small class="text-muted">{{ formatDate(comment.updated_at) }}</small>
          </div>
          <div v-if="comment.user == memberStore.currentUserId">
            <div>
              <button
                class="btn btn-outline-primary btn-sm me-2"
                @click="startCommentEdit(comment)">
                <i class="fa-regular fa-pen-to-square"></i>
                수정
              </button>
              <button
                class="btn btn-outline-danger btn-sm"
                @click="deleteComment(comment.id)">
                <i class="fa-solid fa-trash-can"></i>
                삭제
              </button>
            </div>
          </div>
        </li>
      </ul>
    </div>

    <!-- 댓글 수정 -->
    <div v-if="isCommentEditing" class="card mb-4">
      <div class="card-body">
        <h5>댓글 수정</h5>
        <div class="mb-3">
          <textarea
            id="editContent"
            v-model="editedCommentContent"
            class="form-control"
            :placeholder="editedCommentContent"
            rows="4">
          </textarea>
        </div>
        <div class="d-flex justify-content-end">
          <button
            class="btn btn-outline-primary me-2"
            @click="updateComment(editingCommentId)">
            <i class="fa-regular fa-pen-to-square"></i>
            수정완료
          </button>
          <button
            class="btn btn-outline-danger"
            @click="cancelCommentEdit">
            <i class="fa-solid fa-xmark"></i>
            취소
          </button>
        </div>
      </div>
    </div>

    <!-- 댓글 작성 -->
 
  </div>
</template>

<script setup>
import { useArticleStore } from "@/stores/article"
import { useMemberStore } from "@/stores/member"
import { ref, onMounted } from "vue"
import { useRoute, useRouter } from "vue-router"
import { format, parseISO } from "date-fns"
import axios from "axios"


const route = useRoute()
const router = useRouter()
const store = useArticleStore()
const memberStore = useMemberStore()

const content = ref("")
const editingCommentId = ref(null)
const editedCommentContent = ref("")
const isEditing = ref(false)
const isCommentEditing = ref(false)
const editedTitle = ref("")
const editedContent = ref("")
const BASE_URL = "http://127.0.0.1:8000/"

onMounted(() => {
  store.getArticleDetail(route.params.articleId)
  store.getComment(route.params.articleId)
  memberStore.findCurrentUser()
})

const createComment = async () => {
  try {
    await axios.post(
      `${BASE_URL}article/${route.params.articleId}/comment/`,
      {
        user: memberStore.currentUserId,
        article: route.params.articleId,
        content: content.value,
      },
      {
        headers: { Authorization: `Token ${memberStore.token}` },
      }
    )
    content.value = ""
    store.getComment(route.params.articleId)
  } catch (error) {
    console.error(error)
  }
}

const deleteComment = async (id) => {
  try {
    await axios.delete(`${BASE_URL}article/comment/${id}/`, {
      headers: { Authorization: `Token ${memberStore.token}` },
    })
    store.getComment(route.params.articleId)
  } catch (error) {
    console.error(error)
  }
}

const startCommentEdit = (comment) => {
  isCommentEditing.value = true
  editingCommentId.value = comment.id
  editedCommentContent.value = comment.content
}

const cancelCommentEdit = () => {
  isCommentEditing.value = false
  editingCommentId.value = null
  editedCommentContent.value = ''
}

const updateComment = async (commentId) => {
  try {
    await axios.put(
      `${BASE_URL}article/comment/${commentId}/`,
      {
        content: editedCommentContent.value,
        user: memberStore.currentUserId,
        article: route.params.articleId,
      },
      {
        headers: { Authorization: `Token ${memberStore.token}` },
      }
    )
    isCommentEditing.value = false
    editingCommentId.value = null
    editedCommentContent.value = ""
    store.getComment(route.params.articleId)
  } catch (error) {
    console.error("댓글 수정 실패:", error)
  }
}

const updateAndRedirect = async () => {
  try {
    await store.updateArticle(
      route.params.articleId,
      memberStore.currentUserId,
      editedTitle.value,
      editedContent.value
    )
    isEditing.value = false
    await store.getArticleDetail(route.params.articleId)
    router.push({
      name: "ArticleDetailView",
      params: { articleId: route.params.articleId },
    })
  } catch (error) {
    console.error("Update failed:", error)
  }
}

const startEdit = () => {
  isEditing.value = true
  editedTitle.value = store.articleDetail.title
  editedContent.value = store.articleDetail.content
}

const cancelEdit = () => {
  isEditing.value = false
  editedTitle.value = ""
  editedContent.value = ""
}

// 날짜 변환 함수
const formatDate = (date) => {
  if (!date) return '' // undefined 또는 null 방지
  try {
    return format(parseISO(date), 'yyyy-MM-dd HH:mm') // ISO 8601 형식 지원
  } catch (error) {
    console.error('Invalid date format:', date, error)
    return '' // 기본값 반환
  }
}
</script>

<style scoped>
.btn-primary {
  background: #3498db;
  border-color: #3498db;
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
.btn-outline-primary {
  border-color: #3498db;
  color: #3498db
}
.btn-outline-danger {
  border-color: #e74c3c;
  color: #e74c3c;
}

.comment-form {
  display: flex; /* 댓글 입력과 버튼을 가로로 정렬 */
  flex-direction: column; /* 기본 정렬은 세로 */
}

.comment-form button {
  align-self: flex-end; /* 작성 버튼을 오른쪽 끝으로 정렬 */
  margin-top: 8px; /* 위아래 간격 추가 */
  font-size: 14px; /* 버튼 글자 크기 */
  padding: 6px 12px; /* 버튼 크기 조정 */
}

.container {
  margin-top: 40px;
}
.card {
  border: none;
}
.card-body {
  padding: 0;
}
textarea {
  resize: none;
  min-height: 100px;
  padding: 8px;
  font-size: 14px;
}


.cart-text-container{
  border-bottom: 1px solid #e3e7eb;
  border-top: 1px solid #e3e7eb;
  padding-bottom: 30px;
  padding-top: 30px;
  margin-bottom: 30px;
}

</style>
