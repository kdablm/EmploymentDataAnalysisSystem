<script setup lang="ts">
import { Motion, motion } from 'motion-v'
import { useAnimationControls } from 'motion-v'
import { DoubleLeft, DoubleRight, HomeTwo, PeoplesTwo, CollectionFiles, History, Right, ChartPieOne, DataFile, TrendTwo, Me } from '@icon-park/vue-next'//图标
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
// 定义侧边栏开启与关闭动画
const container = {
    close: {
        width: '5rem'
    },
    open: {
        width: '14rem'
    }
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
        height: 'auto'
    }
}
/*定义动画控制器*/
const animateController = useAnimationControls()
const userInfoContainerController = useAnimationControls()//用户信息动画控制器
const userInfoItemContainerController = useAnimationControls()//用户信息动画控制器
const dataInfoContianerController = useAnimationControls()// 定于数据分析控制器
const dataInfoItemContainerController = useAnimationControls()// 定于数据分析控制器
/*定义动画控制器结束*/
// 定义点击事件
let open = ref(true)//展开标记
function handleChangeAnimate() {
    if (!open.value)
        animateController.start(container.open)
    else {
        animateController.start(container.close)
        // 关闭二级菜单
        userInfoItemContainerController.start(userInfoItemContainer.close)
        dataInfoItemContainerController.start(userInfoItemContainer.close)
        //修改箭头状态
        userInfoContainerController.start(userInfoContainer.close)
        dataInfoContianerController.start(userInfoContainer.close)
        //设置标志状态
        dataInfoOpen.value = false
        userInfoOpen.value = false
    }
    open.value = !open.value
}
// 定义用户下拉框动画
let userInfoOpen = ref(false)//标志
function handleChangeUserInfoAnimationState() {
    if (!open.value) {
        return;
    }
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

let dataInfoOpen = ref(false)
function handleChangeDataInfoAnimationState() {
    if (!open.value) {
        return;
    }
    if (!dataInfoOpen.value) {
        // 改变箭头状态
        dataInfoContianerController.start(userInfoContainer.open)
        // 展开下拉框
        dataInfoItemContainerController.start(userInfoItemContainer.open)
    } else {
        // 改变箭头状态
        dataInfoContianerController.start(userInfoContainer.close)
        // 展开下拉框
        dataInfoItemContainerController.start(userInfoItemContainer.close)
    }
    dataInfoOpen.value = !dataInfoOpen.value
}
//定义路由控制器
const router = useRouter()
const route = useRoute()
function routerTo(path: string) {
    router.push(path)
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
        <div class="px-1 text-md font-semibold">
            <!-- 首页 -->
            <h2 :class="{ 'justify-center': !open }" class="menuItem" @click="routerTo('/')">
                <HomeTwo theme="outline" size="24" />
                <span v-if="open" class="ml-4">首页</span>
            </h2>
            <!-- 个人中心 -->
            <div>
                <motion.div @click="handleChangeUserInfoAnimationState"
                    :class="{ 'justify-between': open, 'justify-center ': !open }" class="menuItem">
                    <h2 :class="{ 'justify-center': !open }" class="flex my-5  flex-row items-center">
                        <PeoplesTwo theme="outline" size="24" />
                        <span v-if="open" class="ml-3">个人中心</span>
                    </h2>
                    <Motion class="flex flex-row items-center" :initial="{
                        rotate: 0
                    }" :variants="userInfoContainer" :animate="userInfoContainerController">
                        <Right v-if="open" size="20" theme="outline" />
                    </Motion>
                </motion.div>
                <Motion class="pl-5 text-sm overflow-hidden font-medium" :transition="{
                    duration: 0.15,
                }" :initial="{ display: 'none' }" :variants="userInfoItemContainer"
                    :animate="userInfoItemContainerController">
                    <!-- 个人信息 -->
                    <h2 :class="{ 'justify-center': !open }" @click="routerTo('/user/info')" class="menuSubItem mb-5">
                        <Me theme="outline" size="20" />
                        <span v-if="open" class="ml-4">个人信息</span>
                    </h2>
                    <!-- 收藏夹 -->
                    <h2 :class="{ 'justify-center': !open }" class="menuSubItem mb-5">
                        <CollectionFiles theme="outline" size="20" />
                        <span v-if="open" class="ml-4">收藏夹</span>
                    </h2>
                    <!-- 历史记录 -->
                    <h2 :class="{ 'justify-center': !open }" class="menuSubItem">
                        <History theme="outline" size="20" />
                        <span v-if="open" class="ml-4">历史记录</span>
                    </h2>
                </Motion>
            </div>
            <!-- 数据分析 -->
            <div>
                <motion.div @click="handleChangeDataInfoAnimationState"
                    :class="{ 'justify-between': open, 'justify-center ': !open }" class="menuItem">
                    <h2 :class="{ 'justify-center': !open }" class="flex my-5 flex-row items-center">
                        <ChartPieOne theme="outline" size="24" />
                        <span v-if="open" class="ml-3">数据分析</span>
                    </h2>
                    <Motion class="flex flex-row items-center" :initial="{
                        rotate: 0
                    }" :variants="userInfoContainer" :animate="dataInfoContianerController">
                        <Right v-if="open" size="20" theme="outline" />
                    </Motion>

                </motion.div>
                <Motion class="pl-5 text-sm overflow-hidden font-medium" :transition="{
                    duration: 0.15,
                }" :initial="{ display: 'none' }" :variants="userInfoItemContainer"
                    :animate="dataInfoItemContainerController">
                    <!-- 数据概览 -->
                    <h2 :class="{ 'justify-center': !open }" class="menuSubItem mb-5">
                        <DataFile theme="outline" size="20" />
                        <span v-if="open" class="ml-4">数据概览</span>
                    </h2>
                    <!-- 岗位分析 -->
                    <h2 :class="{ 'justify-center': !open }" class="menuSubItem">
                        <TrendTwo theme="outline" size="20" />
                        <span v-if="open" class="ml-4">岗位分析</span>
                    </h2>
                    <!--  -->
                </Motion>
            </div>
        </div>
        <!-- 折叠标记 -->
        <div @click="handleChangeAnimate" class="cursor-pointer hover:text-purple-400 flex flex-row justify-center"
            v-if="!open">
            <DoubleRight theme="outline" size="24" />
        </div>
    </motion.div>
</template>
<style scoped>
@import "tailwindcss";

.menuItem {
    @apply flex my-5 h-7 hover:text-purple-400 cursor-pointer flex-row items-center select-none;
}

.menuSubItem {
    @apply flex h-5 hover:text-purple-400 cursor-pointer flex-row items-center select-none;
}
</style>