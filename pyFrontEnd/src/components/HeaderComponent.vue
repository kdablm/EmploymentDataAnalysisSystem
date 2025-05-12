<script setup lang="ts">
</script>
<template>
    <div class="h-15 sticky top-0 z-10 bg-white shadow-sm flex flex-row justify-between items-center px-2">
        <!-- 搜索框 -->
        <div class="flex items-center justify-start w-1/10">
            <input type="text" name="price" id="price" class="input" placeholder="search" />
            <button type="button" class="bg-blue-500 text-sm cursor-pointer hover:bg-blue-600 w-1/6 min-w-15 h-7.5 outline-1 text-white rounded-md px-4 py-1 rounded-l-none">搜索</button>
        </div>
    </div>
</template>
<style scoped>
@import "tailwindcss";

.input {
    @apply block rounded-l-md grow py-1 h-7.5 outline-1 pr-3 pl-1 text-base text-gray-900 min-w-25 placeholder:text-gray-400 focus:outline-blue-200 sm:text-sm/6 outline-blue-100
}
</style>