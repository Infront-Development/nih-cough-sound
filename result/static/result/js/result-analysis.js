function move() {
    var content = document.getElementById("login-form");  
    var progressSection = document.getElementById("progress-bar-section");   
    var progressBar = document.getElementById("progress-bar");   
    var width = 0;
    content.style.display = "none";
    var id = setInterval(frame, 40);
    function frame() {
      if (width >= 100) {
        progressSection.style.display = "none";
        content.style.display = "initial";
        clearInterval(id);
      } else {
        width++;
        progressBar.style.width = width + '%'; 
      }
    }
  }

window.onload = () => {
    move();
}