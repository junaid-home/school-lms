const questionsContainer = document.getElementById("questions-container");
const submitButton = document.getElementById("quizz-button");

fetch(document.BACKEND_GET_DATA_URL).then(async (response) => {
  const data = await response.json();

  data.forEach((q, i) => {
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
});

document.addEventListener("submit", (e) => {
  e.preventDefault();
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
  }).then(async (response) => {
    const result = await response.json();
    if (result.status === "Ok") {
      console.log(result);
      window.location.assign(document.REDIRECT_URL);
    }
  });
});

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
