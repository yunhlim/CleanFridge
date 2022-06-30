import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'


export default {
  state: {
    token: localStorage.getItem('token') || '' ,
    currentUser: {},
    profile: {},
    authError: null,
  },
  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    profile: state => state.profile,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Token ${state.token}`})
  },

  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_PROFILE: (state, profile) => state.profile = profile,
    SET_AUTH_ERROR: (state, error) => state.authError = error,
  },

  actions: {
    saveToken({ commit }, token) {
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
    },

    removeToken({ commit }) {
      commit('SET_TOKEN', '')
      commit('SET_CURRENT_USER','')
      localStorage.setItem('token', '')
    },

    login({ commit, dispatch }, credentials) {
      axios({
        url: drf.accounts.login(),
        method: 'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          commit('SET_AUTH_ERROR', null)
          router.push({ name: 'home' })
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },

    signup({ commit, dispatch }, credentials) {
      axios({
        url: drf.accounts.signup(),
        method: 'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'home' })
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },

    logout({ getters, dispatch,commit }) {
      axios({
        url: drf.accounts.logout(),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(() => {
          dispatch('removeToken')
          commit('SET_PROFILE',{})
          router.push({ name: 'home' })

        })
        .error(err => {
          console.error(err.response)
        })
    },

    fetchCurrentUser({ commit, getters, dispatch }) {
      if (getters.isLoggedIn) {
        axios({
          url: drf.accounts.currentUserInfo(),
          method: 'get',
          headers: getters.authHeader,
        })
          .then(res => {  
            dispatch('fetchProfile',res.data.username)
            commit('SET_CURRENT_USER', res.data)
          })
          .catch(err => {
            if (err.response.status === 401) {
              dispatch('removeToken')
              router.push({ name: 'home' })
            }
          })
      }
    },
    fetchProfile({ commit, getters }, username) {
      axios({
        url: drf.accounts.profile(username),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          console.log(res.data)
          commit('SET_PROFILE', res.data)
        })
        .catch(err => {
          console.error(err.response.data)
        })
    },
    cleanError({ commit }) {
      commit('SET_AUTH_ERROR', null)
    },
    saveProfile({ commit,getters }, profile) {
      axios({
        url: drf.accounts.saveprofile(profile.username),
        method: 'post',
        data:profile,
        headers: getters.authHeader,
      })
        .then(res => {
          console.log(res.data)
          commit('SET_PROFILE', res.data)
          router.go()
        })
        .catch(err => {
          alert(err)
        })
    },

  },
  
}