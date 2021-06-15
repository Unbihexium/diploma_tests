$(document).ready(function (){
    $('.answer').click(
        function (e) {
            let $this = $(this);
            let container = $this.parent('.answer-container');
            container.addClass('d-none');
            let nextContainer = container.next();
            if (nextContainer.length == 1){
                nextContainer.removeClass('d-none');
            } else {
                //finish test
                console.log('test finished')
            }
        }
    )
})
