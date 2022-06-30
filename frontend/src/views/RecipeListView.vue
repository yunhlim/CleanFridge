<template>
  <div>
    <h2>추천 레시피</h2>
    <ul>
      <recipe-list-item/>
    </ul>
  </div>
</template>

<script>
import RecipeListItem from '@/components/Recipe/RecipeListItem.vue'

export default {
  components: { RecipeListItem },
  name: "RecipeList"
}
</script>

<style>

</style>