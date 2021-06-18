$(document).ready(function (){
    $('.answer').click(
        function (e) {
            let $this = $(this);
            let container = $this.parent('.answer-container');
            $.ajax({
                type: 'POST',
                url: '/answer/',
                beforeSend: function (request) {
                    request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                },
                data: {
                    'score': $this.attr('score'),
                    'question_number': container.attr('question_number')
                },
                success: function () {
                    container.addClass('d-none');
                    let nextContainer = container.next();
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
})
