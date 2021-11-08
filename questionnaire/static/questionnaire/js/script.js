const noneOptionSMed = document.getElementById("id_med_cond_opt_0");
const noneOptionSym = document.getElementById("id_symptoms_opt_0");
const noneOptionSmoke = document.getElementById("id_respondent_smoke_0");

noneOptionSym.addEventListener("click", hideOtherOptions);
noneOptionSMed.addEventListener("click", hideOtherOptions);
noneOptionSmoke.addEventListener("click",hideOtherOptions);



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


//Enable and disable date when user select vaccinate
document.getElementById("id_vaccinated_0").addEventListener("change", function(event){
    const chbox = event.target;
    const dateVaccinated = document.getElementById("id_date_vaccinated");
    dateVaccinated.disabled = !chbox.checked;
    dateVaccinated.required = chbox.checked;

})

document.getElementById("id_vaccinated_1").addEventListener("change", function(event){
    const ch1box = event.target;
    const datenVaccinated = document.getElementById("id_date_vaccinated");
    datenVaccinated.disabled = ch1box.checked;
    datenVaccinated.required = !ch1box.checked;

})

document.getElementById("id_respondent_choices_1").addEventListener("change", function(event){
    const ch2box = event.target;
    const dateposit = document.getElementById("id_date_diagnosed");
    dateposit.disabled = !ch2box.checked;
    dateposit.required = ch2box.checked;

})

document.getElementById("id_respondent_choices_0").addEventListener("change", function(event){
    const ch3box = event.target;
    const datenegat1 = document.getElementById("id_date_diagnosed");
    datenegat1.disabled = ch3box.checked;
    datenegat1.required = !ch3box.checked;

})
document.getElementById("id_respondent_choices_2").addEventListener("change", function(event){
    const ch4box = event.target;
    const dateposit = document.getElementById("id_date_diagnosed");
    dateposit.disabled = !ch4box.checked;
    dateposit.required = ch4box.checked;

})

