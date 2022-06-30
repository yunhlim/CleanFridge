<template>
    <div>
        <h1>Login</h1>
        <account-error v-if="authError"></account-error>

        <form @submit.prevent="login(credentials)">
            <div class="txt-field">
                <input v-model="credentials.username" type="text" id="username" required>
                <span></span>
                <label for="username">ID</label>
            </div>

            <div class="txt-field">
                <input v-model="credentials.password" @keyup.enter="sumbit" type="password" id="password" required>
                <span></span>
                <label for="password">PW</label>
            </div>
            <input type="submit" value="Login">
      </form>
    </div>
</template>

<script>
import { mapActions,mapGetters } from 'vuex'
import AccountError from '../components/AccountError.vue'

export default {
    name: 'LoginView',
    components: {
        AccountError,
    },
    data() {
        return {
            credentials: {
            username: '',
            password: '',
            }
        }    
    },
    methods: {
      ...mapActions(['login','cleanError'])
    },
    computed: {
      ...mapGetters(['authError'])
    },
    created () {
      this.cleanError()
    }
}
</script>

<style>

</style>