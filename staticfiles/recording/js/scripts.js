function enableAgreeBtn(event) {
  const agree_btn = document.getElementById("agree-btn");

  if (agree_btn.disabled) {
    agree_btn.disabled = false;
  }
}

function showMessageFromServer(event) {
  alertDom = document.getElementById("alert-message");
  message =
    alertDom != null ? alertDom.innerText : "Welcome to Cough Sound Project";
  alertify.alert("", message, function (event) {
    window.location.href = "/questionnaire/questionnaire-form/";
  });
}

function enableAgreeBtn(event) {
  const agree_btn = document.getElementById("agree-btn");

  if (agree_btn.disabled) {
    agree_btn.disabled = false;
  }
}

// Redirect user to the next page. predefined in backend, by embedding the url in the text input of ID next
function redirectToNextPage(){
  const next = document.getElementById("nextPage").value;
  if (next != undefined){
    window.location.href = next;
  }
}

// document.getElementById("agree-btn").onclick = function () {
//   location.href = "cough";
// };
