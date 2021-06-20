$(document).ready(function (){
    $('.next-question').click(
        function (e) {
            e.preventDefault();
            let answer_container = $('.answer-container').not('.d-none');
            let checked_answer = answer_container.find('.form-check-input:checked');
            if (checked_answer.length == 0) {
                return;
            }
            $.ajax({
                type: 'POST',
                url: '/answer/',
                beforeSend: function (request) {
                    request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                },
                data: {
                    'score': checked_answer.attr('score'),
                    'question_number': answer_container.attr('question_number')
                },
                success: function () {
                    answer_container.addClass('d-none');
                    let nextContainer = answer_container.next('.answer-container');
                    if (nextContainer.length == 1) {
                        nextContainer.removeClass('d-none');
                    } else {
                        window.location.href = result_url;
                    }
                },
                error: function () {
                    console.log('failure');
                }
            })
        }
    )

    $('.previous-question').click(
        function (e) {
            e.preventDefault();
            let answer_container = $('.answer-container').not('.d-none');
            answer_container.addClass('d-none');
            let prev_container = answer_container.prev('.answer-container');
            if (prev_container.length == 1) {
                prev_container.removeClass('d-none');
            }
        }
    )
})
