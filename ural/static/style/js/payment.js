$(document).ready(function() {
    // При изменении состояния первого чекбокса
    $('#cashless_payment').change(function() {
        if(this.checked) {
            // Если чекбокс выбран, добавить дополнительные чекбоксы
            $('#extra_checkbox').html(`
                <div class="mb-3">
                    <input class="form-check-input" type="checkbox" name="nds" id="nds" value="option3">
                    <label class="form-check-label" for="nds">НДС</label>
                </div>
                <div class="mb-3">
                    <input class="form-check-input" type="checkbox" name="without_nds" id="without_nds" value="option4">
                    <label class="form-check-label" for="without_nds">Без НДС</label>
                </div>
            `);
        } else {
            // Если чекбокс не выбран, удалить дополнительные чекбоксы
            $('#extra_checkbox').html('');
        }
    });
});