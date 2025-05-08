<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import SliderBarComponent from './components/SliderBarComponent.vue';
</script>

<template>
  <div class=" flex felx-row w-full">
    <SliderBarComponent class="sticky top-0 left-0"/>
    <RouterView class=" bg-amber-400 flex-1"></RouterView>
  </div>
</template>

<style scoped>

</style>
