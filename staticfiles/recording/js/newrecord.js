// Recorder API
//Reference from https://medium.com/@bryanjenningz/how-to-record-and-play-audio-in-javascript-faa1b2b3e49b

//Recording Pop-up screen flow
const promptRecording = async (
  stopID,
  trackIndicator,
  maskIndicator,
  methodIndicator,
  callbackFn
) => {
  //Part 1a Cough-with-mask POP UP
  if (maskIndicator == "withMask" && methodIndicator == "cough") {
    Swal.fire({
      title: gettext(
        "<div><img style='height: 120px;' src='/static/img/Mask on.png' alt='Mask-on'/></div>" +
          "<div class='h5 text-white font-weight-bold'>Ensure you are in a quiet and safe environment" +
          "<div><br>Example : </div>" +
          '<div class="mt-2 mb-3"><audio controls><source src="/static/audio/3. Cough Normal A.wav"><source src="/static/audio/3. Cough Normal A.ogg"></audio></div>' +
          "<div>"
      ),
      background: "#2B1392",
      cancelButtonText: gettext("Cancel"),
      confirmButtonColor: "#FFFFFF",
      confirmButtonText: gettext(
        "<div class ='font-weight-bold' style='color:#2B1392'>START</div>"
      ),
      customClass: {
        confirmButton: "pop-up-button pl-4 pr-4",
      },
    }).then((result) => {
      if (result.isConfirmed) {
        let timerInterval;
        Swal.fire({
          html: gettext(
            "<div class='h5'>Recording will start in<span style='color:#2B1392'> <countdown></countdown></span> seconds.<br>" +
              "Please provide <span style='color:#2B1392'>3-5 Coughs<br>" +
              "(Min. 5 seconds)</span></div>"
          ),
          timer: 5000,
          timerProgressBar: true,

          didOpen: () => {
            Swal.showLoading();
            const countdown =
              Swal.getHtmlContainer().querySelector("countdown");
            timerInterval = setInterval(() => {
              countdown.textContent = (Swal.getTimerLeft() / 1000).toFixed(0);
            }, 100);
          },
          willClose: () => {
            clearInterval(timerInterval);
            record(stopID, trackIndicator, callbackFn);
          },
        }).then((result) => {
          /* Read more about handling dismissals below */
          if (result.dismiss === Swal.DismissReason.timer) {
          }
        });
      }
    });

    //Part 1b Cough-no-mask POP UP
  } else if (maskIndicator == "noMask" && methodIndicator == "cough") {
    Swal.fire({
      title: gettext(
        "<div><img style='height: 120px;' src='/static/img/Mask off.png' alt='Mask-off'/></div>" +
      "<div class='h5 text-white font-weight-bold'>Ensure you are in a quiet and safe environment before <span style='color: #FF93DD;'>removing your mask</span>" +
          "<div class='p-4'>Example:</div>" +
          '<div class="mt-2 mb-3"><audio controls src="/static/audio/3. Cough Normal A.wav"></audio></div>' +
          "<div>"
      ),
      background: "#2B1392",
      cancelButtonText: gettext("Cancel"),
      confirmButtonColor: "#FFFFFF",
      confirmButtonText: gettext(
        "<div class ='font-weight-bold' style='color:#2B1392'>START</div>"
      ),
      customClass: {
        confirmButton: "pop-up-button pl-4 pr-4",
      },
    }).then((result) => {
      if (result.isConfirmed) {
        let timerInterval;
        Swal.fire({
          html: gettext(
            "<div class='h5'>Recording will start in<span style='color:#2B1392'> <countdown></countdown></span> seconds.<br>" +
              "Please provide <span style='color:#2B1392'>3-5 Coughs<br>" +
              "(Min. 5 seconds)</span></div>"
          ),
          timer: 5000,
          timerProgressBar: true,

          didOpen: () => {
            Swal.showLoading();
            const countdown =
              Swal.getHtmlContainer().querySelector("countdown");
            timerInterval = setInterval(() => {
              countdown.textContent = (Swal.getTimerLeft() / 1000).toFixed(0);
            }, 100);
          },
          willClose: () => {
            clearInterval(timerInterval);
            record(stopID, trackIndicator, callbackFn);
          },
        }).then((result) => {
          /* Read more about handling dismissals below */
          if (result.dismiss === Swal.DismissReason.timer) {
          }
        });
      }
    });

    //Part 2a Breath-with-mask POP UP
  } else if (maskIndicator == "withMask" && methodIndicator == "breath") {
    Swal.fire({
      title: gettext(
        "<div><img style='height: 120px;' src='../../../../static/img/Mask on.png' alt='Mask-on'/></div>" +
          "<div class='h5 text-white font-weight-bold'>Ensure you're in a quiet environment and<span style='color: #FF93DD;'> with mask on</span>" +
          "<div>\nSample Breath Sound:</div>" +
          '<div class="mt-2 mb-3"><audio controls src="../../../../static/audio/3. Breath.wav"></audio></div>' +
          "<div>"
      ),
      background: "#2B1392",
      cancelButtonText: gettext("Cancel"),
      confirmButtonColor: "#FFFFFF",
      confirmButtonText: gettext(
        "<div class ='font-weight-bold' style='color:#2B1392'>Start</div>"
      ),
      customClass: {
        confirmButton: "pop-up-button pl-4 pr-4",
      },
    }).then((result) => {
      if (result.isConfirmed) {
        let timerInterval;
        Swal.fire({
          html: gettext(
            "<div class='h5'>Recording will start in<span style='color:#2B1392'> <countdown></countdown></span> seconds.<br>" +
              "Please provide <span style='color:#2B1392'>3-5 Breaths<br>" +
              "(Min. 5 seconds)</span></div>"
          ),
          timer: 5000,
          timerProgressBar: true,

          didOpen: () => {
            Swal.showLoading();
            const countdown =
              Swal.getHtmlContainer().querySelector("countdown");
            timerInterval = setInterval(() => {
              countdown.textContent = (Swal.getTimerLeft() / 1000).toFixed(0);
            }, 100);
          },
          willClose: () => {
            clearInterval(timerInterval);
            record(stopID, trackIndicator, callbackFn);
          },
        }).then((result) => {
          /* Read more about handling dismissals below */
          if (result.dismiss === Swal.DismissReason.timer) {
          }
        });
      }
    });

    //Part 2b Breath-no-mask POP UP
  } else if (maskIndicator == "noMask" && methodIndicator == "breath") {
    Swal.fire({
      title: gettext(
        "<div><img style='height: 120px;' src='../../../../static/img/Mask off.png' alt='Mask-off'/></div>" +
          "<div class='h5 text-white font-weight-bold'>Ensure you're in a safe environment and<span style='color: #FF93DD;'> with mask on</span>" +
          "<div>\nSample Breath Sound:</div>" +
          '<div class="mt-2 mb-3"><audio controls src="../../../../static/audio/3. Breath.wav"></audio></div>' +
          "<div>"
      ),
      background: "#2B1392",
      cancelButtonText: gettext("Cancel"),
      confirmButtonColor: "#FFFFFF",
      confirmButtonText: gettext(
        "<div class ='font-weight-bold' style='color:#2B1392'>Start</div>"
      ),
      customClass: {
        confirmButton: "pop-up-button pl-4 pr-4",
      },
    }).then((result) => {
      if (result.isConfirmed) {
        let timerInterval;
        Swal.fire({
          html: gettext(
            "<div class='h5'>Recording will start in<span style='color:#2B1392'> <countdown></countdown></span> seconds.<br>" +
              "Please provide <span style='color:#2B1392'>3-5 Breaths<br>" +
              "(Min. 5 seconds)</span></div>"
          ),
          timer: 5000,
          timerProgressBar: true,

          didOpen: () => {
            Swal.showLoading();
            const countdown =
              Swal.getHtmlContainer().querySelector("countdown");
            timerInterval = setInterval(() => {
              countdown.textContent = (Swal.getTimerLeft() / 1000).toFixed(0);
            }, 100);
          },
          willClose: () => {
            clearInterval(timerInterval);
            record(stopID, trackIndicator, callbackFn);
          },
        }).then((result) => {
          /* Read more about handling dismissals below */
          if (result.dismiss === Swal.DismissReason.timer) {
          }
        });
      }
    });
  }
};

