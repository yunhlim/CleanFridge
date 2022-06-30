<template>
    <div>
        <h1>Signup</h1>
        <account-error v-if="authError"/>
        <form @submit.prevent="signup(credentials)">
            <div class="signup-field">
                <input v-model="credentials.username" type="text" id="username" required/>
                <span></span>
                <label for="username">ID</label>
            </div>

            <div class="signup-field">
                <input v-model="credentials.password1" type="password" id="password1" required/>
                <span></span>
                <label for="password1">PW</label>
                
            </div>
            <div class="signup-field">
                <input v-model="credentials.password2" type="password" id="password2" required/>
                <span></span>
                <label for="password2">Confirm PW</label>
            </div>
            <div>
                <p class="pw-note">* 비밀번호는 숫자, 알파벳이 포함된 8자리 이상이어야 합니다.</p>
            </div>
            <input type="submit" value="Sign Up">
        </form>
    </div>
  
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import AccountError from '../components/AccountError.vue'

export default {
  name: 'SignupView',
  components: {
      AccountError,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
    },
}
</script>

<style>

</style>