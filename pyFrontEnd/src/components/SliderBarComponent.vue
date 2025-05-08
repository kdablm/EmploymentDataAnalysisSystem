<script setup lang="ts">
import { Motion, motion } from 'motion-v'
import { useAnimationControls } from 'motion-v'
import { DoubleLeft, DoubleRight } from '@icon-park/vue-next'
import { ref } from 'vue'
// 定义开启与关闭动画
const container = {
    open: {
        wdith: '5rem'
    },
    close: {
        width: '16rem'
    }
}
// 定义动画控制器
const animateController = useAnimationControls()
// 定义点击事件
let open = ref(false)//展开标记
function handleChangeAnimate() {
    if (open.value)
        animateController.start(container.open)
    else animateController.start(container.close)
    open.value = !open.value
}

</script>

<template>
    <motion.div class=" bg-blue-400 text-white h-[100vh] aspect-square" 
        :animate="animateController" 
        :variants="container"
        :initial="{
            width: '5rem'
        }" 
        :transition="{
            duration: 0.5,
            ease: 'easeInOut',
            times: [0, 0.2, 0.5, 0.8, 1],
            type: 'spring',
            repeatDelay: 1,
        }">
        <i @click="handleChangeAnimate">
            <double-left v-if="open" theme="outline" size="24" fill="#ffffff" />
            <DoubleRight v-else theme="outline" size="24" fill="#ffffff" />
        </i>
    </motion.div>
</template>
