import request from '@/utils/request'

export function sendEmail (email) {
  return request({
    url: '/email/send/' + email,
    method: 'POST',
    email
  })
}
