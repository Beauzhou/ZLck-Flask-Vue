import request from '@/utils/request'

export function getDetail (id) {
  return request({
    url: '/detail/search/' + id,
    method: 'get',
    id
  })
}

export function getComment (params) {
  return request({
    url: '/detail/searchComment',
    method: 'get',
    params
  })
}

export function getCountDay (params) {
  return request({
    url: '/detail/countDay',
    method: 'get',
    params
  })
}

export function addComment (data) {
  return request({
    url: '/detail/addComment',
    method: 'post',
    data
  })
}

export function deleteComment (id) {
  return request({
    url: '/detail/delete/' + id,
    method: 'delete',
    id
  })
}
