jQuery(document).ready(function($){
  
    window.onload = function (){
        $('#LanguageModal').modal('show');
        $('#ConsentModal').modal('show');
    };

    $('#LanguageModal').on('hidden.bs.modal', function () {
        $('#ConsentModal').modal('show');
    });

    $(function() {
        $('.selectpicker').selectpicker();
      });
  });
