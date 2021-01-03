$(document).ready(function () {

    $("body").on("click",".deleteBook",function(e){

        if(!confirm("A exclusão será permanente, deseja continuar?")) {
            return false;
        }

        e.preventDefault();
        let id = $(this).data("id");
        let token = $("input[name='csrfmiddlewaretoken']")[0].value;
        let url = this.href;
        let row = $(this).closest('tr');

        $.ajax({
            url: url,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: token,
                id: id
            },
            success: function (response){
                Swal.fire(
                    'Concluído!',
                    response.message,
                    'success'
                );
                row.remove();
            },
            error: function (error){
                Swal.fire(
                    'Operação mal sucedida!',
                    "Tente novamente mais tarde...",
                    'error'
                );
                console.error('error: ', error);
            }
        });
        return false;
    });
});
