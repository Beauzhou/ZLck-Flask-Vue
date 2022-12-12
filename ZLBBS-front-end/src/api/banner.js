import request from '@/utils/request'

export function getBanner (params) {
  return request({
    url: '/banner/search',
    method: 'get',
    params
  })
}

export function addBanner (data) {
  return request({
    url: '/banner/add',
    method: 'POST',
    data
  })
}

export function deleteBanner (id) {
  return request({
    url: '/banner/delete/' + id,
    method: 'delete',
    id
  })
}
