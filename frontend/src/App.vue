<template>
  <div id="app">
    <nav class="d-flex justify-content-between align-items-center">
      <div class="d-flex align-items-center">
        <router-link to="/">Intro</router-link>
        <router-link v-if="login" to="/mypage">MyPage</router-link>
        <router-link v-if="login" to="/logout">Logout</router-link>
        <div v-else>
          <router-link to="/signup">SignUp</router-link>
          <router-link to="/login">Login</router-link>
        </div>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>

export default {
  data: function () {
    return {
      login: false,
      user: '',
    }
  },
}

</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR&family=Poppins&display=swap');

#app {
  font-family: "Noto Sans KR", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  position: relative;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
