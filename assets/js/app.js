// Import Bootstrap JavaScript
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
//import 'bootstrap-icons/font/bootstrap-icons.css';

// Optionally, if you're using Bootstrap's CSS in the app:
//import 'bootstrap/dist/css/bootstrap.min.css';


import '../styles/app.scss';


// window.addEventListener('load', () => {
//     document.getElementById('message').textContent = 'Bundled From javascript!';
// })

document.addEventListener("DOMContentLoaded", function () {
    // Select the form by its ID
    const form = document.getElementById("contactForm");
    const successMessage = document.getElementById("successMessage");

    // Only run this code if the form exists on the current page
    if (form) {
        // Attach event listener to the form
        form.addEventListener("submit", function (event) {
            event.preventDefault(); // Prevent default form submission

            // Perform form validation
            if (!form.checkValidity()) {
                event.stopPropagation();
                form.classList.add("was-validated");
            } else {
                // If the form is valid, submit using AJAX
                const formData = new FormData(form);

                fetch("/", {
                    method: "POST",
                    body: formData,
                })
                    .then((response) => {
                        if (response.ok) {
                            // Replace form with a success message
                            form.style.display = "none";
                            successMessage.style.display = "block";
                        } else {
                            alert("There was an issue submitting the form. Please try again.");
                        }
                    })
                    .catch((error) => {
                        console.error("Form submission error:", error);
                        alert("An error occurred. Please try again later.");
                    });
            }
        });
    }
});

