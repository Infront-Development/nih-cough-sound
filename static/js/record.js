$(document).ready(function () {
  function promptRecording(event) {
    const audios = document.getElementsByTagName('audio');
    let masked = 0, unmasked= 0 ;

    for(i=0; i < audios.length; i++){
      if (audios[i].getAttribute("mask") == "true"){
        masked += 1;
      } else{
        unmasked += 1;
      }
    }   
    
    
    Swal.fire({
      title: gettext("Please confirm if you are wearing a mask"),
      text: gettext("You will need to record twice with a mask and twice without a mask"),
      cancelButtonText: gettext("Cancel"), 
      showConfirmButton: masked != 2,
      showDenyButton : unmasked != 2,
      confirmButtonText: "<i class='fas fa-head-side-mask'></i>" + gettext("I'm wearing a mask"),
      denyButtonText : "<i class='fas fa-head-side-cough'></i>" + gettext("I'm not wearing a mask"),
      showCancelButton: true,
    }).then((result) => {
      if (result.isConfirmed){
        
        startRecording(result.isConfirmed);
      }
      if(result.isDenied){
        startRecording(false);
      }
      
    });
  }

  URL = window.URL || window.webkitURL;
  var gumStream;
  //stream from getUserMedia()
  var rec;
  //Recorder.js object
  var input;
  //MediaStreamAudioSourceNode we'll be recording

  var AudioContext = window.AudioContext || window.webkitAudioContext;
  var audioContext = new AudioContext();

  //new audio context to help record
  var recordButton = document.getElementById("recordButton");
  var stopButton = document.getElementById("stopButton");

  recordButton.addEventListener("click", promptRecording);
  stopButton.addEventListener("click", stopRecording);
  //recordButton.addEventListener("click", completeRecording);
  //var recordButton = document.getElementById("recordButton");
  function startRecording(mask = false) {
    const audios = document.getElementsByTagName("audio");

    Clock.start();
    if (audios.length >= 4) {
      swal(gettext("Cannot Record Audio again. Maximum 4 audio at a time"), "", "error");
      return;
    }
    // Start Recording
    var constraints = {
      audio: true,
      video: false,
    };

    /* Disable the record button until we get a success or fail from getUserMedia() */

    recordButton.disabled = true;
    stopButton.disabled = false;

    /* We're using the standard promise based getUserMedia()

        https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia */

    navigator.mediaDevices
      .getUserMedia(constraints)
      .then(function (stream) {
        /* assign to gumStream for later use */
        gumStream = stream;
        /* use the stream */
        input = audioContext.createMediaStreamSource(stream);
        /* Create the Recorder object and configure to record mono sound (1 channel) Recording 2 channels will double the file size */
        rec = new Recorder(input, {
          numChannels: 1,
        });
        //start the recording process

        rec.mask = mask;
        rec.record();

        // console.log("Recording started");

        const recording_anim = document.getElementById("recording-animation");

        // Recording time indicator
        recording_anim.classList.toggle("recording-stop");
        recording_anim.classList.toggle("recording-start");
      })
      .catch(function (err) {
        //enable the record button if getUserMedia() fails
        recordButton.disabled = false;
        stopButton.disabled = true;
      });
  }

  function stopRecording() {
    Clock.reset();
    //disable the stop button, enable the record too allow for new recordings
    stopButton.disabled = true;
    recordButton.disabled = false;
    rec.stop(); //stop microphone access
    gumStream.getAudioTracks()[0].stop();

    rec.exportWAV(createDownloadLink);
    const recording_anim = document.getElementById("recording-animation");

    recording_anim.classList.toggle("recording-stop");
    recording_anim.classList.toggle("recording-start");
  }

  //This sends data via upload to the backend/database
  function createDownloadLink(blob) {
    var url = URL.createObjectURL(blob);

    var audioContainter = document.createElement("div");
    audioContainter.classList.add("audio-list");

    var wrapper = document.getElementById("audio-wrapper");
    var au = document.createElement("audio");

    //add controls to the <audio> element
    au.controls = true;
    au.src = url;
    au.setAttribute("mask", rec.mask);
    //add the new audio and a elements to the li element

    audioContainter.appendChild(au);
    audioContainter.innerHTML +=
      "<a href='#removeAudio' onclick='removeMeFromParentAudiowrapper(event)'> <i class='fa fa-trash' style='color: red;'> </i> </a>  ";
    if (rec.mask){
      audioContainter.innerHTML += "<i class='fas fa-head-side-mask'></i>"
    }
    wrapper.appendChild(audioContainter);

    //filename to send to server without extension
    //upload link
    var upload = document.createElement("a");
    upload.href = "#";
    upload.innerHTML = "Upload";
  }
});

function removeMeFromParentAudiowrapper(event) {
  var audioWrapper = document.getElementById("audio-wrapper");
  var audioList = event.target.parentElement.parentElement; // <i> -> <a> -> <div>
  audioWrapper.removeChild(audioList);
}
// Functions to upload Audio Files with ajax
async function submitAudio() {
  let csrf = $('input[name="csrfmiddlewaretoken"]').val();
  const fd = new FormData();
  fd.append("csrfmiddlewaretoken", csrf);

  const audios = document.getElementsByTagName("audio");

  for (i = 0; i < audios.length; i++) {
    data = await fetch(audios[i].src);
    blob = await data.blob();

    audio_name =
      audios[i].getAttribute("mask") == "true"
        ? "audio_data_mask"
        : "audio_data_no_mask";
    fd.append(audio_name, blob);
  }
  const pathname = window.location.pathname;
  // Use same path name because we upload to same url name as the current pathname
  $.ajax({
    type: "post",
    url: pathname,
    // type: $(this).attr('method'),
    data: fd,
    cache: false,
    processData: false,
    contentType: false,
    success: function (response) {
      // if (response.status == "Success"){
      //     alert("Success");
      // }else{
      //     alert("Failed to Upload Recordings, please contact Admin!")
      // }
    },
  });
}

async function submitAllAudio(event) {
  event.preventDefault();

  const audios = document.getElementsByTagName("audio");
  if (audios.length != 4) {
    swal("Must Record 4 Audios!", "", "warning");
    return;
  } else {
    await submitAudio(); // From record.js

    swal("Saved!", "", "success").then(function () {
      window.location.href = event.target.href;
    });
    // Simulate HTTP redirect
  }
}

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

document
  .getElementById("recordButton")
  .addEventListener("click", function () {});
document.getElementById("stopButton").addEventListener("click", function () {
  Clock.reset();
});