//Recording API
const recordAudio = () => {
  return new Promise((resolve) => {
    navigator.mediaDevices
      .getUserMedia({
        audio: { channelCount: 2 },
      })
      .then((stream) => {
        const mediaRecorder = new MediaRecorder(stream);
        const audioChunks = new Array();

        mediaRecorder.addEventListener("dataavailable", (event) => {
          audioChunks.push(event.data);
        });

        const start = () => {
          mediaRecorder.start();
        };

        const stop = () => {
          return new Promise((resolve) => {
            mediaRecorder.addEventListener("stop", () => {
              const audioBlob = new Blob(audioChunks, {
                type: "audio/wav",
              });
              const audioUrl = URL.createObjectURL(audioBlob);
              const audio = new Audio();
              audio.preload = "auto";
              audio.controls = true;
              audio.src = audioUrl;

              resolve({ audioBlob, audioUrl, audio });
            }); // End event listener
            stream.getTracks().forEach((track) => {
              if (track.readyState == "live") {
                track.stop();
              }
            });
            mediaRecorder.stop();
          });
        };
        return resolve({ start, stop });
      });
  });
};

const record = async (id, trackIndicator, callbackFn) => {
  // const recorder = await recordAudio();
  const recorder = await audioRecorder();

  recorder.start();

  // Recording Interactive
  var recording_anim = document.getElementById("recording-animation1");
  var record_button = document.getElementById("recordButtonOne");
  var audio_wave = document.getElementById("wave1");
  var audio_wave_anim = document.getElementById("wave1_animate");
  var stop_button = document.getElementById("stopButtonOne");

  var clockIndicator = Clock1;

  clockIndicator.start();
  // Recording time indicator
  recording_anim.classList.toggle("recording-stop");
  recording_anim.classList.toggle("recording-start");

  // Stop Button Interaction
  stop_button.disabled = true;
  stop_button.style.opacity = "0.3";

  //Audio Wave Interaction when START
  audio_wave.style.display = "none";
  audio_wave_anim.style.display = "flex";

  //Record Button Interaction when START
  record_button.style.display = "none";
  stop_button.style.display = "block";

  //Stop Button
  const stopButton = document.getElementById(id);
  stopButton.onclick = async () => {
    clockIndicator.reset();
    recorder.stop(callbackFn);
    // STOP Recording Interactive
    // const recording_anim = document.getElementById("recording-animation");
    recording_anim.classList.toggle("recording-stop");
    recording_anim.classList.toggle("recording-start");

    //Audio Wave Interaction when STOP
    audio_wave.style.display = "flex";
    audio_wave_anim.style.display = "none";

    //Record Button Interaction when STOP
    stop_button.style.display = "none";
  };
};

