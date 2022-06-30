<template>
  <div>
    <h1>RecipeDetail</h1>
    <recipe-info />
    <recipe-ingredient />
    <recipe-process />
  </div>
</template>

<script>
import RecipeInfo from '../components/Recipe/RecipeInfo.vue'
import RecipeIngredient from '../components/Recipe/RecipeIngredient.vue'
import RecipeProcess from '../components/Recipe/RecipeProcess.vue'
export default {
  components: { RecipeInfo, RecipeIngredient, RecipeProcess },
  name: 'RecipeDetailView',
}
</script>

<style>

</style>