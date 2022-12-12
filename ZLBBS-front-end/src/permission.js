import router from './router'
import { getRole } from '@/utils/auth'

router.beforeEach((to, from, next) => {
  let role = getRole()
  if (!role) {
    role = '0'
  }
  console.log(role)
  if (to.meta.roles) {
    console.log(to.meta.roles)
    if (to.meta.roles.includes(role)) {
      next()
    } else {
      next({path: '/403'})
    }
  } else {
    next({path: '/404'})
  }
})
