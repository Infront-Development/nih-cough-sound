// Recorder API
//Reference from https://medium.com/@bryanjenningz/how-to-record-and-play-audio-in-javascript-faa1b2b3e49b

//Recording Pop-up screen flow
const promptRecording = async (stopID) => {
  Swal.fire({
    title: gettext(
      "<div><img style='height: 120px;' src='../../../../static/img/Mask off.png' alt='Mask-off '/></div>" +
        "<div class='h5 text-white font-weight-bold'>Ensure you're in a safe environment and<div style='color: #FF93DD;'>Take off Mask</div></div>"
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
          const countdown = Swal.getHtmlContainer().querySelector("countdown");
          timerInterval = setInterval(() => {
            countdown.textContent = (Swal.getTimerLeft() / 1000).toFixed(0);
          }, 100);
        },
        willClose: () => {
          clearInterval(timerInterval);
          record(stopID);
        },
      }).then((result) => {
        /* Read more about handling dismissals below */
        if (result.dismiss === Swal.DismissReason.timer) {
          console.log("I was closed by the timer");
        }
      });
    }
  });
};

//Recording API
const recordAudio = () => {
  return new Promise((resolve) => {
    navigator.mediaDevices
      .getUserMedia({
        audio: { channelCount: 1 },
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
              const audio = new Audio(audioUrl);
              resolve({ audioBlob, audioUrl, audio });
            }); // End event listener
            mediaRecorder.stop();
          });
        };
        return resolve({ start, stop });
      });
  });
};

const record = async (id, callbackFn) => {
  const recorder = await recordAudio();
  recorder.start();

  console.log("recording started");

  Clock.start();

  const recording_anim = document.getElementById("recording-animation");
  const recording_anim1 = document.getElementById("recording-animation1");
  // Recording time indicator
  recording_anim.classList.toggle("recording-stop");
  recording_anim.classList.toggle("recording-start");
  //Disable stop button indicator
  recording_anim1.classList.toggle("recording-stop");
  recording_anim1.classList.toggle("recording-start");
  const stopButton = document.getElementById(id);

  stopButton.onclick = async () => {
    const { audioBlob, audioUrl, audio } = await recorder.stop();
    console.log("recording stopped");
    callbackFn({ audioBlob, audioUrl, audio });
    // Do dom manipulation here
  };
};

function makeRecordFunction(playID, stopID, callbackFn) {
  const playButton = document.getElementById(playID);
  playButton.onclick = () => record(stopID, callbackFn);
  playButton.onclick = () => promptRecording(stopID);
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

var Clock = {
  totalSeconds: 0,
  start: function () {
    if (!this.interval) {
      var self = this;
      function pad(val) {
        return val > 9 ? val : "0" + val;
      }
      this.interval = setInterval(function () {
        self.totalSeconds += 1;

        document.getElementById("min").innerHTML = pad(
          Math.floor((self.totalSeconds / 60) % 60)
        );
        document.getElementById("sec").innerHTML = pad(
          parseInt(self.totalSeconds % 60)
        );
        //make sure the recording is more than 5 second
        if (self.totalSeconds >= 05) {
          stopButton.disabled = false;
          // recordButton.disabled = false;
        }
      }, 1000);
    }
  },

  reset: function () {
    Clock.totalSeconds = null;
    clearInterval(this.interval);
    document.getElementById("min").innerHTML = "00";
    document.getElementById("sec").innerHTML = "00";
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
    Clock.start();
  },
};
