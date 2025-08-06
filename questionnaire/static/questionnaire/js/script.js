<script src="//cdn.jsdelivr.net/npm/sweetalert2@11"></script>
const noneOptionMed = document.getElementById("div_id_med_cond_opt").querySelector("input[type='checkbox']");
const noneOptionSym = document.getElementById("div_id_symptoms_opt").querySelector("input[type='checkbox']");
// const noneOptionSmoke = document.getElementById("id_respondent_smoke_1");
// const noneOptionSMed = document.getElementById("id_med_cond_opt_1");

noneOptionSym.addEventListener("click", hideOtherOptions);
noneOptionMed.addEventListener("click", hideOtherOptions);
// noneOptionSmoke.addEventListener("click", hideOtherOptions);

function showModal() {
  // $('#loaderModal').modal("show");
  $('#loaderModal').modal({
    backdrop: "static",
    keyboard: false,
    show: true
  });
  var progressBar = document.getElementById("progress-bar");
  var width = 0;
  var id = setInterval(frame,200);
  function frame() {
    if (width >= 100) {
      $('#loaderModal').modal("hide");
      clearInterval(id);
    } else {
      width++;
      progressBar.style.width = width + '%'; 
    }
  }
}

function hideOtherOptions(event) {
  let target = event.target;
  let parent = target.parentElement;
  nextSibling = parent.nextElementSibling;
  while (nextSibling) {
    nextSibling.style.display = target.checked ? "none" : "block";
    nextSibling = nextSibling.nextElementSibling;
  }
}

const respondent_choices = document.getElementsByName("respondent_choices");

const noneChoice = document.getElementById("id_date_diagnosed_0");

for (i = 0; i < respondent_choices.length; i++) {
  respondent_choices[i].addEventListener("change", (event) => {
    const dates = document.getElementById("div_id_date_diagnosed");
    if (event.target.id == "id_respondent_choices_0") {
      if (event.target.checked) {
        dates.style.display = "none";
      } else {
        dates.style.display = "block";
      }
    } else {
      dates.style.display = "block";
    }
  });
}