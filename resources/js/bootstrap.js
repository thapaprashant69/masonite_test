/**
 * We'll load the axios HTTP library which allows us to easily issue requests
 * to our Masonite back-end. This library automatically handles sending the
 * CSRF token as a header based on the value of the "XSRF" token cookie.
 */

window.axios = require('axios');

window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

/**
 * Next we will register the CSRF Token as a common header with Axios so that
 * all outgoing HTTP requests automatically have it attached. This is just
 * a simple convenience so we don't have to attach every token manually.
 */

let token = document.head.querySelector('meta[name="csrf-token"]');

if (token) {
    window.axios.defaults.headers.common['X-CSRF-TOKEN'] = token.content;
} else {
    console.error('CSRF token not found: https://docs.masoniteproject.com/features/csrf#ajax-vue-axios');
}


import {createApp} from 'vue';
import displayBlog from './components/blogsview.vue';
import axios from 'axios';

let app = createApp({
    mounted(){
        console.log('App mounted successfully');
    }
})

app.component("add-blog", {
  template: `
    <button @click="isVisible = !isVisible" class="button">Add Blog</button>
    <a href="/blog/count" class="button">Get Blog Count</a><br />
        <div v-if="isVisible" class="border-2 bg-grey w-content">
            <form action="/blog/create" method="POST" @submit.prevent="createUser">
                <h2 class="mt-2 font-bold">Add a new blog</h2>
                Heading:<input type="text" name="title" v-model="title" class="border-2 color-blue m-2"/><br/>
                Description:<input type="textarea" name="description" v-model="description" class="border-2 color-blue m-2"/><br/>
                <button type="submit" class="border-2 px-3 rounded-md">Add blog</button>
                <button @click="isVisible = !isVisible" class="m-2 px-3 rounded-md border-2">Close</button>
            </form>
        </div>
    `,
  data() {
    return {
      isVisible: false,
      title: '',
      description: ''
    };
  },
  methods:{
    createUser(){
        axios.post('/blog/create',{
            title: this.title,
            description: this.description
        })
        .then((response) => {
            console.log("Blog created successfully")
            this.title = ''
            this.description = ''
            this.isVisible = false
            if (window.alert("Post created successfully")) {
              window.location.reload();
            }
        })
        .catch((error) => {
            console.error(error);
        });
    }
  }
});

app.mount("#app");

let app2 = createApp({
    mounted(){
        console.log("App2 mounted successfully")
    }
})
app2.component("edit-blog", {
    props:{
        blog:{
            type: Object,
            default: {},
        }
    },
  template: `
    <button @click="isVisible = !isVisible" class="button">Edit</button>
    <a :href="'/blog/'+ blog.id + '/delete' " class="button" @click.prevent="deleteBlog">Delete</a><br />
        <div v-if="isVisible" class="border-2 bg-grey w-content">
            <form action="'/blog/' + blog.id + '/edit'" method="POST" @submit.prevent="submitForm">
                <h2 class="mt-2 font-bold">Edit blog</h2>
                Heading:<input type="text" v-model="heading" class="border-2 color-blue m-2"/><br/>
                Description:<input type="textarea" v-model="description" class="border-2 color-blue m-2"/><br/>
                <button class="border-2 px-3 rounded-md">Edit blog</button>
                <button @click="isVisible = !isVisible" class="m-2 px-3 rounded-md border-2">Close</button>
            </form>
        </div>
    `,
  data() {
    return {
      isVisible: false,
      heading: this.blog.title,
      description: this.blog.description
    };
  },
  methods:{
    deleteBlog(){
      axios
        .get(`/blog/${this.blog.id}/delete`)
        .then((response) => {
          this.$emit("delete-blog", this.blog.id);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    submitForm(){
        this.$emit("update-blog",{
            blogId: this.blog.id,
            title: this.heading,
            description:this.description
        });
        this.isVisible=false;
    }
  }
});

app2.component("displayBlog",displayBlog)

app2.mount("#blog");


app.component("view-blogs", blog, {
  blogs: [
    { heading: "Blog 1", description: "This is is a blog post 1" },
    { heading: "Blog 2", description: "This is a blog post 2" },
  ],
});
