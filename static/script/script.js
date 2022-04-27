document.querySelector(".menu").addEventListener("click", () => {
    document.querySelectorAll(".target").forEach((item) => {
      item.classList.toggle("change");
    });
  });
  
  document.querySelectorAll(".wrapper").forEach((item) => {
    item.addEventListener("click", () => {
      document.querySelectorAll(".target").forEach((item) => {
        item.classList.remove("change");
      });
    });
  });




  const icons = document.querySelectorAll('.section-1-img img')

  let i = 1;
  
  setInterval(() =>{
      i++;
  
      const icon = document.querySelector('.section-1-img .change')
      icon.classList.remove('change')
  
      if(i> icons.length){
          icons[0].classList.add('change');
          i=1;
      }
      else{
          icon.nextElementSibling.classList.add('change')
      }
  
  }, 4000);