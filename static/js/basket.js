function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function delete_func(event) {
    let id = event.target.attributes.data.value;
    $.ajax(
        {
            url: `/baskets/remove/${id}/`,
            type: "POST",
            headers: {'X-CSRFToken': getCookie('csrftoken')},
            data: {'': '',},
            success: function (data) {
                $('.basket_list').html(data.result)
                $('.delete').on('click', function (event) {delete_func(event);});
            }
        }
    );
    event.preventDefault()
}

window.onload = function (event) {
    $('.basket_list').on('change', 'input[type="number"]', function (event) {
        let t_href = event.target;
        $.ajax(
            {
                url: `/baskets/edit/${t_href.name}/${t_href.value}/`,
                success: function (data) {
                    $('.basket_list').html(data.result)
                }
            }
        );
        event.preventDefault()
    })

    $('.card_add_basket').on('click', 'button[type="button"]', function (event) {
        let value = event.target.value;
        let page = $('#current_page').html()
        let cat_id = $('#current_cat').html()
        $.ajax(
            {
                url: `/baskets/add/${value}/`,
                data: {
                    'page': page,
                    'cat_id': cat_id
                },
                success: function (data) {
                    $('.card_add_basket').html(data.result)
                }
            }
        );
        event.preventDefault()
    })

    $('.delete').on('click', function (event) {delete_func(event);});
}