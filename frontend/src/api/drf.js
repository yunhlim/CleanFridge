const HOST = 'http://localhost:8000/'

const ACCOUNTS = 'accounts/'
const RECIPES = 'recipes/'

export default {
    accounts: {
        login: () => HOST + ACCOUNTS + 'login/',
        logout: () => HOST + ACCOUNTS + 'logout/',
        signup: () => HOST + ACCOUNTS + 'signup/',
        // Token 으로 현재 user 판단
        currentUserInfo: () => HOST + ACCOUNTS + 'user/',
        // username으로 프로필 제공
        profile: username => HOST + ACCOUNTS + 'profile/' + username,
        ingredients: () => HOST + ACCOUNTS + 'ingredients/',
    },
    recipes: {
        recipes: (page, query, isRecommend, type) => HOST + RECIPES + `${isRecommend}/` + `${type}/` + `?page=${page}` + `?q=${query}`,
        recipe: recipePk => HOST + RECIPES + `${recipePk}/`,
    }
}