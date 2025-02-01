const editButtons = document.getElementsByClassName("btn-edit");
const testimonialText = document.getElementById("id_body");
const testimonialForm = document.getElementById("testimonialForm");
const submitButton = document.getElementById("submitButton");

document.addEventListener("DOMContentLoaded", function () {
  const editButtons = document.querySelectorAll(".btn-edit");
  const testimonialForm = document.getElementById("TestimonialForm");
  const submitButton = document.getElementById("submitButton");

  if (!testimonialForm || !submitButton) {
    console.error("Form elements not found!");
    return;
  }

  editButtons.forEach((button) => {
    button.addEventListener("click", (e) => {
      let testimonialId = e.target.getAttribute("data-testimonial_id");
      let testimonialContent = document.getElementById(`testimonial${testimonialId}`).innerText;

      testimonialForm.action = `/about/edit/${testimonialId}/`;
      testimonialForm.querySelector("textarea").value = testimonialContent;
      submitButton.innerText = "Update";
    });
  });
});

/**
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Fetches the content of the corresponding comment.
 * - Populates the `commentText` input/textarea with the comment's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
 */
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let testimonialId = e.target.getAttribute("data-testimonial_id");
    let testimonialContent = document.getElementById(`testimonial${testimonialId}`).innerText;
    testimonialText.value = testimonialContent;
    submitButton.innerText = "Update";
    testimonialForm.setAttribute("action", `edit_testimonial/${testimonialId}`);
  });
}

/**
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the 
 * deletion endpoint for the specific comment.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 * the user for confirmation before deletion.
 */
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let testimonialId = e.target.getAttribute("data-testimonial_id");
    deleteConfirm.href = `delete_testimonial/${testimonialId}`;
    deleteModal.show();
  });
}