// var form = document.getElementById("#myForm"),
//     imgInput = document.getElementById(".img"),
//     file = document.getElementById("imgInput"),
//     name = document.getElementById("name"),
//     age = document.getElementById("age"),
//     city = document.getElementById("city"),
//     email = document.getElementById("email"),
//     phone = document.getElementById("phone"),
//     post = document.getElementById("post"),
//     sData = document.getElementById("sDate"),
//     submitBtn = document.querySelector(".submit"),
//     userInfo = document.getElementById("data")
//
// let getData = localStorage.getItem('userProfile') ? JSON.parse(localStorage.getItem('userProfile')) : []
// let isData = false, editId
//
// file.onchange = function (){
//     if(file.files[0].size < 1000000) {
//         var fileReader = new FileReader();
//
//         fileReader.onload = function (e) {
//             imgUrl = e.target.result
//             imgInput.src = imgUrl
//         }
//         fileReader.readAsDataURL(file.files[0])
//     }
//     else{
//         alert("Too large")
//         }
//
//
// }
//
//
// form.addEventListener('submit', (e)=>{
//     e.preventDefault()
//
//     const information = {
//         picture: imgInput.src === undefined ? "./profile.jpg" : imgInput.src,
//         employeeName: userName.value,
//         employeeAge: age.value,
//         employeeCity: city.value,
//         employeeEmail: email.value,
//         employeePhone: phone.value,
//         employeePost: post.value,
//         startDate: sData.value
//     }
//
//     if(!isEdit){
//         getData.push(information)
//     }
//     else{
//         isEdit = false
//         getData[editId] = information
//     }
//
//     localStorage.getItem("userProfile", JSON.stringify(getData))
//     submitBtn.innerText = 'Submit'
// })