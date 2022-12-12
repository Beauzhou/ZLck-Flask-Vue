import request from '@/utils/request'

export function getPost (params) {
  return request({
    url: '/post/search',
    method: 'get',
    params
  })
}

export function getCount (params) {
  return request({
    url: '/post/count',
    method: 'get',
    params
  })
}

export function addPost (data) {
  return request({
    url: '/post/add',
    method: 'post',
    data
  })
}

export function deletePost (id) {
  return request({
    url: '/post/delete/' + id,
    method: 'delete',
    id
  })
}
