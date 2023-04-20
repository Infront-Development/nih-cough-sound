$("#myModalEdit").on("show.bs.modal", function (e) {
  var button = $(e.relatedTarget);
  var value = button.data("value");
  var id = button.data("id");
  $(this).find(".modal-title").text(id);
  $("#covid-status-value").val(value);
});
