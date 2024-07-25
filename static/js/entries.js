function openFullscreen() {
  const img = document.getElementById("myImg"); // Get the img element by ID
  if (img.requestFullscreen) {
      img.requestFullscreen();
  } else if (img.webkitRequestFullscreen) { /* Safari */
      img.webkitRequestFullscreen();
  } else if (img.msRequestFullscreen) { /* IE11 */
      img.msRequestFullscreen();
  }
}