async function getQuestion() {
  const response = await fetch("/quiz");
  const data = await response.json();

  console.log(data.arg_1);
  console.log(data.arg_2);

  document.getElementById("arg_1").textContent = data.arg_1;
  document.getElementById("arg_2").textContent = data.arg_2;
}

async function answerQuestion() {
  const answer = { arg_1: 0, arg_2: 0, answer: 0 };
  answer.arg_1 = document.getElementById("arg_1").textContent;
  answer.arg_2 = document.getElementById("arg_2").textContent;
  answer.answer = document.getElementById("answ").value;

  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(answer),
  };
  const response = await fetch("/answer/", options);
  const data = await response.json();

  if (data.result) {
    window.alert("Correct Answer!");
  } else {
    window.alert("Wrong Answer!");
  }
  location.reload();
}
