const quotes = [
    { 
        text: "Coding like poetry should be short and concise.", 
        creator: "Santosh Kalwar" 
    },
    { 
        text: "First, solve the problem. Then, write the code.", 
        creator: "John Johnson" 
    },
    { 
        text: "Code is like humor. When you have to explain it, it’s bad.", 
        creator: "Cory House" 
    },
    { 
        text: "Make it work, make it right, make it fast.", 
        creator: "Kent Beck" 
    },
    { 
        text: "Clean code always looks like it was written by someone who cares.", 
        creator: "Robert C. Martin" 
    },
    { 
        text: "Of course, bad code can be cleaned up. But it’s very expensive.", 
        creator: "Robert C. Martin" 
    },
];

function generateQuote() {
    const quoteText = document.getElementById('quote-text');
    const quoteCreator = document.getElementById('quote-creator');
    const randomIndex = Math.floor(Math.random() * quotes.length);

    quoteText.style.opacity = 0;
    quoteCreator.style.opacity = 0;

    setTimeout(() => {
        quoteText.textContent = quotes[randomIndex].text;
        quoteCreator.textContent = `- ${quotes[randomIndex].creator} -`;
        quoteText.style.opacity = 1;
        quoteCreator.style.opacity = 1;
    }, 500);
}

function showCreator() {
    const quoteCreator = document.getElementById('quote-creator');
    quoteCreator.style.opacity = 1;
}

function hideCreator() {
    const quoteCreator = document.getElementById('quote-creator');
    quoteCreator.style.opacity = 0;
}


generateQuote();


setInterval(generateQuote, 10000);
