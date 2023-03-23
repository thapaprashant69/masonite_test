<template>
    <div v-for="blog in blogs" :key="blog.id">
        <h4>{{blog.title}}</h4>
        <p>{{blog.description}}</p>
        <edit-blog :blog="blog" @delete-blog="deleteBlog" @update-blog="updateBlog"/>
        <hr>
    </div>
</template>

<script>
    import axios from "axios";
    export default{
        name:"displayBlog",
        props:{
            blogs:{
                type:Array,
                default:[],
            }
        },
        methods:{
            deleteBlog(blogId){
                // this.blogs = this.blogs.filter((blog) => blog.id !== blogId);
                if (window.alert("Post deleted successfully")) {
                    window.location.reload();
                }
            },
            updateBlog(blog){
                axios.post(`/blog/${blog.blogId}/update`,{
                    title:blog.title,
                    description:blog.description
                })
                .then(response =>{
                    const updatedBlog = response.data.data;
                    const index = this.blogs.findIndex(blog => blog.id === updatedBlog.id);
                    if (index !== -1) {
                        this.blogs[index] = updatedBlog;
                    
                        if (window.alert("Post edited successfully")) {
                            window.location.reload();
                        }
                        // this.$set(this,'blogs',this.blogs);
                        // this.setState({blogs: this.blogs});
                        // this.forceUpdate();
                    }
                })
                .catch(error =>{
                    console.error(error);
                })
            }
        }
    }
</script>