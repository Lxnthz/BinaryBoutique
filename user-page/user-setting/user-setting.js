const deleteAccount = (event) => {
    event.preventDefault();

    const confirmationInput = document.getElementById("confirmation");
    const confirmationValue = confirmationInput.value.trim().toUpperCase();

    // Check if the user entered 'DELETE' to confirm
    if (confirmationValue !== "DELETE") {
        alert("Please type 'DELETE' to confirm the account deletion.");
        return;
    }

    // Perform the actual account deletion logic here (may involve sending data to a server)
    alert("Account deleted successfully!");
};