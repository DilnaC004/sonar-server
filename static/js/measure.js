$(function () {
  setInterval(refresh_table, 1000);
});

function refresh_table() {
  $.get("/get_table_data", (data) => {
    $("#table-body").html(data[0]);
    $("#update-time").html(data[1]);
  });
}
