var start = document.getElementById("start");
var input = document.getElementById("input");
start.focus();
start.style.backgroundColor = "#2F93F6";
start.style.color = "white";
elid = 1;
var links = null;

function dotheneedful(sibling, elidp) {
  if (sibling != null) {
    start.focus();
    start.style.backgroundColor = "";
    start.style.color = "";
    sibling.focus();
    sibling.style.backgroundColor = "#2F93F6";
    sibling.style.color = "white";
    start = sibling;

    elid = elid + elidp;
    links = document.getElementsByClassName(elid);
  }
}

document.onkeydown = checkKey;

function checkKey(e) {
  e = e || window.event;
  if (e.keyCode == "38") {
    // Arriba
    input.blur();
    var sibling = start.previousElementSibling;
    dotheneedful(sibling, -1);
    input.value='';

  } else if (e.keyCode == "40") {
    // Abajo
    input.blur();
    var sibling = start.nextElementSibling;
    dotheneedful(sibling, 1);
    input.value='';
  }

  // 'Q' - Modal
  if (e.keyCode == "81") {
    if (links[0] != null) {
      links[0].click();
    }
  }
  // 'Supr' - Eliminar
  if (e.keyCode == "46") {
    if (links[1] != null) {
      links[1].click();
    }
  }
  // 'Enter' - Modificar
  if (e.keyCode == "13") {
    if (links[2] != null) {
      links[2].click();
    }
  }
  // 'Espacio' - Buscar
  if( e.keyCode == "32"){
    input.focus();
    input.value='';
    console.log("asd");
  }
}

