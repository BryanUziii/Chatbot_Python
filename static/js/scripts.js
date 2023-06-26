document.addEventListener("DOMContentLoaded", function() {

     const btnLimpiar = document.getElementById("btnLimpiar");


      function limpiarChat(){
        var chatDiv = document.getElementById('chat');
        chatDiv.innerHTML = "";
      }

      // Función para agregar un mensaje al chat
      function addMessage(message, sender) {
        var chatDiv = document.getElementById('chat');
        var messageDiv = document.createElement('div');
        messageDiv.className = 'message ' + (sender === 'Tú' ? 'user-message' : 'bot-message');
        var contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';




        // contentDiv.innerText = sender + ': ' + message;

        if (sender === 'Tú') {
          // Acciones si el remitente es "Tú" (usuario)
          console.log('Mensaje enviado por el usuario');
          contentDiv.innerText =  message;
        } else {
          // Acciones si el remitente no es "Tú" (chatbot)
          console.log('Mensaje enviado por el chatbot');

          // Crea un objeto FormData y agrega el valor de entrada al formulario
          const formData = new FormData();
          formData.append('entrada', message);


          // Realiza la solicitud POST con el formulario como datos
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
        chatDiv.appendChild(messageDiv);

        // Scroll automático hacia el último mensaje
        chatDiv.scrollTop = chatDiv.scrollHeight;


      }

      // Evento de envío de mensaje
      document.getElementById('chat-inputs').addEventListener('submit', function(event) {
        event.preventDefault();
        var messageInput = document.getElementById('inputMensaje');
        var message = messageInput.value;

        // Agregar el mensaje enviado al chat
        addMessage(message, 'Tú');
        addMessage(message, 'Chatbot');

        // Simular respuesta después de 1 segundo
        // setTimeout(function() {
        //   addMessage(message, 'Chatbot');
        // }, 1000);

        // Limpiar el campo de entrada
        messageInput.value = '';
      });
  
      btnLimpiar.addEventListener("click", limpiarChat);

  });
  
  
  
  
  
  
  