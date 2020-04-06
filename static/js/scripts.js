const numInputs = document.querySelectorAll('input[type=number]')

numInputs.forEach(function(input) {
  input.addEventListener('blur', function(e) {
    if (e.target.value == '') {
      e.target.value = 0
    }
  })
})