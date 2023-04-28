<template>
  <el-row class="tac">
    <h5></h5>
    <el-menu
      router
      class="el-menu-vertical-demo"
      @open="handleOpen"
      @close="handleClose">
      <el-menu-item index="/">
        <i class="el-icon-menu"></i>
        <span slot="title">Main</span>
      </el-menu-item>
      <el-menu-item index="/email">
        <i class="el-icon-document"></i>
        <span slot="title">邮箱</span>
      </el-menu-item>
      <el-menu-item index="/phone">
        <i class="el-icon-setting"></i>
        <span slot="title">手机号</span>
      </el-menu-item>
    </el-menu>
  </el-row>
</template>

<script>
export default {
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
  },
  data() {
    return {

    };
  },
}
</script>

<style>
</style>
