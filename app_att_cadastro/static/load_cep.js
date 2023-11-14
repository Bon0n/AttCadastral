$("#buscar-cep").on('click', function(){
        var $this = $("#cep")
        if($this.val() != ''){
            $.ajax({
                url: 'buscacep/'+$this.val(),
                type: 'GET',
                success: function(resp){
                    let options = '';
                    $("#rua").val(resp['data']['logradouro'])
                    $("#bairro").val(resp['data']['bairro'])
                    $('#estado option[value='+resp['data']['uf']).prop('selected', true)
                    options = '<option value='+resp['data']['localidade']+'>'+resp['data']['localidade']+'</option>';
                    $("#dadosPessoais select[name='cidades']").find('.depois').after(options);
                    $("#cidade").val(resp['data']['localidade']).prop('selected', true)
                },
                error: function(resp){
                    console.log('Something went wrong');
                }
            });
        }else {
            $("#dadosPessoais select[name='cidades']").find('.depois').nextAll().remove();
        }
});