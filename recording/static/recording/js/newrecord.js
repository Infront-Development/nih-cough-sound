// Recorder API
//Reference from https://medium.com/@bryanjenningz/how-to-record-and-play-audio-in-javascript-faa1b2b3e49b

const recordAudio = () => {
  return new Promise((resolve) => {
    navigator.mediaDevices
      .getUserMedia({ audio: true })

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
              const audioBlob = new Blob(audioChunks);
              const audioUrl = URL.createObjectURL(audioBlob);
              const audio = new Audio(audioUrl);
              const play = () => {
                audio.play();
              };
              resolve({ audioBlob, audioUrl, play });
            });
            mediaRecorder.stop();
          });
        };
        return resolve({ start, stop });
      });
  });
};

// (async () => {
//   const recorder = await recordAudio();
//   $("#recordButtonOne").click(function () {
//     recorder.start();
//   });

//   // await sleep(3000);
//   const audio = await recorder.stop();
//   $("#stopButtonOne").click(function () {
//     recorder.stop();
//   });

//   audio.play();
// })();
const sleep = (time) => new Promise((resolve) => setTimeout(resolve, time));

(async () => {
  const recorder = await recordAudio();
  recorder.start();
  await sleep(3000);
  const audio = await recorder.stop();
  audio.play();
})();
