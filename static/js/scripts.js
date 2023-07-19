document.addEventListener("DOMContentLoaded", function() {

     const btnLimpiar = document.getElementById("btnLimpiar");
     const btnEnviar = document.getElementById('btnEnviar');
     const inputMensaje = document.getElementById('inputMensaje');

     const messageInput = document.getElementById('inputMensaje');


    //  Redimencionar input acorde al texto 
     inputMensaje.addEventListener('input', function() {
       this.style.height = ''; // Restablece la altura para obtener la altura de contenido actual
       this.style.height = `${this.scrollHeight}px`; // Establece la altura según el contenido
     
       // Desplaza el scroll hacia arriba para mostrar el contenido más reciente
       this.scrollTop = 0;
     });

    //  Precionar "Enter" para mandar el mensaje
     inputMensaje.addEventListener('keydown', function(event) {
      if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault(); // Evita que se inserte una nueva línea
        enviarInfo(); // Llama a la función para enviar el mensaje
      }
    });
     



      function limpiarChat(){
        var chatDiv = document.getElementById('chat');
        chatDiv.innerHTML = "";
      }

      // Función para agregar un mensaje al chat
      // function addMessage(message, sender) {
      //   var chatDiv = document.getElementById('chat');
      //   var messageDiv = document.createElement('div');
      //   messageDiv.className = 'message ' + (sender === 'Tú' ? 'user-message' : 'bot-message');
      //   var contentDiv = document.createElement('div');
      //   contentDiv.className = 'message-content';
      //   contentDiv.innerText = "...";

      //   // contentDiv.innerText = sender + ': ' + message;

      //   if (sender === 'Tú') {
      //     // Acciones si el remitente es "Tú" (usuario)
      //     console.log('Mensaje enviado por el usuario');
      //     contentDiv.innerText =  message;
      //   } else {
      //     // Acciones si el remitente no es "Tú" (chatbot)
      //     console.log('Mensaje enviado por el chatbot');

      //     // Crea un objeto FormData y agrega el valor de entrada al formulario
      //     const formData = new FormData();
      //     formData.append('entrada', message);


      //     // Realiza la solicitud POST con el formulario como datos
      //     axios.post('/chatbot', formData)
      //       .then(function(response) {
      //         const respuesta = response.data;
      //         console.log(respuesta);
      //         contentDiv.innerText = respuesta;
      //       })
      //       .catch(function(error) {
      //         console.error(error);
      //       });
      //   }


      //   messageDiv.appendChild(contentDiv);
      //   chatDiv.appendChild(messageDiv);

      //   // Scroll automático hacia el último mensaje
      //   chatDiv.scrollTop = chatDiv.scrollHeight;


      // }

      function addMessage(message, sender) {
        var chatDiv = document.getElementById('chat');
        var chatMessageDiv = document.createElement('div');
        chatMessageDiv.className = 'chat-div ' + (sender === 'Tú' ? 'user-message' : 'bot-message');
      
        var chatDivContent = document.createElement('div');
        chatDivContent.className = 'chat-div-content';
      
        var chatImgDiv = document.createElement('div');
        chatImgDiv.className = 'chat-img';
        var img = document.createElement('embed');
        img.src = sender === 'Tú' ? '/static/img/person-circle.svg' : '/static/img/robot.svg';
        img.type = 'image/svg+xml';
        img.alt = 'Descripción de la imagen';
        chatImgDiv.appendChild(img);
      
        var messageDiv = document.createElement('div');

        messageDiv.className = 'message';
        var contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
      
        if (sender === 'Tú') {
          console.log('Mensaje enviado por el usuario');
          img.classList.add('user');
          contentDiv.innerText = message;
        } else {
          console.log('Mensaje enviado por el chatbot');
          img.classList.add('bot');

      
          const formData = new FormData();
          formData.append('entrada', message);
      
          axios.post('/chatbot', formData)
            .then(function(response) {
              const respuesta = response.data;
              console.log(respuesta);
              contentDiv.innerText = respuesta;
            })
            .catch(function(error) {
              console.error(error);
            });
        }
      
        messageDiv.appendChild(contentDiv);
        chatDivContent.appendChild(chatImgDiv);
        chatDivContent.appendChild(messageDiv);
        chatMessageDiv.appendChild(chatDivContent);
        chatDiv.appendChild(chatMessageDiv);
        chatDiv.scrollTop = chatDiv.scrollHeight;
      }
      

      const enviarInfo = () => {
        var message = messageInput.value;
        message = message.charAt(0).toUpperCase() + message.slice(1);

                // Agregar el mensaje enviado al chat
                addMessage(message, 'Tú');
                addMessage(message, 'Chatbot');
        
                // Simular respuesta después de 1 segundo
                // setTimeout(function() {
                //   addMessage(message, 'Chatbot');
                // }, 1000);
        
                // Limpiar el campo de entrada
                messageInput.value = '';

      }
  
      btnLimpiar.addEventListener("click", limpiarChat);
      btnEnviar.addEventListener("click", enviarInfo)

  });
  
  
  
  
  
  
  