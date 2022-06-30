import Vue from 'vue'
import Vuex from 'vuex'
import accounts from './modules/accounts'
import recipes from './modules/recipes'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    accounts, recipes
  }
})
