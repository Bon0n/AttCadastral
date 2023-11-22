$("#dadosPessoais select[name='estado']").on('change', function(){
        $("#cidade").val($("#cidade option:first").val());
        var $this = $(this);
        if($this.val() != ''){
            $.ajax({
                url: 'pegarcidades/'+$this.val(),
                type: 'GET',
                success: function(resp){
                    let options = '';
                    resp.data.forEach(cidade => {
                        options+='<option value='+cidade.nome+'>'+cidade.nome+'</option>';
                    });
                    $("#dadosPessoais select[name='cidades']").find('.depois').after(options);
                },
                error: function(resp){
                    console.log('Something went wrong');
                }
            });
        }else {
            $("#dadosPessoais select[name='cidades']").find('.depois').nextAll().remove();
        }
});