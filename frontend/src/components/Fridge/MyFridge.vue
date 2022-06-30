<template>
  <div>
    <ingredient-item />
    <ingredient-form />
  </div>
</template>

<script>
import IngredientForm from './IngredientForm.vue'
import IngredientItem from './IngredientItem.vue'

export default {
  components: { IngredientItem, IngredientForm },
    name: 'MyFridge',
}
</script>

<style>

</style>