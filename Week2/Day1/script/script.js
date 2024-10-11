/**
 * @class       : script
 * @author      : mailitg (mailitg@$HOSTNAME)

*/

const socket = new WebSocket('ws://10.1.224.63/'); // Change this to your ESP32 IP  

socket.onopen = function() {  
  console.log('WebSocket connection opened');  
  socket.send('Hello from client!');  
};  

socket.onmessage = function(event) {  
  console.log('Message from server: ', event.data);
  const clicked = event.data;
  if (clicked == "Button pressed")
  {
    let buttonCount = parseInt(localStorage.getItem('buttonCount') || 0);
    buttonCount +=1;
    localStorage.setItem('buttonCount', buttonCount);

    if (buttonCount == 1)
    {
      window.location.href ="button.html?message=1";
    }

    if (buttonCount == 2)
    {
      window.location.href ="button.html?message=2";
    }

    if (buttonCount == 3)
    {
      window.location.href ="button.html?message=3";
    }

    if (buttonCount == 4)
    {
      window.location.href ="button.html?message=4";
      localStorage.setItem('buttonCount', 0);
    }

    if (buttonCount >= 5)
    {
      localStorage.setItem('buttonCount', 0);
    }

  }

};  

socket.onclose = function() {  
  console.log('WebSocket connection closed');  

}

function HandleWhyClick() {
  let clickCount = parseInt(localStorage.getItem('clickCount') || 0);
  clickCount +=1;
  localStorage.setItem('clickCount', clickCount);
  if (clickCount == 1)
  {
    window.location.href ="newPage.html?message=1";
  }

  if (clickCount == 2)
  {
    window.location.href ="newPage.html?message=2";
  }

  if (clickCount == 3)
  {
    window.location.href ="newPage.html?message=3";
  }

  if (clickCount == 4)
  {
    window.location.href ="newPage.html?message=4";
  }

  if (clickCount >= 5)
  {
    localStorage.setItem('clickCount', 0);
  }
}

document.getElementById("why").addEventListener("click", HandleWhyClick);

