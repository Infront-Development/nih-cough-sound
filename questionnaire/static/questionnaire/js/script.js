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

const respondent_choices = document.getElementsByName("respondent_choices");

const noneChoice =  document.getElementById("id_date_diagnosed_0").parentElement.style.display = "none";


for(i=0; i < respondent_choices.length; i++){
    respondent_choices[i].addEventListener("change", (event) =>{
        const dates = document.getElementById("div_id_date_diagnosed");
        const noneChoice =  dates.querySelector("#id_date_diagnosed_0");
        if (event.target.id == "id_respondent_choices_0"){
            if (event.target.checked){
                dates.style.display = "none";
                noneChoice.checked = true;
            }else{
                dates.style.display = "block";
            }
        }else{
            noneChoice.checked = false;
            noneChoice.parentElement.style.display = "none"
            dates.style.display = "block";
        }
       
    
    })
}

