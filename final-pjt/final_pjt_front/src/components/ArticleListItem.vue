<template>
  <div>
    <RouterLink :to="{name: 'ArticleDetailView', params:{articleId : article.id}}">
    {{ article.id }} | 
    {{ article.title }}
    </RouterLink>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';

defineProps({
  article:Object
})


</script>

<style scoped>

</style>