function makeRecordFunction(
  playID,
  stopID,
  trackIndicator,
  maskIndicator,
  methodIndicator,
  callbackFn
) {
  const playButton = document.getElementById(playID);
  playButton.onclick = () =>
    promptRecording(
      stopID,
      trackIndicator,
      maskIndicator,
      methodIndicator,
      callbackFn
    );
}

// Callback function takes 3 arguments : audioBlob, audioUrl, play as a single javascritp object
// audioBlob : An array of bytes representing the audio
// audioUrl  : A URL to the audio blob
// audio     : HTML Node of the audio tag
//Usage
/*
makeRecordFunction("buttonOne", "buttonTwo", ({audioBlob, audioUrl, audio}) => {
    //Do Dom manipulation or operations here
}

*/

//Create Recorded Audio Playback Track and POST audio file to Backend
function createDownloadLink(blob, trackIndicator) {
  // Create the Recorded Playback Track

  URL = window.webkitURL || window.URL;
  const audioUrl = URL.createObjectURL(blob);
  // const audioBlob = blob;
  // const audio = new Audio();
  // audio.src = audioUrl;
  // audio.controls = true;
  var url = audioUrl;
  var audioContainter = document.createElement("div");
  audioContainter.classList.add("audio-list");
  if (trackIndicator == 1) {
    audioContainter.setAttribute("id", "recorded-track-1");
  } else {
    audioContainter.setAttribute("id", "recorded-track-2");
  }
  var au = document.createElement("audio");
  //add controls to the <audio> element
  au.controls = true;
  au.preload = "metadata";
  au.src = url;
  au.classList.add("audioRecording");
  // au.setAttribute("mask", rec.mask);
  //add the new audio and a elements to the li element
  audioContainter.appendChild(au);
  if (trackIndicator == 1) {
    audioContainter.innerHTML +=
      "<a href='#removeAudio' onclick='removeMeFromParentAudiowrapper(event,1)'> <i class='fa fa-trash' style='color: red;'> </i> </a>  ";
  } else {
    audioContainter.innerHTML +=
      "<a href='#removeAudio' onclick='removeMeFromParentAudiowrapper(event,2)'> <i class='fa fa-trash' style='color: red;'> </i> </a>  ";
  }

  // End of Recorded Playback Track

  // Get the div in HTML that need to place the above created recorded playback
  if (trackIndicator == 1) {
    var wrapper = document.getElementById("audio-wrapper1");
  } else {
    var wrapper = document.getElementById("audio-wrapper2");
  }
  wrapper.appendChild(audioContainter);

  //filename to send to server without extension
  //upload link
  // var upload = document.createElement("a");
  // upload.href = "#";
  // upload.innerHTML = "Upload";
}

