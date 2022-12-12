import { getToken, setToken, removeToken, getName, setName, removeName, getRole, setRole, removeRole, getUserInfo, setUserInfo, removeUserInfo, getEmail, setEmail, removeEmail } from '@/utils/auth'
import { login } from '@/api/user'
const state = {
  token: getToken(),
  userInfo: getUserInfo(),
  username: getName(),
  role: getRole(),
  email: getEmail()
}

const mutations = {
  SET_TOKEN: (state, token) => {
    state.token = token
  },
  SET_USERINFO: (state, userInfo) => {
    state.userInfo = userInfo
  },
  SET_USERNAME: (state, username) => {
    state.username = username
  },
  SET_ROLE: (state, role) => {
    state.role = role
  },
  SET_EMAIL: (state, email) => {
    state.email = email
  }
}

const actions = {
  // user login
  login ({ commit }, userInfo) {
    const { email, password } = userInfo
    return new Promise((resolve, reject) => {
      login({
        email: email, password: password }).then(res => {
        commit('SET_TOKEN', res.token)
        setToken(res.token)
        commit('SET_ROLE', res.userInfo.is_staff)
        setRole(res.userInfo.is_staff)
        commit('SET_USERINFO', JSON.stringify(res.userInfo))
        setUserInfo(JSON.stringify(res.userInfo))
        commit('SET_USERNAME', res.userInfo.username)
        setName(res.userInfo.username)
        commit('SET_EMAIL', res.userInfo.email)
        setEmail(res.userInfo.email)
        resolve()
      })
    })
  },
  logout ({ commit }) {
    return new Promise(async (resolve) => {
      await commit('SET_TOKEN', '')
      await commit('SET_USERINFO', '')
      await commit('SET_USERNAME', '')
      await commit('SET_ROLE', '')
      await commit('SET_EMAIL', '')
      removeEmail()
      removeRole()
      removeToken()
      removeUserInfo()
      removeName()
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
