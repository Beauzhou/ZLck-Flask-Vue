import axios from 'axios'
import router from '@/router'
import { Message } from 'element-ui'
// import { getToken } from '@/utils/auth'

const service = axios.create({
  baseURL: process.env.VUE_APP_BASE_API, // url = base url + request url
  timeout: 5000 // request timeout
})

service.interceptors.request.use(
  config => {
    // if (!getToken()) {
    //   config.headers['Authorization'] = ''
    // } else {
    //   config.headers['Authorization'] = 'bearer ' + getToken()
    // }
    // // }
    // config.headers.put['Content-Type'] = 'application/json'
    return config
  },
  error => {
    // do something with request error
    return Promise.reject(error)
  }
)
// interceptors
service.interceptors.response.use(
  response => {
    if (response.status === 200) {
      return Promise.resolve(response.data)
    } else {
      return Promise.reject(response)
    }
  },
  error => {
    if (error.response.status) {
      switch (error.response.status) {
        case 400:
          Message({
            message: error.response.data.error_description,
            duration: 1000,
            type: 'error'
          })
          break
        case 401:
          console.log(error.response)
          if (error.response.data.error === 'invalid_token') {
            Message({
              message: 'user is not logged in or the login has expired, please log in',
              duration: 1000,
              type: 'error'
            })
            router.replace({
              path: '/login',
              query: {
                redirect: router.currentRoute.fullPath
              }
            })
          } else {
            Message({
              message: error.response.data.error_description,
              duration: 1000,
              type: 'error'
            })
          }
          break
        case 403:
          Message({
            message: 'Access is denied',
            type: 'error',
            duration: 5 * 1000
          })
          break
        case 405:
          Message({
            message: 'Method Not Allowed',
            type: 'error',
            duration: 5 * 1000
          })
          break

        case 500:
          Message({
            message: 'error API',
            type: 'error',
            duration: 5 * 1000
          })
          break

        case 504:
          Message({
            message: 'Server not responding',
            type: 'error',
            duration: 5 * 1000
          })
          break

        case 801:
          Message({
            message: error.response.data.msg,
            duration: 1000,
            type: 'error'
          })
          break

        case 802:
          Message({
            message: error.response.data.msg,
            duration: 1000,
            type: 'error'
          })
          break

        case 803:
          Message({
            message: error.response.data.msg,
            duration: 1000,
            type: 'error'
          })
          break
        default:
          Message({
            message: error.response.data.msg,
            type: 'error',
            duration: 5 * 1000
          })
      }
      return Promise.reject(error.response)
    }
  }
)

export default service