function removeMeFromParentAudiowrapper(event, trackIndicator) {
  var audioTrack = document.getElementById("recorded-track-1");
  var record_button = document.getElementById("recordButtonOne");
  if (trackIndicator == 1) {
    audioTrack = document.getElementById("recorded-track-1");
    record_button = document.getElementById("recordButtonOne");
    audioTrack.remove();
    record_button.style.display = "block";
  } else {
    audioTrack = document.getElementById("recorded-track-2");
    record_button = document.getElementById("recordButtonTwo");
    record_button.style.display = "block";
    audioTrack.remove();
  }
}

// Clock Countdown Function for Recording
var Clock1 = {
  totalSeconds: 0,
  start: function () {
    if (!this.interval) {
      var self = this;
      function pad(val) {
        return val > 9 ? val : "0" + val;
      }
      this.interval = setInterval(function () {
        self.totalSeconds += 1;

        document.getElementById("min1").innerHTML = pad(
          Math.floor((self.totalSeconds / 60) % 60)
        );
        document.getElementById("sec1").innerHTML = pad(
          parseInt(self.totalSeconds % 60)
        );
        const stopButton = document.getElementById("stopButtonOne");

        //make sure the recording is more than 5 second
        if (self.totalSeconds >= 05) {
          stopButton.disabled = false;
          stopButton.style.opacity = "1.0";
        }
      }, 1000);
    }
  },

  reset: function () {
    Clock1.totalSeconds = null;
    clearInterval(this.interval);
    document.getElementById("min1").innerHTML = "00";
    document.getElementById("sec1").innerHTML = "00";
    delete this.interval;
  },
  pause: function () {
    clearInterval(this.interval);
    delete this.interval;
  },

  resume: function () {
    this.start();
  },

  restart: function () {
    this.reset();
    Clock1.start();
  },
};

// Clock Countdown Function for Recording
var Clock2 = {
  totalSeconds: 0,
  start: function () {
    if (!this.interval) {
      var self = this;
      function pad(val) {
        return val > 9 ? val : "0" + val;
      }
      this.interval = setInterval(function () {
        self.totalSeconds += 1;

        document.getElementById("min2").innerHTML = pad(
          Math.floor((self.totalSeconds / 60) % 60)
        );
        document.getElementById("sec2").innerHTML = pad(
          parseInt(self.totalSeconds % 60)
        );

        const stopButton = document.getElementById("stopButtonTwo");
        //make sure the recording is more than 5 second
        if (self.totalSeconds >= 5) {
          stopButton.disabled = false;
          stopButton.style.opacity = "1.0";
        }
      }, 1000);
    }
  },

  reset: function () {
    Clock2.totalSeconds = null;
    clearInterval(this.interval);
    document.getElementById("min2").innerHTML = "00";
    document.getElementById("sec2").innerHTML = "00";
    delete this.interval;
  },
  pause: function () {
    clearInterval(this.interval);
    delete this.interval;
  },

  resume: function () {
    this.start();
  },

  restart: function () {
    this.reset();
    Clock2.start();
  },
};

