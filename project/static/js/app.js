window.onload = function(){
    $('.checkbox').change(change_complete)
    $('.edit_icon').click(edit_mode)
    $('.form_btn').click(edit_btn)
    $('.form_area').change(form_btn_disabled)
}

function change_complete() {
    let id = $(this).attr('name');
    if ($(this).prop('checked')) {
        window.location.href = "/complete/" + id;
    }else {
        window.location.href = "/uncomplete/" + id;
    };
}


function edit_mode() {
    if ($('.form_btn').text() === '追加') {
        console.log('編集モード')
        let data = $(this).data();
        $('.form_area').attr('data-id', 'data.id');
        $('.form_area').val(data.item);
        $('.form_btn').attr('type', 'button').text('編集');
    }else {
        console.log('解除')
        $('.form_area').removeAttr('placeholder value')
        $('.form_btn').attr('type', 'submit').text('追加');
    }
    return false
}


function edit_btn() {
    let id = $('.form_area').data('id');
    window.location.href = "/edit/" + id + '/' + $('.form_area').val();
}


function form_btn_disabled() {
    if ($('.form_area').val() != '') {
        $('.form_btn').prop('disabled', false);
    }else {
        $('.form_btn').prop('disabled', true);
    }
}