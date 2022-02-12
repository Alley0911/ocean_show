<template>
  <div id='band'>
    <div class="middle">
        <h1>{{title}}</h1>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'Banner',
  data(){
      return {
          title: "海洋产品展示平台"
      }
  }
}
</script>

<style>
div#head_nav a{
  font-size: 18px;
  letter-spacing: 3px;
  color: white; 
  text-decoration: none;
}
div#head_nav a:hover {  
  color:#000; 
  text-decoration: underline;
}
div#band{
    height: 100px;
    background-image: url(../assets/img/head.jpg);
    background-repeat: no-repeat;
    background-size: 100% 100%;
}

div.middle h1{
    height: 100px;
    line-height: 90px;  
    margin: 0px;  
    padding: 0px;
    color:#00529c;
    font-weight: 800;
}

span{
  padding: 10px 10px
}

div#head_nav{
  position: absolute;
  top:50px;
  right:40px;
}

</style>
