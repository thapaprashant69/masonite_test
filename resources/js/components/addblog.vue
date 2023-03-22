<template>
    Title:<input type="text" name="title"><br/>
    Description:<input type="text-area" name="description"><br/>
    <button type="submit" @click.prevent="addblog">Post Blog</button>
</template>

<script>
    import {createapp} from 'vue'
    let app = createapp({
        data:function(){
            return{
                isVisible : false
            }
        }
    })

    app.mount('#app')
</script>