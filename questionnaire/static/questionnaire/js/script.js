const noneOptionSMed = document.getElementById("id_med_cond_opt_0");
const noneOptionSym = document.getElementById("id_symptoms_opt_0");
const noneOptionSmoke = document.getElementById("id_respondent_smoke_0");

noneOptionSym.addEventListener("click", hideOtherOptions);
noneOptionSMed.addEventListener("click", hideOtherOptions);
noneOptionSmoke.addEventListener("click", hideOtherOptions);

src = "//cdn.jsdelivr.net/npm/sweetalert2@11";
function validation_questionnaire() {
  var a = document.getElementById("id_vaccinated_0");
  var b = document.getElementById("id_vaccinated_1");
  var c = document.getElementById("id_date_vaccinated");

  if (a.checked || b.checked) {
    if (a.checked) {
      if (c.value == "") {
        swal("Please fill in date of vaccinated", "", "warning");
      }
    }

    // swal("Please check your information in Patient Information Form").then(function(){
    //     // $('#nav-tab a[href="#nav-patient"]').tab('show');
    // });
  } else {
    swal("Please fill in your vaccination status", "", "warning");
  }
  return true;
}

function respondent_validation() {
  var a = document.getElementById("id_respondent_choices_0");
  var b = document.getElementById("id_respondent_choices_1");
  var c = document.getElementById("id_respondent_choices_2");
  var d = document.getElementById("id_date_diagnosed");

  if (a.checked || b.checked || c.checked) {
    if (b.checked || c.checked) {
      if (d.value == "") {
        swal("Please fill in date of your diagnosed positive", "", "warning");
      }
    }

    // swal("Please check your information in Patient Information Form").then(function(){
    //     // $('#nav-tab a[href="#nav-patient"]').tab('show');
    // });
  } else {
    swal("Please choose your respondent group", "", "warning");
  }
  return validation_questionnaire();
}

function sex_validation() {
  var a = document.getElementById("id_respondent_sex_0");
  var b = document.getElementById("id_respondent_sex_1");
  var c = document.getElementById("id_age");

  if (c.value == "") swal("Please fill your age", "", "warning");

  if (a.checked || b.checked) {
  } else {
    swal("Please choose your gender", "", "warning");
  }

  return respondent_validation();
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

const vaccinate = document.getElementsByName("vaccinated");

const none = document.getElementById("id_vaccinated_0");

for (i = 0; i < vaccinate.length; i++) {
  vaccinate[i].addEventListener("change", (event) => {
    const dates = document.getElementById("div_id_date_vaccinated");

    if (event.target.id == "id_vaccinated_1") {
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
//
$(document).ready(function () {
  var iso = new Date().toISOString();
  var maxDate = iso.substring(0, iso.length - 14);
  var minDate = iso.substring(0, iso.length - 14);
  $("#id_date_vaccinated").attr("max", minDate);
  $("#id_date_diagnosed").attr("max", minDate);
});

//Enable and disable date when user select vaccinate
document
  .getElementById("id_vaccinated_0")
  .addEventListener("change", function (event) {
    const chbox = event.target;
    const dateVaccinated = document.getElementById("id_date_vaccinated");
    dateVaccinated.disabled = !chbox.checked;
    dateVaccinated.required = chbox.checked;
  });

document
  .getElementById("id_vaccinated_1")
  .addEventListener("change", function (event) {
    const chbox = event.target;
    const dateVaccinated = document.getElementById("id_date_vaccinated");
    dateVaccinated.disabled = chbox.checked;
    dateVaccinated.required = !chbox.checked;
  });

// Select your input element.
var age = document.getElementById("id_age");
// Listen for input event on numInput.
age.onkeydown = function (e) {
  if (
    !(
      (e.keyCode > 95 && e.keyCode < 106) ||
      (e.keyCode > 47 && e.keyCode < 58) ||
      e.keyCode == 8
    )
  ) {
    return false;
  }
};

document
  .getElementById("id_respondent_choices_1")
  .addEventListener("change", function (event) {
    const ch2box = event.target;
    const dateposit = document.getElementById("id_date_diagnosed");
    dateposit.disabled = !ch2box.checked;
    dateposit.required = ch2box.checked;
  });

document
  .getElementById("id_respondent_choices_2")
  .addEventListener("change", function (event) {
    const ch4box = event.target;
    const dateposit = document.getElementById("id_date_diagnosed");
    dateposit.disabled = !ch4box.checked;
    dateposit.required = ch4box.checked;
  });

document
  .getElementById("id_respondent_choices_0")
  .addEventListener("change", function (event) {
    const ch4box = event.target;
    const dateposit = document.getElementById("id_date_diagnosed");
    dateposit.disabled = ch4box.checked;
    dateposit.required = !ch4box.checked;
  });