async function uploadAudio(endPoint, onSuccess, onFail) {
  // Prepare form data
  const fd = new FormData();
  // Get the csrf token

  const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  fd.append("csrfmiddlewaretoken", csrfToken);

  // Get all audio Tag
  const audioTags = document.getElementsByClassName("audioRecording");

  const category = document.querySelector("#record_category").value
  fd.append("record_category", category)

  for (let i = 0; i < audioTags.length; i++) {
    const data = await fetch(audioTags[i].src);
    const blob = await data.blob();

    URL = window.webkitURL || window.URL;
    URL.revokeObjectURL(audioTags.src);
    fd.append("audio[]", blob);
  }

  const res = await fetch(endPoint, {
    body: fd,
    method: "post",
    credentials: "same-origin",
  });

  const json = await res.json();
  if (!res.ok) {
    onFail();
  }
  sessionStorage.clear();
  onSuccess();
}

function initRecordPage() {
  const nextButton = document.getElementById("next");
  nextButton.addEventListener("click", (e) => {
    if (document.getElementsByTagName("audio").length < 1) {
      Swal.fire({
        icon: "error",
        title: gettext("Oops..."),
        text: gettext("You must record audio !"),
      });
      return;
    }
    uploadAudio(
      window.location.pathname,
      () => {
        Swal.fire({
          icon: "success",
          title: gettext("Audio Recorded!"),
          text: gettext("Your audio has been recorded!"),
        }).then((result) => {
          if (result.isConfirmed) {
            redirectToNextPage();
          }
        });
      },
      () => {
        Swal.fire({
          icon: "error",
          title: gettext("Oops..."),
          text: gettext("It seems there is an issue, please contact admin"),
        });
      }
    );
  });
}

initRecordPage();


function sessionSaveRecordingBlob(url, itemName){
  const blob = sessionStorage.getItem(itemName);
  // Revoke old blob
  if(itemName != null){
    URL.revokeObjectURL(blob);
  }
  sessionStorage.setItem(url, itemName);
}


class Timer{
  totalSeconds = 0;
  sec =  "00";
  min = "00";

  interval = null;
  pad = (val) => val > 9 ? val : "0" + val;

  start(){
    this.interval = setInterval( () => {
      this.totalSeconds++;
      this.min = this.pad(Math.floor(this.totalSeconds / 60) % 60);
      this.sec = this.pad(Math.floor(this.totalSeconds % 60))
    }, 1000);
  }

  stop(callbackFn = null){
    clearInterval(this.interval);
    if (callbackFn == null) return;
    callbackFn();
  }

  getTimeText(){
    return `${this.min}:${this.sec}`;
  }

}




function sessionSaveRecordingBlob(data, itemName){
  sessionStorage.setItem(data, itemName);
  
}

// Save recording as data url if the user change language
$(".langchange").on("submit", function(e){
  e.preventDefault();

  // Clear existing session storage
  sessionStorage.clear();
  const saveBlobs = async () =>{

    const blobName = document.getElementById("recordBlobName").value;

    const audios = document.getElementsByClassName("audioRecording");

      for(i=0; i < audios.length; i++){
        let data = null;
        const e = audios[i];
        const reader = new FileReader();
        const res = await fetch(e.src);
        const blob = await res.blob();
        reader.onload = () =>{
          data = reader.result;
          sessionSaveRecordingBlob(data, getBlobKeyNameString(blobName, i+1))
        }
        reader.readAsDataURL(blob);

    }
  }
  saveBlobs()
  .then(()=> e.target.submit());
})
function getBlobKeyNameString(blobName, i){
  return `${blobName}${i}`
}

async function loadAudioFromSessionsStorage(){
    for( let i=0;  i < sessionStorage.length; i++){
      const data = sessionStorage.key(i);
      if(data == null) return;
      const response = await fetch(data);
      const blob = await response.blob();
      createDownloadLink(blob, i+1);
    }
    //Clear the session storage after usage
    sessionStorage.clear();

}

loadAudioFromSessionsStorage();