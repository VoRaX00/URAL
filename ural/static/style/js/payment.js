$(document).ready(function() {
    // При изменении состояния первого чекбокса
    $('#cboxCashless').change(function() {
        if(this.checked) {
            // Если чекбокс выбран, добавить дополнительные чекбоксы
            $('#extra_checkbox').html(`
                <div class="mb-3">
                    <input class="form-check-input" type="checkbox" name="cashless" id="nds" value="nds">
                    <label class="form-check-label" for="nds">НДС</label>
                </div>
                <div class="mb-3">
                    <input class="form-check-input" type="checkbox" name="cashless" id="without_nds" value="without_nds">
                    <label class="form-check-label" for="without_nds">Без НДС</label>
                </div>
            `);
        } else {
            // Если чекбокс не выбран, удалить дополнительные чекбоксы
            $('#extra_checkbox').html('');
        }
    });
});