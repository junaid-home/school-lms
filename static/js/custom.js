const questionsContainer = document.getElementById("questions-container");
const submitButton = document.getElementById("quizz-button");
const alertBox = document.getElementById("quizz-alert-box");
const timerBox = document.getElementById("quizz-timer");

fetch(document.BACKEND_GET_DATA_URL).then(async (response) => {
  const data = await response.json();
  alertBox.classList.add("d-none");
  timerBox.classList.remove("d-none");

  data.questions.forEach((q, i) => {
    questionsContainer.innerHTML += `
    <div class="question mb-2">
        <h4 class="query">Q${i + 1}:&nbsp;&nbsp;${q.question}</h4>
        <div class="d-flex flex-column align-items-start">
        <div class="radio radiofill radio-success radio-inline">
          <label>
            <input class="answer" value="${q.option_1}" type="radio" name="${q.id}" />
            <i class="helper"></i>${q.option_1}
          </label>
        </div>
        <div class="radio radiofill radio-success radio-inline">
          <label>
            <input class="answer" value="${q.option_2}" type="radio" name="${q.id}" />
            <i class="helper"></i>${q.option_2}
          </label>
        </div>
        <div class="radio radiofill radio-success radio-inline">
          <label>
            <input class="answer" value="${q.option_3}" type="radio" name="${q.id}" />
            <i class="helper"></i>${q.option_3}
          </label>
        </div>
        <div class="radio radiofill radio-success radio-inline">
          <label>
            <input class="answer" value="${q.option_4}" type="radio" name="${q.id}" />
            <i class="helper"></i>${q.option_4}
          </label>
        </div>
        </div>
    <div>
    `;
  });

  startTimer(data.time);
});

document.addEventListener("submit", (e) => {
  e.preventDefault();

  sendData();
});

function sendData() {
  submitButton.setAttribute("disabled", true);
  const questions = document.getElementsByClassName("question");
  const data = [];

  Array.from(questions).forEach((q, i) => {
    const query = q.getElementsByClassName("query");
    const answers = q.getElementsByClassName("answer");
    let _answer = null;
    Array.from(answers).forEach((a) => {
      if (a.checked) {
        _answer = a.value;
      }
    });

    const answer = _answer;
    const title = query[0].innerText.replace(`Q${i + 1}:`, "").trim();
    data.push({ [title]: answer });
  });

  fetch(document.BACKEND_SAVE_DATA_URL, {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
  })
    .then(async (response) => {
      const result = await response.json();
      if (result.status === "Ok") {
        console.log(result);
        window.location.assign(document.REDIRECT_URL);
      } else {
        $("#confirmation-model").modal("hide");
        alertBox.classList.remove("d-none");
        window.scrollTo(0, 0);
      }
    })
    .catch(() => {
      $("#confirmation-model").modal("hide");
      alertBox.classList.remove("d-none");
      setTimeout(() => {
        window.scrollTo(0, 0);
      }, 500);
    });
}

const startTimer = (time) => {
  if (time.toString().length < 2) {
    timerBox.innerText = `0${time}:00`;
  } else {
    timerBox.innerText = `${time}:00`;
  }

  let minutes = time - 1;
  let seconds = 60;
  let displaySeconds;
  let displayMinutes;

  const timer = setInterval(() => {
    seconds--;
    if (seconds < 0) {
      seconds = 59;
      minutes--;
    }
    if (minutes.toString().length < 2) {
      displayMinutes = "0" + minutes;
    } else {
      displayMinutes = minutes;
    }
    if (seconds.toString().length < 2) {
      displaySeconds = "0" + seconds;
    } else {
      displaySeconds = seconds;
    }
    if (minutes === 0 && seconds === 0) {
      timerBox.innerText = "00:00";
      setTimeout(() => {
        clearInterval(timer);
        sendData();
      }, 500);
    }

    timerBox.innerText = `${displayMinutes}:${displaySeconds}`;
  }, 1000);
};

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
