<template>
  <div id="app">
    <nav-menu v-if="navMenuVisible"/>
    <admin-menu v-if="adminMenuVisible"/>
    <div class="main">
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
    navMenu: () => import('@/menu/index'),
    adminMenu: () => import('@/adminMenu/index')
  },
  computed: {
    navMenuVisible () {
      if (this.$route.name === 'index' || this.$route.name === 'post' || this.$route.name === 'modifyInfo' || this.$route.name === 'detail') {
        return true
      }
    },
    adminMenuVisible () {
      if (this.$route.name === 'CmsIndex' || this.$route.name === 'CmsBanner' || this.$route.name === 'cmsPost' || this.$route.name === 'CmsComment' || this.$route.name === 'CmsUser') {
        return true
      }
    }
  }
}
</script>

<style>
[v-cloak] {
  display: none !important;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.main {
  text-align: center;
  color: #2c3e50;
  margin: 5px 15%;
  overflow: hidden;
}
* {
  margin: 0;
  padding: 0;
  border: 0;
  text-decoration: none;
  vertical-align: baseline;
}
</style>
