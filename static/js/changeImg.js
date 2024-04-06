var imgInput = document.getElementById('imgInput');
var imgView = document.getElementById('imgView');
var imgBtn = document.getElementById('imgBtn');

imgBtn.addEventListener('click',()=>{
    imgInput.click()
})

imgInput.addEventListener('change',(e)=>{
    imgView.src = URL.createObjectURL(e.target.files[0])
})