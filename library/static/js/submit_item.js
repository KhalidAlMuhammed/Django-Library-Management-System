document.addEventListener('DOMContentLoaded', function() {
    var itemType = document.getElementById('item_type').value;
    updateFormFields(itemType);
});

document.getElementById('item_type').addEventListener('change', function() {
    var itemType = this.value;
    updateFormFields(itemType);
});

function updateFormFields(itemType) {
    var formFieldsContainer = document.getElementById('form_fields');
    formFieldsContainer.innerHTML = '';
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                formFieldsContainer.innerHTML = xhr.responseText;
            } else {
                console.error('Error fetching form fields:', xhr.status);
            }
        }
    };
    xhr.open('GET', '/get-form-fields/' + itemType + '/', true);
    xhr.send();
}