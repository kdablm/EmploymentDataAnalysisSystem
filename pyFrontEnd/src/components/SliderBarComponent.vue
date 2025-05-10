<script setup lang="ts">
import { color, Motion, motion } from 'motion-v'
import { useAnimationControls } from 'motion-v'
import { DoubleLeft, DoubleRight, HomeTwo, PeoplesTwo, CollectionFiles, History, Right } from '@icon-park/vue-next'
import { onMounted, ref } from 'vue'
// 定义开启与关闭动画
const container = {
    close: {
        width: '5rem'
    },
    open: {
        width: '14rem'
    }
}

// 定义动画控制器
const animateController = useAnimationControls()
// 定义点击事件
let open = ref(true)//展开标记
function handleChangeAnimate() {
    if (!open.value)
        animateController.start(container.open)
    else animateController.start(container.close)
    open.value = !open.value
}
// 个人中心下拉框 
const userInfoContainer = {
    close: {
        rotate: 0
    },
    open: {
        rotate: 90
    }
}
const userInfoItemContainer = {
    close: {
        display: 'none',
        height: '0px'
    },
    open: {
        display: 'block',
    }
}
// 定义用户下拉框动画控制器
const userInfoContainerController = useAnimationControls()
const userInfoItemContainerController = useAnimationControls()
let userInfoOpen = ref(false)//标志
function handleChangeUserInfoAnimationState() {
    if (!userInfoOpen.value) {
        // 改变箭头状态
        userInfoContainerController.start(userInfoContainer.open)
        // 展开下拉框
        userInfoItemContainerController.start(userInfoItemContainer.open)
    } else {
        // 改变箭头状态
        userInfoContainerController.start(userInfoContainer.close)
        // 展开下拉框
        userInfoItemContainerController.start(userInfoItemContainer.close)
    }
    userInfoOpen.value = !userInfoOpen.value
}
</script>

<template>
    <motion.div class="px-5 py-3 bg-blue-50 text-gray-500 h-[100vh] aspect-square" :animate="animateController"
        :variants="container" :initial="{
            width: '14rem'
        }" :transition="{
            duration: 0.5,
            ease: 'easeInOut',
            times: [0, 0.2, 0.5, 0.8, 1],
            type: 'spring',
            repeatDelay: 1,
        }">
        <!-- logo -->
        <div :class="{ 'justify-between': open, 'justify-center ': !open }" class="flex flex-row  items-center">
            <h1 class="flex cursor-pointer flex-row items-center text-xl font-bold">
                <img src="@/assets/logo-sm.svg" class="size-10" alt="">
                <span v-if="open" class=" font-bold">菜单</span>
            </h1>
            <i @click="handleChangeAnimate" class="  flex cursor-pointer hover:text-purple-400 items-center">
                <DoubleLeft v-if="open" theme="outline" size="24" />
            </i>
        </div>
        <!-- 菜单列表 -->
        <div class="px-1 text-md">
            <!-- 首页 -->
            <h2 :class="{ 'justify-center': !open }"
                class="flex my-5 h-5 hover:text-purple-400 cursor-pointer flex-row items-center">
                <HomeTwo theme="outline" size="24" />
                <span v-if="open" class="ml-4 font-bold">首页</span>
            </h2>
            <!-- 个人中心 -->
            <div>
                <motion.div @click="handleChangeUserInfoAnimationState"
                    :class="{ 'justify-between': open, 'justify-center ': !open }"
                    class="hover:text-purple-400 select-none cursor-pointer flex h-5 flex-row items-center">
                    <h2 :class="{ 'justify-center': !open }" class="flex my-5  flex-row items-center">
                        <PeoplesTwo theme="outline" size="24" />
                        <span v-if="open" class="ml-4 font-bold">个人中心</span>
                    </h2>
                    <Motion class="flex flex-row items-center" :initial="{
                        rotate: 0
                    }" :variants="userInfoContainer" :animate="userInfoContainerController">
                        <Right v-if="open" size="20" theme="outline" />
                    </Motion>

                </motion.div>
                <Motion class="pl-5 text-sm" :transition="{
                    duration: 0.1,
                }" :initial="{ display: 'none' }" :variants="userInfoItemContainer"
                    :animate="userInfoItemContainerController">
                    <!-- 收藏夹 -->
                    <h2 :class="{ 'justify-center': !open }"
                        class="flex my-5 h-5 hover:text-purple-400 z-0 cursor-pointer flex-row items-center">
                        <CollectionFiles theme="outline" size="20" />
                        <span v-if="open" class="ml-4 font-bold">收藏夹</span>
                    </h2>
                    <!-- 历史记录 -->
                    <h2 :class="{ 'justify-center': !open }"
                        class="flex my-5 h-5 hover:text-purple-400 cursor-pointer flex-row items-center">
                        <History theme="outline" size="20" />
                        <span v-if="open" class="ml-4 font-bold">历史记录</span>
                    </h2>
                </Motion>
            </div>
            <!-- 历史记录 -->
            <h2 :class="{ 'justify-center': !open }"
                class="flex my-5 h-5 hover:text-purple-400 z-10 bg-blue-50 cursor-pointer flex-row items-center">
                <History theme="outline" size="20" />
                <span v-if="open" class="ml-4 font-bold">历史记录</span>
            </h2>

        </div>
        <!-- 折叠标记 -->
        <div @click="handleChangeAnimate" class="cursor-pointer hover:text-purple-400 flex flex-row justify-center"
            v-if="!open">
            <DoubleRight theme="outline" size="24" />
        </div>
    </motion.div>
</template>