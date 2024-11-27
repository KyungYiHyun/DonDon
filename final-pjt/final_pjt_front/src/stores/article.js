import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useMemberStore } from './member'
import { useRouter } from 'vue-router'

export const useArticleStore = defineStore('article', () => {

    const BASE_URL = 'http://127.0.0.1:8000/'
    const articles = ref([])
    const store = useMemberStore()
    const articleDetail = ref([])
    const comment = ref([]) 
    const router = useRouter()
    
    const getArticle = function(){
      axios({
        method: 'get',
        url : BASE_URL + 'article/',
        headers : {Authorization : `Token ${store.token}`}
      })
      .then(res=>{
        console.log(res.data)
        articles.value = res.data
        console.log(articles.value)
      })
    }

    const getArticleDetail = function(id){
      axios({
        method: 'get',
        url : BASE_URL + `article/${id}/`,
        headers : {Authorization : `Token ${store.token}`}
      })
      .then(res=>articleDetail.value = res.data)

    }

    const getComment = async function(id){
      await axios({
        method: 'get',
        url : BASE_URL + `article/${id}/comment/`,
        headers : {Authorization : `Token ${store.token}`}
      })
      .then(res=>comment.value = res.data)
      for (const item of comment.value) {
        item.username = store.currentUsername
      }
    

    }

    const deleteArticle = function(id){
      axios({
        method: 'delete',
        url : BASE_URL + `article/${id}/`,
        headers : {Authorization : `Token ${store.token}`}
      })
      .then(res=>{router.push({ name: 'ArticleView' })})

    }

    const updateArticle = async function(id, user, title, content) {
      try {
        const response = await axios({
          method: 'put',
          url: BASE_URL + `article/${id}/`,
          headers: { Authorization: `Token ${store.token}` },
          data: {
            user,
            title,
            content
          }
        })
        
        console.log(321)
     
      } catch (error) {
        console.error('Error:', error)
      }
    }

  return {getArticle,articles,  getArticleDetail,articleDetail, getComment, comment,deleteArticle,updateArticle}
})
