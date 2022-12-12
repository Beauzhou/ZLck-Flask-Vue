import Cookies from 'js-cookie'

export function getToken () {
  return Cookies.get('token')
}

export function setToken (token) {
  return Cookies.set('token', token)
}

export function removeToken () {
  return Cookies.remove('token')
}

export function getName () {
  return Cookies.get('username')
}

export function setName (username) {
  return Cookies.set('username', username)
}

export function removeName () {
  return Cookies.remove('username')
}

export function getRole () {
  return Cookies.get('role')
}

export function setRole (role) {
  return Cookies.set('role', role)
}

export function removeRole () {
  return Cookies.remove('role')
}

export function getUserInfo () {
  return Cookies.get('userInfo')
}

export function setUserInfo (userInfo) {
  return Cookies.set('userInfo', userInfo)
}

export function removeUserInfo () {
  return Cookies.remove('userInfo')
}

export function getEmail () {
  return Cookies.get('email')
}

export function setEmail (email) {
  return Cookies.set('email', email)
}

export function removeEmail () {
  return Cookies.remove('email')
}
