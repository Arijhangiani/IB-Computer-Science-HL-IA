var unitTwoArray = localStorage.getItem('cards3') ? JSON.parse(localStorage.getItem('cards3')) : [];

document.getElementById("save_card").addEventListener("click", () => {
  addFlashcard();
});

document.getElementById("delete_cards").addEventListener("click", () => {
  localStorage.clear();
  flashcards.innerHTML = '';
  unitThreeArray = [];
});

document.getElementById("show_card_box").addEventListener("click", () => {
  document.getElementById("create_card").style.display = "block";
});

document.getElementById("close_card_box").addEventListener("click", () => {
  document.getElementById("create_card").style.display = "none";
});

flashcardMaker = (text) => {
  const flashcard3 = document.createElement("div");
  const question = document.createElement('h2');
  const answer = document.createElement('h2');

  flashcard3.className = 'flashcard';

  question.setAttribute("style", "border-top:1px solid red; padding: 15px; margin-top:30px");
  question.textContent = text.my_question;

  answer.setAttribute("style", "text-align:center; display:none; color:red");
  answer.textContent = text.my_answer;

  flashcard3.appendChild(question);
  flashcard3.appendChild(answer);

  flashcard3.addEventListener("click", () => {
    if(answer.style.display == "none")
      answer.style.display = "block";
    else
      answer.style.display = "none";
  })

  document.querySelector("#flashcards").appendChild(flashcard3);
}

unitThreeArray.forEach(flashcardMaker);

addFlashcard = () => {
  const question = document.querySelector("#question");
  const answer = document.querySelector("#answer");

  let flashcard_info = {
    'my_question' : question.value,
    'my_answer'  : answer.value
  }

  unitThreeArray.push(flashcard_info);
  localStorage.setItem('card3', JSON.stringify(unitThreeArray));
  flashcardMaker(unitThreeArray[unitThreeArray.length - 1]);
  question.value = "";
  answer.value = "";
}