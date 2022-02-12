axios = require('axios')

function getData(){
  let p = new Promise((resolve, reject) =>{
    axios.get("http://10.28.16.192:8080/products/config_ini/data.json").then(
      response => {
        resolve(response.data) 
      },
      error => {
        reject(error)
      }
  )
  })
  return p
}
async function main(){
  let res = await getData()
  console.log(res)
  console.log(123)
}

main()