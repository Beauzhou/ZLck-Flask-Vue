import request from '@/utils/request'

export function download (filename) {
  return request({
    url: '/file/download/' + filename,
    method: 'get',
    responseType: 'blob'
  })
}
