const noneOptionSMed = document.getElementById("id_med_cond_opt_0");
const noneOptionSym = document.getElementById("id_symptoms_opt_0");

noneOptionSym.addEventListener("click", hideOtherOptions);
noneOptionSMed.addEventListener("click", hideOtherOptions);


function hideOtherOptions(event){
    let target = event.target;
    let parent = target.parentElement;
    nextSibling = parent.nextElementSibling;
    while(nextSibling){
        nextSibling.style.display = target.checked ? "none" : "block";
        nextSibling = nextSibling.nextElementSibling;

    }
}