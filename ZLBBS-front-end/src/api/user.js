import request from '@/utils/request'

export function login (data) {
  return request({
    url: '/user/login',
    method: 'post',
    data
  })
}

export function register (data) {
  return request({
    url: '/user/register',
    method: 'post',
    data
  })
}

export function getUser (params) {
  return request({
    url: '/user/search',
    method: 'get',
    params
  })
}

export function getUserById (id) {
  return request({
    url: '/user/search/' + id,
    method: 'get',
    id
  })
}

export function updateUser (data) {
  return request({
    url: '/user/update',
    method: 'PUT',
    data
  })
}

export function deleteUser (id) {
  return request({
    url: '/user/delete/' + id,
    method: 'delete',
    id
  })
}
