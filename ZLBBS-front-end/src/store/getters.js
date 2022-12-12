const getters = {
  token: state => state.user.token,
  userInfo: state => {
    const userInfo = state.user.userInfo
    return JSON.parse(userInfo)
  },
  username: state => state.user.username,
  role: state => state.user.role,
  email: state => state.user.email
}

export default getters
