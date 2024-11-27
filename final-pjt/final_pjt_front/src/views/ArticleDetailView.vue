 <template>
  <div>
    <ArticleDetail :articleId="articleId"/>
  </div>
 </template>
 
 <script setup>
import { useRoute } from 'vue-router';
import ArticleDetail from '@/components/ArticleDetail.vue';
import { ref } from 'vue';

const route = useRoute()
const articleId = ref(route.params.articleId)
 </script>
 
 <style scoped>
 
 </style>