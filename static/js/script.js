var xhr = new XMLHttpRequest()
xhr.open(
  'POST',
  '/get_messages/',
  true
)
xhr.send()

xhr.onreadystatechange = function() {
  if (xhr.readyState != 4) {
    return
  }

  if (xhr.status === 200) {
    console.log('result', JSON.parse(xhr.responseText))
  } else {
    console.log('err', xhr.responseText)
  }
}