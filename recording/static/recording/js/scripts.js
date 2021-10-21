
function enableAgreeBtn(event){
        const agree_btn = document.getElementById("agree-btn");

        if (agree_btn.disabled){
            agree_btn.disabled = false;
        }
    }



document.getElementById("recordButton").addEventListener("click", function () { Clock.start(); });
document.getElementById("stopButton").addEventListener("click", function () { Clock.reset(); });