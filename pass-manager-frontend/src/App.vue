<template>
  <div>
    <el-header></el-header>
    <el-main>
      <el-row :gutter="20">
        <el-col :span="2">
          <div class="grid-content bg-purple">
        </div>
        </el-col>
        <el-col :span="2">
          <div class="grid-content bg-purple">
            <NavBar></NavBar>
          </div>
        </el-col>
        <el-col :span="15">
          <div class="grid-content bg-purple">
            <router-view></router-view>
          </div>
        </el-col>
        <el-col :span="1"><div class="grid-content bg-purple"></div></el-col>
      </el-row>
    </el-main>
    <el-footer></el-footer>
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    NavBar
  }
}
</script>


<style>

.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

</style>
