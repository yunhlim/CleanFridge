<template>
  <div>
    <h1>MyPage</h1>
    <my-fridge />
  </div>
</template>

<script>
import MyFridge from '../components/Fridge/MyFridge.vue'
export default {
  components: { MyFridge },
  name: 'MyPageView',
}
</script>

<style>

</style>